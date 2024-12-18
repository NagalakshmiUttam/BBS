
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
from pageobjects.locators import LocatorsBlog
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

class BlogPage():
    
    path=r"test_data\BBS6.xlsx"

    def __init__(self,driver):
        self.driver=driver

    def create_excel(self):
        # workbook=xlsxwriter.Workbook(r"C:\Nagalakshmi\PythonPractice\BBS_automation\test_data\BBS.xlsx")
        # worksheet = workbook.add_worksheet("Blog")
        # worksheet.write(0, 0, "TEXT FOR ASSERTION")
        # worksheet.write(0, 1, "RESULTS")
        # worksheet.write(2, 0, "BLOG")
        # worksheet.write(3, 0, "FEATURED ARTICLE")
        # worksheet.write(4, 0, "Recent Article")
        # worksheet.write(5, 0, "All Articles")
        # worksheet.write(7, 0, "FOOTER:")
        # worksheet.write(8, 0, "GET IN TOUCH")
        # worksheet.write(9, 0, "SWITZERLAND")
        # worksheet.write(10, 0, "INDIA - Mangalore")
        # worksheet.write(11, 0, "CANADA")
        # worksheet.write(12, 0, "INDIA - Bangalore")
        # worksheet.write(13, 0, "Bix Bytes Solutions Pvt. Ltd.")
        # worksheet.write(14, 0, "info@bixbytessolutions.com")
        # worksheet.write(15, 0, "Copyright © 2022 BixBytes Solutions")

        # workbook.close()
        wb = Workbook()
        file_path = "test_data"
        create_duplicate = 'BixBytes website' + str(datetime.datetime.now().strftime('%d-%m-%Y %H-%M-%S')) + '.xlsx'
        replica = os.path.join(file_path, create_duplicate)
        wb.save(replica)
        source = "test_data\BBS6.xlsx"
        dest = replica
        shutil.copy(source, dest)

#================================================================BLOG PAGE================================================================
    def click_hamburger(self):
        self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()

    def menu_blog_link(self):
        menu_blog_link=XLUtils.readData(self.path,"Blog",3,2)
        print(menu_blog_link)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsMenu.menu_blog_link))
        print((self.driver.find_element(*LocatorsMenu().menu_blog_link)).text)
        if (self.driver.find_element(*LocatorsMenu.menu_blog_link)).text == menu_blog_link:
            XLUtils.writeData(self.path,"Blog",3,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",3,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",3,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",3,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
        time.sleep(2)
        blog=self.driver.find_element(*LocatorsMenu.menu_blog_link)
        self.driver.execute_script('arguments[0].click()', blog)
        time.sleep(2)
        hamburger=self.driver.find_element(*LocatorsBlog.hamburger_blog_page_x)
        self.driver.execute_script('arguments[0].click()', hamburger)
        time.sleep(2)
        self.driver.refresh()

    def scroll_down_Page(self):
        # self.driver.refresh()
        txt= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.txt_featured_article))
        txt.click()
        for i in range(0,9):
            if i<9:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
                 time.sleep(1)

    def scroll_up_Page(self):
        for i in range(0,9):
            if i<9:
                 ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
                 time.sleep(1)

    def scroll_stop_between(self):
        txt= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.txt_featured_article))
        txt.click()
        for i in range(0,3):
            if i<5:
                 ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
                 time.sleep(1)
#================================================================FEATURED ARTICLE================================================================#

    def txt_featured_article(self):
        txt_featured_article=XLUtils.readData(self.path,"Blog",4,2)
        print(txt_featured_article)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsBlog.txt_featured_article))
        print((self.driver.find_element(*LocatorsBlog().txt_featured_article)).text)
        if (self.driver.find_element(*LocatorsBlog.txt_featured_article)).text == txt_featured_article:
            XLUtils.writeData(self.path,"Blog",4,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",4,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",4,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",4,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    # def share_icon_featured_art(self):
    #     WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.txt_featured_article)).click()
    #     ActionChains(self.driver).send_keys(Keys.SPACE).perform()
    #     WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_featured_art))
    #     time.sleep(3)
    #     twitter=self.driver.find_element(By.XPATH, "//div[@class='right_project_card']//li[@class='twitter_btn btn_outer']//button[@type='button']//*[name()='svg']")
    #     ActionChains(self.driver).move_to_element(twitter).click().perform()
    #     time.sleep(2)
    #     print(self.driver.current_window_handle, "#value of parent window")
    #     child_windows=self.driver.window_handles
    #     for each_window in child_windows:
    #         self.driver.switch_to.window(each_window)
    #         print(self.driver.title, "#title of all windows")
    #         time.sleep(1)
    #         if self.driver.title!="Blog posts of Bix Bytes Solutions":
    #            self.driver.close()
    #     self.driver.switch_to.window(self.driver.window_handles[0])    
       
    def close_child_windows_fea_artcl(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.txt_featured_article)).click()
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_featured_art))
        time.sleep(3)
        links_3=self.driver.find_elements(By.XPATH, "//div[@class='right_project_card']//li[@class]")
        for each_link in range(len(links_3)):
            links_3=self.driver.find_elements(By.XPATH, "//div[@class='right_project_card']//li[@class]")
            links_3[each_link].click()
            # self.driver.execute_script("arguments[0].click();", links_3[each_link])
            time.sleep(2)
            print(self.driver.current_window_handle, "#value of parent window")
            child_windows=self.driver.window_handles
            print(child_windows, "#value of child windows")
            for each_window in child_windows:
                self.driver.switch_to.window(each_window)
                print(self.driver.title, "#title of all windows")
                time.sleep(1)
                if self.driver.title!="Blog posts of Bix Bytes Solutions":
                    self.driver.close()
                    time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[0])

        
    def click_readmore_fea_artcl(self):
        read_more_fea_artcle=self.driver.find_element(*LocatorsBlog.read_more_fea_artcle)
        self.driver.execute_script('arguments[0].click()', read_more_fea_artcle)
        time.sleep(2)

    def scroll_down_Page1(self):
        fea_artcle_detailpage_hdline=self.driver.find_element(By.XPATH,"//h1[contains(text(),'Top Technological Trends Transforming Various Indu')]")
        fea_artcle_detailpage_hdline.click()
        for i in range(0,9):
            if i<9:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
                 time.sleep(1)

    def scroll_up_Page1(self):
        for i in range(0,9):
            if i<9:
                 ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
                 time.sleep(1)

    
    # def social_web_linkedin_detpage(self):
        # self.driver.execute_script("window.scrollTo(0, window.scrollY + 1500)")
        # self.driver.find_element(By.XPATH,"//h1[contains(text(),'Top Technological Trends Transforming Various Indu')]").click()
        # for i in range(0,7):
        #     if i<7:
        #          ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        #          time.sleep(1)
        # social_web_linkedin_detpage= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.social_web_linkedin_detpage))
        # social_web_linkedin_detpage.click()
        # print(self.driver.current_window_handle, "#value of parent window")
        # child_windows=self.driver.window_handles
        # print(child_windows, "#value of child windows")
        # for each_window in child_windows:
        #     self.driver.switch_to.window(each_window)
        #     print(self.driver.title, "#title of all windows")
        #     time.sleep(2)
        #     if self.driver.title!="Blog | Top Technological Trends Transforming Various Industries":
        #        self.driver.close()
        #        time.sleep(3)
        # self.driver.switch_to.window(self.driver.window_handles[0])

    def close_child_windows_fea_artcl_detpage(self):
        self.driver.find_element(By.XPATH,"//h1[contains(text(),'Top Technological Trends Transforming Various Indu')]").click()
        for i in range(0,7):
            if i<7:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
                 time.sleep(1)
        links_3=self.driver.find_elements(By.XPATH, "//li[@class]//button[@type='button']//*[name()='svg']")
        for each_link in range(len(links_3)):
            links_3=self.driver.find_elements(By.XPATH, "//li[@class]//button[@type='button']//*[name()='svg']")
            links_3[each_link].click()
            # self.driver.execute_script("arguments[0].click();", links_3[each_link])
            time.sleep(2)
            print(self.driver.current_window_handle, "#value of parent window")
            child_windows=self.driver.window_handles
            print(child_windows, "#value of child windows")
            for each_window in child_windows:
                self.driver.switch_to.window(each_window)
                print(self.driver.title, "#title of all windows")
                time.sleep(1)
                if self.driver.title!="Blog | Top Technological Trends Transforming Various Industries":
                    self.driver.close()
                    time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[0])

    def click_backto_blog(self):
        backto_blog=self.driver.find_element(*LocatorsBlog.back_to_blog)
        self.driver.execute_script('arguments[0].click()', backto_blog)
        time.sleep(2)
        # self.driver.back()
        # time.sleep(2)
        # self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()
        # time.sleep(2)
        # menu_close_btn= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_close_btn))
        # self.driver.execute_script("arguments[0].click();",menu_close_btn)
        # time.sleep(2)
#================================================================RECENT ARTICLE================================================================
    
    def txt_recent_article(self):
        txt_recent_article=XLUtils.readData(self.path,"Blog",5,2)
        print(txt_recent_article)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsBlog.txt_recent_article))
        print((self.driver.find_element(*LocatorsBlog().txt_recent_article)).text)
        if (self.driver.find_element(*LocatorsBlog.txt_recent_article)).text == txt_recent_article:
            XLUtils.writeData(self.path,"Blog",5,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",5,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",5,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",5,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def close_child_windows_rcnt_artcl(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.txt_featured_article)).click()
        for i in range(0,2):
            if i<2:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_recent_art1))
        time.sleep(3)
        links_3=self.driver.find_elements(By.XPATH, "//div[@class='col-xl order-xl-0']//li[@class]//button[@type='button']")
        for each_link in range(len(links_3)):
            links_3=self.driver.find_elements(By.XPATH, "//div[@class='col-xl order-xl-0']//li[@class]//button[@type='button']")
            links_3[each_link].click()
            # self.driver.execute_script("arguments[0].click();", links_3[each_link])
            time.sleep(2)
            print(self.driver.current_window_handle, "#value of parent window")
            child_windows=self.driver.window_handles
            print(child_windows, "#value of child windows")
            for each_window in child_windows:
                self.driver.switch_to.window(each_window)
                print(self.driver.title, "#title of all windows")
                time.sleep(1)
                if self.driver.title!="Blog posts of Bix Bytes Solutions":
                    self.driver.close()
                    time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[0])

    # def fb_recent_art1(self):
    #     WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.txt_featured_article)).click()
    #     for i in range(0,2):
    #         if i<2:
    #              ActionChains(self.driver).send_keys(Keys.SPACE).perform()
    #     shareicon=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_recent_art1))
    #     time.sleep(3)
    #     ActionChains(self.driver).move_to_element(shareicon).perform()
    #     time.sleep(3)
    #     fb=self.driver.find_element(By.XPATH, "//div[@class='col-xl order-xl-0']//li[@class='facebook_btn btn_outer']//button[@type='button']//*[name()='svg']")
    #     fb.click()
    #     parent_window = print(self.driver.current_window_handle, "#value of parent window")
    #     child_windows=self.driver.window_handles
    #     print(child_windows, "#value of child windows")
    #     for each_window in child_windows:
    #         self.driver.switch_to.window(each_window)
    #         print(self.driver.title, "#title of all windows")
    #         time.sleep(2)
    #         if self.driver.title!="Blog posts of Bix Bytes Solutions":
    #            self.driver.switch_to.window(each_window)
    #            self.driver.close()
    #            break

    def click_readmore_rcnt_art1(self):
        readmore_rcnt_art1=self.driver.find_element(*LocatorsBlog.readmore_rcnt_art1)
        self.driver.execute_script('arguments[0].click()', readmore_rcnt_art1)
        time.sleep(2)

    def scroll_down_Page_ra1(self):
        click_on_top=self.driver.find_element(By.XPATH,"//div[@class='card_img']//div[1]")
        click_on_top.click()
        for i in range(0,9):
            if i<9:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
                 time.sleep(1)

    def scroll_up_Page_ra1(self):
        for i in range(0,9):
            if i<9:
                 ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
                 time.sleep(1)

    def click_backto_blog_ra1(self):
        backto_blog=self.driver.find_element(*LocatorsBlog.back_to_blog)
        self.driver.execute_script('arguments[0].click()', backto_blog)
        # time.sleep(2)
        # self.driver.back()
        # time.sleep(2)
        # self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()
        # time.sleep(2)
        # menu_close_btn= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_close_btn))
        # self.driver.execute_script("arguments[0].click();",menu_close_btn)
        # time.sleep(2)
        # self.driver.back()

#Recent article 2:

    def share_icon_recent_art2(self):
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.txt_featured_article)).click()
        txt_featured_article=self.driver.find_element(*LocatorsBlog.txt_featured_article)
        self.driver.execute_script('arguments[0].click()', txt_featured_article)
        for i in range(0,5):
            if i<5:
                 ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()  
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_recent_art2))
        time.sleep(2)
        # ActionChains(self.driver).move_to_element(shareicon).perform()
        links_3=self.driver.find_elements(By.XPATH, "//div[@class='col-xl order-xl-0 order-xl-2']//li[@class]//button[@type='button']")
        for each_link in range(len(links_3)):
            links_3=self.driver.find_elements(By.XPATH, "//div[@class='col-xl order-xl-0 order-xl-2']//li[@class]//button[@type='button']")
            # links_3[each_link].click()
            self.driver.execute_script("arguments[0].click();", links_3[each_link])
            time.sleep(2)
            print(self.driver.current_window_handle, "#value of parent window")
            child_windows=self.driver.window_handles
            print(child_windows, "#value of child windows")
            for each_window in child_windows:
                self.driver.switch_to.window(each_window)
                print(self.driver.title, "#title of all windows")
                time.sleep(1)
                if self.driver.title!="Blog posts of Bix Bytes Solutions":
                    self.driver.close()
                    time.sleep(3)
            self.driver.switch_to.window(self.driver.window_handles[0])

    def click_readmore_rcnt_art2(self):
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.txt_featured_article)).click()
        txt_featured_article=self.driver.find_element(*LocatorsBlog.txt_featured_article)
        self.driver.execute_script('arguments[0].click()', txt_featured_article)
        for i in range(0,5):
            if i<5:
                 ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()
        readmore_rcnt_art2=self.driver.find_element(*LocatorsBlog.readmore_rcnt_art2)
        self.driver.execute_script('arguments[0].click()', readmore_rcnt_art2)
        time.sleep(2)

    def scroll_down_Page_ra2(self):
        click_on_top=self.driver.find_element(By.XPATH,"//div[@class='card_img']//div[1]")
        click_on_top.click()
        for i in range(0,9):
            if i<9:
                 ActionChains(self.driver).send_keys(Keys.SPACE).perform()
                 time.sleep(1)

    def scroll_up_Page_ra2(self):
        for i in range(0,9):
            if i<9:
                 ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
                 time.sleep(1)

    def click_backto_blog_ra2(self):
        backto_blog=self.driver.find_element(*LocatorsBlog.back_to_blog)
        self.driver.execute_script('arguments[0].click()', backto_blog)
        time.sleep(2)
        # self.driver.back()
        # time.sleep(2)
        # self.driver.find_element(*LocatorsHomePage.btn_Hamburger_hmpg_x).click()
        # time.sleep(2)
        # menu_close_btn= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsMenu.menu_close_btn))
        # self.driver.execute_script("arguments[0].click();",menu_close_btn)
        # time.sleep(2)
        # self.driver.back()
   
#================================================================All Articles================================================================#

    def txt_all_articles(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.txt_featured_article)).click()
        for i in range(0,3):
            if i<3:
                ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        txt_all_articles=XLUtils.readData(self.path,"Blog",6,2)
        print(txt_all_articles)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsBlog.txt_all_articles))
        print((self.driver.find_element(*LocatorsBlog().txt_all_articles)).text)
        if (self.driver.find_element(*LocatorsBlog.txt_all_articles)).text == txt_all_articles:
            XLUtils.writeData(self.path,"Blog",6,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",6,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",6,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",6,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def click_frw_bal_arrows(self):
        # frw_arrow=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.frw_arrow_all_artcl))
        # frw_arrow.click()
        frw_arrow=self.driver.find_element(*LocatorsBlog.frw_arrow_all_artcl)
        self.driver.execute_script('arguments[0].click()', frw_arrow)
        time.sleep(4)
        # back_arrow=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.back_arrow_all_artcl))
        # back_arrow.click()
        back_arrow=self.driver.find_element(*LocatorsBlog.back_arrow_all_artcl)
        self.driver.execute_script('arguments[0].click()', back_arrow)
        time.sleep(2)

   
    def mouse_hoever_card1(self):
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsBlog.txt_all_articles)).click()
        hdline=self.driver.find_element(*LocatorsBlog.txt_all_articles)
        self.driver.execute_script('arguments[0].click()', hdline)
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        time.sleep(1)
        card1=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_aa1))
        ActionChains(self.driver).move_to_element(card1).perform()
        time.sleep(2)
        card2=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_aa2))
        ActionChains(self.driver).move_to_element(card2).perform()
        time.sleep(2)
        card3=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_aa3))
        ActionChains(self.driver).move_to_element(card3).perform()
        time.sleep(2)
        clicking=self.driver.find_element(By.XPATH, "//span[contains(text(),'Microsoft 365: Prices to rise by up to 25 percent ')]").click()
        self.driver.execute_script('arguments[0].click()', clicking)
        # for i in range(0,2):
        #     if i<2:  
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        time.sleep(2)
        card4=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_aa4))
        ActionChains(self.driver).move_to_element(card4).perform()
        time.sleep(2)
        card5=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_aa5))
        ActionChains(self.driver).move_to_element(card5).perform()
        time.sleep(2)
        card6=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.share_icon_aa6))
        ActionChains(self.driver).move_to_element(card6).perform()
        time.sleep(2)

    def all_art_6read_more(self):
        ActionChains(self.driver).send_keys(Keys.PAGE_UP).perform()
        six_readmore=WebDriverWait(self.driver,20).until(EC.presence_of_all_elements_located(LocatorsBlog.all_art_6read_more))
        for each_link in range(len(six_readmore)):
            #Added this line to avoid stale which re-assigned the element again.
            six_readmore=self.driver.find_elements(By.XPATH, "//a[@class='read_more font-weight-4000 fontSize-2_0 cursor-pointer text-uppercase'] [text()=' READ MORE ']")
            # six_readmore[each_link].click()
            self.driver.execute_script("arguments[0].click();", six_readmore[each_link])
            time.sleep(2)
            self.driver.back()
            time.sleep(2)
            for i in range(0,5):
                if i<5:
                    ActionChains(self.driver).send_keys(Keys.SPACE).perform()

    def search_bar_all_artcl(self):
        searchbar=WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsBlog.search_bar_all_artcl))
        searchbar.send_keys("The question employer faces: How can I guarantee work safety at the workplace?")
        searchbar.send_keys(Keys.ENTER)
        time.sleep(5)
        searchbar.clear()
        hdline=self.driver.find_element(*LocatorsBlog.txt_all_articles)
        self.driver.execute_script('arguments[0].click()', hdline)
        for i in range(0,2):
            if i<2:  
                ActionChains(self.driver).send_keys(Keys.SPACE).perform()

#================================================================FOOTER================================================================#

    def footer_headline(self):
        footer_headline=XLUtils.readData(self.path,"Blog",9,2)
        print(footer_headline)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_headline))
        print((self.driver.find_element(*LocatorsHomePage().footer_headline)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_headline)).text == footer_headline:
            XLUtils.writeData(self.path,"Blog",9,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",9,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",9,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",9,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_switzerland(self):
        footer_assert_switzerland=XLUtils.readData(self.path,"Blog",10,2)
        print(footer_assert_switzerland)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_switzerland))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_switzerland)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_switzerland)).text == footer_assert_switzerland:
            XLUtils.writeData(self.path,"Blog",10,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",10,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",10,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",10,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_Ind_mang(self):
        footer_assert_br_Ind_mang=XLUtils.readData(self.path,"Blog",11,2)
        print(footer_assert_br_Ind_mang)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_Ind_mang))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_Ind_mang)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_Ind_mang)).text == footer_assert_br_Ind_mang:
            XLUtils.writeData(self.path,"Blog",11,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",11,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",11,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",11,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_canada(self):
        footer_assert_br_canada=XLUtils.readData(self.path,"Blog",12,2)
        print(footer_assert_br_canada)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_canada))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_canada)).text)
        if (self.driver.find_element(*LocatorsHomePage().footer_assert_br_canada)).text == footer_assert_br_canada:
            XLUtils.writeData(self.path,"Blog",12,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",12,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",12,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",12,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_br_Ind_bang(self):
        footer_assert_br_Ind_bang=XLUtils.readData(self.path,"Blog",13,2)
        print(footer_assert_br_Ind_bang)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_br_Ind_bang))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_br_Ind_bang)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_br_Ind_bang)).text == footer_assert_br_Ind_bang:
            XLUtils.writeData(self.path,"Blog",13,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",13,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",13,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",13,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False

    def footer_assert_company_name(self):
        footer_assert_company_name=XLUtils.readData(self.path,"Blog",14,2)
        print(footer_assert_company_name)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_assert_company_name))
        print((self.driver.find_element(*LocatorsHomePage().footer_assert_company_name)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_assert_company_name)).text == footer_assert_company_name:
            XLUtils.writeData(self.path,"Blog",14,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",14,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",14,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",14,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
            time.sleep(2)

    def footer_mailaddress_company_page(self):
        footer_mailaddress_company_page=XLUtils.readData(self.path,"Blog",15,2)
        print(footer_mailaddress_company_page)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(LocatorsCompany.footer_mailaddress_company_page))
        print((self.driver.find_element(*LocatorsCompany().footer_mailaddress_company_page)).text)
        if (self.driver.find_element(*LocatorsCompany.footer_mailaddress_company_page)).text == footer_mailaddress_company_page:
            XLUtils.writeData(self.path,"Blog",15,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",15,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",15,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",15,3)
            self.driver.save_screenshot(r"C:\\Nagalakshmi\\PythonPractice\\BBS_automation\\screenshots\\failed_tc.png")
            allure.attach(self.driver.get_screenshot_as_png(), name="dashboard_tc_fail", attachment_type=AttachmentType.PNG)
            assert False
            time.sleep(2)

    def footer_end_text(self):
        footer_end_text=XLUtils.readData(self.path,"Blog",16,2)
        print(footer_end_text)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LocatorsHomePage.footer_end_text))
        print((self.driver.find_element(*LocatorsHomePage().footer_end_text)).text)
        if (self.driver.find_element(*LocatorsHomePage.footer_end_text)).text == footer_end_text:
            XLUtils.writeData(self.path,"Blog",16,3,"pass")
            XLUtils.fillGreenColor(self.path,"Blog",16,3)
            assert True
        else:
            XLUtils.writeData(self.path,"Blog",16,3,"failed")
            XLUtils.fillRedColor(self.path,"Blog",16,3)
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
            if self.driver.title!="Blog posts of Bix Bytes Solutions":
               self.driver.close()
               time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[0])
        
    def footer_contact_num_link_cp(self):
        footer_contact_num_link_cp= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsCompany.footer_contact_num_link_cp))
        self.driver.execute_script("arguments[0].click();",footer_contact_num_link_cp)
        time.sleep(2)

    def clear_pop_up(self):
        pyautogui.press('Esc')
        time.sleep(2) 

    def click_footer_mail_address_link(self):
        footer_mailaddress_company_page= WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LocatorsCompany.footer_mailaddress_company_page))
        self.driver.execute_script("arguments[0].click();",footer_mailaddress_company_page)
        time.sleep(4)

    def close_mail_window(self):
        pyautogui.hotkey('alt','F4')
        time.sleep(2)
        pyautogui.hotkey('PAGE_DOWN','ENTER')

   
       

