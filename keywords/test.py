# coding:utf8
from keywords.web import Web


# 创建一个关键字对象，用来调用功能
web = Web()

# 打开浏览器
web.openbrowser()
web.geturl('http://112.74.191.10:8000/index.php')

# 登录
web.click('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
web.input('//*[@id="username"]','13800138006')
web.input('//*[@id="password"]','123456')
web.input('//*[@id="verify_code"]','1111')
web.click('//*[@id="loginform"]/div/div[6]/a')

# 搜索
web.input('//*[@id="q"]','手机')
web.click('//*[@id="sourch_form"]/a')

# 购物车
web.click('/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[5]/div[2]/a')
web.click('//*[@id="join_cart"]')
web.sleep(1)
web.click('//*[@id="layui-layer1"]/span/a')
web.moveto('//*[@id="hd-my-cart"]/a/div')







