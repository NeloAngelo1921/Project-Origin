# -*- coding: UTF-8 -*-
# 感知器算法实现 and 逻辑运算

def f(x):
    '''
    定义激活函数f 阶跃函数
    '''
    return 1 if x > 0 else 0

def f2(x):
    '''
    定义激活函数 线性函数
    '''
    return x

def perceptronTest():
    '''
    感知器实现线型分类 训练and感知器
    '''
   
    # 原始数据
    input_vecs = [[1,1], [0,0], [1,0], [0,1]]
    labels = [1, 0, 0, 0]

    # 初始化偏置为0
    bias = 0.0 
     # 初始化权重 默认权重为0
    weights = [0.0 for _ in range(len(input_vecs[0]))]
    # 设置学习率为 0.1 训练轮数为10 
    rate = 0.1
    trans_num = 10
    for i in range(0,trans_num):
        for j in range(len(input_vecs)):
            # 计算训练实际结果
            t = 0
            for w in range(len(weights)):
                t += weights[w] * input_vecs[j][w]
            t += bias
            label = f(t)
            # 更新权重
            for w in range(len(weights)):
                weights[w] += rate * (labels[j] - label) * input_vecs[j][w]
            bias += rate * (labels[j] - label)
    print(weights)
    print(bias)

def LinearUnit():
    '''
    线性回归
    '''
    # 原始数据
    input_vecs = [[5], [3], [8], [1.4], [10.1]]
    labels = [5500, 2300, 7600, 1800, 11400]

    # 初始化偏置为0
    bias = 0.0 
     # 初始化权重 默认权重为0
    weights = [0.0 for _ in range(len(input_vecs[0]))]
    # 设置学习率为 0.01 训练轮数为10 
    rate = 0.01
    trans_num = 10
    for i in range(0,trans_num):
        for j in range(len(input_vecs)):
            # 计算训练实际结果
            t = 0
            for w in range(len(weights)):
                t += weights[w] * input_vecs[j][w]
            t += bias
            label = f2(t)   # 激活函数使用线性函数
            # 更新权重
            for w in range(len(weights)):
                weights[w] += rate * (labels[j] - label) * input_vecs[j][w]
            bias += rate * (labels[j] - label)
    print(weights)
    print(bias)


if __name__ == '__main__': 
    LinearUnit()