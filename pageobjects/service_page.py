
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
from pageobjects.locators import LocatorsServices
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

class ServicesPage():
    
    path=r"test_data\BBS6.xlsx"

    def __init__(self,driver):
        self.driver=driver

    def create_excel(self):
        # workbook=xlsxwriter.Workbook(r"C:\Nagalakshmi\PythonPractice\BBS_automation\test_data\BBS.xlsx")
        # worksheet = workbook.add_worksheet("Services")
        # worksheet.write(0, 0, "TEXT FOR ASSERTION")
        # worksheet.write(0, 1, "RESULTS")
        # worksheet.write(2, 0, "SERVICES")
        # worksheet.write(3, 0, "Services we provide")
        # worksheet.write(5, 0, "Our Services")
        # worksheet.write(6, 0, "Software development made easy")
        # worksheet.write(7, 0, "Consultancy")
        # worksheet.write(8, 0, "UI/UX Design")
        # worksheet.write(9, 0, "Engineering")
        # worksheet.write(10, 0, "QA Services")
        # worksheet.write(11, 0, "Collaboration")
        # worksheet.write(12, 0, "Outsourcing")
        # worksheet.write(14, 0, "SALESFORCE CRM:")
        # worksheet.write(15, 0, "Salesforce CRM")
        # worksheet.write(16, 0, "Your Salesforce Partner for success")
        # worksheet.write(17, 0, "Business Consulting")
        # worksheet.write(18, 0, "Data Services")
        # worksheet.write(19, 0, "Integration Services")
        # worksheet.write(20, 0, "Business Systems Automation")
        # worksheet.write(21, 0, "Managed Services")
        # worksheet.write(22, 0, "Strategic Consulting Services")
        # worksheet.write(23, 0, "Product Development (ISV)")
        # worksheet.write(25, 0, "Our Values:")
        # worksheet.write(26, 0, "Our Values")
        # worksheet.write(27, 0, "RESPONSIVE AND TIMELY")
        # worksheet.write(28, 0, "INDIVIDUALIZED")
        # worksheet.write(29, 0, "CLIENT SATISFACTION")
        # worksheet.write(31, 0, "Our Expertise:")
        # worksheet.write(32, 0, "Our Expertise")
        # worksheet.write(33, 0, "HEALTHCARE")
        # worksheet.write(34, 0, "REAL ESTATE")
        # worksheet.write(35, 0, "TRAVEL AGENCY")
        # worksheet.write(36, 0, "PROJECT MANAGEMENT")
        # worksheet.write(38, 0, "Agile Framework:")
        # worksheet.write(39, 0, "Agile Framework")
        # worksheet.write(40, 0, "AGILE FRAMEWORK")
        # worksheet.write(41, 0, "Term scrum")
        # worksheet.write(42, 0, "Scrum method")
        # worksheet.write(43, 0, "Scrum definition")
        # worksheet.write(45, 0, "Our Process section:")
        # worksheet.write(46, 0, "OUR PROCESS")
        # worksheet.write(47, 0, "Requirements")
        # worksheet.write(48, 0, "Design Wireframe")
        # worksheet.write(49, 0, "Design Visual Rollout")
        # worksheet.write(50, 0, "Coding")
        # worksheet.write(51, 0, "Verification Testing")
        # worksheet.write(52, 0, "Implementation")
        # worksheet.write(53, 0, "Maintenance")
        # worksheet.write(55, 0, "Let's Discuss Your Ideas section:")
        # worksheet.write(56, 0,"Let's Discuss Your Ideas")
        # worksheet.write(57, 0,"This field is required.")
        # worksheet.write(59, 0, "FOOTER:")
        # worksheet.write(60, 0, "GET IN TOUCH")
        # worksheet.write(61, 0, "SWITZERLAND")
        # worksheet.write(62, 0, "INDIA - Mangalore")
        # worksheet.write(63, 0, "CANADA")
        # worksheet.write(64, 0, "INDIA - Bangalore")
        # worksheet.write(65, 0, "Bix Bytes Solutions Pvt. Ltd.")
        # worksheet.write(66, 0, "info@bixbytessolutions.com")
        # worksheet.write(67, 0, "Copyright © 2022 BixBytes Solutions")
        
        # workbook.close()
        wb = Workbook()
        file_path = "test_data"
        create_duplicate = 'BixBytes website' + str(datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')) + '.xlsx'
        replica = os.path.join(file_path, create_duplicate)
        wb.save(replica)
        source = "test_data\BBS6.xlsx"
        dest = replica
        shutil.copy(source, dest)

#================================================================SERVICES PAGE================================================================
    def click_hamburger(self):
        self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()

    def menu_services_link(self):
        menu_services_link=XLUtils.readData(self.path,"Services",3,2)
        print(menu_services_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_services_link))
        print((self.driver.find_element(*LocatorsMenu().menu_services_link)).text)
        if (self.driver.find_element(*LocatorsMenu.menu_services_link)).text == menu_services_link:
            XLUtils.writeData(self.path,"Services",3,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",3,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",3,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",3,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(2)
        services=self.driver.find_element(*LocatorsMenu.menu_services_link)
        self.driver.execute_script('arguments[0].click()', services)
        time.sleep(2)
        hamburger=self.driver.find_element(*LocatorsServices.hamburger_service_page_x)
        self.driver.execute_script('arguments[0].click()', hamburger)
        time.sleep(2)
        self.driver.refresh()

    def scroll_down_Page(self):
        # self.driver.refresh()
        headline= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsServices.services_headline_x))
        headline.click()
        for i in range(0,8):
            if i<8:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
                 time.sleep(1)

    def scroll_up_Page(self):
        for i in range(0,8):
            if i<8:
                 ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
                 time.sleep(1)

    def scroll_stop_between(self):
        headline= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsServices.services_headline_x))
        headline.click()
        for i in range(0,3):
            if i<5:
                 ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                 time.sleep(1)

    def services_headline_x(self):
        ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
        services_headline_x=XLUtils.readData(self.path,"Services",4,2)
        print(services_headline_x)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.services_headline_x))
        print((self.driver.find_element(*LocatorsServices().services_headline_x)).text)
        if (self.driver.find_element(*LocatorsServices.services_headline_x)).text == services_headline_x:
            XLUtils.writeData(self.path,"Services",4,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",4,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",4,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",4,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def services_5menu_icons(self):
        menu_icons=self.driver.find_elements(By.XPATH, "//div[@class='bbs_activetab service_tab']")
        for icon in range(len(menu_icons)):
            menu_icons=self.driver.find_elements(By.XPATH, "//div[@class='bbs_activetab service_tab']")
            self.driver.execute_script('arguments[0].click()', menu_icons[icon])
            time.sleep(2)

#================================================================OUR SERVICES================================================================
    
    def our_services(self):
        our_services=self.driver.find_element(*LocatorsServices.our_services_tab)
        self.driver.execute_script('arguments[0].click()', our_services)
        list_data1=[]
        seven_elements= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsServices.our_services_7headlines))
        text_of_7ele = seven_elements.text
        all_elements_in_list = text_of_7ele.replace("\n",",").split(",")
        print(all_elements_in_list, "<==locators data==>")
        print(len(all_elements_in_list))
        
        for r in range(7,14):
            data1=XLUtils.readData(self.path,"Services",r,2)
            list_data1.append(data1)
        print(list_data1, "<==Excel data==>")
        print(len(list_data1))

        for i in range(len(all_elements_in_list)): #we can take len(list_data1), result will be same because both the length is equal to 7.
            for t in range(7,14):
                if list_data1[i]==all_elements_in_list[i]:
                    XLUtils.writeData(self.path,"Services",t,3,"pass")
                    XLUtils.fillGreenColor(self.path,"Services",t,3)
                    assert True
                else:
                    XLUtils.writeData(self.path,"Services",t,3,"failed")
                    XLUtils.fillRedColor(self.path,"Services",t,3)
                    assert False

    def click_6readmore_links(self):
        links=self.driver.find_elements(By.XPATH, "//a[@class='d-flex justify-content-end fontSize-2_4 font-weight-400']")
        for link in range(len(links)):
            for i in range(0,3):
                if i<3:
                    ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                    time.sleep(1)
                    links=self.driver.find_elements(By.XPATH, "//a[@class='d-flex justify-content-end fontSize-2_4 font-weight-400']")
                    self.driver.execute_script('arguments[0].click()', links[link])
                    time.sleep(2)
                    our_ser_tab=self.driver.find_element(*LocatorsServices.our_services_tab)
                    self.driver.execute_script('arguments[0].click()', our_ser_tab)
                    time.sleep(2)

#================================================================SALESFORCE CRM================================================================
    def assert_salesforce_name(self):
        salesforce_crm_tab=XLUtils.readData(self.path,"Services",16,2)
        print(salesforce_crm_tab)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.salesforce_crm_tab)).click()
        print((self.driver.find_element(*LocatorsServices().salesforce_crm_tab)).text)
        if (self.driver.find_element(*LocatorsServices.salesforce_crm_tab)).text == salesforce_crm_tab:
            XLUtils.writeData(self.path,"Services",16,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",16,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",16,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",16,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
    
    def salesforce_headline_x(self):
        salesforce_crm_heading=XLUtils.readData(self.path,"Services",17,2)
        print(salesforce_crm_heading)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.salesforce_crm_heading))
        print((self.driver.find_element(*LocatorsServices().salesforce_crm_heading)).text)
        if (self.driver.find_element(*LocatorsServices.salesforce_crm_heading)).text == salesforce_crm_heading:
            XLUtils.writeData(self.path,"Services",17,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",17,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",17,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",17,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def assert_7hdlines_salesforce_crm(self):
        salesforce=self.driver.find_element(*LocatorsServices.salesforce_crm_tab)
        self.driver.execute_script('arguments[0].click()', salesforce)
        list_data1=[]
        seven_elements= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsServices.salesforce_crm_7headlines))
        text_of_7ele = seven_elements.text
        all_elements_in_list = text_of_7ele.replace("\n",",").split(",")
        print(all_elements_in_list, "<==locators data==>")
        print(len(all_elements_in_list))
        
        for r in range(18,25):
            data1=XLUtils.readData(self.path,"Services",r,2)
            list_data1.append(data1)
        print(list_data1, "<==Excel data==>")
        print(len(list_data1))

        for i in range(len(all_elements_in_list)): #we can take len(list_data1), result will be same because both the length is equal to 7.
            for t in range(18,25):
                if list_data1[i]==all_elements_in_list[i]:
                    XLUtils.writeData(self.path,"Services",t,3,"pass")
                    XLUtils.fillGreenColor(self.path,"Services",t,3)
                    assert True
                else:
                    XLUtils.writeData(self.path,"Services",t,3,"failed")
                    XLUtils.fillRedColor(self.path,"Services",t,3)
                    assert False

    def click_5readmore_links(self):
        links=self.driver.find_elements(By.XPATH, "//a[@class='d-flex justify-content-end fontSize-2_4 font-weight-400']")
        for link in range(len(links)):
            ActionChains(self.driver).send_keys(Keys.SPACE).perform()
            ActionChains(self.driver).send_keys(Keys.SPACE).perform()
            time.sleep(1)
            links=self.driver.find_elements(*LocatorsServices.salesforce_5readmore_links)
            self.driver.execute_script('arguments[0].click()', links[link])
            time.sleep(2)
            salesforce_crm_tab=self.driver.find_element(*LocatorsServices.salesforce_crm_tab)
            self.driver.execute_script('arguments[0].click()', salesforce_crm_tab)
            time.sleep(2)
        # for i in range(0,3):
        #         if i<3:
        #             ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        # readmore_6th=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsServices.salesforce_6th_readmore_links))
        # readmore_6th.click()
        salesforce_crm_tab=self.driver.find_element(*LocatorsServices.salesforce_crm_tab).click()
        time.sleep(2)
#================================================================OUR VALUES================================================================
    def assert_our_values_tab(self):
        our_values_tab=XLUtils.readData(self.path,"Services",27,2)
        print(our_values_tab)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.our_values_tab)).click()
        print((self.driver.find_element(*LocatorsServices().our_values_tab)).text)
        if (self.driver.find_element(*LocatorsServices.our_values_tab)).text == our_values_tab:
            XLUtils.writeData(self.path,"Services",27,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",27,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",27,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",27,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def assert_3hdlines_ourvalues(self):
        our_values_tab=self.driver.find_element(*LocatorsServices.our_values_tab)
        self.driver.execute_script('arguments[0].click()', our_values_tab)
        list_data1=[]
        three_elements= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsServices.our_values_3headlines))
        text_of_3ele = three_elements.text
        list_3_elements= text_of_3ele.replace("\n",",").split(",")
        print(list_3_elements, "<==locators data==>")
        print(len(list_3_elements))
        
        for r in range(28,31):
            data1=XLUtils.readData(self.path,"Services",r,2)
            list_data1.append(data1)
        print(list_data1, "<==Excel data==>")
        print(len(list_data1))

        for i in range(len(list_3_elements)): #we can take len(list_data1), result will be same because both the length is equal to 7.
            for t in range(28,31):
                if list_data1[i]==list_3_elements[i]:
                    XLUtils.writeData(self.path,"Services",t,3,"pass")
                    XLUtils.fillGreenColor(self.path,"Services",t,3)
                    assert True
                else:
                    XLUtils.writeData(self.path,"Services",t,3,"failed")
                    XLUtils.fillRedColor(self.path,"Services",t,3)
                    assert False

#================================================================OUR EXPERTISE================================================================

    def our_expertise_tab(self):
        our_expertise_tab=XLUtils.readData(self.path,"Services",33,2)
        print(our_expertise_tab)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.our_expertise_tab)).click()
        print((self.driver.find_element(*LocatorsServices().our_expertise_tab)).text)
        if (self.driver.find_element(*LocatorsServices.our_expertise_tab)).text == our_expertise_tab:
            XLUtils.writeData(self.path,"Services",33,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",33,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",33,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",33,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def our_exprts_4headlines(self):
        list_data1=[]
        list_4_elements=[]
       
        four_elements=self.driver.find_elements(*LocatorsServices.our_exprts_4headlines)
        for each_element in four_elements:
            list_4_elements.append(each_element.text)

        for r in range(34,38):
            data1=XLUtils.readData(self.path,"Services",r,2)
            list_data1.append(data1)
        print(list_data1)
        print(list_4_elements)
        print(len(list_data1))
        print(len(list_4_elements))
            
        for i in range(len(list_data1)) :
            for r in range(34,38):
                if list_data1[i]==list_4_elements[i]:
                    XLUtils.writeData(self.path,"Services",r,3,"pass")
                    XLUtils.fillGreenColor(self.path,"Services",r,3)
                    assert True
                else:
                    XLUtils.writeData(self.path,"Services",r,3,"failed")
                    XLUtils.fillRedColor(self.path,"Services",r,3)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
                    assert False 
#================================================================AGILE FRAMEWORK================================================================#

    def agile_framework_tab(self):
        agile_framework_tab=XLUtils.readData(self.path,"Services",40,2)
        print(agile_framework_tab)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.agile_framework_tab)).click()
        print((self.driver.find_element(*LocatorsServices().agile_framework_tab)).text)
        if (self.driver.find_element(*LocatorsServices.agile_framework_tab)).text == agile_framework_tab:
            XLUtils.writeData(self.path,"Services",40,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",40,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",40,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",40,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def hdline_agile_framework(self):
        hdline_agile_framework=XLUtils.readData(self.path,"Services",41,2)
        print(hdline_agile_framework)
        print((self.driver.find_element(*LocatorsServices().hdline_agile_framework)).text)
        if (self.driver.find_element(*LocatorsServices.hdline_agile_framework)).text == hdline_agile_framework:
            XLUtils.writeData(self.path,"Services",41,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",41,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",41,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",41,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def hdlines3_agile_framework(self):
        list_data1=[]
        list_3_elements=[]
       
        three_elements=self.driver.find_elements(*LocatorsServices.hdlines3_agile_framework)
        for each_element in three_elements:
            list_3_elements.append(each_element.text)

        for r in range(42,45):
            data1=XLUtils.readData(self.path,"Services",r,2)
            list_data1.append(data1)
        print(list_data1)
        print(list_3_elements)
        print(len(list_data1))
        print(len(list_3_elements))
            
        for i in range(len(list_data1)) :
            for r in range(42,45):
                if list_data1[i]==list_3_elements[i]:
                    XLUtils.writeData(self.path,"Services",r,3,"pass")
                    XLUtils.fillGreenColor(self.path,"Services",r,3)
                    assert True
                else:
                    XLUtils.writeData(self.path,"Services",r,3,"failed")
                    XLUtils.fillRedColor(self.path,"Services",r,3)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
                    assert False 
    
    def link_soft_dev_af(self):
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        link_soft_dev_af=self.driver.find_element(*LocatorsServices.link_soft_dev_af)
        self.driver.execute_script('arguments[0].click()', link_soft_dev_af)
        time.sleep(3)
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        time.sleep(3)
        self.driver.back()

    def link_proj_mgmnt_af(self):
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        link_proj_mgmnt_af=self.driver.find_element(*LocatorsServices.link_proj_mgmnt_af)
        self.driver.execute_script('arguments[0].click()', link_proj_mgmnt_af)
        time.sleep(3)
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        time.sleep(3)
        self.driver.back()

    def link_scrum_defn_af(self):
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        link_scrum_defn_af=self.driver.find_element(*LocatorsServices.link_scrum_defn_af)
        self.driver.execute_script('arguments[0].click()', link_scrum_defn_af)

    def close_child_windows(self):
        print(self.driver.current_window_handle, "#value of parent window")
        child_windows=self.driver.window_handles
        print(child_windows, "#value of child windows")
        for each_window in child_windows:
            self.driver.switch_to.window(each_window)
            print(self.driver.title, "#title of all windows")
            time.sleep(1)
            if self.driver.title!="Agile Framework for Software Engineering - Bix Bytes Solutions":
               self.driver.close()
               time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0]) 
#================================================================OUR PROCESS================================================================#

    def assert_our_process_sec(self):
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.our_services_tab)).click()
        our_services_tab=self.driver.find_element(*LocatorsServices.our_services_tab)
        self.driver.execute_script('arguments[0].click()', our_services_tab)
        for i in range(0,3):
                if i<3:
                    ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        assert_our_process_sec=XLUtils.readData(self.path,"Services",47,2)
        print(assert_our_process_sec)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsServices.assert_our_process_sec))
        print((self.driver.find_element(*LocatorsServices().assert_our_process_sec)).text)
        if (self.driver.find_element(*LocatorsServices.assert_our_process_sec)).text == assert_our_process_sec:
            XLUtils.writeData(self.path,"Services",47,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",47,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",47,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",47,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def asrt_7process_testing(self):
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.our_services_tab)).click()
        # for i in range(0,3):
        #         if i<3:
        #             ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        list_data1=[]
        list_7_elements=[]
       
        seven_elements=self.driver.find_elements(By.XPATH, "/html[1]/body[1]/app-root[1]/app-layout[1]/div[1]/app-our-service[1]/app-our-process[1]/section[1]/div[1]/div[2]/ul/li/span")
        for each_element in seven_elements:
            print("locater_text_7: ", each_element.text)
            list_7_elements.append(each_element.text)

        for r in range(48,55):
            data1=XLUtils.readData(self.path,"Services",r,2)
            list_data1.append(data1)
        print(list_data1)
        print(list_7_elements)
        print(len(list_data1))
        print(len(list_7_elements))
            
        for i in range(0,len(list_data1)):
            for r in range(48,55):
                if list_data1[i]==list_7_elements[i]:
                    XLUtils.writeData(self.path,"Services",r,3,"pass")
                    XLUtils.fillGreenColor(self.path,"Services",r,3)
                    assert True
                else:
                    XLUtils.writeData(self.path,"Services",r,3,"failed")
                    XLUtils.fillRedColor(self.path,"Services",r,3)
                    self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BPMT admin_login\\screenshots\\failed_tc.png")
                    allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
                    assert False

#================================================================LET'S DISCUSS YOUR IDEA SECTION================================================================#
    def lets_discuss_sec_heline(self):
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.our_services_tab)).click()
        # for i in range(0,5):
        #         if i<5:
        #             ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        lets_discuss_sec_heline=XLUtils.readData(self.path,"Services",57,2)
        print(lets_discuss_sec_heline)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsServices.lets_discuss_sec_heline))
        print((self.driver.find_element(*LocatorsServices().lets_discuss_sec_heline)).text)
        if (self.driver.find_element(*LocatorsServices.lets_discuss_sec_heline)).text == lets_discuss_sec_heline:
            XLUtils.writeData(self.path,"Services",57,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",57,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",57,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",57,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def name_field_lets_sec(self):
        name=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.name_field_lets_sec))
        name.send_keys("xyz")

    def email_field_lets_sec(self):
        email=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.email_field_lets_sec))
        email.send_keys("xyz@gmail.com")

    def empty_field_warning_msg(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.empty_field_warning_msg))
        war_msg=XLUtils.readData(self.path,"Services",59,2)
        print(war_msg)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsServices.captch_warning_msg))
        print((self.driver.find_element(*LocatorsServices().empty_field_warning_msg)).text)
        if (self.driver.find_element(*LocatorsServices.empty_field_warning_msg)).text == war_msg:
            XLUtils.writeData(self.path,"Services",59,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",59,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",58,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",58,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def captch_warning_msg(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsServices.captch_warning_msg))
        war_msg=XLUtils.readData(self.path,"Services",58,2)
        print(war_msg)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocatorsServices.captch_warning_msg))
        print((self.driver.find_element(*LocatorsServices().captch_warning_msg)).text)
        if (self.driver.find_element(*LocatorsServices.captch_warning_msg)).text == war_msg:
            XLUtils.writeData(self.path,"Services",58,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",58,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",58,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",58,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def btn_get_touch_lets(self):
        conf_btn=self.driver.find_element(*LocatorsServices.btn_get_touch_lets)
        self.driver.execute_script('arguments[0].click()', conf_btn)

#================================================================Footer================================================================#

    def footer_headline(self):
        footer_headline=XLUtils.readData(self.path,"Services",61,2)
        print(footer_headline)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_headline))
        print((self.driver.find_element(*LocatorsHomePage().footer_headline)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_headline)).text == footer_headline:
            XLUtils.writeData(self.path,"Services",61,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",61,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",61,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",61,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_switzerland(self):
        footer_assert_switzerland=XLUtils.readData(self.path,"Services",62,2)
        print(footer_assert_switzerland)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_switzerland))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_switzerland)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_switzerland)).text == footer_assert_switzerland:
            XLUtils.writeData(self.path,"Services",62,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",62,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",62,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",62,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_Ind_mang(self):
        footer_assert_br_Ind_mang=XLUtils.readData(self.path,"Services",63,2)
        print(footer_assert_br_Ind_mang)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_Ind_mang))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_Ind_mang)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_Ind_mang)).text == footer_assert_br_Ind_mang:
            XLUtils.writeData(self.path,"Services",63,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",63,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",63,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",63,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_canada(self):
        footer_assert_br_canada=XLUtils.readData(self.path,"Services",64,2)
        print(footer_assert_br_canada)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_canada))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_canada)).text)
        if (self.driver.find_element(*LocatorsHomePage().footer_assert_br_canada)).text == footer_assert_br_canada:
            XLUtils.writeData(self.path,"Services",64,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",64,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",64,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",64,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_Ind_bang(self):
        footer_assert_br_Ind_bang=XLUtils.readData(self.path,"Services",65,2)
        print(footer_assert_br_Ind_bang)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_Ind_bang))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_Ind_bang)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_Ind_bang)).text == footer_assert_br_Ind_bang:
            XLUtils.writeData(self.path,"Services",65,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",65,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",65,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",65,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_company_name(self):
        footer_assert_company_name=XLUtils.readData(self.path,"Services",66,2)
        print(footer_assert_company_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_company_name))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_company_name)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_company_name)).text == footer_assert_company_name:
            XLUtils.writeData(self.path,"Services",66,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",66,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",66,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",66,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
            time.sleep(2)

    def footer_mailaddress_company_page(self):
        footer_mailaddress_company_page=XLUtils.readData(self.path,"Services",67,2)
        print(footer_mailaddress_company_page)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(LocatorsCompany.footer_mailaddress_company_page))
        print((self.driver.find_element(*LocatorsCompany().footer_mailaddress_company_page)).text)
        if (self.driver.find_element(*LocatorsCompany.footer_mailaddress_company_page)).text == footer_mailaddress_company_page:
            XLUtils.writeData(self.path,"Services",67,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",67,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",67,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",67,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
            time.sleep(2)

    def footer_end_text(self):
        footer_end_text=XLUtils.readData(self.path,"Services",68,2)
        print(footer_end_text)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_end_text))
        print((self.driver.find_element(*LocatorsHomePage().footer_end_text)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_end_text)).text == footer_end_text:
            XLUtils.writeData(self.path,"Services",68,3,"pass")
            XLUtils.fillGreenColor(self.path,"Services",68,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Services",68,3,"failed")
            XLUtils.fillRedColor(self.path,"Services",68,3)
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
        print(self.driver.current_window_handle, "#value of parent window")
        child_windows=self.driver.window_handles
        print(child_windows, "#value of child windows")
        for each_window in child_windows:
            self.driver.switch_to.window(each_window)
            print(self.driver.title, "#title of all windows")
            time.sleep(1)
            if self.driver.title!="Software development services - Bix Bytes Solutions":
               self.driver.close()
               time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_footer_mail_address_link(self):
        footer_mailaddress_company_page= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsCompany.footer_mailaddress_company_page))
        self.driver.execute_script("arguments[0].click();",footer_mailaddress_company_page)
        time.sleep(2)

    def close_mail_window(self):
        pyautogui.hotkey('alt','F4')
        time.sleep(2)
        pyautogui.hotkey('PAGE_DOWN','ENTER')
        
    def footer_contact_num_link_cp(self):
        footer_contact_num_link_cp= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsCompany.footer_contact_num_link_cp))
        self.driver.execute_script("arguments[0].click();",footer_contact_num_link_cp)

    def clear_pop_up(self):
        pyautogui.press('Esc') 
        
   

   
    
        
    
