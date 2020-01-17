#coding:utf-8
from base.find_element import FindElement

#读取元素的信息，然后用handle层读取该层
class LoginPage(object):

    def __init__(self,driver):
        self.find_element = FindElement(driver)

    def get_user_element(self):
        return self.find_element.get_element("user_name")

    def get_pwd_element(self):
        return self.find_element.get_element("user_name")

    def get_btn_element(self):
        return self.find_element.get_element("btn")

    def get_text_element(self):
        return self.find_element.get_element("msg")

