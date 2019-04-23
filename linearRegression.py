# -*- coding: UTF-8 -*-
# 机器学习算法：线性回归

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# 设置随机数的可预见性，即生成123个随机数时随机数相同
np.random.seed(123)

# 原始数据集类似于((x,y),(x,y),(x,y)...)
# X的数据在2*（0~1）之间即0~2之间 rand取在0~1之间的随机数 生成(500,1)的矩阵
X = 2 * np.random.rand(500,1)
# randn从标准正态分布中返回一个或多个样本值
y = 5 + 3 * X + np.random.randn(500,1)
# fig = plt.figure(figsize=(8,6))
# plt.scatter(X, y)
# plt.title("Dataset")
# plt.xlabel("First feature")
# plt.ylabel("Second feature")
# plt.show()

# 数据集切片拆分
# train_test_split函数用于将矩阵随机划分为训练子集和测试子集，并返回划分好的训练集测试集样本和训练集测试集标签。
X_train, X_test, y_train, y_test = train_test_split(X, y)
print(f'Shape X_trans:{X_train.shape}')
print(f'Shape y_train:{y_train.shape}')
print(f'Shape X_test:{X_test.shape}')
print(f'Shape y_test:{y_test.shape}')

# 线性回归分类
class LinearRegression:
    
    def __init__(self):
        pass

    def train_gradient_descent(self, X, y, learning_rate=0.01, n_iters=100):
        '利用梯度下降模型训练线性回归'
        # 0.初始化参数
        n_samples, n_features = X.shape
        # np.zeros生成对应格式的数据，如下则是一个(n_features,1)的矩阵
        self.weights  = np.zeros(shape=(n_features,1))
        self.bias = 0
        costs = []

        for i in range(n_iters):
            # 1.计算输入特征和权重的线性组合
            y_predict = np.dot(X, self.weights) + self.bias

            # 2.计算训练集成本
            cost = (1 / n_samples) * np.sum((y_predict - y)**2)
            costs.append(cost)

            if i % 100 == 0:
                print(f'Cost at iteration{i}:{cost}')
            
            # 3.计算梯度
            dJ_dw = (2 / n_samples) * np.dot(X.T, (y_predict - y))
            dJ_db = (2 / n_samples) * np.sum((y_predict - y))

            # 4.更新参数
            self.weights = self.weights - learning_rate * dJ_dw
            self.bias = self.bias - learning_rate * dJ_db
        
        return self.weights, self.bias, costs
    
    def train_normal_equation(self, X, y):
        '利用正态方程训练线性回归模型'
        self.weights = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
        self.bias = 0
        return self.weights, self.bias

    def predict(self,X):
        return np.dot(X, self.weights) + self.bias

# 使用梯度下降就行训练
n_iters = 600
regressor = LinearRegression()
w_trained, b_trained, costs = regressor.train_gradient_descent(X_train, y_train, learning_rate=0.005, n_iters=600)
# fig = plt.figure(figsize=(8,6))
# plt.plot(np.arange(n_iters), costs)
# plt.title("Development of cost during training")
# plt.xlabel("Number of iterations")
# plt.ylabel("Cost")
# plt.show()

# 测试梯度下降模型
n_samples, _ = X_train.shape
n_samples_test, _ = X_test.shape

y_p_train = regressor.predict(X_train)
y_p_test = regressor.predict(X_test)

error_train = (1 / n_samples) * np.sum((y_p_train - y_train) ** 2)
error_test = (1 / n_samples_test) * np.sum((y_p_test- y_test) ** 2)

print(f"Error on training set: {np.round(error_train, 4)}")
print(f"Error on test set: {np.round(error_test)}")

# 使用回归方程训练
# X_b_train = np.c_[np.ones((n_samples)), X_train]
# X_b_test = np.c_[np.ones((n_samples_test)), X_test]

# reg_normal = LinearRegression()
# w_trained = reg_normal.train_normal_equation(X_b_train, y_train)

# # 测试回归方程模型
# y_p_train = reg_normal.predict(X_b_train)
# y_p_test = reg_normal.predict(X_b_test)

# error_train =  (1 / n_samples) * np.sum((y_p_train - y_train) ** 2)
# error_test =  (1 / n_samples_test) * np.sum((y_p_test - y_test) ** 2)

print(f"Error on training set: {np.round(error_train, 4)}")
print(f"Error on test set: {np.round(error_test, 4)}")

fig = plt.figure(figsize=(8,6))
# plt.scatter(X_train, y_train)
plt.scatter(X_test, y_p_test)
plt.xlabel("First feature")
plt.ylabel("Second feature")
plt.show()