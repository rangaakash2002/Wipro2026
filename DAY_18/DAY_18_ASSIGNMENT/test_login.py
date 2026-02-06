from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from DAY_18.DAY_18_ASSIGNMENT.Login_page import loginpage
def test_login():

    driver = webdriver.Firefox()

    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
# time.sleep(5)
    loginobj = loginpage(driver)

    loginobj.enterusername("Admin")
    loginobj.enterpassword("admin123")

    loginobj.clicklogin()




