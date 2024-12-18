
import datetime
import os
from selenium.webdriver.common.by import By
from utilities import XLUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.locators import LocatorsHomePage
from page_objects.locators import LocatorsMenu
from page_objects.locators import LocatorsContact
from page_objects.locators import LocatorsJobs
from allure_commons.types import AttachmentType
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import xlsxwriter
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException 
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver
import pyautogui
import shutil
from openpyxl import Workbook
import time
import xlsxwriter

class ContactPage():
    
    path=r"test_data\BBS6.xlsx"

    def __init__(self,driver):
        self.driver=driver

    def create_excel(self):
    
        wb = Workbook()
        file_path = "test_data"
        create_duplicate = 'BixBytes website' + str(datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')) + '.xlsx'
        replica = os.path.join(file_path, create_duplicate)
        wb.save(replica)
        source = "test_data\BBS6.xlsx"
        dest = replica
        shutil.copy(source, dest)

#================================================================CONTACT PAGE================================================================
    def click_hamburger(self):
        self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()

    def menu_contact_link(self):
        menu_contact_link=XLUtils.readData(self.path,"Contact",3,2)
        print(menu_contact_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_contact_link))
        print((self.driver.find_element(*LocatorsMenu().menu_contact_link)).text)
        if (self.driver.find_element(*LocatorsMenu().menu_contact_link)).text == menu_contact_link:
            XLUtils.writeData(self.path,"Contact",3,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",3,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",3,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",3,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(2)
        contact=self.driver.find_element(*LocatorsMenu.menu_contact_link)
        self.driver.execute_script('arguments[0].click()', contact)
        time.sleep(2)

    def scroll_down_Page(self):
        logo= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsContact.contact_page_hdline))
        logo.click()
        for i in range(0,5):
            if i<12:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
                 time.sleep(1)

    def scroll_up_Page(self):
        for i in range(0,5):
            if i<12:
                 ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
                 time.sleep(1)
        hamburger=self.driver.find_element(*LocatorsContact.hamburger_contact_page)
        self.driver.execute_script('arguments[0].click()', hamburger)
        time.sleep(2)
        self.driver.refresh()
        # self.driver.back()

    def scroll_stop_between(self):
        txt= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((LocatorsContact.contact_page_hdline)))
        txt.click()
        for i in range(0,3):
            if i<5:
                 ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                 time.sleep(1)

    def contact_page_hdline(self):
        contact_page_hdline=XLUtils.readData(self.path,"Contact",4,2)
        print(contact_page_hdline)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsContact.contact_page_hdline))
        print((self.driver.find_element(*LocatorsContact().contact_page_hdline)).text)
        if (self.driver.find_element(*LocatorsContact().contact_page_hdline)).text == contact_page_hdline:
            XLUtils.writeData(self.path,"Contact",4,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",4,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",4,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",4,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def contpage_name_txtfield(self):
        contpage_name_txtfield=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_name_txtfield))
        contpage_name_txtfield.send_keys("abc")

    def contpage_email_txtfield(self):
        contpage_email_txtfield=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_email_txtfield))
        contpage_email_txtfield.send_keys("abc")

    def contpage_phnnum_txtfield(self):
        contpage_phnnum_txtfield=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_phnnum_txtfield))
        contpage_phnnum_txtfield.send_keys("123")

    def contpage_proj_txtfield(self):
        contpage_proj_txtfield=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_proj_txtfield))
        contpage_proj_txtfield.send_keys("techruler")

    def contpage_des_txtfield(self):
        contpage_des_txtfield=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_des_txtfield))
        contpage_des_txtfield.send_keys("HRM based")

    def contpage_chbox_captcha(self):
        captcha=self.driver.find_element(*LocatorsContact.contpage_chbox_captcha)
        self.driver.execute_script('arguments[0].click()', captcha)

    def contpage_lets_dscs_btn(self):
        # for i in range(0,2):
        #     if i<2:
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        btn=self.driver.find_element(*LocatorsContact.contpage_lets_dscs_btn)
        self.driver.execute_script('arguments[0].click()', btn)

    def contpage_errmsg_invalid_email(self):
        contpage_errmsg_invalid_email=XLUtils.readData(self.path,"Contact",12,2)
        print(contpage_errmsg_invalid_email)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsContact.contpage_errmsg_invalid_email))
        print((self.driver.find_element(*LocatorsContact().contpage_errmsg_invalid_email)).text)
        if (self.driver.find_element(*LocatorsContact().contpage_errmsg_invalid_email)).text == contpage_errmsg_invalid_email:
            XLUtils.writeData(self.path,"Contact",12,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",12,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",12,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",12,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def contpage_errmsg_invalid_phone(self):
        contpage_errmsg_invalid_phone=XLUtils.readData(self.path,"Contact",13,2)
        print(contpage_errmsg_invalid_phone)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsContact.contpage_errmsg_invalid_phone))
        print((self.driver.find_element(*LocatorsContact().contpage_errmsg_invalid_phone)).text)
        if (self.driver.find_element(*LocatorsContact().contpage_errmsg_invalid_phone)).text == contpage_errmsg_invalid_phone:
            XLUtils.writeData(self.path,"Contact",13,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",13,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",13,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",13,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def contpage_warmsg_name(self):
        contpage_name_txtfield=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_name_txtfield))
        contpage_name_txtfield.click()
        contpage_email_txtfield=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_email_txtfield))
        contpage_email_txtfield.click()
        contpage_warmsg_name=XLUtils.readData(self.path,"Contact",6,2)
        print(contpage_warmsg_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsContact.contpage_warmsg_name))
        print((self.driver.find_element(*LocatorsContact().contpage_warmsg_name)).text)
        if (self.driver.find_element(*LocatorsContact().contpage_warmsg_name)).text == contpage_warmsg_name:
            XLUtils.writeData(self.path,"Contact",6,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",6,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",6,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",6,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def contpage_warmsg_email(self):
        contpage_phnnum_txtfield=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_phnnum_txtfield))
        contpage_phnnum_txtfield.click()
        contpage_warmsg_email=XLUtils.readData(self.path,"Contact",7,2)
        print(contpage_warmsg_email)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsContact.contpage_warmsg_email))
        print((self.driver.find_element(*LocatorsContact().contpage_warmsg_email)).text)
        if (self.driver.find_element(*LocatorsContact().contpage_warmsg_email)).text == contpage_warmsg_email:
            XLUtils.writeData(self.path,"Contact",7,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",7,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",7,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",7,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def contpage_warmsg_phnnum(self):
        contpage_proj_txtfield=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_proj_txtfield))
        contpage_proj_txtfield.click()
        contpage_warmsg_phnnum=XLUtils.readData(self.path,"Contact",8,2)
        print(contpage_warmsg_phnnum)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsContact.contpage_warmsg_phnnum))
        print((self.driver.find_element(*LocatorsContact().contpage_warmsg_phnnum)).text)
        if (self.driver.find_element(*LocatorsContact().contpage_warmsg_phnnum)).text == contpage_warmsg_phnnum:
            XLUtils.writeData(self.path,"Contact",8,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",8,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",8,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",8,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def contpage_warmsg_proj(self):
        contpage_des_txtfield=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_des_txtfield))
        self.driver.execute_script('arguments[0].click()', contpage_des_txtfield)
        contpage_warmsg_proj=XLUtils.readData(self.path,"Contact",9,2)
        print(contpage_warmsg_proj)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsContact.contpage_warmsg_proj))
        print((self.driver.find_element(*LocatorsContact().contpage_warmsg_proj)).text)
        if (self.driver.find_element(*LocatorsContact().contpage_warmsg_proj)).text == contpage_warmsg_proj:
            XLUtils.writeData(self.path,"Contact",9,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",9,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",9,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",9,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def contpage_warmsg_description(self):
        contpage_lets_dscs_btn=WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsContact.contpage_lets_dscs_btn))
        contpage_lets_dscs_btn.click()
        contpage_warmsg_description=XLUtils.readData(self.path,"Contact",10,2)
        print(contpage_warmsg_description)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsContact.contpage_warmsg_description))
        print((self.driver.find_element(*LocatorsContact().contpage_warmsg_description)).text)
        if (self.driver.find_element(*LocatorsContact().contpage_warmsg_description)).text == contpage_warmsg_description:
            XLUtils.writeData(self.path,"Contact",10,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",10,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",10,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",10,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def contpage_warmsg_captcha(self):
        contpage_warmsg_captcha=XLUtils.readData(self.path,"Contact",11,2)
        print(contpage_warmsg_captcha)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsContact.contpage_warmsg_captcha))
        print((self.driver.find_element(*LocatorsContact().contpage_warmsg_captcha)).text)
        if (self.driver.find_element(*LocatorsContact().contpage_warmsg_captcha)).text == contpage_warmsg_captcha:
            XLUtils.writeData(self.path,"Contact",11,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",11,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",11,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",11,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

#================================================================FOOTER================================================================#

    def footer_headline(self):
        footer_headline=XLUtils.readData(self.path,"Contact",16,2)
        print(footer_headline)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_headline))
        print((self.driver.find_element(*LocatorsHomePage().footer_headline)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_headline)).text == footer_headline:
            XLUtils.writeData(self.path,"Contact",16,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",16,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",16,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",16,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_switzerland(self):
        footer_assert_switzerland=XLUtils.readData(self.path,"Contact",17,2)
        print(footer_assert_switzerland)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_switzerland))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_switzerland)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_switzerland)).text == footer_assert_switzerland:
            XLUtils.writeData(self.path,"Contact",17,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",17,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",17,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",17,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_Ind_mang(self):
        footer_assert_br_Ind_mang=XLUtils.readData(self.path,"Contact",18,2)
        print(footer_assert_br_Ind_mang)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_Ind_mang))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_Ind_mang)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_Ind_mang)).text == footer_assert_br_Ind_mang:
            XLUtils.writeData(self.path,"Contact",18,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",18,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",18,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",18,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_canada(self):
        footer_assert_br_canada=XLUtils.readData(self.path,"Contact",19,2)
        print(footer_assert_br_canada)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_canada))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_canada)).text)
        if (self.driver.find_element(*LocatorsHomePage().footer_assert_br_canada)).text == footer_assert_br_canada:
            XLUtils.writeData(self.path,"Contact",19,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",19,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",19,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",19,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_Ind_bang(self):
        footer_assert_br_Ind_bang=XLUtils.readData(self.path,"Contact",20,2)
        print(footer_assert_br_Ind_bang)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_Ind_bang))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_Ind_bang)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_Ind_bang)).text == footer_assert_br_Ind_bang:
            XLUtils.writeData(self.path,"Contact",20,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",20,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",20,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",20,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_company_name(self):
        footer_assert_company_name=XLUtils.readData(self.path,"Contact",21,2)
        print(footer_assert_company_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_company_name))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_company_name)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_company_name)).text == footer_assert_company_name:
            XLUtils.writeData(self.path,"Contact",21,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",21,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",21,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",21,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
            time.sleep(2)

    def footer_mailaddress_cnp(self):
        footer_mailaddress_cnp=XLUtils.readData(self.path,"Contact",22,2)
        print(footer_mailaddress_cnp)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(LocatorsContact.footer_mailaddress_cnp))
        print((self.driver.find_element(*LocatorsContact().footer_mailaddress_cnp)).text)
        if (self.driver.find_element(*LocatorsContact.footer_mailaddress_cnp)).text == footer_mailaddress_cnp:
            XLUtils.writeData(self.path,"Contact",22,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",22,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",22,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",22,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
            time.sleep(2)

    def footer_end_text(self):
        footer_end_text=XLUtils.readData(self.path,"Contact",23,2)
        print(footer_end_text)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_end_text))
        print((self.driver.find_element(*LocatorsHomePage().footer_end_text)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_end_text)).text == footer_end_text:
            XLUtils.writeData(self.path,"Contact",23,3,"pass")
            XLUtils.fillGreenColor(self.path,"Contact",23,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Contact",23,3,"failed")
            XLUtils.fillRedColor(self.path,"Contact",23,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_footer_insta_link(self):
        footer_insta_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.footer_insta_link))
        self.driver.execute_script("arguments[0].click();",footer_insta_link)
        time.sleep(1)
    

    def click_footer_fb_link(self):
        footer_fb_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.footer_fb_link))
        self.driver.execute_script("arguments[0].click();",footer_fb_link)
        time.sleep(1)

    def click_footer_twitter_link(self):
        footer_twitter_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.footer_twitter_link))
        self.driver.execute_script("arguments[0].click();",footer_twitter_link)
        time.sleep(1)

    def click_footer_linkedin_link(self):
        footer_linkedin_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.footer_linkedin_link))
        self.driver.execute_script("arguments[0].click();",footer_linkedin_link)
        time.sleep(1)

    def close_child_windows(self):
        parent_window = print(self.driver.current_window_handle, "#value of parent window")
        child_windows=self.driver.window_handles
        print(child_windows, "#value of child windows")
        for each_window in child_windows:
            self.driver.switch_to.window(each_window)
            print(self.driver.title, "#title of all windows")
            time.sleep(1)
            if self.driver.title!="Contact Leading Web Application Development - Bix Bytes Solutions":
               self.driver.close()
               time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        
    def footer_contact_num_link_cnp(self):
        footer_contact_num_link_cnp= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsContact.footer_contact_num_link_cnp))
        self.driver.execute_script("arguments[0].click();",footer_contact_num_link_cnp)
        time.sleep(3)

    def clear_pop_up(self):
        pyautogui.press('Esc')
        time.sleep(3) 
       
    def click_footer_mail_address_link(self):
        footer_mail_link=self.driver.find_element(By.XPATH, "//div[@class='row mb-lg-130 mb-md-70 mb-40 lg_flagged_information']//div[1]//div[1]//div[1]//p[2]//a[1]")
        for i in range(0,12):
            if i<12:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        footer_mail_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsJobs.footer_mail_link))
        self.driver.execute_script("arguments[0].click();",footer_mail_link)
        time.sleep(6)

    def close_mail_window(self):
        pyautogui.hotkey('alt','F4')
        time.sleep(2)
        pyautogui.hotkey('PAGE_DOWN','ENTER')



