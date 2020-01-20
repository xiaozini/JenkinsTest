#coding:utf-8
from page.login_page import LoginPage

#操作层--用来输入用户信息
class LoginHandle(object):

    def __init__(self,driver):
        self.login_page = LoginPage(driver)

    #输入用户名
    def send_user_name(self,user):
        self.login_page.get_user_element().send_keys(user)

    # 输入密码
    def send_user_pwd(self,pwd):
        self.login_page.get_pwd_element().send_keys(pwd)

     #提示信息
    def send_msg(self,info,user_info):
        if info == 'msg':
            self.login_page.get_text_element().get_attribute("value")

        # 点击按钮
    def btn_submit(self):
        self.login_page.get_btn_element().click()

    #退出登录按钮
    def logout_btn(self):
        return self.login_page.get_logout_btn().text()
