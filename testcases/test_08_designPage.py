from pageobjects.designlab_page import DesignPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class TestDesignPage():

    logger=LogGen.loggen() 
    logger.info("*** starting test_008_design_page***")
    baseURL=ReadConfig.getApplicationURL()

    def test_design_page(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        
        self.dp=DesignPage(self.driver)
        self.dp.click_hamburger()
        self.dp.menu_designlab_link()
        self.dp.create_excel()
        self.dp.close_child_windows()
        # self.dp.mouse_hover_designlab()

