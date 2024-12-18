
import datetime
import os
import shutil
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from utilities import XLUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pageobjects.locators import LocatorsHomePage
from pageobjects.locators import LocatorsMenu
from pageobjects.locators import LocatorsCompany
from allure_commons.types import AttachmentType
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import xlsxwriter
import time
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException 
from selenium.common.exceptions import NoAlertPresentException
from selenium import webdriver
import pyautogui

class CompanyPage():
    
    path=r"test_data\BBS6.xlsx"

    def __init__(self,driver):
        self.driver=driver

    def create_excel(self):
        # workbook=xlsxwriter.Workbook(r"C:\Nagalakshmi\PythonPractice\BBS_automation\test_data\BBS.xlsx")
        # worksheet = workbook.add_worksheet("Company")
        # worksheet.write(0, 0, "TEXT FOR ASSERTION")
        # worksheet.write(0, 1, "RESULTS")
        # worksheet.write(2, 0, "COMPANY")
        # worksheet.write(3, 0, "The Principles that matter most")
        # worksheet.write(4, 0, "Who we are")
        # worksheet.write(5, 0, "OUR WORK CULTURE")
        # worksheet.write(6, 0, "CLIENT MEETINGS @ BBS")
        # worksheet.write(7, 0, "What we do")
        # worksheet.write(8, 0, "Why BBS")
        # worksheet.write(9, 0, "WHY BIX BYTES SOLUTIONS?")
        # worksheet.write(11, 0, "FOOTER:")
        # worksheet.write(12, 0, "GET IN TOUCH")
        # worksheet.write(13, 0, "SWITZERLAND")
        # worksheet.write(14, 0, "INDIA - Mangalore")
        # worksheet.write(15, 0, "CANADA")
        # worksheet.write(16, 0, "INDIA - Bangalore")
        # worksheet.write(17, 0, "Bix Bytes Solutions Pvt. Ltd.")
        # worksheet.write(18, 0, "info@bixbytessolutions.com")
        # worksheet.write(19, 0, "Copyright © 2022 BixBytes Solutions")
        
        # workbook.close()
        wb = Workbook()
        file_path = "test_data"
        create_duplicate = 'BixBytes website' + str(datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')) + '.xlsx'
        replica = os.path.join(file_path, create_duplicate)
        wb.save(replica)
        source = "test_data\BBS6.xlsx"
        dest = replica
        shutil.copy(source, dest)

#================================================================COMPANY PAGE================================================================
    def click_hamburger(self):
        self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()

    def menu_companylink_assert(self):
        companylink_Assert=XLUtils.readData(self.path,"Company",3,2)
        print(companylink_Assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_company_link))
        print((self.driver.find_element(*LocatorsMenu().menu_company_link)).text)
        if (self.driver.find_element(*LocatorsMenu.menu_company_link)).text == companylink_Assert:
            XLUtils.writeData(self.path,"Company",3,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",3,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",3,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",3,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(2)
        company=self.driver.find_element(*LocatorsMenu.menu_company_link)
        self.driver.execute_script('arguments[0].click()', company)
        time.sleep(2)
        hamburger=self.driver.find_element(*LocatorsCompany.hamburger_company_page_x)
        self.driver.execute_script('arguments[0].click()', hamburger)
        time.sleep(2)
        self.driver.refresh()

    def scroll_down_Page(self):
        # self.driver.refresh()
        headline= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsCompany.headline_company_page))
        headline.click()
        for i in range(0,7):
            if i<7:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
                 time.sleep(1)

    def scroll_up_Page(self):
        for i in range(0,7):
            if i<7:
                 ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
                 time.sleep(1)

    def scroll_stop_between(self):
        headline= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsCompany.headline_company_page))
        headline.click()
        for i in range(0,3):
            if i<5:
                 ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                 time.sleep(1)
                 

    def headline_company_page(self):
        ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
        headline_company_page=XLUtils.readData(self.path,"Company",4,2)
        print(headline_company_page)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsCompany.headline_company_page))
        print((self.driver.find_element(*LocatorsCompany().headline_company_page)).text)
        if (self.driver.find_element(*LocatorsCompany.headline_company_page)).text == headline_company_page:
            XLUtils.writeData(self.path,"Company",4,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",4,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",4,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",4,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def who_v_r_company_page(self):
        who_v_r_company_page=XLUtils.readData(self.path,"Company",5,2)
        print(who_v_r_company_page)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsCompany.who_v_r_company_page))
        print((self.driver.find_element(*LocatorsCompany().who_v_r_company_page)).text)
        if (self.driver.find_element(*LocatorsCompany.who_v_r_company_page)).text == who_v_r_company_page:
            XLUtils.writeData(self.path,"Company",5,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",5,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",5,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",5,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def asrt_work_culture(self):
        asrt_work_culture=XLUtils.readData(self.path,"Company",6,2)
        print(asrt_work_culture)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsCompany.asrt_work_culture))
        print((self.driver.find_element(*LocatorsCompany().asrt_work_culture)).text)
        if (self.driver.find_element(*LocatorsCompany.asrt_work_culture)).text == asrt_work_culture:
            XLUtils.writeData(self.path,"Company",6,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",6,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",6,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",6,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def asrt_client_meeting(self):
        asrt_client_meeting=XLUtils.readData(self.path,"Company",7,2)
        print(asrt_client_meeting)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsCompany.asrt_client_meeting))
        print((self.driver.find_element(*LocatorsCompany().asrt_client_meeting)).text)
        if (self.driver.find_element(*LocatorsCompany.asrt_client_meeting)).text == asrt_client_meeting:
            XLUtils.writeData(self.path,"Company",7,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",7,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",7,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",7,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def client_meeting_slides(self):
        elements=self.driver.find_elements(By.XPATH, "//ngb-carousel[@class='carousel slide bbs_carousel_wrapper']//li")
        slides = len(elements)
        for slide in range(slides):
            #Added this line to avoid stale which re-assigned the element again.
            # elements=self.driver.find_elements(By.XPATH, "//ngb-carousel[@class='carousel slide bbs_carousel_wrapper']//li")
            # elements[slide].click()
            elements=self.driver.find_elements(By.XPATH, "//ngb-carousel[@class='carousel slide bbs_carousel_wrapper']//li")
            self.driver.execute_script('arguments[0].click()', elements[slide])
            time.sleep(2)

    def click_wt_v_do_company_page(self):
        wt_v_do_company_page=self.driver.find_element(*LocatorsCompany().wt_v_do_company_page)
        self.driver.execute_script('arguments[0].click()', wt_v_do_company_page)

    def wt_v_do_company_page(self):
        wt_v_do_company_page=XLUtils.readData(self.path,"Company",8,2)
        print(wt_v_do_company_page)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsCompany.wt_v_do_company_page))
        print((self.driver.find_element(*LocatorsCompany().wt_v_do_company_page)).text)
        if (self.driver.find_element(*LocatorsCompany.wt_v_do_company_page)).text == wt_v_do_company_page:
            XLUtils.writeData(self.path,"Company",8,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",8,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",8,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",8,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_y_bbs_icon_company_page(self):
        y_bbs_icon_company_page=self.driver.find_element(*LocatorsCompany().y_bbs_icon_company_page)
        self.driver.execute_script('arguments[0].click()', y_bbs_icon_company_page)

    def y_bbs_icon_company_page(self):
        y_bbs_icon_company_page=XLUtils.readData(self.path,"Company",9,2)
        print(y_bbs_icon_company_page)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsCompany.y_bbs_icon_company_page))
        print((self.driver.find_element(*LocatorsCompany().y_bbs_icon_company_page)).text)
        if (self.driver.find_element(*LocatorsCompany.y_bbs_icon_company_page)).text == y_bbs_icon_company_page:
            XLUtils.writeData(self.path,"Company",9,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",9,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",9,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",9,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def y_bbs_hdline_company_page(self):
        y_bbs_hdline_company_page=XLUtils.readData(self.path,"Company",10,2)
        print(y_bbs_hdline_company_page)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsCompany.y_bbs_hdline_company_page))
        print((self.driver.find_element(*LocatorsCompany().y_bbs_hdline_company_page)).text)
        if (self.driver.find_element(*LocatorsCompany.y_bbs_hdline_company_page)).text == y_bbs_hdline_company_page:
            XLUtils.writeData(self.path,"Company",10,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",10,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",10,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",10,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

#================================================================Footer================================================================

    def footer_headline(self):
        # headline= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsCompany.headline_company_page))
        # headline.click()
        # for i in range(0,7):
        #     if i<7:
        #          ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        footer_headline=XLUtils.readData(self.path,"Company",13,2)
        print(footer_headline)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_headline))
        print((self.driver.find_element(*LocatorsHomePage().footer_headline)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_headline)).text == footer_headline:
            XLUtils.writeData(self.path,"Company",13,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",13,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",13,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",13,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_switzerland(self):
        footer_assert_switzerland=XLUtils.readData(self.path,"Company",14,2)
        print(footer_assert_switzerland)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_switzerland))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_switzerland)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_switzerland)).text == footer_assert_switzerland:
            XLUtils.writeData(self.path,"Company",14,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",14,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",14,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",14,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_Ind_mang(self):
        footer_assert_br_Ind_mang=XLUtils.readData(self.path,"Company",15,2)
        print(footer_assert_br_Ind_mang)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_Ind_mang))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_Ind_mang)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_Ind_mang)).text == footer_assert_br_Ind_mang:
            XLUtils.writeData(self.path,"Company",15,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",15,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",15,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",15,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_canada(self):
        footer_assert_br_canada=XLUtils.readData(self.path,"Company",16,2)
        print(footer_assert_br_canada)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_canada))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_canada)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_canada)).text == footer_assert_br_canada:
            XLUtils.writeData(self.path,"Company",16,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",16,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",16,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",16,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_Ind_bang(self):
        footer_assert_br_Ind_bang=XLUtils.readData(self.path,"Company",17,2)
        print(footer_assert_br_Ind_bang)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_Ind_bang))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_Ind_bang)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_Ind_bang)).text == footer_assert_br_Ind_bang:
            XLUtils.writeData(self.path,"Company",17,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",17,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",17,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",17,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_company_name(self):
        footer_assert_company_name=XLUtils.readData(self.path,"Company",18,2)
        print(footer_assert_company_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_company_name))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_company_name)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_company_name)).text == footer_assert_company_name:
            XLUtils.writeData(self.path,"Company",18,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",18,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",18,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",18,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
            time.sleep(2)

    def footer_mailaddress_company_page(self):
        footer_mailaddress_company_page=XLUtils.readData(self.path,"Company",19,2)
        print(footer_mailaddress_company_page)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(LocatorsCompany.footer_mailaddress_company_page))
        print((self.driver.find_element(*LocatorsCompany().footer_mailaddress_company_page)).text)
        if (self.driver.find_element(*LocatorsCompany.footer_mailaddress_company_page)).text == footer_mailaddress_company_page:
            XLUtils.writeData(self.path,"Company",19,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",19,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",19,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",19,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
            time.sleep(2)

    def footer_end_text(self):
        footer_end_text=XLUtils.readData(self.path,"Company",20,2)
        print(footer_end_text)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_end_text))
        print((self.driver.find_element(*LocatorsHomePage().footer_end_text)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_end_text)).text == footer_end_text:
            XLUtils.writeData(self.path,"Company",20,3,"pass")
            XLUtils.fillGreenColor(self.path,"Company",20,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Company",20,3,"failed")
            XLUtils.fillRedColor(self.path,"Company",20,3)
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
            if self.driver.title!="Together individual quality software - Bix Bytes Solutions":
               self.driver.close()
               time.sleep(3)
               
        self.driver.switch_to.window(self.driver.window_handles[0])

    def footer_contact_num_link_cp(self):
        for i in range(0,3):
            if i<3:    
                ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        footer_contact_num_link_cp= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsCompany.footer_contact_num_link_cp))
        self.driver.execute_script("arguments[0].click();",footer_contact_num_link_cp)
        time.sleep(2)

    def clear_pop_up(self):
        pyautogui.press('Esc') 

    def click_footer_mail_address_link(self):
        # mail_id= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsCompany.footer_mailaddress_company_page))
        # mail_id.click()
        footer_mailaddress_company_page= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsCompany.footer_mailaddress_company_page))
        self.driver.execute_script("arguments[0].click();",footer_mailaddress_company_page)
        time.sleep(2)
    
    def close_mail_window(self):
        pyautogui.hotkey('alt','F4')
        time.sleep(2)
        pyautogui.hotkey('PAGE_DOWN','ENTER')