
from pageobjects.blog_page import BlogPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import time

class TestBlogPage():

    logger=LogGen.loggen() 
    logger.info("*** starting test_004_blog_page***")
    baseURL=ReadConfig.getApplicationURL()

    def test_blog_page(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.bp=BlogPage(self.driver)
        # self.bp.create_excel()
        self.bp.click_hamburger()
        self.bp.menu_blog_link()
        self.bp.scroll_down_Page()
        self.bp.scroll_up_Page()
        # self.bp.scroll_stop_between()

        #Featured Article:
        self.bp.txt_featured_article()
        self.bp.close_child_windows_fea_artcl()
        self.bp.click_readmore_fea_artcl()
        self.bp.scroll_down_Page1()
        self.bp.scroll_up_Page1()
        self.bp.close_child_windows_fea_artcl_detpage()
        self.bp.click_backto_blog()

        #Recent Article:
        self.bp.txt_recent_article()
        self.bp.close_child_windows_rcnt_artcl()
        self.bp.click_readmore_rcnt_art1()
        self.bp.scroll_down_Page_ra1()
        self.bp.scroll_up_Page_ra1()
        self.bp.click_backto_blog_ra1()

        self.bp.share_icon_recent_art2()
        self.bp.click_readmore_rcnt_art2()
        self.bp.scroll_down_Page_ra2()
        self.bp.scroll_up_Page_ra2()
        self.bp.click_backto_blog_ra2()

        #All Article:
        self.bp.txt_all_articles()
        self.bp.click_frw_bal_arrows()
        # # self.bp.mouse_hoever_card1()
        self.bp.all_art_6read_more()
        self.bp.search_bar_all_artcl()

        #Footer:
        self.bp.footer_headline()
        self.bp.footer_assert_switzerland()
        self.bp.footer_assert_br_Ind_mang()
        self.bp.footer_assert_br_canada()
        self.bp.footer_assert_br_Ind_bang()
        self.bp.footer_assert_company_name()
        self.bp.footer_mailaddress_company_page()
        self.bp.footer_end_text()

        self.bp.create_excel()

        self.bp.click_footer_insta_link()
        self.bp.click_footer_fb_link()
        self.bp.click_footer_twitter_link()
        self.bp.click_footer_linkedin_link()
        self.bp.close_child_windows()

        self.bp.footer_contact_num_link_cp()
        self.bp.clear_pop_up()
        self.bp.click_footer_mail_address_link()
        self.bp.close_mail_window()
        
        self.logger.info("***End of the test_004_blog_page***")
        



