from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_visibility_of_element(driver,web_element_locator):
    myWait = WebDriverWait(driver,10)
    return myWait.until(EC.visibility_of_element_located(web_element_locator))


def wait_for_presence_of_element(driver,web_element_locator):
    myWait = WebDriverWait(driver,10)
    return myWait.until(EC.presence_of_element_located(web_element_locator))


def wait_for_element_to_be_clickable(driver,web_element_locator):
    myWait = WebDriverWait(driver,15)
    return myWait.until(EC.element_to_be_clickable(web_element_locator))


def wait_for_element_to_be_invisible(driver,web_element_locator):
    myWait = WebDriverWait(driver,15)
    return myWait.until(EC.invisibility_of_element_located(web_element_locator))


def wait_for_alert(driver):
    myWait = WebDriverWait(driver,10)
    return myWait.until(EC.alert_is_present())