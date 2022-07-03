import pytest
from selenium import webdriver
import logging
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ChromeOptions

from utilities.browserLogs import BrowserLog


@pytest.fixture(params=["chrome","firefox"],scope="class")
def setup(request):
    print("============Setup====================")
    if request.param=="chrome":
        '''capabilities = DesiredCapabilities.CHROME
        capabilities['loggingPrefs'] = {'browser': 'ALL'}
        '''
        opts = ChromeOptions()
        capabilities = webdriver.DesiredCapabilities.CHROME
        capabilities['goog:loggingPrefs'] = {'browser': 'ALL','driver': 'ALL'}
        driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=capabilities,options=opts)
    if request.param == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.implicitly_wait(10)

    request.cls.driver=driver
    yield driver
    if request.param == "chrome":
        print("=============Error console=============")
      #  print('browser = ', driver.get_log('browser'))
      #  print('driver = ', driver.get_log('driver'))
        consolemsgs = BrowserLog.get_browser_log_entries(request.cls.driver)
       # print(' consolemsgs = ',consolemsgs)

        print("=============Tear=================")
        request.cls.driver.close()

    if request.param == "firefox":
        request.cls.driver.close()

'''
#cmd pytest -v -s --browser chrome
def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")
    '''

