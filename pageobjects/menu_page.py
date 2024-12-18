
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
from allure_commons.types import AttachmentType
import allure
import xlsxwriter
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import StaleElementReferenceException, MoveTargetOutOfBoundsException
from selenium.webdriver.common.keys import Keys

class MenuPage():

    path=r"test_data\BBS6.xlsx"
   
    def __init__(self,driver):
        self.driver=driver

    def click_hamburger(self):
        # self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()
        hamburger=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.btn_Hamburger_hmpg_x))
        self.driver.execute_script("arguments[0].click();", hamburger)
        time.sleep(2)

    def create_excel(self):
        # workbook=xlsxwriter.Workbook("test_data\BBS.xlsx")
        # worksheet = workbook.add_worksheet("Menu")
        # worksheet.write(0, 0, "Name")
        # worksheet.write(0, 1, "Result")
        # worksheet.write(2, 0, "HOME")
        # worksheet.write(3, 0, "COMPANY")
        # worksheet.write(4, 0, "SERVICES")
        # worksheet.write(5, 0, "DESIGN LAB")
        # worksheet.write(6, 0, "BLOG")
        # worksheet.write(7, 0, "JOBS")
        # worksheet.write(8, 0, "CONTACT")

        # worksheet.write(10, 0, "German Text:")
        # worksheet.write(11, 0, "INNOVATIVE SOFTWAREENTWICKLUNG")
        # worksheet.write(12, 0, "PROJEKTE")
        # worksheet.write(13, 0, "DIENSTLEISTUNGEN")
        # worksheet.write(14, 0, "KUNDEN")
        # worksheet.write(15, 0, "KONTAKT AUFNEHMEN")
       
        # workbook.close()

        wb = Workbook()
        file_path = "test_data"
        create_duplicate = 'BixBytes website' + str(datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')) + '.xlsx'
        replica = os.path.join(file_path, create_duplicate)
        wb.save(replica)
        source = "test_data\BBS6.xlsx"
        dest = replica
        shutil.copy(source, dest)

    def menu_homelink_assert(self):
        homelink_Assert=XLUtils.readData(self.path,"Menu",3,2)
        print(homelink_Assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_home_link))
        print((self.driver.find_element(*LocatorsMenu().menu_home_link)).text)
        if (self.driver.find_element(*LocatorsMenu.menu_home_link)).text == homelink_Assert:
            XLUtils.writeData(self.path,"Menu",3,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",3,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",3,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",3,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(1)
        # home=self.driver.find_element(*LocatorsMenu.menu_home_link)
        # self.driver.execute_script('arguments[0].click()', home)
        # time.sleep(1)
        # hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
        # self.driver.execute_script('arguments[0].click()', hamburger)
        # time.sleep(1)

    def menu_companylink_assert(self):
        companylink_Assert=XLUtils.readData(self.path,"Menu",4,2)
        print(companylink_Assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_company_link))
        print((self.driver.find_element(*LocatorsMenu().menu_company_link)).text)
        if (self.driver.find_element(*LocatorsMenu.menu_company_link)).text == companylink_Assert:
            XLUtils.writeData(self.path,"Menu",4,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",4,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",4,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",4,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(4)
        company=self.driver.find_element(*LocatorsMenu.menu_company_link)
        self.driver.execute_script('arguments[0].click()', company)
        time.sleep(6)
        hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
        self.driver.execute_script('arguments[0].click()', hamburger)
        time.sleep(6)

    def menu_serviceslink_assert(self):
        serviceslink_Assert=XLUtils.readData(self.path,"Menu",5,2)
        print(serviceslink_Assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_services_link))
        print((self.driver.find_element(*LocatorsMenu().menu_services_link)).text)
        if (self.driver.find_element(*LocatorsMenu.menu_services_link)).text == serviceslink_Assert:
            XLUtils.writeData(self.path,"Menu",5,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",5,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",5,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",5,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(5)
        services=self.driver.find_element(*LocatorsMenu.menu_services_link)
        self.driver.execute_script('arguments[0].click()', services)
        time.sleep(5)
        hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
        self.driver.execute_script('arguments[0].click()', hamburger)
        time.sleep(5)

    def menu_designlab_assert(self):
        designLablink_Assert=XLUtils.readData(self.path,"Menu",6,2)
        print(designLablink_Assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_designlab_link))
        print((self.driver.find_element(*LocatorsMenu().menu_designlab_link)).text)
        if (self.driver.find_element(*LocatorsMenu.menu_designlab_link)).text == designLablink_Assert:
            XLUtils.writeData(self.path,"Menu",6,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",6,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",6,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",6,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(1)
        designlab=self.driver.find_element(*LocatorsMenu.menu_designlab_link)
        self.driver.execute_script('arguments[0].click()', designlab)
        time.sleep(2)

    def close_child_windows(self):
        parent_window = print(self.driver.current_window_handle, "#value of parent window")
        child_windows=self.driver.window_handles
        print(child_windows, "#value of child windows")
        for each_window in child_windows:
            self.driver.switch_to.window(each_window)
            print(self.driver.title, "#title of all windows")
            time.sleep(5)
            if self.driver.title!="Jobs | Web Application Engineering - India - Bix Bytes Solutions":
               self.driver.close()
               time.sleep(6)
        # menu_close_btn=self.driver.find_element(*LocatorsMenu.menu_close_btn)
        # self.driver.execute_script('arguments[0].click()', menu_close_btn)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsMenu.menu_close_btn))
        # time.sleep(3)
        # hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
        # self.driver.execute_script('arguments[0].click()', hamburger)
        # time.sleep(3)

    def menu_blog_assert(self):
        bloglink_Assert=XLUtils.readData(self.path,"Menu",7,2)
        print(bloglink_Assert)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsMenu.menu_blog_link))
        print((self.driver.find_element(*LocatorsMenu().menu_blog_link)).text)
        if (self.driver.find_element(*LocatorsMenu.menu_blog_link)).text == bloglink_Assert:
            XLUtils.writeData(self.path,"Menu",7,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",7,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",7,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",7,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(5)
        blog=self.driver.find_element(*LocatorsMenu.menu_blog_link)
        self.driver.execute_script('arguments[0].click()', blog)
        time.sleep(5)
        hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
        self.driver.execute_script('arguments[0].click()', hamburger)
        time.sleep(5)

    def menu_jobs_assert(self):
        jobslink_Assert=XLUtils.readData(self.path,"Menu",8,2)
        print(jobslink_Assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_jobs_link))
        print((self.driver.find_element(*LocatorsMenu().menu_jobs_link)).text)
        if (self.driver.find_element(*LocatorsMenu.menu_jobs_link)).text == jobslink_Assert:
            XLUtils.writeData(self.path,"Menu",8,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",8,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",8,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",8,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(5)
        jobs=self.driver.find_element(*LocatorsMenu.menu_jobs_link)
        self.driver.execute_script('arguments[0].click()', jobs)
        time.sleep(5)
        hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
        self.driver.execute_script('arguments[0].click()', hamburger)
        time.sleep(5)

    def menu_contact_assert(self):
        contactlink_Assert=XLUtils.readData(self.path,"Menu",9,2)
        print(contactlink_Assert)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsMenu.menu_contact_link))
        print((self.driver.find_element(*LocatorsMenu().menu_contact_link)).text)
        if (self.driver.find_element(*LocatorsMenu.menu_contact_link)).text == contactlink_Assert:
            XLUtils.writeData(self.path,"Menu",9,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",9,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",9,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",9,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(5)
        # contact=self.driver.find_element(*LocatorsMenu.menu_contact_link)
        # self.driver.execute_script('arguments[0].click()', contact)
        # time.sleep(5)
        # hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
        # self.driver.execute_script('arguments[0].click()', hamburger)
        # time.sleep(5)
        # homelink=self.driver.find_element(*LocatorsMenu.menu_home_link)
        # self.driver.execute_script('arguments[0].click()', homelink)
        # time.sleep(1)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.btn_Hamburger_hmpg_x))
        # time.sleep(2)

    def main_module(self):
        list_data=[]
        list_eachEle=[]
       
        seven_elements=WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(LocatorsMenu.menu_main_modules))
        for each_element in seven_elements:
            list_eachEle.append(each_element.text)
        print(list_eachEle, "all elements names")
        
        for r in range(3,10):
            data=XLUtils.readData(self.path,"Menu",r,1)
            list_data.append(data)
        print(list_data, "2222")
        
        for i in range(0,len(list_data)) :
            for r in range(3,10):
                if list_data[i]==list_eachEle[i]:
                    XLUtils.writeData(self.path,"Menu",r,4,"pass")
                    XLUtils.fillGreenColor(self.path,"Menu",r,4)
                    assert True
                else:
                    XLUtils.writeData(self.path,"Menu",r,4,"failed")
                    XLUtils.fillRedColor(self.path,"Menu",r,4)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="tc_fail", attachment_type=AttachmentType.PNG)
                    assert False

    def click_main_module(self):
        # seven_elements=WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(LocatorsMenu.menu_main_modules))
        # for i in range(0,7):
        #     if i<7:
        #         seven_elements=WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(LocatorsMenu.menu_main_modules))
        #         seven_elements.click()
        #         self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()
        try:
            seven_elements= WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(LocatorsMenu.menu_main_modules))
            print("Above loop", len(seven_elements))
            print("Above loop", type(seven_elements))
            for i in range(len(seven_elements)):
                print(seven_elements[i])
                # self.driver.find_elements(*LocatorsMenu.menu_main_modules)
                # seven_elements[i].click()
                self.driver.execute_script('arguments[0].click()', seven_elements[i])
                print("inside loop", len(seven_elements))
                print("inside loop", type(seven_elements))
                # ActionChains(self.driver).move_to_element(each_button[i]).click().perform()
                time.sleep(2)
                hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
                self.driver.execute_script('arguments[0].click()', hamburger)
                time.sleep(2)   
        except (StaleElementReferenceException, MoveTargetOutOfBoundsException):
            pass
    
    def click_GTC(self):
        menu_GTC_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_GTC_link))
        self.driver.execute_script("arguments[0].click();",menu_GTC_link)
        menu_GTC_download= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_GTC_download))
        #Scrolling page up and down
        for i in range(0,5):
            if i<5:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        time.sleep(1)

        for i in range(0,5):
            if i<5:
                ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();",menu_GTC_download)
        time.sleep(1)
        hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
        self.driver.execute_script('arguments[0].click()', hamburger)
        time.sleep(2)

    def click_privacy_poly(self):
        menu_Privacypolicy_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_Privacypolicy_link))
        self.driver.execute_script("arguments[0].click();",menu_Privacypolicy_link)
        #Scrolling page up and down
        for i in range(0,4):
            if i<4:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
                 time.sleep(1)

        for i in range(0,4):
            if i<4:
                ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
                time.sleep(1)

        self.driver.back()
        time.sleep(2)
        self.driver.back()
        hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
        self.driver.execute_script('arguments[0].click()', hamburger)

    def click_sitemap(self):
        menu_SiteMap_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_SiteMap_link))
        self.driver.execute_script("arguments[0].click();",menu_SiteMap_link)
        parent_window = print(self.driver.current_window_handle, "#value of parent window")
        child_windows=self.driver.window_handles
        print(child_windows, "#value of child windows")
        for each_window in child_windows:
            self.driver.switch_to.window(each_window)
            print(self.driver.title, "#title of all windows")
            time.sleep(5)
            if self.driver.title!="Jobs | Web Application Engineering - India - Bix Bytes Solutions":
               self.driver.close()
               time.sleep(6)

    def click_menu_insta_link(self):
        menu_insta_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_insta_link))
        self.driver.execute_script("arguments[0].click();",menu_insta_link)
        time.sleep(1)

    def click_menu_fb_link(self):
        menu_fb_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_fb_link))
        self.driver.execute_script("arguments[0].click();",menu_fb_link)
        time.sleep(1)

    def click_menu_twitter_link(self):
        menu_twitter_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_twitter_link))
        self.driver.execute_script("arguments[0].click();",menu_twitter_link)
        time.sleep(1)

    def click_menu_linkedin_link(self):
        menu_linkedin_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_linkedin_link))
        self.driver.execute_script("arguments[0].click();",menu_linkedin_link)
        time.sleep(1)

    def close_child_windows_menu(self):
       print(self.driver.current_window_handle, "#value of parent window")
       child_windows=self.driver.window_handles
       print(child_windows, "#value of child windows")
       for each_window in child_windows:
            self.driver.switch_to.window(each_window)
            print(self.driver.title, "#title of all windows")
            time.sleep(1)
            if self.driver.title!="Jobs | Web Application Engineering - India - Bix Bytes Solutions":
               self.driver.close()
       time.sleep(1)
       self.driver.switch_to.window(self.driver.window_handles[0])

    #    hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
    #    self.driver.execute_script('arguments[0].click()', hamburger)
    #    time.sleep(2)

    def close_menu(self):
        menu_close_btn= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_close_btn))
        self.driver.execute_script("arguments[0].click();",menu_close_btn)
        time.sleep(1)

    def menu_lang_change_DE(self):
        menu_lang_change_DE= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_lang_change_DE))
        self.driver.execute_script("arguments[0].click();",menu_lang_change_DE)
        time.sleep(1)
        hamburger=self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x)
        self.driver.execute_script('arguments[0].click()', hamburger)
        time.sleep(2)
        home=self.driver.find_element(By.XPATH, "//span[@data-title='Home']")
        home.click()

    def txt_hpg_DE_headline(self):
        txt_hpg_DE_headline=XLUtils.readData(self.path,"Menu",12,2)
        print(txt_hpg_DE_headline)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.txt_hpg_DE_headline))
        print((self.driver.find_element(*LocatorsMenu().txt_hpg_DE_headline)).text)
        if (self.driver.find_element(*LocatorsMenu.txt_hpg_DE_headline)).text == txt_hpg_DE_headline:
            XLUtils.writeData(self.path,"Menu",12,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",12,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",12,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",12,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def txt_hpg_DE_project(self):
        txt_hpg_DE_project=XLUtils.readData(self.path,"Menu",13,2)
        print(txt_hpg_DE_project)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.txt_hpg_DE_project))
        print((self.driver.find_element(*LocatorsMenu().txt_hpg_DE_project)).text)
        if (self.driver.find_element(*LocatorsMenu.txt_hpg_DE_project)).text == txt_hpg_DE_project:
            XLUtils.writeData(self.path,"Menu",13,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",13,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",13,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",13,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def txt_hpg_DE_services(self):
        txt_hpg_DE_services=XLUtils.readData(self.path,"Menu",14,2)
        print(txt_hpg_DE_services)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.txt_hpg_DE_services))
        print((self.driver.find_element(*LocatorsMenu().txt_hpg_DE_services)).text)
        if (self.driver.find_element(*LocatorsMenu.txt_hpg_DE_services)).text == txt_hpg_DE_services:
            XLUtils.writeData(self.path,"Menu",14,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",14,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",14,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",14,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def txt_hpg_DE_clients(self):
        txt_hpg_DE_clients=XLUtils.readData(self.path,"Menu",15,2)
        print(txt_hpg_DE_clients)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.txt_hpg_DE_clients))
        print((self.driver.find_element(*LocatorsMenu().txt_hpg_DE_clients)).text)
        if (self.driver.find_element(*LocatorsMenu.txt_hpg_DE_clients)).text == txt_hpg_DE_clients:
            XLUtils.writeData(self.path,"Menu",15,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",15,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",15,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",15,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def txt_hpg_DE_footer_hline(self):
        txt_hpg_DE_footer_hline=XLUtils.readData(self.path,"Menu",16,2)
        print(txt_hpg_DE_footer_hline)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.txt_hpg_DE_footer_hline))
        print((self.driver.find_element(*LocatorsMenu().txt_hpg_DE_footer_hline)).text)
        if (self.driver.find_element(*LocatorsMenu.txt_hpg_DE_footer_hline)).text == txt_hpg_DE_footer_hline:
            XLUtils.writeData(self.path,"Menu",16,3,"pass")
            XLUtils.fillGreenColor(self.path,"Menu",16,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Menu",16,3,"failed")
            XLUtils.fillRedColor(self.path,"Menu",16,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    

    
           
