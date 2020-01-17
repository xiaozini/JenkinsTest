#coding:utf-8
from business.login_business import LoginBusiness

#登录的用例
class LoginCase(object):

    def __init__(self,driver):
        self.login_busi = LoginBusiness(driver)

     #用户名错误
    def test_login_user_error(self,user,pwd):
        self.login_busi.login_user(user,pwd)

    #通过assert判断是否error
    def test_login_pwd_error(self,user,pwd):
        self.login_busi.login_pwd(user,pwd)

    def test_login_success(self,user,pwd):
        self.login_busi.login_base(user,pwd)