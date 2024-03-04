from data_read import *

import numpy as np
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
import torch.optim as optim

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# torch重整型号
data = data.reshape(-1, 1, 9, 9)
# data = data.reshape(-1, 1, 9, 8)  # 显著性分析
label = label.reshape(-1, 1)
print(data.shape)
print(label.shape)

# 训练集和测试集划分
X_train, X_test, y_train, y_test = train_test_split(data, label, test_size=0.3, random_state=0)
print(X_train.shape)
print(X_test.shape)
print(np.isnan(X_train).any())
print(np.isinf(X_train).any())
# 格式转换
X_train = torch.from_numpy(X_train).float()
X_test = torch.from_numpy(X_test).float()
y_train = torch.from_numpy(y_train).float()
y_test = torch.from_numpy(y_test).float()
# 创建数据集和对象
train_dataset = torch.utils.data.TensorDataset(X_train, y_train)
test_dataset = torch.utils.data.TensorDataset(X_test, y_test)
trainloader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True)
testloader = torch.utils.data.DataLoader(test_dataset, batch_size=64, shuffle=False)


# 网络定义
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 64, 3, stride=1, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
            nn.Conv2d(64, 128, 3, stride=1, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),
        )
        self.classifier = nn.Sequential(
            nn.Linear(128 * 2 * 2, 2048),
            nn.ReLU(inplace=True),
            nn.Dropout(0.2),
            nn.Linear(2048, 1),
            nn.Sigmoid()
        )

        # 权重初始化
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_uniform_(m.weight, nonlinearity='relu')
            elif isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x


model = Net()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters())

# 训练模型
# 测试集精度连续10次没有提升，提前终止训练；每次训练保存测试集精度最高的模型（命名规范）
train_losses = []
train_accs = []
test_losses = []
test_accs = []
best_test_acc = 0.0
test_acc_not_improve = 0

for epoch in range(100):
    running_loss = 0.0
    correct = 0
    total = 0
    # 训练模式
    model.train()
    for i, data in enumerate(trainloader):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        predicted = (outputs > 0.5).float()
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    # 训练过程的损失和精确度
    train_loss = running_loss / len(trainloader)
    train_acc = correct / total
    train_losses.append(train_loss)
    train_accs.append(train_acc)

    # 测试集上评估模型
    test_loss = 0.0
    correct = 0
    total = 0
    # 评估模式
    model.eval()
    with torch.no_grad():
        for data in testloader:
            inputs, labels = data
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            test_loss += loss.item()
            predicted = (outputs > 0.5).float()
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    # 测试集上的损失和精确度
    test_loss /= len(testloader)
    test_acc = correct / total
    test_losses.append(test_loss)

    
    test_accs.append(test_acc)

    # 判断测试集上的精度提升情况
    if test_acc > best_test_acc:
        best_test_acc = test_acc
        test_acc_not_improve = 0
        torch.save(model.state_dict(), "best_model.pt")
    else:
        test_acc_not_improve += 1

    print('Epoch %d train loss: %.3f train accuracy: %.3f test loss: %.3f test accuracy: %.3f' % (
        epoch + 1, train_loss, train_acc, test_loss, test_acc))

    if test_acc_not_improve >= 10:
        print("测试集精度10epoch未提升,训练结束")
        break

# loss作图
plt.plot(train_losses, label='Training Loss')
plt.plot(test_losses, label='Testing Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()
# 精确度作图
plt.plot(train_accs, label='Training Accuracy')
plt.plot(test_accs, label='Testing Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# ROC曲线绘制
model_best = Net()
model_best.load_state_dict(torch.load("best_model.pt"))

y_train_true = []
y_train_score = []
y_test_true = []
y_test_score = []

model_best.eval()
with torch.no_grad():
    for data in trainloader:
        inputs, labels = data
        outputs = model_best(inputs)
        y_train_score += outputs.tolist()
        y_train_true += labels.tolist()
with torch.no_grad():
    for data in testloader:
        inputs, labels = data
        outputs = model_best(inputs)
        y_test_score += outputs.tolist()
        y_test_true += labels.tolist()

# 训练集参数计算
fpr_train, tpr_train, thresholds_train = roc_curve(y_train_true, y_train_score)
roc_auc_train = auc(fpr_train, tpr_train)
# 测试集参数计算
fpr_test, tpr_test, thresholds_test = roc_curve(y_test_true, y_test_score)
roc_auc_test = auc(fpr_test, tpr_test)

# 曲线绘制
plt.plot(fpr_train, tpr_train, label='Training set (AUC = %0.4f)' % roc_auc_train)
plt.plot(fpr_test, tpr_test, label='Testing set (AUC = %0.4f)' % roc_auc_test)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()

# 模型的准确率
model_test = Net()
model_test.load_state_dict(torch.load("best_model.pt"))

correct_train = 0
total_train = 0
correct_test = 0
total_test = 0

model_test.eval()
with torch.no_grad():
    for data in trainloader:
        inputs, labels = data
        outputs = model_test(inputs)
        predicted = (outputs > 0.5).float()
        total_train += labels.size(0)
        correct_train += (predicted == labels).sum().item()
with torch.no_grad():
    for data in testloader:
        inputs, labels = data
        outputs = model_test(inputs)
        predicted = (outputs > 0.5).float()
        total_test += labels.size(0)
        correct_test += (predicted == labels).sum().item()

print('again train accuracy: %.6f' % (correct_train / total_train))
print('again test accuracy: %.6f' % (correct_test / total_test))


