import requests
import time
import datetime
from DrissionPage import ChromiumPage


# 创建页面对象，并启动或接管浏览器
page = ChromiumPage()
# 跳转到登录页面
page.get('https://buyanbuyan.com/user-login.htm')

# 同意协议按钮
page.ele('#isClose').click()
# 定位到账号文本框，获取文本框元素
ele = page.ele('#email')
# 输入对文本框输入账号
ele.input('3617637203@qq.com')
# 定位到密码文本框并输入密码
page.ele('#password').input('yu090517')
# 点击登录按钮
page.ele('#submit').click()
# 等待页面加载
page.wait.load_start()
ele1 = page.ele('#body')
ele2 = ele1.ele('.container')
ele3 = ele2.ele('.row')
ele4 = ele3.ele('.col-lg-9 main')
ele5 = ele4.ele('.card card-threadlist')
ele6 = ele5.ele('.card-header')
ele7 = ele6.ele('.nav nav-tabs card-header-tabs')
ele8 = ele7.ele('.btn btn-primary ft')
page.ele(ele8).click()
time.sleep(5)
page.quit()
print('签到完毕')
nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=12e11bff-cd9c-4893-b893-7a177510f650"

data = {
   "msgtype": "text",
    "text": {
        "content": nowtime + "已签到"
    }
}

response = requests.post(url, json=data)
