# form_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class FormPage(BasePage):
    URL = "https://v0-classic-registration-form-u8ghow.vercel.app/"
    
    # Element locators
    NAME_FIELD = (By.XPATH, "//input[@placeholder='Ingrese su nombre']")
    LASTNAME_FIELD = (By.XPATH, "//input[@placeholder='Ingrese su apellido']")
    EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Ingrese su email']")
    PHONE_FIELD = (By.XPATH, "//input[@placeholder='Ingrese su teléfono']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='Ingrese su dirección']")
    CITY_FIELD = (By.XPATH, "//input[@placeholder='Ingrese su ciudad']")
    POSTAL_CODE_FIELD = (By.XPATH, "//input[@placeholder='Ingrese su código postal']")
    COUNTRY_FIELD = (By.XPATH, "//input[@placeholder='Ingrese su país]")
    PROFESSION_FIELD = (By.XPATH, "//input[@placeholder='Ingrese su profesión']")
    INTERESTS_FIELD = (By.XPATH, "//input[@placeholder='Ingrese sus intereses']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar Registro')]")
    
    def navigate_form(self):
        self.navigate_to(self.URL)

    def fill_field(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)
    
    def fill_name(self, name):
        self.fill_field(self.NAME_FIELD, name)
    
    def fill_lastname(self, lastname):
        self.fill_field(self.LASTNAME_FIELD, lastname)
    
    def fill_email(self, email):
        self.fill_field(self.EMAIL_FIELD, email)
    
    def fill_phone(self, phone):
        self.fill_field(self.PHONE_FIELD, phone)
    
    def fill_address(self, address):
        self.fill_field(self.ADDRESS_FIELD, address)
    
    def fill_city(self, city):
        self.fill_field(self.CITY_FIELD, city)
    
    def fill_postal_code(self, code):
        self.fill_field(self.POSTAL_CODE_FIELD, code)
    
    def fill_country(self, country):
        self.fill_field(self.COUNTRY_FIELD, country)
    
    def fill_profession(self, profession):
        self.fill_field(self.PROFESSION_FIELD, profession)
    
    def fill_interests(self, interests):
        self.fill_field(self.INTERESTS_FIELD, interests)
    
    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)
    
    def get_error_message(self, error_text):
        error_locator = (By.XPATH, f"//*[contains(text(), '{error_text}')]")
        return self.is_element_visible(error_locator)
    
    def get_success_message(self):
        success_locator = (By.XPATH, "//*[contains(text(), '¡Registro exitoso!')]")
        return self.is_element_visible(success_locator)
    
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False