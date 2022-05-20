import json
import random
from random import randint

import requests
import time
import datetime
import os
import sys

from bs4 import BeautifulSoup
import urllib3


class User:
    def __init__(self,name,username,password,qq):
        self.name = name
        self.username = username
        self.password = password
        self.qq = qq

def checkDaka(user:User):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
    loginUrl = "http://zyt.zjnu.edu.cn/H5/Login.aspx"

    checkUrl = "http://zyt.zjnu.edu.cn/H5/ZJSFDX/CheckFillIn.aspx"

    headers = {
        "Content-Type":"application/x-www-form-urlencoded",
        'User-Agent': random.choice(user_agent_list)
    }

    session=requests.session() #使用session会话技术自动保存所有cookie
    session.headers.update(headers)
    body = {
        "__VIEWSTATE":"/wEPDwUKMjAwMjg1NDgwNQ9kFgICAw9kFgYCAQ8PFgIeBFRleHQFLea1meaxn+W4iOiMg+Wkp+WtpuaImOeWq+mAmuS/oeaBr+ebtOaKpeezu+e7n2RkAgcPFgIfAAUZ55So5oi35ZCN5oiW5a+G56CB6ZSZ6K+vIWQCCw8WAh8AZWRkUqgrcKX6bTUJPg4n2cRud+UUkaHvQwWfp3I0fVoPxac="
        ,"btn_Login":"登录 Log In".encode('GB2312')
        ,"__VIEWSTATEGENERATOR":"C483C0FE"
        ,"__EVENTVALIDATION":"/wEdAASrKE/z5+btNhh89+mHDvOF0elL860XNtv4rogmL6mawP3Vqw5XZsL40jZDizLHlCVw1VqEhL0Qs5iJV9Ksp6V6Yxb2oGgMWJsg3EGFyIpPh0b5BCgVWfZeIaGuiGQ/GCg="
       ,"UserText":user.username
       ,"PasswordText":user.password
    }
    #time.sleep(10)
    res = session.post(url = loginUrl, data = body)
    time.sleep(5)
    res = session.get(checkUrl)
    if '<div id="check1" style="display:;">' in res.text:
        return False
    elif '<div id="check1" style="display:none;">' in res.text:
        return True
    else :
        # 说明zyt代码有更新，提示赶快更新代码
        return 'error'
if __name__ == '__main__':
    aaa= User("姓名", "学号", "密码", "qq")
    users = [
        aaa
    ]
    for e in users:
        res = checkDaka(e)
        print(res)