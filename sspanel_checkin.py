#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File :sspanel_checkin.py
@Time :2020/04/28 13:09:51
@Author :gc chan 
@Contact :cgc.elvin@gmail.com
@Desc : None
'''

import requests
from bs4 import BeautifulSoup as bs
import sys

login_url = "https://domain_name/auth/login"
checkin_url = "https://domain_name/user/checkin"


class SSPanel():
    def __init__(self, *args):
        headers = {
            "Accept": "text/html, application/xhtml+xml, application/xml",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN, zh",
            "Cache-Control": "max-age = 0",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
        }

        self.session = requests.Session()
        self.session.headers.update(headers)

        if(len(sys.argv) == 3):
            self.email = sys.argv[1]
            self.password = sys.argv[2]
        else:
            self.email = args[0]
            self.password = args[1]

    def login(self):
        postdata = {
            'email': self.email,
            'passwd': self.password,
            'code': '',
            'remember_me': 'on'
        }

        try:
            r = self.session.post(login_url, data=postdata)
            if r.json()["ret"] == 0:
                print(
                    "请检查账号密码是否出错\n使用方法:\n命令行添加参数: sspanel_checkin.py username password\n或在代码中添加账密: sspanel(username, password)")
                return
            elif r.json()["ret"] == 1:
                print(r.json()["msg"])
        except:
            print("登录出错")

    def checkin(self):
        try:
            r = self.session.post(checkin_url)
            print(r.json()["msg"])
        except:
            print("签到出错")


def main():
    ss = SSPanel()
    ss.login()
    ss.checkin()


if __name__ == '__main__':
    main()
