from page_objects.base_page import BasePage

class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    valid_product_search_result_link_text = "HP LP3065"
    invalid_product_search_warning_message_xpath = "//input[@id='button-search']/following-sibling::p"


    def display_status_of_searched_product(self):
        return self.verify_element_is_displayed(
            "valid_product_search_result_link_text",self.valid_product_search_result_link_text)


    def display_status_of_warning_message(self,expected_message):
        return self.verify_element_is_displayed_and_text_equals_expected_text(
            "invalid_product_search_warning_message_xpath",
            self.invalid_product_search_warning_message_xpath,
            expected_message)

