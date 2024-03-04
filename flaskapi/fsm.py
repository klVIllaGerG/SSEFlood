from cnn import *

import numpy as np
import torch
from skimage import exposure

import matplotlib.pyplot as plt

# 异常值处理，在dem和slope有效区(均值代替法)
region_mask = (dataset[:, :, 0] != 255) & (np.logical_and(dataset[:, :, 1] >= 0, dataset[:, :, 1] <= 361)) & (
    np.logical_and(dataset[:, :, 2] >= 0, dataset[:, :, 2] <= 56))
# print(region_mask.shape)
# print("True的个数:", np.count_nonzero(region_mask))
normal_ranges = {
    3: [-14, 19],
    4: [-3, 2],
    5: [-26, 27],
}
for channel in range(3, 6):
    channel_data = dataset[:, :, channel]
    lower_bound, upper_bound = normal_ranges[channel]
    valid_data = channel_data[region_mask]
    valid_mask = (valid_data >= lower_bound) & (valid_data <= upper_bound)
    channel_mean = np.mean(valid_data[valid_mask])
    # 将超出范围的值替换为平均值
    channel_data[region_mask] = np.where(~valid_mask, channel_mean, channel_data[region_mask])
    dataset[:, :, channel] = channel_data

# 研究区域内的点(轮廓定义)
region = []
for x in range(dataset.shape[0]):
    for y in range(dataset.shape[1]):
        # 遍历，在区域内，记录
        if dataset[x, y, 0] != 255:
            region.append((x, y))
region = np.array(region)  # 列表转数组
print("区域内样本：", region.shape[0])

# 有效样本取样（预测）
valid = []
for x in range(dataset.shape[0]):
    for y in range(dataset.shape[1]):
        # 遍历，在区域内，记录
        if (dataset[x, y, 0] != 255) and (0 <= dataset[x, y, 1] <= 361) and (0 <= dataset[x, y, 2] <= 56):
            valid.append((x, y))
valid = np.array(valid)  # 列表转数组
print("预测样本数量：", valid.shape[0])

# 归一化
for i in range(1, 10):
    layer = dataset[:, :, i]
    if np.isnan(layer[valid[:, 0], valid[:, 1]]).all():
        continue
    min_val = np.nanmin(layer[valid[:, 0], valid[:, 1]])
    max_val = np.nanmax(layer[valid[:, 0], valid[:, 1]])
    normalized_layer = exposure.rescale_intensity(layer[valid[:, 0], valid[:, 1]], in_range=(min_val, max_val),
                                                  out_range=(0, 1))
    dataset[:, :, i][valid[:, 0], valid[:, 1]] = normalized_layer


# 归一化后判断该点的有效性
def data_around(x, y):
    if (dataset[x, y, 0] != 255) and all(0 <= dataset[x, y, i] <= 1 for i in range(1, 10)):
        return True
    else:
        return False


# 输入格式转换
def input_turn(a, b):
    feature = 9  # 有效特征数
    feature_matrix = np.zeros((9, feature))
    for i in range(-1, 2):
        for j in range(-1, 2):
            # 周围点的坐标
            x = a + i
            y = b + j
            # 控制数组越界问题，越界用中心点代替
            if 0 <= x < dataset.shape[0] and 0 <= y < dataset.shape[1]:
                # 判定周围点是否在研究区域内，不在的用中心点代替
                if data_around(x, y):
                    for k in range(feature):
                        feature_matrix[(i + 1) * 3 + j + 1, k] = dataset[x, y, k + 1]
                else:
                    for k in range(feature):
                        feature_matrix[(i + 1) * 3 + j + 1, k] = dataset[a, b, k + 1]
            else:
                for k in range(feature):
                    feature_matrix[(i + 1) * 3 + j + 1, k] = dataset[a, b, k + 1]
    return feature_matrix


# 分块处理，避免内存爆炸；运行一次，保存结果
model_FSM = Net()
model_FSM.load_state_dict(torch.load("best_model.pt"))
# model_FSM = model_FSM.cuda()
model_FSM.eval()
# 创建一个与原始数据维度相同的数组（浮点类型，避免截断）
prediction_dense = np.full((6424, 4584), -1.0)
block_size = 100000  # 分块大小
count = 0  # 进度计数器
for i in range(0, len(valid), block_size):
    # 提取当前块的数据
    block = valid[i:i + block_size]
    areas = []
    for x, y in block:
        area = input_turn(x, y)
        areas.append(area)
    areas = np.array(areas)
    areas = areas.reshape(-1, 1, 9, 9)
    areas = torch.from_numpy(areas).float()
    # areas = areas.cuda()
    with torch.no_grad():
        probs = model_FSM(areas)
    # 将数据填充到对应的坐标位置
    for j, (x, y) in enumerate(block):
        prediction_dense[x, y] = probs[j]
    count += 1
    print(count)

# 结果数组保存
save_path = 'array_data.txt'
np.savetxt(save_path, prediction_dense)

# 创建区域轮廓图
contour_array = np.zeros((6424, 4584))
# 将valid数组中的坐标点标记为1
contour_array[region[:, 0], region[:, 1]] = 1
# 获取边界点的坐标
boundary_points = []
for x, y in region:
    neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for nx, ny in neighbors:
        if 0 <= nx < contour_array.shape[0] and 0 <= ny < contour_array.shape[1] and contour_array[nx, ny] == 0:
            boundary_points.append((x, y))
            break
boundary_points = np.array(boundary_points)
print(boundary_points.shape)

# prediction_dense = np.loadtxt('/content/drive/MyDrive/Colab/FSM_code/array_data.txt')

# 绘制
x = np.arange(4584)  # x轴坐标
y = np.arange(6424)  # y轴坐标
X, Y = np.meshgrid(x, y)
prediction_dense[prediction_dense == -1] = np.nan
# 绘制热力图+轮廓，设置nan的颜色为白色
plt.figure(figsize=(6, 6))
plt.scatter(boundary_points[:, 1], boundary_points[:, 0], color='black', s=1)
plt.pcolormesh(X, Y, prediction_dense, cmap='RdYlGn_r', shading='auto', vmin=0, vmax=1)
# 反转y
plt.gca().invert_yaxis()
plt.colorbar(label='probability')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sensitive Map')
plt.savefig("SensitiveMap.png")
