# !/usr/bin/env python3
# -*- encoding: utf-8 -*-
# author: elvin

import sys
from datetime import datetime

import requests


class SSPanel(object):

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

        if len(sys.argv) == 4:
            self.email = sys.argv[1]
            self.password = sys.argv[2]
            self.url_domain = sys.argv[3]
            self.url_login = "{}/auth/login".format(self.url_domain)
            self.url_checkin = "{}/user/checkin".format(self.url_domain)

        elif len(sys.argv) > 1 and len(sys.argv) != 4:
            print("命令行参数格式错误")
            return

        else:
            self.email = args[0]
            self.password = args[1]
            self.url_domain = args[2]
            self.url_login = "{}/auth/login".format(self.url_domain)
            self.url_checkin = "{}/user/checkin".format(self.url_domain)

        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # 打印时间信息
        self.session.get(self.url_domain)

        self.login()  # 登录
        self.checkin()  # 签到

    def login(self):
        """登录函数
        """
        postdata = {
            'email': self.email,
            'passwd': self.password,
            'code': '',
            # 'remember_me': 'on'
        }

        try:
            self.session.get(self.url_login)
            r = self.session.post(self.url_login, data=postdata)
            # print(r.json())
            if r.json()["ret"] == 0:
                print("""请检查账号密码是否出错
使用方法:
命令行添加参数: sspanel_checkin.py username password domain
或在代码中添加账密: sspanel(username, password, domain)""")
                return
            elif r.json()["ret"] == 1:
                print(r.json()["msg"])
        except Exception as e:
            print("登录出错")
            print(e)

    def checkin(self):
        """签到函数
        """
        try:
            r = self.session.post(self.url_checkin)
            print(r.json()["msg"])
        except Exception as e:
            print("签到出错")
            print(e)


if __name__ == '__main__':
    # SSPanel(username, password, domain)
    SSPanel()
