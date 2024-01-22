from BaseApp import BasePage
from selenium.webdriver.common.by import By


class Locators:
    ANSWER = (By.TAG_NAME, "pre")


class ServicePy(BasePage):
    def endpoint_greet(self):
        answer = self.find_element(Locators.ANSWER).text
        return answer
