from selenium.webdriver.common.by import By


class MainPageLocators:

    COOKIE_ACCEPT_BUTTON = By.ID, 'rcc-confirm-button'

    HEADER_ORDER_BUTTON = By.XPATH, './/button[text()="Заказать"]'

    ORDER_BUTTON = By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'

    ACCORDION = By.CLASS_NAME, 'accordion'

    FIRST_FAQ = By.ID, 'accordion__heading-0'

    SECOND_FAQ = By.ID, 'accordion__heading-1'

    THIRD_FAQ = By.ID, 'accordion__heading-2'

    FOURTH_FAQ = By.ID, 'accordion__heading-3'

    FIFTH_FAQ = By.ID, 'accordion__heading-4'

    SIXTH_FAQ = By.ID, 'accordion__heading-5'

    SEVENTH_FAQ = By.ID, 'accordion__heading-6'

    EIGHT_FAQ = By.ID, 'accordion__heading-7'

    FIRST_ANSWER = By.XPATH, './/div[@id="accordion__panel-0"]/p'

    SECOND_ANSWER = By.XPATH, './/div[@id="accordion__panel-1"]/p'

    THIRD_ANSWER = By.XPATH, './/div[@id="accordion__panel-2"]/p'

    FOURTH_ANSWER = By.XPATH, './/div[@id="accordion__panel-3"]/p'

    FIFTH_ANSWER = By.XPATH, './/div[@id="accordion__panel-4"]/p'

    SIXTH_ANSWER = By.XPATH, './/div[@id="accordion__panel-5"]/p'

    SEVENTH_ANSWER = By.XPATH, './/div[@id="accordion__panel-6"]/p'

    EIGHT_ANSWER = By.XPATH, './/div[@id="accordion__panel-7"]/p'
