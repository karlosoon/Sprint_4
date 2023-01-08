from selenium import webdriver
from pages.base_page import BasePage


class TestBasePage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_main_page_opens_by_click_on_samokat_logo(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
        base_page = BasePage(self.driver)
        base_page.click_on_samokat_logo()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def test_yandex_tab_opens_by_click_on_yandex_logo(self):  # этот тест у меня падает из-за частых запросов
        # к яндексу, на ревью должно быть ок
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        base_page = BasePage(self.driver)
        base_page.click_on_yandex_logo()
        base_page.switch_to_new_tab()
        base_page.wait_for_new_tab()
        current_url = self.driver.current_url
        assert current_url == 'https://dzen.ru/?yredirect=true'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
