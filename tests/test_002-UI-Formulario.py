# tests/test_002-form.py
import pytest
import allure
from selenium import webdriver
from pages.form_page import FormPage 

pytestmark = pytest.mark.form

class TestFormValidation:
#-------------------------------------------------------FORM-001
    @allure.title("Empty mandatory fields prevent form submission")
    @allure.story("Validate that empty mandatory fields show errors")
    @allure.testcase("FORM-001")
    def test_empty_mandatory_fields_prevent_submission(self, form_page):
        with allure.step("Given that I navigate to the form page"):
            form_page.navigate_form()
        with allure.step("When I try to submit the form without filling mandatory fields"):
            form_page.submit_form()
        with allure.step("Then I see errors in the mandatory fields"):
            assert form_page.get_error_message("El nombre debe tener al menos 2 caracteres.")
            assert form_page.get_error_message("El apellido debe tener al menos 2 caracteres.")
            assert form_page.get_error_message("Ingrese un email válido.")
            assert form_page.get_error_message("Ingrese un número de teléfono válido.")
            assert form_page.get_error_message("La dirección debe tener al menos 5 caracteres.")
            assert form_page.get_error_message("Ingrese una ciudad válida.")
            assert form_page.get_error_message("Este campo es obligatorio.")

#-------------------------------------------------------FORM-002
    @allure.title("Empty non-mandatory fields allow form submission")
    @allure.story("Validate successful submission with only mandatory fields")
    @allure.testcase("FORM-002")
    def test_empty_non_mandatory_fields_allow_submission(self, form_page):
        with allure.step("Given that I fill only the mandatory fields"):
            form_page.navigate_form()
            form_page.fill_name("John")
            form_page.fill_lastname("Doe")
            form_page.fill_email("john@example.com")
            form_page.fill_phone("1234567890")
            form_page.fill_address("123 Fake Street")
            form_page.fill_city("Tandil")
            form_page.fill_interests("Programming")
        with allure.step("When I submit the form"):
            form_page.submit_form()
        with allure.step("Then I see a success message"):
            assert form_page.get_success_message(), "Success message not displayed"

#-------------------------------------------------------FORM-003
    @allure.title("Invalid email format shows an error")
    @allure.story("Validate email format validation")
    @allure.testcase("FORM-003")
    def test_invalid_email_format_shows_error(self, form_page):
        with allure.step("Given that I fill the email with an invalid format"):
            form_page.navigate_form()
            form_page.fill_name("John")
            form_page.fill_lastname("Doe")
            form_page.fill_email("invalid-email")
            form_page.fill_phone("1234567890")
            form_page.fill_interests("Programming")
        with allure.step("When I try to submit the form"):
            form_page.submit_form()
        with allure.step("Then I see an error in the email field"):
            assert form_page.get_error_message("Ingrese un email válido.")

#-------------------------------------------------------FORM-004
    @allure.title("Phone with letters shows an error")
    @allure.story("Validate phone number format")
    @allure.testcase("FORM-004")
    def test_phone_with_letters_shows_error(self, form_page):
        with allure.step("Given that I fill the phone with letters"):
            form_page.navigate_form()
            form_page.fill_name("John")
            form_page.fill_lastname("Doe")
            form_page.fill_email("john@example.com")
            form_page.fill_phone("abcde")
            form_page.fill_interests("Programming")
        with allure.step("When I try to submit the form"):
            form_page.submit_form()
        with allure.step("Then I see an error in the phone field"):
            assert form_page.get_error_message("Ingrese un número de teléfono válido.")

#-------------------------------------------------------FORM-005
    @allure.title("Complete form with valid data shows success")
    @allure.story("Validate successful submission with all fields")
    @allure.testcase("FORM-005")
    def test_complete_form_with_valid_data(self, form_page):
        with allure.step("Given that I fill all fields with valid data"):
            form_page.navigate_form()
            form_page.fill_name("John")
            form_page.fill_lastname("Doe")
            form_page.fill_email("john@example.com")
            form_page.fill_phone("1234567890")
            form_page.fill_address("123 Fake Street")
            form_page.fill_city("Buenos Aires")
            form_page.fill_interests("Programming")
        with allure.step("When I submit the form"):
            form_page.submit_form()
        with allure.step("Then I see a success message"):
            assert form_page.get_success_message(), "Success message not displayed"

#-------------------------------------------------------FORM-006
    @allure.title("Individual mandatory field empty shows error")
    @allure.story("Validate single mandatory field validation")
    @allure.testcase("FORM-006")
    def test_individual_mandatory_field_empty(self, form_page):
        with allure.step("Given that I leave the name field empty"):
            form_page.navigate_form()
            form_page.fill_lastname("Doe")
            form_page.fill_email("john@example.com")
            form_page.fill_phone("1234567890")
            form_page.fill_interests("Programming")
        with allure.step("When I try to submit the form"):
            form_page.submit_form()
        with allure.step("Then I see an error only in the name field"):
            assert form_page.get_error_message("El nombre debe tener al menos 2 caracteres.")
            assert not form_page.get_error_message("Ingrese un email válido.")
            assert not form_page.get_error_message("Ingrese un número de teléfono válido.")