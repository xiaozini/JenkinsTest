#coding:utf-8
#执行操作
from handle.login_handle import LoginHandle

class LoginBusiness(object):
    def __init__(self,driver):
        self.login_handle = LoginHandle(driver)

   #执行操作
    def login_user_error(self,user,pwd):
        self.login_base(user,pwd)
        if self.login_handle.send_msg('用户名或密码不对'):
            print("用户检验成功")
            return True
        else:
            return False

    def login_pwd_error(self, user, pwd):
        self.login_base(user, pwd)
        if self.login_handle.send_msg('用户名或密码不对'):
            print("密码检验成功")
            return True
        else:
            return False

    def login_base(self, user, pwd):
        self.login_handle.send_user_name(user)
        self.login_handle.send_user_pwd(pwd)
        self.login_handle.btn_submit()
        self.login_handle.logout_btn()


    def logout_btn(self):
        success = self.login_handle.logout_btn()
        if success != None:
            return True
        else:
            return False
