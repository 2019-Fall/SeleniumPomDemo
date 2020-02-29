from features.ui.all_imports import *


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_element_by_xpath(self, xpath):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
        except NoSuchElementException as err:
            print(f"Error: Element was not found {element}")
            self.take_screenshot('Error')
            raise

    def enter_text_xpath(self, xpath, phrase):
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element.clear()
            element.send_keys(phrase)
        except NoSuchElementException as err:
            print(f"Error: Element was not found {element}")
            self.take_screenshot('Error')
            raise

    def take_screenshot(self, phrase=""):
        filepath = f"./screenshots/{phrase}-{utils.get_timestamp()}.png"
        self.driver.save_screenshot(filepath)