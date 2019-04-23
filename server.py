# -*- coding: UTF-8 -*-
# 文件名: server.py

# 导入socket模块
import socket

# 创建socket对象
s = socket.socket()

# 获取本地主机名
host = 'localhost'

# 设置端口号
port = 12345

# 绑定端口号
s.bind((host, port))

# 等待客户端连接
s.listen(5)
while True:
	c,addr = s.accept()
	print ('连接地址：', addr)
	c.send('欢迎'.encode())
	c.close()	# 关闭连接