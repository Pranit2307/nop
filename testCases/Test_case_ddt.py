import time
import pytest
from pageObjects.loginpage import login
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
from utilities import XLUtils


class Test_ddt_0002:
    baseurl = ReadConfig.getApplicationURL()
    path = ".//Testdata/testdata.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("**********************Test_ddt_0001***********************")
        self.logger.info("***************** test_login started **********************")
        self.driver = setup
        self.driver.get(self.baseurl)

        self.lp = login(self.driver)
        self.rows = XLUtils.getRowcount(self.path, 'Sheet1')
        print("number of rows ", self.rows)

        list_status = []  # empty list

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readdata(self.path, "Sheet1", r, 1)
            self.password = XLUtils.readdata(self.path, "Sheet1", r, 2)
            self.exp = XLUtils.readdata(self.path, "Sheet1", r, 3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("**********passed**********")
                    self.lp.logout()
                    list_status.append("Pass")

                elif self.exp != "Fail":
                    self.logger.info("**********fail**********")
                    self.lp.logout()
                    list_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**********failed")
                    self.lp.logout()
                    list_status.append("Fail")

                elif self.exp != "Fail":
                    self.logger.info("**********passed")
                    self.lp.logout()
                    list_status.append("Pass")

        if "fail" not in list_status:
            self.logger.info("************ Login test pass *************")
            self.driver.close()
            assert True

        else:
            self.logger("************ login test fail ************")
            self.driver.close()

            assert False

        self.logger.info("************** end of logi l=test *************")
        self.logger.info("************ Completed tc login ddt _002 ****** ")
