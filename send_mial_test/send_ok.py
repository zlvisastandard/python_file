import smtplib  #加载smtplib模块from email.mime.text import MIMEText
from email.mime.text import MIMEText
from email.utils import formataddr

def mail():
    # user_list = '18868875563@163.com'

    user_list = "919460849@qq.com"
    sub = 'hello world'
    content = 'hello world'
    my_sender='zl919460849@126.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量

    msg=MIMEText(content,'plain','utf-8')

    msg['From']=formataddr(["hello world",my_sender])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["收件人邮箱昵称",user_list])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']=sub #邮件的主题，也可以说是标题
    try:
        server=smtplib.SMTP("smtp.126.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender,"love340827")    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[user_list],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
        print("发送成功...")

    except smtplib.SMTPException as e:
        print("发送失败...")


mail()