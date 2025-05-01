from page_objects.base_page import BasePage
from page_objects.login_page import LoginPage
from page_objects.register_page import RegisterPage
from page_objects.search_page import SearchPage


class HomePage(BasePage):

    def __init__(self,driver):
       super().__init__(driver)


    search_box_field_name = "search"
    my_account_menu_xpath = "//a[@title='My Account']"
    login_link_link_text = "Login"
    register_link_link_text = "Register"
    search_button_xpath = "//span[@class='input-group-btn']/button"


    def check_home_page_title(self,expected_title):
        return self.verify_page_title(expected_title)

    def click_on_my_account_menu(self):
        self.perform_click_action_on_element("my_account_menu_xpath", self.my_account_menu_xpath)

    def click_on_login_link(self):
        self.perform_click_action_on_element("login_link_link_text", self.login_link_link_text)
        return LoginPage(self.driver)

    def click_on_register_link(self):
        self.perform_click_action_on_element("register_link_link_text", self.register_link_link_text)
        return RegisterPage(self.driver)

    def enter_product_into_search_box_field(self, product_name):
        self.type_into_element("search_box_field_name", self.search_box_field_name, product_name)

    def click_on_search_button(self):
        self.click_on_element("search_button_xpath",self.search_button_xpath)
        return SearchPage(self.driver)
