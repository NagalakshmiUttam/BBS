
from pageobjects.jobs_page import JobsPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class TestJobsPage():

    logger=LogGen.loggen() 
    logger.info("*** starting test_005_jobs_page***")
    baseURL=ReadConfig.getApplicationURL()

    def test_jobs_page(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.jp=JobsPage(self.driver)
        
        self.jp.click_hamburger()
        self.jp.menu_jobs_link()
        self.jp.scroll_down_Page()
        self.jp.scroll_up_Page()
        # self.jp.scroll_stop_between()
        # self.jp.jobs_12read_more()
        self.jp.txt_all_job_openings()
        # self.jp.all_openings_12job_cards()

        self.jp.jobs_read_more_12th()
        self.jp.asrt_job_detpag_hdline()
        self.jp.asrt_job_detpag_txt1()
        self.jp.asrt_job_detpag_txt2()
        self.jp.asrt_job_detpag_txt3()
        self.jp.asrt_job_detpag_txt4()

        self.jp.jop_application_heading()
        self.jp.job_aplcn_first_name()
        self.jp.job_aplcn_last_name()
        self.jp.job_aplcn_email()
        self.jp.job_aplcn_phone()
        self.jp.upload_resume()
        # #self.jp.job_aplcn_portfolio()
        # #self.jp.click_ch_box()
        # self.jp.job_aplcn_submit_btn()

        # self.jp.warning_msg1_aplcn_form()
        # self.jp.warning_msg_last_name()
        # self.jp.warning_msg_phnum()
        # self.jp.warning_msg_uploadfile()
        # self.jp.warning_msg_captcha()
        # self.jp.jop_aplcn_footer_txt()

        # self.jp.error_msg_invalid_mailid()
        # self.jp.error_msg_invalid_phn_num()

        #FOOTER:
        self.jp.footer_headline()
        self.jp.footer_assert_switzerland()
        self.jp.footer_assert_br_Ind_mang()
        self.jp.footer_assert_br_canada()
        self.jp.footer_assert_br_Ind_bang()
        self.jp.footer_assert_company_name()
        self.jp.footer_mailaddress_company_page()
        self.jp.footer_end_text()
        # self.jp.merge_cells()
       
        self.jp.click_footer_insta_link()
        self.jp.click_footer_fb_link()
        self.jp.click_footer_twitter_link()
        self.jp.click_footer_linkedin_link()
        self.jp.close_child_windows()
        self.jp.footer_contact_num_link_cp()
        self.jp.clear_pop_up()
        self.jp.click_footer_mail_address_link()
        self.jp.close_mail_window()
        
        self.logger.info("***End of the test_005_jobs_page***")
        
