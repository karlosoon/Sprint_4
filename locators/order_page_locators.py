from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_FIELD = By.XPATH, './/input[@placeholder="* Имя"]'

    SURNAME_FIELD = By.XPATH, './/input[@placeholder="* Фамилия"]'

    ADDRESS_FIELD = By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]'

    NUMBER_FIELD = By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]'

    METRO_FIELD = By.XPATH, './/input[@placeholder="* Станция метро"]'

    NEXT_BUTTON = By.XPATH, './/button[text()="Далее"]'

    METRO_BULVAR_ROKO = By.XPATH, './/button/div[text()="Бульвар Рокоссовского"]'

    DELIVERY_DATE = By.XPATH, './/input[@placeholder="* Когда привезти самокат"]'

    RENT_PERIOD_FIELD = By.CLASS_NAME, 'Dropdown-placeholder'

    RENT_PERIOD_ONE_DAY = By.XPATH, './/div[text()="сутки"]'

    RENT_PERIOD_TWO_DAYS = By.XPATH, './/div[text()="двое суток"]'

    BLACK_COLOR = By.ID, 'black'

    GREY_COLOR = By.ID, 'grey'

    COMMENTARY = By.XPATH, './/input[@placeholder="Комментарий для курьера"]'

    PLACE_ORDER_BUTTON = By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]'

    CONFIRM_BUTTON = By.XPATH, './/button[text()="Да"]'

    ORDER_IS_PLACED_TEXT = By.XPATH, './/div[contains(text(),"Заказ оформлен")]'
