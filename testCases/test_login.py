import pytest

from pageObjects.loginpage import login
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen


class Test_0001:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    # @pytest.Mark.sanity
    # @pytest.mark.smoke
    @pytest.mark.regression
    def test_homepage(self, setup):
        self.logger.info("*****************Test_001_Login***************")
        self.logger.info("******************* 'verifying Home Page ***************")

        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("***************** test passed **********************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_001.png")
            self.driver.close()
            self.logger.error("***************** test_001 fail  **********************")

            assert False

    # @pytest.Mark.smoke
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***************** test_login started **********************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.login()
        act_title = self.driver.title
        # self.driver.close()

        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            self.logger.info("***************** test_login passed **********************")
            assert True
        else:
            self.driver.save_screenshot(".//Screenshot//" + "test_login.png")
            self.driver.close()
            self.logger.error("***************** test_login fail **********************")
            assert False
