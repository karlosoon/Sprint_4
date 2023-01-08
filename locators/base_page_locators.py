from selenium.webdriver.common.by import By


class BasePageLocators:

    SAMOKAT_LOGO = By.CLASS_NAME, 'Header_LogoScooter__3lsAR'

    YANDEX_LOGO = By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']"
