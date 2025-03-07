from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:
    #constructor-receives the webdriver instance and stores it in the class
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 
    #navigate to a specified URL
    def navigate_to(self, url):
        self.driver.get(url)
    #wait until a specific element is visible on the page, then return the element
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    #click on an element after waiting for it to be visible
    def click(self, locator):
        self.wait_for_element(locator).click()
    #type text into a field
    def type_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)
    #select an option from a dropdown using the visible text
    def select_from_dropdown_by_visible_text(self, locator, text):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_visible_text(text)
    #select an option from a dropdown using the option index
    def select_from_dropdown_by_index(self, locator, index):
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_index(index)
    #retrieve all available options from a dropdown and return them as a list of text strings
    def get_select_options(self, locator):
        dropdown = Select(self.wait_for_element(locator))
        return [option.text for option in dropdown.options]
    #select a checkbox or radio button if its not already selected
    def select_element(self, locator):
        element = self.wait_for_element(locator)
        if not element.is_selected():
            element.click()
    #unselect a checkbox if it's currently selected
    def unselect_checkbox(self, locator):
        checkbox = self.wait_for_element(locator)
        if checkbox.is_selected():
            checkbox.click()
    #hover the mouse pointer over an element
    def hover_over_element(self, locator):
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
    #refresh the current page
    def reload_page(self):
        self.driver.refresh()
