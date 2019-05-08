# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# sender = '919460849@qq.com'
# receivers = ['zl919460849@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')  # 发送者
# message['To'] = Header("测试", 'utf-8')  # 接收者
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")


import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "919460849@qq.com"  # 用户名
mail_pass = "liang340827!"  # 口令

sender = '919460849@qq.com'
receivers = ['zl919460849@126.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")


# import smtplib
# from email.mime.text import MIMEText
#
# msg_from = '919460849@qq.com'  # 发送方邮箱
# passwd = 'liang340827!'  # 填入发送方邮箱的授权码
# msg_to = 'zl919460849@126.com'  # 收件人邮箱
#
# subject = "python邮件测试"  # 主题
# content = "这是我使用python smtplib及email模块发送的邮件"
# msg = MIMEText(content)
# msg['Subject'] = subject
# msg['From'] = msg_from
# msg['To'] = msg_to
# try:
#     s = smtplib.SMTP_SSL("smtp.qq.com",465)# 邮件服务器及端口号
#     s.login(msg_from, passwd)
#     s.sendmail(msg_from,msg_to,msg.as_string())
#     print("发送成功")
#
# except smtplib.SMTPException as e:
#     print("发送失败")
