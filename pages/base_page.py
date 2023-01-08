from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def browser_wait(self):
        self.driver.implicitly_wait(10)

    def click_on_samokat_logo(self):
        self.driver.find_element(*BasePageLocators.SAMOKAT_LOGO).click()

    def click_on_yandex_logo(self):
        self.driver.find_element(*BasePageLocators.YANDEX_LOGO).click()

    def wait_for_new_tab(self):
        WebDriverWait(self.driver, 5).until(ec.url_to_be('https://dzen.ru/?yredirect=true'))

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])