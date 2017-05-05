import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import http.cookiejar
import re


class SDU:

    def __init__(self):
        self.loginUrl = 'https://pawscas.usask.ca/cas-web/login?service=https%3A%2F%2Fpaws5.usask.ca%2Fc%2Fportal%2Flogin'
        self.cookies = http.cookiejar.CookieJar()
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
        self.postdata = urllib.parse.urlencode({
            'username':'dax599',
            'password':'xDy199326',
            # 'lt':'LT-3662517-KsuvzFdPnjgi6mkRSL3Zc6xg6wIxgN',
            # 'execution':'e5s1',
            # '_eventId':'submit'
         })
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookies))

    def getPage(self):
        binary_data = self.postdata.encode('utf8')
        request  = urllib.request.Request(
            url = self.loginUrl,
            data = binary_data,
            headers=self.header)
        result = self.opener.open(request)
        #打印登录内容
        print(result.read().decode('gbk'))


sdu = SDU()
sdu.getPage()