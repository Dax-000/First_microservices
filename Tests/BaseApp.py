from selenium.common import TimeoutException, WebDriverException, InvalidSelectorException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


class BasePage:

    def __init__(self, driver, logger):
        self.logger = logger
        self.driver = driver

    def find_element(self, locator, time=2.5):
        try:
            web_element = WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator))
            self.logger.info(f"Find element by locator {locator}")
            return web_element
        except TimeoutException:
            self.logger.error(f"Can't find element by locator {locator}", exc_info=True)
        except InvalidSelectorException:
            self.logger.error(f"Invalid locator {locator}")

    def go_to_url(self, url):
        try:
            self.driver.get(url)
            self.logger.info(f"Visit url {url}")
        except WebDriverException as _:
            self.logger.error(f"Can't visit url {url}", exc_info=True)
