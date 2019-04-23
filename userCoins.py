# -*- coding: UTF-8 -*-
import requests
import json
import pymysql

def getHTMLText(id):
	try:
		url = 'https://api.bilibili.com/x/space/acc/info?mid=' + str(id) + '&jsonp=jsonp'
		headers = {
			"Content-Type": "application/x-www-form-urlencoded",
			"Referer": "https://space.bilibili.com",  # 必须带这个参数，不然会报错
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
        }
		results = requests.get(url,headers).text
		return results
	except:
		return 'error'
		
if __name__ == '__main__':

	# 打开数据库连接
	db = pymysql.connect("123.206.91.197","root","root","origin" )
 
	# 使用 cursor() 方法创建一个游标对象 cursor
	cursor = db.cursor()
	
	for id in range(7152,213969247):
		try:
			data = json.loads(getHTMLText(id))
			if data != 'error' and data["code"] == 0 and "data" in data:
				coins = ''
				if "coins" in data["data"]:
					coins = data["data"]["coins"]
				# SQL 插入语句
				sql = "INSERT INTO user_coins(mid, coins) \
						VALUES (%s, '%s')" % \
						(id, coins)
				try:
					# 执行sql语句
					cursor.execute(sql)
					# 提交到数据库执行
					db.commit()
					print(id, '用户硬币数入库成功！')
				except:
					# 如果发生错误则回滚
					db.rollback()
			else:
				print(id, '用户信息获取失败')
		except:
			print('用户信息获取失败')