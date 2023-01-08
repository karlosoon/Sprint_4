from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from my_test_data import MyTestData


class TestOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_order_by_clicking_lower_order_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_on_order_button()
        order_page = OrderPage(self.driver)
        order_page.set_order_first_step_valid_test_data(MyTestData.name, MyTestData.surname, MyTestData.address,
                                                        MyTestData.number)
        order_page.set_metro()
        order_page.click_next_button()
        order_page.set_delivery_date(MyTestData.delivery_date)
        order_page.set_rent_period_one_day()
        order_page.set_color_black()
        order_page.set_commentary(MyTestData.comment)
        order_page.click_place_order_button()
        order_page.click_confirm_button()
        assert "Заказ оформлен" in order_page.get_order_placed_text()

    def test_order_by_clicking_header_order_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(self.driver)
        main_page.click_on_header_order_button()
        order_page = OrderPage(self.driver)
        order_page.set_order_first_step_valid_test_data(MyTestData.name1, MyTestData.surname1, MyTestData.address1,
                                                        MyTestData.number1)
        order_page.set_metro()
        order_page.click_next_button()
        order_page.set_delivery_date(MyTestData.delivery_date1)
        order_page.set_rent_period_two_days()
        order_page.set_color_grey()
        order_page.click_place_order_button()
        order_page.click_confirm_button()
        assert "Заказ оформлен" in order_page.get_order_placed_text()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
