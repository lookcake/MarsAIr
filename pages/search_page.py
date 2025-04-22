from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    DEPARTURE_DROPDOWN = (By.ID, "departing")
    RETURN_DROPDOWN = (By.ID, "returning")
    PROMO_CODE_INPUT = (By.ID, "promotional_code")
    SEARCH_BUTTON = (By.XPATH, "//input[@type='submit' and @value='Search']")
    RESULT_MESSAGE = (By.ID, "content")  # result message

    # Actions
    def is_departure_dropdown_visible(self):
        return self.driver.find_element(*self.DEPARTURE_DROPDOWN).is_displayed()

    def is_return_dropdown_visible(self):
        return self.driver.find_element(*self.RETURN_DROPDOWN).is_displayed()

    def get_departure_options(self):
        return Select(self.driver.find_element(*self.DEPARTURE_DROPDOWN)).options

    def get_return_options(self):
        return Select(self.driver.find_element(*self.RETURN_DROPDOWN)).options

    def select_departure_by_index(self, index):
        Select(self.driver.find_element(*self.DEPARTURE_DROPDOWN)).select_by_index(index)

    def select_departure_by_text(self, visible_text):
        Select(self.driver.find_element(*self.DEPARTURE_DROPDOWN)).select_by_visible_text(visible_text)

    def select_return_by_index(self, index):
        Select(self.driver.find_element(*self.RETURN_DROPDOWN)).select_by_index(index)

    def select_return_by_text(self, visible_text):
        Select(self.driver.find_element(*self.DEPARTURE_DROPDOWN)).select_by_visible_text(visible_text)

    def enter_promo_code(self, code):
        self.driver.find_element(*self.PROMO_CODE_INPUT).clear()
        self.driver.find_element(*self.PROMO_CODE_INPUT).send_keys(code)

    def click_search(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def get_result_text(self):
        container = self.driver.find_element(*self.RESULT_MESSAGE)
        result = container.find_elements(By.TAG_NAME, "p")
        return " ".join(p.text for p in result if p.text.strip())

    def is_promotional_code_visible(self):
        return self.driver.find_element(*self.PROMO_CODE_INPUT).is_displayed()
