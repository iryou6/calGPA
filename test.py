
import urllib
import urllib.request
import http.cookiejar
import re


#山东大学绩点运算
class SDU:

    def __init__(self):
        self.loginUrl = 'https://pawscas.usask.ca/cas-web/login?service=https%3A%2F%2Fpaws5.usask.ca%2Fc%2Fportal%2Flogin'
        self.cookies = http.cookiejar.CookieJar()
        self.postdata = urllib.parse.urlencode({
            'username':'dax599',
            'password':'xDy199326'
         })
        self.opener = urllib.request.urlopen(urllib.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        request  = urllib.Request(
            url = self.loginUrl,
            data = self.postdata)
        result = self.opener.open(request)
        #打印登录内容
        print(result.read().decode('gbk'))


sdu = SDU()
sdu.getPage()