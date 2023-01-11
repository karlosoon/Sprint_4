import pytest
from selenium.webdriver import Firefox


@pytest.fixture()
def driver():
    driver = Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
