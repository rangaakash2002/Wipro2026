import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driverfactory import get_driver


@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_google(browser):
    driver = get_driver(browser)
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.google.com")

    wait.until(EC.title_contains("Google"))
    assert "Google" in driver.title

    driver.quit()


@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_google_search(browser):
    driver = get_driver(browser)
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.google.com")

    # Handle consent popup (Grid-safe)
    try:
        agree = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[.//text()[contains(.,'Accept')]]")
            )
        )
        agree.click()
    except:
        pass

    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    search_box.send_keys("selenium grid")
    search_box.submit()

    wait.until(EC.title_contains("selenium"))
    assert "selenium" in driver.title.lower()

    driver.quit()
