#coding:utf-8
from business.login_business import LoginBusiness
from selenium import webdriver
import unittest
#登录的用例
class LoginCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://h5-qa.admin.yuedaowang.com/#/driverSettle")
        cls.login_busi = LoginBusiness(cls.driver)

     #用户名错误
    def test_login_user_error(self,user,pwd):
        user = self.login_busi.login_user_error(user,pwd)
        if user == True:
            print("登录失败，此条case执行失败")

    #通过assert判断是否error
    def test_login_pwd_error(self,user,pwd):
        pwd = self.login_busi.login_pwd_error(user,pwd)
        # self.assertFalse(pwd)
        if pwd == True:
            print("登录失败，此条case执行失败")

    def test_login_success(self):
        success = self.login_busi.logout_btn()
        if success == True:
            print('登录成功')

    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        pass
if __name__ == "__main__":
   unittest.main()