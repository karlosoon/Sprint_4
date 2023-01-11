from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestAccordion:

    def test_first_faq_text_is_correct(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_on_question(MainPageLocators.FIRST_FAQ)
        assert main_page.get_first_answer_text() == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_second_faq_text_is_correct(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_on_question(MainPageLocators.SECOND_FAQ)
        assert main_page.get_second_answer_text() == "Пока что у нас так: один заказ — один самокат. Если хотите " \
                                                     "покататься с друзьями, можете просто сделать несколько заказов" \
                                                     " — один за другим."

    def test_third_faq_text_is_correct(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_on_question(MainPageLocators.THIRD_FAQ)
        assert main_page.get_third_answer_text() == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат" \
                                                    " 8 мая в течение дня. Отсчёт времени аренды начинается с " \
                                                    "момента, когда вы оплатите заказ курьеру. Если мы привезли " \
                                                    "самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    def test_fourth_faq_text_is_correct(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_on_question(MainPageLocators.FOURTH_FAQ)
        assert main_page.get_fourth_answer_text() == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def test_fifth_faq_text_is_correct(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_on_question(MainPageLocators.FIFTH_FAQ)
        assert main_page.get_fifth_answer_text() == "Пока что нет! Но если что-то срочное — всегда можно позвонить " \
                                                    "в поддержку по красивому номеру 1010."

    def test_sixth_faq_text_is_correct(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_on_question(MainPageLocators.SIXTH_FAQ)
        assert main_page.get_sixth_answer_text() == "Самокат приезжает к вам с полной зарядкой. Этого хватает на " \
                                                    "восемь суток — даже если будете кататься без передышек и во " \
                                                    "сне. Зарядка не понадобится."

    def test_seventh_faq_text_is_correct(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_on_question(MainPageLocators.SEVENTH_FAQ)
        assert main_page.get_seventh_answer_text() == "Да, пока самокат не привезли. Штрафа не будет, объяснительной " \
                                                      "записки тоже не попросим. Все же свои."

    def test_eight_faq_text_is_correct(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.cookie_button_click()
        main_page.click_on_question(MainPageLocators.EIGHT_FAQ)
        assert main_page.get_eight_answer_text() == "Да, обязательно. Всем самокатов! И Москве, и Московской области."
