import sys
import re
import urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.parse, urllib.error
import requests
import http.cookiejar
import imp

## 这段代码是用于解决中文报错的问题
# imp.reload(sys)
# sys.setdefaultencoding("utf8")
#####################################################
# 登录人人
loginurl = 'http://www.renren.com/PLogin.do'
logindomain = 'renren.com'


class Login(object):
    def __init__(self):
        self.name = ''
        self.passwprd = ''
        self.domain = ''

        self.cj = http.cookiejar.LWPCookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cj))
        urllib.request.install_opener(self.opener)

    def setLoginInfo(self, username, password, domain):
        '''''设置用户登录信息'''
        self.name = username
        self.pwd = password
        self.domain = domain

    def login(self):
        '''''登录网站'''
        loginparams = {'domain': self.domain, 'email': self.name, 'password': self.pwd}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
        req = urllib.request.Request(loginurl, urllib.parse.urlencode(loginparams), headers=headers)
        response = urllib.request.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()


if __name__ == '__main__':
    userlogin = Login()
    username = 'username'
    password = 'password'
    domain = logindomain
    userlogin.setLoginInfo(username, password, domain)
    userlogin.login()