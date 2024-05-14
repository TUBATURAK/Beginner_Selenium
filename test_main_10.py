from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class Test_Sau:
    def setup_method(self):
        #her test başlangıcında çalışacak fonksiyon
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() 
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        #her test bitiminde çalışacak fonksiyon
        self.driver.quit()

       
    pytest
    def test_empty_login(self):
        sleep(5)
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert  errorMessage.text == "Epic sadface: Username is required"
       
        
   
    def test_empty_password_login(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Password is required"
        

    
    
    def test_locked_login(self):
        self.driver.refresh()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("locked_out_user")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("secret_sauce")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
       
    def test_valid_login(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        #action chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(username,"standard_user")
        actions.send_keys_to_element(password,"secret_sauce")
        actions.move_to_element(loginButton) #elementin olduğu yere sayfayı taşı anlamına geliyor
        actions.perform() #depolanmış aksiyonlarımızı çalıştırır
        loginButton.click()
        appLogo = self.driver.find_element(By.CLASS_NAME,"app_logo")
        assert appLogo.text == "Swag Labs"
        link = self.driver.current_url
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        products = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert (len(products)) == 6
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
      

# testClass = Test_Sau()
# testClass.Test_empty_login()
# testClass.Test_empty_password_login()
# testClass.Test_locked_login()
# testClass.Test_valid_login()


