from pageobjects.home_page import HomePage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest
import time
from allure_commons.types import AttachmentType
import allure
from pageobjects.company_page import CompanyPage

class TestCompanyPage():

    logger=LogGen.loggen() 
    logger.info("*** starting test_002_company_page***")
    baseURL=ReadConfig.getApplicationURL()

    def test_company_page(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.cp=CompanyPage(self.driver)
        # self.cp.create_excel()
        self.cp.click_hamburger()
        self.cp.menu_companylink_assert()
        self.cp.scroll_down_Page()
        self.cp.scroll_up_Page()
        # self.cp.scroll_stop_between()

        self.cp.headline_company_page()
        self.cp.who_v_r_company_page()
        self.cp.asrt_work_culture()
        self.cp.asrt_client_meeting()
        self.cp.client_meeting_slides()
        self.cp.click_wt_v_do_company_page()
        self.cp.wt_v_do_company_page()
        self.cp.click_y_bbs_icon_company_page()
        self.cp.y_bbs_icon_company_page()
        self.cp.y_bbs_hdline_company_page()

        #Footer:
        self.cp.footer_headline()
        self.cp.footer_assert_switzerland()
        self.cp.footer_assert_br_Ind_mang()
        self.cp.footer_assert_br_canada()
        self.cp.footer_assert_br_Ind_bang()
        self.cp.footer_assert_company_name()
        self.cp.footer_mailaddress_company_page()
        self.cp.footer_end_text()
        self.cp.create_excel()

        self.cp.click_footer_insta_link()
        self.cp.click_footer_fb_link()
        self.cp.click_footer_twitter_link()
        self.cp.click_footer_linkedin_link()
        self.cp.close_child_windows()

        
        self.cp.footer_contact_num_link_cp()
        self.cp.clear_pop_up()
        self.cp.click_footer_mail_address_link()
        self.cp.close_mail_window() #after execution closing the virtual browser
        

        self.logger.info("***End of the test_002_company_page***")


        