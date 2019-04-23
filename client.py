# -*- coding: UTF-8 -*-
# 文件名：client.py

# 导入socket模块
import socket

s = socket.socket();
host = 'localhost'
port = 12345

s.connect((host, port))
print (s.recv(1024).decode())
s.close()