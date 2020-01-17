#coding:utf-8
import configparser
class ReadIni(object):
    def __init__(self,node=None,fileName=None):
        if fileName == None:
            fileName = "F:/yy/appDemo/selenium_test1/config/config.ini"
        if node == None:
            self.node = "login_element"
        else:
            self.node = node
        self.cf = self.load_ini(fileName)

    def load_ini(self,fileName):
        cfconfig = configparser.ConfigParser()
        cfconfig.read(fileName)
        return cfconfig

    def get_value(self,key):
        data = self.cf.get(self.node,key)
        return data

if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value("user_name"))