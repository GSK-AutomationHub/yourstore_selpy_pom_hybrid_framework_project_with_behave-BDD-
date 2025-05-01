from page_objects.account_page import AccountPage
from page_objects.base_page import BasePage
from utilities.read_config import read_configuration


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    invalid_login_warning_message_xpath = "//div[contains(@class,'alert-dismissible')]"

    def enter_email_address(self, email):
        self.type_into_element("email_address_field_id", self.email_address_field_id, email)

    def enter_password(self, password):
        self.type_into_element("password_field_id", self.password_field_id, password)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        return AccountPage(self.driver)

    def display_status_of_invalid_login_warning_message(self):
        expected_warnings_messages_list = read_configuration(
            'login page warnings', 'expected_warning_message_list')
        return self.verify_element_is_displayed_and_text_in_expected_list(
            "invalid_login_warning_message_xpath",
            self.invalid_login_warning_message_xpath,expected_warnings_messages_list)
