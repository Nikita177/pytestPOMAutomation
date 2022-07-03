from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class LoginPage:
    # Login Page
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"
    #Text_Field=(By.ID,"Email")



    def __init__(self,driver):
        self.driver=driver
        wait=WebDriverWait(driver,10)

    def performLogin(self,username,password):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
        self.driver.find_element_by_xpath(self.button_login_xpath).click()