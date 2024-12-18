from pageobjects.home_page import HomePage
from pageobjects.menu_page import MenuPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest
import time
from allure_commons.types import AttachmentType
import allure
import xlsxwriter

class TestMenu():
    logger=LogGen.loggen() 
    logger.info("*** starting test_007_menu***")
    baseURL=ReadConfig.getApplicationURL()

    def test_menu(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.mp=MenuPage(self.driver)
        self.mp.click_hamburger()
        # self.mp.close_menu()

        self.mp.menu_homelink_assert()
        self.mp.menu_companylink_assert()
        self.mp.menu_serviceslink_assert()
        self.mp.menu_blog_assert()
        self.mp.menu_jobs_assert()
        self.mp.menu_contact_assert()
        # self.mp.menu_designlab_assert()
        # self.mp.close_child_windows()

        self.mp.click_GTC()
        self.mp.click_privacy_poly()
        # self.mp.click_sitemap()

        self.mp.click_menu_insta_link()
        self.mp.click_menu_fb_link()
        self.mp.click_menu_twitter_link()
        self.mp.click_menu_linkedin_link()
        self.mp.close_child_windows_menu()
        
        self.mp.menu_lang_change_DE()
        self.mp.txt_hpg_DE_headline()
        self.mp.txt_hpg_DE_project()
        self.mp.txt_hpg_DE_services()
        self.mp.txt_hpg_DE_clients()
        self.mp.txt_hpg_DE_footer_hline()
        self.mp.click_hamburger()

        self.mp.create_excel()
        
        self.logger.info("***End of the test_007_menu***")


