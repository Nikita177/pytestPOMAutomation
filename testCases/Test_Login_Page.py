import pytest
from selenium import webdriver


from pageObjects.LoginPage import LoginPage
from utilities.custonLogger import LogGen
from utilities.readProperties import ReadConfig

@pytest.mark.usefixtures("setup")
class Test_001_Login:
  url=ReadConfig.readConfigFile().get('common info','baseURL')
  user_n=ReadConfig.readConfigFile().get('common info','useremail')
  password=ReadConfig.readConfigFile().get('common info','password')
  logger = LogGen.loggen()

  def test_login(self):
    self.logger.info("*************** Test_001_Login *****************")
    self.driver.get(ReadConfig.readConfigFile().get('common info','baseURL'))
    self.lp=LoginPage(self.driver)
    username = ReadConfig.readConfigFile().get('common info', 'useremail')
    password = ReadConfig.readConfigFile().get('common info', 'password')
    self.lp.performLogin(username,password)
    act_title = self.driver.title
    if act_title == "Dashboard / nopCommerce administration":
      self.logger.info("****Login test passed ****")
      #self.driver.close()
      assert True
    else:
      self.logger.error("****Login test failed ****")
      self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
     # self.driver.close()
      assert False
