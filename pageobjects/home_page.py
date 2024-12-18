
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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException 
from selenium.common.exceptions import NoAlertPresentException
import pyautogui

class HomePage():
    
    path=r"test_data\BBS6.xlsx"

    def __init__(self,driver):
        self.driver=driver

    def create_excel(self):
        # workbook=xlsxwriter.Workbook(r"C:\Nagalakshmi\PythonPractice\BBS_automation\test_data\BBS.xlsx")
        # worksheet = workbook.add_worksheet("HomePage")
        # worksheet.write(0, 0, "TEXT FOR ASSERTION")
        # worksheet.write(0, 1, "RESULTS")
        # worksheet.write(2, 0, "INNOVATIVE SOFTWARE DEVELOPMENT")
        # worksheet.write(4, 0, "PROJECT SECTION:")
        # worksheet.write(5, 0, "ImmoSpice")
        # worksheet.write(6, 0, "Viasuisse")
        # worksheet.write(7, 0, "Prozessraum")
        # worksheet.write(9, 0, "SERVICES SECTION:")
        # worksheet.write(10, 0, "DESIGN")
        # worksheet.write(11, 0, "CONSULTANCY")
        # worksheet.write(12, 0, "SHAREPOINT")
        # worksheet.write(13, 0, "ENGINEERING")
        # worksheet.write(14, 0, "QUALITY-ASSURANCE")
        # worksheet.write(15, 0, "SALESFORCE CRM")
        # worksheet.write(17, 0, "CLIENTS SECTION:")
        # worksheet.write(19, 0, "MARTIN KÜNG")
        # worksheet.write(20, 0, "THOMAS HIRSIGER")
        # worksheet.write(21, 0, "CEO @ ASAGO")
        # worksheet.write(22, 0, "DOMAN OBRIST")
        # worksheet.write(23, 0, "Co Founder @ Reach")
        # worksheet.write(24, 0, "DANIEL GASSER")
        # worksheet.write(25, 0, "@ Bouygues Energies & Services")
        # worksheet.write(26, 0, "M. LARA FERRARI")
        # worksheet.write(27, 0, "CEO @ Prozessraum Ltd")
        # worksheet.write(28, 0, "DAMIAN BIRCH")
        # worksheet.write(29, 0, "Head of Solutions & Technology @ Viasuisse AG")
        # worksheet.write(31, 0, "FOOTER:")
        # worksheet.write(32, 0, "GET IN TOUCH")
        # worksheet.write(33, 0, "SWITZERLAND")
        # worksheet.write(34, 0, "INDIA - Mangalore")
        # worksheet.write(35, 0, "CANADA")
        # worksheet.write(36, 0, "INDIA - Bangalore")
        # worksheet.write(37, 0, "Bix Bytes Solutions Pvt. Ltd.")
        # worksheet.write(38, 0, "info@bixbytessolutions.com")
        # worksheet.write(39, 0, "Copyright © 2022 BixBytes Solutions")
        
        # workbook.close()
        
        wb = Workbook()
        file_path = "test_data"
        create_duplicate = 'BixBytes website' + str(datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')) + '.xlsx'
        replica = os.path.join(file_path, create_duplicate)
        wb.save(replica)
        source = "testdata\BBS6.xlsx"
        dest = replica
        shutil.copy(source, dest)
        
#================================================================HOME PAGE================================================================
    def click_hamburger(self):
        self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()

    def homePage_headline_assert(self):
        hmpg_Assert=XLUtils.readData(self.path,"HomePage",3,2)
        print(hmpg_Assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.txt_hpg_headline_x))
        print((self.driver.find_element(*LocatorsHomePage().txt_hpg_headline_x)).text)
        if (self.driver.find_element(*LocatorsHomePage.txt_hpg_headline_x)).text == hmpg_Assert:
            XLUtils.writeData(self.path,"HomePage",3,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",3,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",3,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",3,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        # time.sleep(2)

    def scroll_down_Page(self):
        headline= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.txt_hpg_headline_x))
        headline.click()
        for i in range(0,5):
            if i<5:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
                 time.sleep(1)

    def scroll_up_Page(self):
        footer= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.footer_end_text))
        footer.click()
        for i in range(0,5):
            if i<5:
                 ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
                 time.sleep(1)

    def scroll_stop_between(self):
        headline= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.txt_hpg_headline_x))
        headline.click()
        for i in range(0,3):
            if i<5:
                 ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                 time.sleep(1)

#================================================================PROJECTS SECTION================================================================        
    
    def click_proj_carousel1(self):
        # self.driver.find_element(*LocatorsHomePage.carousel1_proj_x).click()
        carousel1=self.driver.find_element(*LocatorsHomePage.carousel_1_proj_x)
        self.driver.execute_script("arguments[0].click();", carousel1)
        time.sleep(1)

    def carousel1_text_assert(self):
        carousel1_text_assert=XLUtils.readData(self.path,"HomePage",6,2)
        print(carousel1_text_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.carousel1_text_assert))
        print((self.driver.find_element(*LocatorsHomePage().carousel1_text_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.carousel1_text_assert)).text == carousel1_text_assert:
            XLUtils.writeData(self.path,"HomePage",6,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",6,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",6,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",6,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_proj_carousel2(self):
        carousel2=self.driver.find_element(*LocatorsHomePage.carousel_2_proj_x)
        self.driver.execute_script("arguments[0].click();", carousel2)

    def carousel2_text_assert(self):
        carousel2_text_assert=XLUtils.readData(self.path,"HomePage",7,2)
        print(carousel2_text_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.carousel2_text_assert))
        print((self.driver.find_element(*LocatorsHomePage().carousel2_text_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.carousel2_text_assert)).text == carousel2_text_assert:
            XLUtils.writeData(self.path,"HomePage",7,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",7,3)
            assert True
            
        else:
            XLUtils.writeData(self.path,"HomePage",7,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",7,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(1)   

    def click_proj_carousel3(self):
        carousel3=self.driver.find_element(*LocatorsHomePage.carousel_3_proj_x)
        self.driver.execute_script("arguments[0].click();", carousel3)
        time.sleep(1)

    def carousel3_text_assert(self):
        carousel3_text_assert=XLUtils.readData(self.path,"HomePage",8,2)
        print(carousel3_text_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.carousel3_text_assert))
        print((self.driver.find_element(*LocatorsHomePage().carousel3_text_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.carousel3_text_assert)).text == carousel3_text_assert:
            XLUtils.writeData(self.path,"HomePage",8,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",8,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",8,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",8,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

#================================================================SERVICES SECTION================================================================
    def assert_card_design(self):
        assert_card_design=XLUtils.readData(self.path,"HomePage",11,2)
        print(assert_card_design)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.assert_card_design))
        print((self.driver.find_element(*LocatorsHomePage().assert_card_design)).text)
        if (self.driver.find_element(*LocatorsHomePage.assert_card_design)).text == assert_card_design:
            XLUtils.writeData(self.path,"HomePage",11,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",11,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",11,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",11,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_design_card(self):
        design = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.service_card_1))
        self.driver.execute_script("arguments[0].click();", design)
        time.sleep(2)
        self.driver.back()

    def click_home_menu(self):
        home=self.driver.find_element(*LocatorsMenu.menu_home_link)
        self.driver.execute_script("arguments[0].click();", home)
        time.sleep(2)

    def assert_card_consultancy(self):
        assert_card_consultancy=XLUtils.readData(self.path,"HomePage",12,2)
        print(assert_card_consultancy)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.assert_card_consultancy))
        print((self.driver.find_element(*LocatorsHomePage().assert_card_consultancy)).text)
        if (self.driver.find_element(*LocatorsHomePage.assert_card_consultancy)).text == assert_card_consultancy:
            XLUtils.writeData(self.path,"HomePage",12,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",12,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",12,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",12,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_consultancy_card(self):
        consultancy = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.service_card_2))
        self.driver.execute_script("arguments[0].click();", consultancy)
        time.sleep(2)
        # time.sleep(2)
        self.driver.back()

    def assert_card_sharepoint(self):
        assert_card_sharepoint=XLUtils.readData(self.path,"HomePage",13,2)
        print(assert_card_sharepoint)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.assert_card_sharepoint))
        print((self.driver.find_element(*LocatorsHomePage().assert_card_sharepoint)).text)
        if (self.driver.find_element(*LocatorsHomePage.assert_card_sharepoint)).text == assert_card_sharepoint:
            XLUtils.writeData(self.path,"HomePage",13,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",13,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",13,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",13,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_sharepoint_card(self):
        sharepoint = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.service_card_3))
        self.driver.execute_script("arguments[0].click();", sharepoint)
        time.sleep(1)
        # time.sleep(2)
        self.driver.back()

    def assert_card_engineering(self):
        assert_card_engineering=XLUtils.readData(self.path,"HomePage",14,2)
        print(assert_card_engineering)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.assert_card_engineering))
        print((self.driver.find_element(*LocatorsHomePage().assert_card_engineering)).text)
        if (self.driver.find_element(*LocatorsHomePage.assert_card_engineering)).text == assert_card_engineering:
            XLUtils.writeData(self.path,"HomePage",14,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",14,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",14,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",14,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_engineering_card(self):
        sharepoint = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.service_card_4))
        self.driver.execute_script("arguments[0].click();", sharepoint)
        time.sleep(2)
        self.driver.back()

    def assert_card_QA(self):
        assert_card_QA=XLUtils.readData(self.path,"HomePage",15,2)
        print(assert_card_QA)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.assert_card_QA))
        print((self.driver.find_element(*LocatorsHomePage().assert_card_QA)).text)
        if (self.driver.find_element(*LocatorsHomePage.assert_card_QA)).text == assert_card_QA:
            XLUtils.writeData(self.path,"HomePage",15,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",15,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",15,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",15,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_QA_card(self):
        qa = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.service_card_5))
        self.driver.execute_script("arguments[0].click();",qa)
        time.sleep(2)
        self.driver.back()

    def assert_card_salesforce(self):
        assert_card_salesforce=XLUtils.readData(self.path,"HomePage",16,2)
        print(assert_card_salesforce)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.assert_card_salesforce))
        print((self.driver.find_element(*LocatorsHomePage().assert_card_salesforce)).text)
        if (self.driver.find_element(*LocatorsHomePage.assert_card_salesforce)).text == assert_card_salesforce:
            XLUtils.writeData(self.path,"HomePage",16,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",16,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",16,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",16,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_salesforce_card(self):
        salesforce= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.service_card_6))
        self.driver.execute_script("arguments[0].click();",salesforce)
        time.sleep(2)
        self.driver.back()

    def flip_service_cards(self):
        headline= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.txt_hpg_headline_x))
        headline.click()
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        for i in range(0,15):
            if i<15:
                 ActionChains(self.driver).send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(1)
       
        cards=WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located(LocatorsHomePage.flip_6cards))
        for card in range(len(cards)):
            cards=WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located(LocatorsHomePage.flip_6cards))
            ActionChains(self.driver).move_to_element(cards[card]).perform()
            time.sleep(2)

    def text_flip_6cards(self):
        list_data1=[]
        list_6_elements=[]
       
        six_elements=self.driver.find_elements(By.XPATH, "//p[@class='text-grey mb-0 fontSize-2_4 mt-20'][text()]")
        for each_element in six_elements:
            print("locater_text_6: ", each_element.text)
            list_6_elements.append(each_element.text)

        for r in range(54,60):
            data1=XLUtils.readData(self.path,"HomePage",r,2)
            list_data1.append(data1)
        print("excel values:", list_data1)
        print("locaters value:", list_6_elements)
        print(len(list_data1))
        print(len(list_6_elements))
            
        for i in range(0,len(list_data1)):
            print("this is i value", i)
            for r in range(54,60):
                print("this is r value", r)
                if list_data1[i]==list_6_elements[i]:
                    XLUtils.writeData(self.path,"HomePage",r,3,"pass")
                    XLUtils.fillGreenColor(self.path,"HomePage",r,3)
                    assert True
                else:
                    XLUtils.writeData(self.path,"HomePage",r,3,"failed")
                    XLUtils.fillRedColor(self.path,"HomePage",r,3)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
                    assert False

#================================================================CLIENTS SECTION================================================================
    def click_clients_carousel1_x(self):
        clients_carousel1_x= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.clients_carousel1_x))
        self.driver.execute_script("arguments[0].click();",clients_carousel1_x)
        time.sleep(1)

    def clients_crsl1_name_assert(self):
        clients_crsl1_name_assert=XLUtils.readData(self.path,"HomePage",20,2)
        print(clients_crsl1_name_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl1_name_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl1_name_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl1_name_assert)).text == clients_crsl1_name_assert:
            XLUtils.writeData(self.path,"HomePage",20,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",20,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",20,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",20,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def clients_crsl1_des_assert(self):
        clients_crsl1_des_assert=XLUtils.readData(self.path,"HomePage",21,2)
        print(clients_crsl1_des_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl1_des_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl1_des_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl1_des_assert)).text == clients_crsl1_des_assert:
            XLUtils.writeData(self.path,"HomePage",21,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",21,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",21,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",21,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_clients_carousel2_x(self):
        clients_carousel2_x= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.clients_carousel2_x))
        self.driver.execute_script("arguments[0].click();",clients_carousel2_x)
        time.sleep(1)

    def clients_crsl2_name_assert(self):
        clients_crsl2_name_assert=XLUtils.readData(self.path,"HomePage",21,2)
        print(clients_crsl2_name_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl2_name_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl2_name_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl2_name_assert)).text == clients_crsl2_name_assert:
            XLUtils.writeData(self.path,"HomePage",21,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",21,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",21,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",21,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def clients_crsl2_des_assert(self):
        clients_crsl2_des_assert=XLUtils.readData(self.path,"HomePage",22,2)
        print(clients_crsl2_des_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl2_des_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl2_des_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl2_des_assert)).text == clients_crsl2_des_assert:
            XLUtils.writeData(self.path,"HomePage",22,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",22,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",22,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",22,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_clients_carousel3_x(self):
        clients_carousel3_x= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.clients_carousel3_x))
        self.driver.execute_script("arguments[0].click();",clients_carousel3_x)
        time.sleep(1)

    def clients_crsl3_name_assert(self):
        clients_crsl3_name_assert=XLUtils.readData(self.path,"HomePage",23,2)
        print(clients_crsl3_name_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl3_name_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl3_name_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl3_name_assert)).text == clients_crsl3_name_assert:
            XLUtils.writeData(self.path,"HomePage",23,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",23,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",23,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",23,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def clients_crsl3_des_assert(self):
        clients_crsl3_des_assert=XLUtils.readData(self.path,"HomePage",24,2)
        print(clients_crsl3_des_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl3_des_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl3_des_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl3_des_assert)).text == clients_crsl3_des_assert:
            XLUtils.writeData(self.path,"HomePage",24,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",24,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",24,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",24,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_clients_carousel4_x(self):
        clients_carousel4_x= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.clients_carousel4_x))
        self.driver.execute_script("arguments[0].click();",clients_carousel4_x)
        time.sleep(1)

    def clients_crsl4_name_assert(self):
        clients_crsl4_name_assert=XLUtils.readData(self.path,"HomePage",25,2)
        print(clients_crsl4_name_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl4_name_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl4_name_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl4_name_assert)).text == clients_crsl4_name_assert:
            XLUtils.writeData(self.path,"HomePage",25,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",25,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",25,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",25,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def clients_crsl4_des_assert(self):
        clients_crsl4_des_assert=XLUtils.readData(self.path,"HomePage",26,2)
        print(clients_crsl4_des_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl4_des_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl4_des_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl4_des_assert)).text == clients_crsl4_des_assert:
            XLUtils.writeData(self.path,"HomePage",26,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",26,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",26,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",26,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_clients_carousel5_x(self):
        clients_carousel5_x= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.clients_carousel5_x))
        self.driver.execute_script("arguments[0].click();",clients_carousel5_x)
        time.sleep(1)

    def clients_crsl5_name_assert(self):
        clients_crsl5_name_assert=XLUtils.readData(self.path,"HomePage",27,2)
        print(clients_crsl5_name_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl5_name_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl5_name_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl5_name_assert)).text == clients_crsl5_name_assert:
            XLUtils.writeData(self.path,"HomePage",27,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",27,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",27,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",27,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def clients_crsl5_des_assert(self):
        clients_crsl5_des_assert=XLUtils.readData(self.path,"HomePage",28,2)
        print(clients_crsl5_des_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl5_des_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl5_des_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl5_des_assert)).text == clients_crsl5_des_assert:
            XLUtils.writeData(self.path,"HomePage",28,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",28,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",28,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",28,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_clients_carousel6_x(self):
        clients_carousel6_x= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.clients_carousel6_x))
        self.driver.execute_script("arguments[0].click();",clients_carousel6_x)
        time.sleep(1)

    def clients_crsl6_name_assert(self):
        clients_crsl6_name_assert=XLUtils.readData(self.path,"HomePage",29,2)
        print(clients_crsl6_name_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl6_name_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl6_name_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl6_name_assert)).text == clients_crsl6_name_assert:
            XLUtils.writeData(self.path,"HomePage",29,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",29,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",29,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",29,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def clients_crsl6_des_assert(self):
        clients_crsl6_des_assert=XLUtils.readData(self.path,"HomePage",30,2)
        print(clients_crsl6_des_assert)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_crsl6_des_assert))
        print((self.driver.find_element(*LocatorsHomePage().clients_crsl6_des_assert)).text)
        if (self.driver.find_element(*LocatorsHomePage.clients_crsl6_des_assert)).text == clients_crsl6_des_assert:
            XLUtils.writeData(self.path,"HomePage",30,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",30,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",30,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",30,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def clients_12elements(self):
        # clients_slide2_6elements=self.driver.find_elements(By.XPATH,"//div[@id='slide-ngb-slide-35']/div[@class='row justify-content-sm-center ng-star-inserted']/div[@class='col mb-30']")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.clients_slides_12elements))
        time.sleep(2)

    def clients_slides_12elements_text(self):
        clients12=self.driver.find_elements(By.XPATH,"//ngb-carousel[@class='carousel slide client_carousel_slides client_carousel_indicator_height']//div[@class='row justify-content-sm-center ng-star-inserted']/div[@class='col mb-30']//descendant::img[@alt]")
        # clients12=WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(LocatorsHomePage.clients_slides_12elements))
        print(len(clients12))
        print(type(clients12))
        for each_client in clients12:
            clients12=self.driver.find_elements(By.XPATH,"//ngb-carousel[@class='carousel slide client_carousel_slides client_carousel_indicator_height']//div[@class='row justify-content-sm-center ng-star-inserted']/div[@class='col mb-30']//descendant::img[@alt]")
            print(each_client.get_attribute('alt'))
        time.sleep(1)

    def assert_10_companynames(self):
        list_data10=[]
        list_eachEle=[]
        
        ten_names=self.driver.find_elements(By.XPATH,"//ngb-carousel[@class='carousel slide client_carousel_slides client_carousel_indicator_height']//div[@class='row justify-content-sm-center ng-star-inserted']/div[@class='col mb-30']//descendant::img[@alt]")
        for each_element in ten_names[0:]:
            ten_names=self.driver.find_elements(By.XPATH,"//ngb-carousel[@class='carousel slide client_carousel_slides client_carousel_indicator_height']//div[@class='row justify-content-sm-center ng-star-inserted']/div[@class='col mb-30']//descendant::img[@alt]")
            print(each_element.get_attribute('alt'))
            list_eachEle.append(each_element.get_attribute('alt'))
        print(list_eachEle)
        while("" in list_eachEle):
            list_eachEle.remove("")
        print("Modified list is : " + str(list_eachEle))
            
        for r in range(43,53):
            data10=XLUtils.readData(self.path,"HomePage",r,2)
            list_data10.append(data10)
        print(list_data10)
        print(list_eachEle)
            
        for i in range(0,len(list_data10)) :
            # print("this is i:",i)
            for s in range(43,53):
                # print("this is s:",s)
                if list_data10[i]==list_eachEle[i]:
                    XLUtils.writeData(self.path,"HomePage",s,3,"pass")
                    XLUtils.fillGreenColor(self.path,"HomePage",s,3)
                    assert True
                else:
                    XLUtils.writeData(self.path,"HomePage",s,3,"failed")
                    XLUtils.fillRedColor(self.path,"HomePage",s,3)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
                    assert False 

    #================================================================Footer================================================================

    def footer_headline(self):
        footer_headline=XLUtils.readData(self.path,"HomePage",33,2)
        print(footer_headline)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_headline))
        print((self.driver.find_element(*LocatorsHomePage().footer_headline)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_headline)).text == footer_headline:
            XLUtils.writeData(self.path,"HomePage",33,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",33,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",33,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",33,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_switzerland(self):
        footer_assert_switzerland=XLUtils.readData(self.path,"HomePage",34,2)
        print(footer_assert_switzerland)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_switzerland))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_switzerland)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_switzerland)).text == footer_assert_switzerland:
            XLUtils.writeData(self.path,"HomePage",34,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",34,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",34,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",34,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_Ind_mang(self):
        footer_assert_br_Ind_mang=XLUtils.readData(self.path,"HomePage",35,2)
        print(footer_assert_br_Ind_mang)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_Ind_mang))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_Ind_mang)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_Ind_mang)).text == footer_assert_br_Ind_mang:
            XLUtils.writeData(self.path,"HomePage",35,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",35,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",35,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",35,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_canada(self):
        footer_assert_br_canada=XLUtils.readData(self.path,"HomePage",36,2)
        print(footer_assert_br_canada)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_canada))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_canada)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_canada)).text == footer_assert_br_canada:
            XLUtils.writeData(self.path,"HomePage",36,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",36,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",36,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",36,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_Ind_bang(self):
        footer_assert_br_Ind_bang=XLUtils.readData(self.path,"HomePage",37,2)
        print(footer_assert_br_Ind_bang)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_Ind_bang))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_Ind_bang)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_Ind_bang)).text == footer_assert_br_Ind_bang:
            XLUtils.writeData(self.path,"HomePage",37,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",37,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",37,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",37,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_company_name(self):
        footer_assert_company_name=XLUtils.readData(self.path,"HomePage",38,2)
        print(footer_assert_company_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_company_name))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_company_name)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_company_name)).text == footer_assert_company_name:
            XLUtils.writeData(self.path,"HomePage",38,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",38,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",38,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",38,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_mail_address(self):
        footer_assert_mail_address=XLUtils.readData(self.path,"HomePage",39,2)
        print(footer_assert_mail_address)

        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_mail_address))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_mail_address)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_mail_address)).text == footer_assert_mail_address:
            XLUtils.writeData(self.path,"HomePage",39,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",39,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",39,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",39,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_end_text(self):
        footer_end_text=XLUtils.readData(self.path,"HomePage",40,2)
        print(footer_end_text)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_end_text))
        print((self.driver.find_element(*LocatorsHomePage().footer_end_text)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_end_text)).text == footer_end_text:
            XLUtils.writeData(self.path,"HomePage",40,3,"pass")
            XLUtils.fillGreenColor(self.path,"HomePage",40,3)
            assert True
        else:
            XLUtils.writeData(self.path,"HomePage",40,3,"failed")
            XLUtils.fillRedColor(self.path,"HomePage",40,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_footer_insta_link(self):
        footer_insta_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.footer_insta_link))
        self.driver.execute_script("arguments[0].click();",footer_insta_link)
        time.sleep(1)
        # print(self.driver.current_window_handle, "#value of parent window")
        # handles=self.driver.window_handles
        # print(handles, "#value of child windows")

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
        print(self.driver.current_window_handle, "#value of parent window")
        child_windows=self.driver.window_handles
        print(child_windows, "#value of child windows")
        for each_window in child_windows:
            self.driver.switch_to.window(each_window)
            print(self.driver.title, "#title of all windows")
            time.sleep(1)
            if self.driver.title!="Software development services - Bix Bytes Solutions":
               self.driver.close()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_footer_mail_address_link(self):
        # ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
        # time.sleep(2)
        # headline= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.txt_hpg_headline_x))
        # headline.click()
        for i in range(0,3):
            if i<3:    
                ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        # ActionChains.move_to_element(footer_mail_address_link).perform()
        footer_mail_address_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.footer_mail_address_link))
        self.driver.execute_script("arguments[0].click();",footer_mail_address_link)
        time.sleep(4)

    def close_mail_window(self):
        pyautogui.hotkey('alt','F4')
        time.sleep(2)
        pyautogui.hotkey('PAGE_DOWN','ENTER')
        time.sleep(2)
        for i in range(0,3):
            if i<3:    
                ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        time.sleep(2)
        
    def footer_contact_num_link(self):
        footer_contact_num_link= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsHomePage.footer_contact_num_link))
        self.driver.execute_script("arguments[0].click();",footer_contact_num_link)
        time.sleep(2)

    def clear_pop_up(self):
        pyautogui.press('Esc')
        time.sleep(2)

       


