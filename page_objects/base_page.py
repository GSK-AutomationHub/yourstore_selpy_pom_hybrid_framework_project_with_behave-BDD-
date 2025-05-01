from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.action = ActionChains(self.driver)


    def get_element(self,locator_type,locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID,locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_class"):
            element = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_tag"):
            element = self.driver.find_elements(By.TAG_NAME, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element


    def verify_page_title(self,expected_page_title):
        return self.driver.title.__eq__(expected_page_title)


    def click_on_element(self,locator_type,locator_value):
        element = self.get_element(locator_type,locator_value)
        element.click()


    def perform_click_action_on_element(self,locator_type,locator_value):
        element = self.get_element(locator_type,locator_value)
        self.action.click(element).perform()


    def type_into_element(self, locator_type, locator_value,content):
        element = self.get_element(locator_type, locator_value)
        element.clear()
        element.send_keys(content)

    def verify_element_is_displayed(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.is_displayed()


    def verify_element_text_contains_expected_text(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__contains__(expected_text)


    def verify_element_text_equals_expected_text(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(expected_text)


    def verify_element_is_displayed_and_text_contains_expected_text(self,locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.is_displayed() and element.text.__contains__(expected_text)


    def verify_element_is_displayed_and_text_equals_expected_text(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.is_displayed() and element.text.__eq__(expected_text)

    def verify_element_is_displayed_and_text_in_expected_list(self, locator_type, locator_value, expected_list):
        element = self.get_element(locator_type, locator_value)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.is_displayed() and element.text in expected_list