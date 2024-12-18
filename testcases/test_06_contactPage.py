
from pageobjects.contact_page import ContactPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class TestContactPage():

    logger=LogGen.loggen() 
    logger.info("*** starting test_006_contact_page***")
    baseURL=ReadConfig.getApplicationURL()

    def test_contact_page(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        
        self.cnp=ContactPage(self.driver)
        
        self.cnp.click_hamburger()
        self.cnp.menu_contact_link()
        self.cnp.scroll_down_Page()
        self.cnp.scroll_up_Page()
        # self.jp.scroll_stop_between()
        self.cnp.contact_page_hdline()
        self.cnp.contpage_name_txtfield()
        self.cnp.contpage_email_txtfield()
        self.cnp.contpage_phnnum_txtfield()
        self.cnp.contpage_proj_txtfield()
        self.cnp.contpage_des_txtfield()
        # self.cnp.contpage_chbox_captcha()
        self.cnp.contpage_lets_dscs_btn()
        # self.cnp.contpage_errmsg_invalid_email()
        # self.cnp.contpage_errmsg_invalid_phone()
        # self.cnp.contpage_warmsg_name()
        # self.cnp.contpage_warmsg_email()
        # self.cnp.contpage_warmsg_phnnum()
        # self.cnp.contpage_warmsg_proj()
        # self.cnp.contpage_warmsg_description()
        # self.cnp.contpage_warmsg_captcha()

        #FOOTER:
        self.cnp.footer_headline()
        self.cnp.footer_assert_switzerland()
        self.cnp.footer_assert_br_Ind_mang()
        self.cnp.footer_assert_br_canada()
        self.cnp.footer_assert_br_Ind_bang()
        self.cnp.footer_assert_company_name()
        self.cnp.footer_mailaddress_cnp()
        self.cnp.footer_end_text()
        
        self.cnp.click_footer_insta_link()
        self.cnp.click_footer_fb_link()
        self.cnp.click_footer_twitter_link()
        self.cnp.click_footer_linkedin_link()
        self.cnp.close_child_windows()
        
        self.cnp.click_footer_mail_address_link()
        self.cnp.close_mail_window()
        self.cnp.footer_contact_num_link_cnp()
        self.cnp.clear_pop_up()

        self.cnp.create_excel()
        
        self.logger.info("***End of the test_006_contact_page***")
        
