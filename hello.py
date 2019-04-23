# -*- coding: UTF-8 -*-
import os

print("hello world!你好 世界！");
var1 = 12345;
var2 = "12345";
var3 = 12345;
print(var2[::-1]);
print(oct(12));
print(id(var1));
print(id(var2));
print(id(var3));

def getName(str):
	"函数文档字符串"
	print(str);
	return

def getAge():
	pass;

# 函数调用
print("函数调用")
getName(123);
getName(234);

print("打开一个文件，创建文件")
fo = open("e:/wx/python/test/test.txt","w")
fo.write("test Python IO\n")
fo.write("PHP是世界上最好的语言\n")

# 关闭文件流
fo.close()

# 获取系统打开文件的默认路径
print(os.getcwd())
