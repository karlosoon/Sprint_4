from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.main_page_locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def cookie_button_click(self):
        self.driver.find_element(*MainPageLocators.COOKIE_ACCEPT_BUTTON).click()

    def click_on_header_order_button(self):
        self.driver.find_element(*MainPageLocators.HEADER_ORDER_BUTTON).click()

    def click_on_order_button(self):
        order_button = self.driver.find_element(*MainPageLocators.ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", order_button)
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(MainPageLocators.ORDER_BUTTON))
        order_button.click()

    def scroll_to_accordion(self):
        accordion = self.driver.find_element(*MainPageLocators.ACCORDION)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion)
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(MainPageLocators.ACCORDION))

    def first_faq_click(self):
        self.driver.find_element(*MainPageLocators.FIRST_FAQ).click()

    def second_faq_click(self):
        self.driver.find_element(*MainPageLocators.SECOND_FAQ).click()

    def third_faq_click(self):
        self.driver.find_element(*MainPageLocators.THIRD_FAQ).click()

    def fourth_faq_click(self):
        self.driver.find_element(*MainPageLocators.FOURTH_FAQ).click()

    def fifth_faq_click(self):
        self.driver.find_element(*MainPageLocators.FIFTH_FAQ).click()

    def sixth_faq_click(self):
        self.driver.find_element(*MainPageLocators.SIXTH_FAQ).click()

    def seventh_faq_click(self):
        self.driver.find_element(*MainPageLocators.SEVENTH_FAQ).click()

    def eight_faq_click(self):
        self.driver.find_element(*MainPageLocators.EIGHT_FAQ).click()

    def get_first_answer_text(self):
        return self.driver.find_element(*MainPageLocators.FIRST_ANSWER).text

    def get_second_answer_text(self):
        return self.driver.find_element(*MainPageLocators.SECOND_ANSWER).text

    def get_third_answer_text(self):
        return self.driver.find_element(*MainPageLocators.THIRD_ANSWER).text

    def get_fourth_answer_text(self):
        return self.driver.find_element(*MainPageLocators.FOURTH_ANSWER).text

    def get_fifth_answer_text(self):
        return self.driver.find_element(*MainPageLocators.FIFTH_ANSWER).text

    def get_sixth_answer_text(self):
        return self.driver.find_element(*MainPageLocators.SIXTH_ANSWER).text

    def get_seventh_answer_text(self):
        return self.driver.find_element(*MainPageLocators.SEVENTH_ANSWER).text

    def get_eight_answer_text(self):
        return self.driver.find_element(*MainPageLocators.EIGHT_ANSWER).text


