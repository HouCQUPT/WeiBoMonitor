# -*- author:H -*-
# -*- UTF-8 -*-


import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests
from bs4 import BeautifulSoup
import time


My_headers = {"Host": "weibo.cn",
              "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}


def info_cookie():
    """
    return WeiBo cookies
    :return: cookies
    """
    with open("cookie.txt", "r+") as f:
        info = f.read()
    dic = {}
    info = info.strip().split(":")
    dic[info[0]] = info[1]
    return dic


def info_mail():
    """
    返回 发送邮件地址，SMTP口令， 接受邮件地址
    :return: send_mail, license, rece_mail
    """
    dic = {}
    with open("config.txt","r+") as f:
        info = f.read()
    for line in info:
        line = line.strip().split(":")
        try:
            dic[line[0]] = line[1]
        except IndexError:
            pass
    return dic


def send_email(send_mail, rece_mail, license):
    mail_host = "SMTP.QQ.COM"  # 设置服务器
    mail_user = send_mail      # 用户名
    mail_pass = license        # 口令

    sender = send_mail
    receivers = rece_mail  # 接收邮件

    message = MIMEText("更新请查看", 'plain', 'utf-8')
    message['From'] = Header("Python Shell", 'utf-8')
    message['To'] = Header("your name", 'utf-8')

    subject = '微博更新提示'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        print("登陆成功")
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


def wei_bo(headers, monitor_usr):
    """
    :type: monitor_usrURL: basestring
    :type: headers: dir
    :param headers: 请求头
    :param monitor_usr: 被监控微博URL
    :rtype: id: basestring
    :return: id
    """
    girl_url = monitor_usr
    r_url = requests.get(girl_url, headers=headers)
    print(r_url.text)
    soup = BeautifulSoup(r_url.text, "html.parser")
    first = soup.find_all('div', attrs={"id": True})[0]
    id = first.get('id')
    return id


if __name__ == "__main__":
    cookie = info_cookie()# type:dict
    config = info_mail()  # type:dict
    monitor_url = "URL"   # 监控微博Host URL
    while True:
        with open("new_id.txt", "r+") as f:
            old_id = f.read()
        new_id = wei_bo(dict(My_headers, **cookie), monitor_url)
        if new_id != old_id:
            """
            更新
            """
            send_email(config["send_mail"], config["rece_mail"], config["license"])
            with open("new_id.txt", "w+") as f:
                f.write(new_id)
        else:
            pass
        time.sleep(300)






