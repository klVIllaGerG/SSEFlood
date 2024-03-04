import numpy as np
import tifffile
import random
from skimage import exposure

# 读入tif
area = tifffile.imread('./uploads/zhanjiangrs.tif')
dem = tifffile.imread('./uploads/dem.tif')
slope = tifffile.imread('./uploads/dem_slope.tif')
ndvi = tifffile.imread('./uploads/NDVI.tif')
mndwi = tifffile.imread('./uploads/MNDWI.tif')
eibi = tifffile.imread('./uploads/EIBI.tif')
glcm = tifffile.imread('./uploads/glcm.tif')
band1 = tifffile.imread('./uploads/flood1.tif')
band5 = tifffile.imread('./uploads/water.tif')
# 图片合并,按第三维堆叠
dataset = np.dstack([area, dem, slope, ndvi, mndwi, eibi, glcm, band1, band5])
print(dataset.shape)


# 判断该点的有效性（存在特征异常的点都不参与训练，保证了训练数据的真实合理）
def data_select(x, y):
    if (dataset[x, y, 0] != 255) and (0 <= dataset[x, y, 1] <= 361) and (0 <= dataset[x, y, 2] <= 56) and (
            -14 <= dataset[x, y, 3] <= 19) and (-3 <= dataset[x, y, 4] <= 2) and (-26 <= dataset[x, y, 5] <= 27):
        return True
    else:
        return False


# 有效样本取样（训练）
valid = []
for x in range(dataset.shape[0]):
    for y in range(dataset.shape[1]):
        # 遍历，在区域内，记录
        if data_select(x, y):
            valid.append((x, y))
valid = np.array(valid)  # 列表转数组
print("在区域内样本数量：", valid.shape[0])
print(valid)

# 淹没区样本数组（有效数组中取）
inundated = []
random.seed(0)  # 设置随机数种子，每次运行该部分，输出的随机数序列相同
for x, y in valid:
    # 遍历有效数组，满足条件（band==1,band5!=1）,写入作为标签为1的数据
    # 满足要求约46万样本，设置随机数，取1/10
    if (dataset[x, y, 10] == 1) and (dataset[x, y, 11] != 1) and (random.random() < 0.1):
        inundated.append((x, y))
inundated = np.array(inundated)  # 列表转数组
print("淹没区样本数量：", inundated.shape[0])

# 非淹没区样本数组
non_inundated = []
random.seed(0)  # 暂时，每次生成的随机数序列相同
# 取与正样本数量相等的负样本
i = 0
while i < inundated.shape[0]:
    around = True
    #x, y = random.choice(valid)  # 在有效数组范围内随机取点
    index = random.choice(range(valid.shape[0]))  # 随机选择一个索引
    x, y = valid[index]  # 获取坐标点
    # 随机取的点和周围的点(坐标±10)均满足如下条件
    if (dataset[x, y, 10] == 0) and (dataset[x, y, 11] != 1) and (x, y) not in non_inundated:
        for j in range(max(0, x - 10), min(dataset.shape[0], x + 11)):  # range函数，左闭右开，起始不写默认0，终止必写，还可以指定步长
            for k in range(max(0, y - 10), min(dataset.shape[1], y + 11)):
                if (data_select(j, k) != True) or (dataset[j, k, 10] == 1) or (dataset[j, k, 11] == 1):
                    around = False
        if around:
            non_inundated.append((x, y))
            i += 1
non_inundated = np.array(non_inundated)  # 列表转数组
print("非淹没区样本数量：", non_inundated.shape[0])

# 空间因子有效数据归一化
for i in range(1, 10):
    layer = dataset[:, :, i]
    # 确保只有具有有效像素的层才被规范化，并避免了NaN值或无效像素的任何问题。
    if np.isnan(layer[valid[:, 0], valid[:, 1]]).all():
        continue
    min_val = np.nanmin(layer[valid[:, 0], valid[:, 1]])
    max_val = np.nanmax(layer[valid[:, 0], valid[:, 1]])
    normalized_layer = exposure.rescale_intensity(layer[valid[:, 0], valid[:, 1]], in_range=(min_val, max_val),
                                                  out_range=(0, 1))
    dataset[:, :, i][valid[:, 0], valid[:, 1]] = normalized_layer


# 归一化后有效性判断
def data_around(x, y):
    if (dataset[x, y, 0] != 255) and all(0 <= dataset[x, y, i] <= 1 for i in range(1, 10)):
        return True
    else:
        return False


# 输入格式转换函数（坐标→特征矩阵）
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

    # return np.delete(feature_matrix, 8, axis=1)  # 显著性评估实验
    return feature_matrix


# # 输入格式转换函数(邻里效应分析时)
# def input_turn(a, b):
#     feature = 9  # 有效特征数
#     feature_matrix = np.zeros((9, feature))
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             for k in range(0, feature):
#                 feature_matrix[(i + 1) * 3 + j + 1, k] = dataset[a, b, k + 1]
#
#     return feature_matrix


# 样本数据与标签
data = []
label = []
# 正样本标注划分
for x, y in inundated:
    data.append(input_turn(x, y))
    label.append(1)
# 负样本标注划分
for x, y in non_inundated:
    data.append(input_turn(x, y))
    label.append(0)

data = np.array(data)
label = np.array(label)
print(data.shape)
print(label.shape)
print(np.all((data >= 0) & (data <= 1)))
