from pageobjects.home_page import HomePage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest
import time
from allure_commons.types import AttachmentType
import allure

class TestHomePage():
    logger=LogGen.loggen() 
    logger.info("*** starting test_001_homepage***")
    baseURL=ReadConfig.getApplicationURL()

    def test_homepage(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.hp=HomePage(self.driver)
        # self.hp.create_excel()
        self.hp.homePage_headline_assert()
       
        # self.hp.click_hamburger()
        self.hp.scroll_down_Page()
        self.hp.scroll_up_Page()
        # self.hp.scroll_stop_between()

        #Project section:
        self.hp.click_proj_carousel1()
        self.hp.carousel1_text_assert()
        self.hp.click_proj_carousel2()
        self.hp.carousel2_text_assert()
        self.hp.click_proj_carousel3()
        self.hp.carousel3_text_assert()

        #Service section:
        self.hp.assert_card_design()
        self.hp.click_design_card()
        self.hp.assert_card_consultancy()
        self.hp.click_consultancy_card()

        self.hp.assert_card_sharepoint()
        self.hp.click_sharepoint_card()
        self.hp.assert_card_engineering()
        self.hp.click_engineering_card()

        self.hp.assert_card_QA()
        self.hp.click_QA_card()
        self.hp.assert_card_salesforce()
        self.hp.click_salesforce_card()
    
        self.hp.flip_service_cards()
        self.hp.text_flip_6cards()

        # Clients section:
        self.hp.click_clients_carousel1_x()
        self.hp.clients_crsl1_name_assert()
        self.hp.click_clients_carousel2_x()
        self.hp.clients_crsl2_name_assert()
        self.hp.clients_crsl2_des_assert()
        self.hp.click_clients_carousel3_x()
        self.hp.clients_crsl3_name_assert()
        self.hp.clients_crsl3_des_assert()
        self.hp.click_clients_carousel4_x()
        self.hp.clients_crsl4_name_assert()
        self.hp.clients_crsl4_des_assert()
        self.hp.click_clients_carousel5_x()
        self.hp.clients_crsl5_name_assert()
        self.hp.clients_crsl5_des_assert()
        self.hp.click_clients_carousel6_x()
        self.hp.clients_crsl6_name_assert()
        self.hp.clients_crsl6_des_assert()

        self.hp.clients_12elements()
        self.hp.clients_slides_12elements_text()
        self.hp.assert_10_companynames()
        
        # #Footer:
        self.hp.footer_headline()
        self.hp.footer_assert_switzerland()
        self.hp.footer_assert_br_Ind_mang()
        self.hp.footer_assert_br_canada()
        self.hp.footer_assert_br_Ind_bang()
        self.hp.footer_assert_company_name()
        self.hp.footer_assert_mail_address()
        self.hp.footer_end_text()
        
        self.hp.create_excel()

        self.hp.click_footer_insta_link()
        self.hp.click_footer_fb_link()
        self.hp.click_footer_twitter_link()
        self.hp.click_footer_linkedin_link()
        self.hp.close_child_windows()

        self.hp.click_footer_mail_address_link()
        self.hp.close_mail_window()
        self.hp.footer_contact_num_link()
        self.hp.clear_pop_up()
        
        self.logger.info("***End of the test_001_homepage***")

        
   
           
        
       
