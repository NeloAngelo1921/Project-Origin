# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 发件人邮箱账号
my_sender = 'wxiao0921@qq.com'
# 授权码
# my_pass = 'wkvvdtgtaejmfhef'
my_pass = 'jlyyxndlqatobjib'
# 收件人邮箱账号
my_user = 'wxiao1921@qq.com'
def mail(title,mailbody):
    ret=True
    try:
        msg = MIMEText(mailbody,'plain','utf-8')
        msg['From'] = formataddr(["月华君",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["潇儿思密达",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = title             # 邮件的主题，也可以说是标题
 
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret
bt = "1334"
mailMessage = "嘻嘻嘻嘻！"
ret=mail(bt,mailMessage)
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")