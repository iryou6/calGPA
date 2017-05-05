import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re

agent = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
headers = {
    'Host':'pawscas.usask.ca',
    'Origin':'https://pawscas.usask.ca',
    'Referer':'https://pawscas.usask.ca/cas-web/login?service=https%3A%2F%2Fpaws5.usask.ca%2Fc%2Fportal%2Flogin',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':agent
}

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename='cookies')
try:
    session.cookies.load(ignore_discard=True)
except:
    print("Cookie 未能加载")

def login():
    post_url = 'https://pawscas.usask.ca/cas-web/login?service=https%3A%2F%2Fpaws5.usask.ca%2Fc%2Fportal%2Flogin'
    post_data={
        'username':'dax599',
        'password':'xDy199326'
    }
    login_page = session.post(url=post_url, data=post_data, headers=headers)
    print(login_page.status_code)


if __name__ == '__main__':
    login()
    pawsurl='https://paws5.usask.ca/web/home-community'
    pawsrespones=session.get(url=pawsurl,headers=headers)

    print(pawsrespones.status_code)
