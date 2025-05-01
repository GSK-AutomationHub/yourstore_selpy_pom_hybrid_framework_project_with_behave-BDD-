from selenium.webdriver.common.by import By
from page_objects.account_page import AccountPage
from page_objects.base_page import BasePage
from utilities.read_config import read_configuration

class RegisterPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    newsletter_select_option_xpath = "(//input[@name='newsletter'])[1]"
    privacy_policy_check_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"
    first_name_field_warning_xpath = "//div[@class='text-danger' and contains(text(),'First Name')]"
    last_name_field_warning_xpath = "//div[@class='text-danger' and contains(text(),'Last Name')]"
    email_field_warning_xpath = "//div[@class='text-danger' and contains(text(),'E-Mail')]"
    telephone_field_warning_xpath = "//div[@class='text-danger' and contains(text(),'Telephone')]"
    password_field_warning_xpath = "//div[@class='text-danger' and contains(text(),'Password')]"
    privacy_policy_warning_xpath = "//div[contains(@class,'alert-dismissible')]"
    email_already_registered_warning_xpath = "//div[contains(@class,'alert-dismissible') and contains(text(),'already registered!')]"

    def enter_first_name(self,first_name):
        self.type_into_element("first_name_field_id",self.first_name_field_id,first_name)

    def enter_last_name(self,last_name):
        self.type_into_element("last_name_field_id",self.last_name_field_id,last_name)

    def enter_email(self,email):
        self.type_into_element("email_field_id",self.email_field_id,email)

    def enter_telephone(self,telephone_no):
        self.type_into_element("telephone_field_id",self.telephone_field_id,telephone_no)

    def enter_password(self,password):
        self.type_into_element("password_field_id",self.password_field_id,password)

    def confirm_password(self,password):
        self.type_into_element("confirm_password_field_id",self.confirm_password_field_id,password)

    def subscribe_newsletter(self):
        self.click_on_element("newsletter_select_option_xpath",self.newsletter_select_option_xpath)

    def accept_privacy_policy_check(self):
        self.click_on_element("privacy_policy_check_xpath",self.privacy_policy_check_xpath)

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath",self.continue_button_xpath)
        return AccountPage(self.driver)

    def check_first_name_field_warning(self):
        expected_warning_text = read_configuration('register page warnings', 'first_name_expected_warning_text')
        return self.verify_element_is_displayed_and_text_contains_expected_text(
            "first_name_field_warning_xpath",self.first_name_field_warning_xpath,expected_warning_text)

    def check_last_name_field_warning(self):
        expected_warning_text = read_configuration('register page warnings', 'last_name_expected_warning_text')
        return self.verify_element_is_displayed_and_text_contains_expected_text(
            "last_name_field_warning_xpath", self.last_name_field_warning_xpath, expected_warning_text)

    def check_email_field_warning(self):
         expected_warning_text = read_configuration('register page warnings', 'email_expected_warning_text')
         return self.verify_element_is_displayed_and_text_contains_expected_text(
             "email_field_warning_xpath", self.email_field_warning_xpath, expected_warning_text)

    def check_telephone_field_warning(self):
        expected_warning_text =  read_configuration('register page warnings', 'telephone_expected_warning_text')
        return self.verify_element_is_displayed_and_text_contains_expected_text(
            "telephone_field_warning_xpath", self.telephone_field_warning_xpath, expected_warning_text)

    def check_password_field_warning(self):
        expected_warning_text = read_configuration('register page warnings', 'password_expected_warning_text')
        return self.verify_element_is_displayed_and_text_contains_expected_text(
            "password_field_warning_xpath", self.password_field_warning_xpath, expected_warning_text)

    def check_privacy_policy_warning(self):
        expected_warning_text = read_configuration('register page warnings', 'privacy_policy_expected_warning_text')
        return self.verify_element_is_displayed_and_text_contains_expected_text(
            "privacy_policy_warning_xpath", self.privacy_policy_warning_xpath, expected_warning_text)

    def check_email_already_registered_warning(self):
        expected_warning_text = read_configuration('register page warnings', 'email_already_registered_warning_text')
        return self.verify_element_is_displayed_and_text_contains_expected_text(
            "email_already_registered_warning_xpath", self.email_already_registered_warning_xpath, expected_warning_text)

    
    def check_all_field_warnings(self):
        warning_check_result = list()
        warning_check_result.extend(
            [self.check_first_name_field_warning(),self.check_last_name_field_warning(),
            self.check_email_field_warning(),self.check_telephone_field_warning(),
            self.check_password_field_warning(),self.check_privacy_policy_warning()]
        )
        print(warning_check_result)
        return False not in warning_check_result