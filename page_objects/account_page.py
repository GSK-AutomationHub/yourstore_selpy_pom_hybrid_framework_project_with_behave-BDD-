from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utilities.read_config import read_configuration

class AccountPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    new_account_created_heading_xpath = "//div[@id='content']/h1"
    edit_account_info_link_link_text = "Edit your account information"

    def display_status_of_edit_account_info_link(self):
        return self.verify_element_is_displayed(
            "edit_account_info_link_link_text",self.edit_account_info_link_link_text)


    def display_status_of_new_account_created_heading(self):
        expected_heading_text = read_configuration('account page info', 'new_account_created_heading_text')
        return self.verify_element_is_displayed_and_text_contains_expected_text(
            "new_account_created_heading_xpath",
            self.new_account_created_heading_xpath,
            expected_heading_text)
