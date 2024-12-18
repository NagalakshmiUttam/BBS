import datetime
import os
from selenium.webdriver.common.by import By
from utilities import XLUtils
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pageobjects.locators import LocatorsHomePage
from pageobjects.locators import LocatorsMenu
from allure_commons.types import AttachmentType
import allure
from selenium import webdriver
import pyautogui
import shutil
from openpyxl import Workbook
import time
import xlsxwriter
from selenium.webdriver.common.action_chains import ActionChains

class DesignPage():
    
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

#================================================================DESIGN PAGE================================================================
    def click_hamburger(self):
        self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()

    def menu_designlab_link(self):
        menu_designlab_link=XLUtils.readData(self.path,"DesignLab",3,1)
        print(menu_designlab_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_designlab_link))
        print((self.driver.find_element(*LocatorsMenu().menu_designlab_link)).text)
        if (self.driver.find_element(*LocatorsMenu().menu_designlab_link)).text == menu_designlab_link:
            XLUtils.writeData(self.path,"DesignLab",3,2,"pass")
            XLUtils.fillGreenColor(self.path,"DesignLab",3,2)
            assert True
        else:
            XLUtils.writeData(self.path,"DesignLab",3,2,"failed")
            XLUtils.fillRedColor(self.path,"DesignLab",3,2)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(2)
        design=self.driver.find_element(*LocatorsMenu.menu_designlab_link)
        self.driver.execute_script('arguments[0].click()', design)
        time.sleep(2)

    def close_child_windows(self):
        parent_window = print(self.driver.current_window_handle, "#value of parent window")
        child_windows=self.driver.window_handles
        print(child_windows, "#value of child windows")
        for each_window in child_windows:
            self.driver.switch_to.window(each_window)
            print(self.driver.title, "#title of all windows")
            time.sleep(1)
            if self.driver.title!="Web Application Development Company - Bix Bytes Solutions":
               self.driver.close()
               time.sleep(3)

    def mouse_hover_designlab(self):
        design=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_designlab_link))
        ActionChains.move_to_element(design).perform()


