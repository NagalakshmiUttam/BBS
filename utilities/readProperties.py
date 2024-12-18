import configparser
import os

config=configparser.RawConfigParser()
#config.read(os.path.abspath(os.curdir)+'\\Configurations\\config.ini')
config.read(r"C:\\Users\\Nagalakshmi S\\Desktop\\Bix\\bbsAutomation\\configurations\\config.ini")
# config.read(".\\Configurations\\config.ini")
class ReadConfig:
    @ staticmethod
    def getApplicationURL():
        url=config.get('commonInfo', 'baseURL')
        return url
    
    @ staticmethod
    def getUseremail():
        email=config.get('commonInfo', 'email')
        return email
    
    @ staticmethod
    def getPassword():
        password=config.get('commonInfo', 'password')
        return password
