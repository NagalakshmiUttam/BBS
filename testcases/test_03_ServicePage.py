from pageobjects.service_page import ServicesPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time

class TestServicesPage():

    logger=LogGen.loggen() 
    logger.info("*** starting test_003_service_page***")
    baseURL=ReadConfig.getApplicationURL()

    def test_services_page(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.sp=ServicesPage(self.driver)
        # self.sp.create_excel()
        self.sp.click_hamburger()
        self.sp.menu_services_link()
        self.sp.services_headline_x()
        self.sp.scroll_down_Page()
        self.sp.scroll_up_Page()
        # self.sp.scroll_stop_between()
        self.sp.services_5menu_icons()

        self.sp.our_services()
        self.sp.click_6readmore_links()
        self.sp.assert_salesforce_name()
        self.sp.salesforce_headline_x()
        self.sp.assert_7hdlines_salesforce_crm()
        self.sp.click_5readmore_links()
        
        self.sp.assert_our_values_tab()
        self.sp.assert_3hdlines_ourvalues()
        self.sp.our_expertise_tab()
        self.sp.our_exprts_4headlines()
        self.sp.agile_framework_tab()
        self.sp.hdline_agile_framework()
        self.sp.hdlines3_agile_framework()
        self.sp.link_soft_dev_af()
        self.sp.link_proj_mgmnt_af()
        # #self.sp.link_scrum_defn_af()
        # #self.sp.close_child_windows()

        self.sp.assert_our_process_sec()
        self.sp.asrt_7process_testing()
        self.sp.lets_discuss_sec_heline()
        # self.sp.name_field_lets_sec()
        # self.sp.email_field_lets_sec()
        self.sp.btn_get_touch_lets()
        self.sp.captch_warning_msg()
        self.sp.empty_field_warning_msg()

        #Footer:
        self.sp.footer_headline()
        self.sp.footer_assert_switzerland()
        self.sp.footer_assert_br_Ind_mang()
        self.sp.footer_assert_br_canada()
        self.sp.footer_assert_br_Ind_bang()
        self.sp.footer_assert_company_name()
        self.sp.footer_mailaddress_company_page()
        self.sp.footer_end_text()

        self.sp.create_excel()

        self.sp.click_footer_insta_link()
        self.sp.click_footer_fb_link()
        self.sp.click_footer_twitter_link()
        self.sp.click_footer_linkedin_link()
        self.sp.close_child_windows()
        
        # self.sp.footer_contact_num_link_cp()
        # self.sp.clear_pop_up()
        # self.sp.click_footer_mail_address_link()
        # self.sp.close_mail_window()
        

        self.logger.info("***End of the test_003_service_page***")





