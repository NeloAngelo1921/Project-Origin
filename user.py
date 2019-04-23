# -*- coding: UTF-8 -*-
import requests
import json
import pymysql

def getHTMLText(id):
	try:
		url = 'https://space.bilibili.com/ajax/member/GetInfo'
		# kv = {'user-agent' : 'Mozilla/5.0','Referer':'https://space.bilibili.com'}
		headers = {
			"Content-Type": "application/x-www-form-urlencoded",
			"Referer": "https://space.bilibili.com",  # 必须带这个参数，不然会报错
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        }
		form_data = {'mid': id}
		results = requests.post(url, form_data, headers=headers).text
		return results
	except:
		return 'error'
		
if __name__ == '__main__':
	
	# 打开数据库连接
	db = pymysql.connect("123.206.91.197","root","root","origin" )
 
	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()
	
	for id in range(270663,213969247):
		try:
			data = json.loads(getHTMLText(id))
			if data != 'error' and data["status"]:
				name = data["data"]["name"]
				sex = data["data"]["sex"]
				rank = data["data"]["rank"]
				regtime = ""
				if "regtime" in data["data"].keys():
					regtime = data["data"]["regtime"]
				spacesta = data["data"]["spacesta"]
				birthday = ""
				if "birthday" in data["data"].keys():
					birthday = data["data"]["birthday"]
				sign = ""
				if "sign" in data["data"].keys():
					sign = data["data"]["sign"].replace("'","").replace("\r","").replace("\n","").replace("\t","")
				level = data["data"]["level_info"]["current_level"]
				# SQL 插入语句
				sql = "INSERT INTO user_bilibili(mid, name, sex, rank, regtime, spacesta, birthday, sign, level) \
						VALUES (%s, '%s',  '%s',  %s,  '%s', %s, '%s', '%s', '%s')" % \
						(id, name, sex, rank, regtime, spacesta, birthday, sign, level)
				print(sql)
				try:
					# 执行sql语句
					cursor.execute(sql)
					# 提交到数据库执行
					db.commit()
					print(id, '用户信息入库成功！')
				except:
					# 如果发生错误则回滚
					db.rollback()
			else:
				print(id,"用户信息获取失败！")
		except:
			print("用户信息解析失败")
	# 关闭数据库连接
	db.close()