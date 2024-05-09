from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class Test_Sauce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() #ekranı büyütür
        self.driver.get("https://www.saucedemo.com/")
       

    def empty_invalid_login(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(3)

    def empty_password_login(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        username = self.driver.find_element(By.ID,"user-name")
        username.send_keys("standard_user")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.NAME,"password")
        password.send_keys("")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(3)

    
    
    def invalid_login(self):
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
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
        sleep(3)
        
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
        testResult = appLogo.text == "Swag Labs"
        print(f"TEST SONUCU: {testResult}")
        link = self.driver.current_url
        result = self.driver.current_url == "https://www.saucedemo.com/inventory.html"
        print(f"Test Sonucu: {result}")
        products = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(len(products))
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click()
        print("Ürün sepete eklendi")
        sleep(4)
        


testClass = Test_Sauce()
testClass.empty_invalid_login()
testClass.empty_password_login()
testClass.invalid_login()
testClass.test_valid_login()

#self.driver.execute.script("window.scrollTo(0,500)")
