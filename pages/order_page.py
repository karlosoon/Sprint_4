from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys(address)

    def set_number(self, number):
        self.driver.find_element(*OrderPageLocators.NUMBER_FIELD).send_keys(number)

    def set_metro(self):
        self.driver.find_element(*OrderPageLocators.METRO_FIELD).click()
        self.driver.find_element(*OrderPageLocators.METRO_BULVAR_ROKO).click()

    def set_order_first_step_valid_test_data(self, name, surname, address, number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_number(number)

    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()
        WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located(OrderPageLocators.PLACE_ORDER_BUTTON))

    def set_delivery_date(self, date):
        self.driver.find_element(*OrderPageLocators.DELIVERY_DATE).send_keys(date)
        self.driver.find_element(*OrderPageLocators.DELIVERY_DATE).send_keys(Keys.ESCAPE)

    def set_rent_period_one_day(self):
        self.driver.find_element(*OrderPageLocators.RENT_PERIOD_FIELD).click()
        self.driver.find_element(*OrderPageLocators.RENT_PERIOD_ONE_DAY).click()

    def set_rent_period_two_days(self):
        self.driver.find_element(*OrderPageLocators.RENT_PERIOD_FIELD).click()
        self.driver.find_element(*OrderPageLocators.RENT_PERIOD_TWO_DAYS).click()

    def set_color_black(self):
        self.driver.find_element(*OrderPageLocators.BLACK_COLOR).click()

    def set_color_grey(self):
        self.driver.find_element(*OrderPageLocators.GREY_COLOR).click()

    def set_commentary(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENTARY).send_keys(comment)

    def click_place_order_button(self):
        self.driver.find_element(*OrderPageLocators.PLACE_ORDER_BUTTON).click()

    def click_confirm_button(self):
        self.driver.find_element(*OrderPageLocators.CONFIRM_BUTTON).click()

    def get_order_placed_text(self):
        return self.driver.find_element(*OrderPageLocators.ORDER_IS_PLACED_TEXT).text

