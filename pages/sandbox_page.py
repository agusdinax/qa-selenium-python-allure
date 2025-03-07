from selenium.webdriver.common.by import By
from .base_page import BasePage

class SandboxPage(BasePage):
    URL = 'https://thefreerangetester.github.io/sandbox-automation-testing/'
    ENVIAR_BUTTON = (By.XPATH, "//button[contains(text(), 'Enviar')]")
    DYNAMIC_ID_BUTTON = (By.XPATH,"//button[contains(text(), 'Hacé click para generar un ID dinámico y mostrar el elemento oculto')]",)
    HIDDEN_TEXT_LABEL = (By.XPATH,"//p[contains(text(), 'OMG, aparezco después de 3 segundos de haber hecho click en el botón')]",)
    DEPORTE_DROPDOWN = (By.ID,"formBasicSelect",)
    MOSTRAR_POPUP_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'btn-primary') and text()='Mostrar popup']",)
    POPUP_TITLE = (By.ID,"contained-modal-title-vcenter",)

    def navigate_sandbox(self):
        self.navigate_to(self.URL)

    def click_enviar(self):
        self.click(self.ENVIAR_BUTTON)

    def click_boton_id_dinamico(self):
        self.click(self.DYNAMIC_ID_BUTTON)

    def hover_over_dynamic_id_button(self):
        self.hover_over_element(self.DYNAMIC_ID_BUTTON)

    def select_checkbox_with_label(self, label_text):
        assert label_text in [
            "Pizza",
            "Hamburguesa",
            "Pasta",
            "Helado",
            "Torta",
        ], "Las opciones aceptadas son Pizza, Hamburguesa, Pasta, Helado y Torta"
        checkbox_locator = (
            By.XPATH,
            f"//label[contains(., '{label_text}')]/preceding-sibling::input[@type='checkbox']",
        )
        self.select_element(checkbox_locator)

    def is_checkbox_selected(self, label_text):
        assert label_text in [
            "Pizza",
            "Hamburguesa",
            "Pasta",
            "Helado",
            "Torta",
        ], "Las opciones aceptadas son Pizza, Hamburguesa, Pasta, Helado y Torta"
        checkbox_locator = (
            By.XPATH,
            f"//label[contains(., '{label_text}')]/preceding-sibling::input[@type='checkbox']",
        )
        checkbox_element = self.driver.find_element(*checkbox_locator)
        return checkbox_element.is_selected()

    def select_radio_button(self, option):
        assert option in ["Si", "No"], "La opción tiene que ser Si o No"
        radio_button_locator = (
            By.XPATH,
            f"//label[@class='form-check-label' and contains(text(),'{option}')]",
        )

        self.select_element(radio_button_locator)

    def is_radio_button_selected(self, option):
        assert option in ["Si", "No"], "La opción tiene que ser Si o No"
        radio_button_locator = (
            By.XPATH,
            f"//label[@class='form-check-label' and contains(text(),'{option}')]/preceding-sibling::input",
        )
        radio_button_element = self.driver.find_element(*radio_button_locator)
        return radio_button_element.is_selected()

    def select_deporte(self, deporte):
        self.select_from_dropdown_by_visible_text(self.DEPORTE_DROPDOWN, deporte)

    def get_deporte_dropdown_options(self):
        return self.get_select_options(self.DEPORTE_DROPDOWN)

    def click_boton_popup(self):
        self.hover_over_element(self.MOSTRAR_POPUP_BUTTON)
        self.click(self.MOSTRAR_POPUP_BUTTON)

    def get_popup_title_text(self):
        return self.wait_for_element(self.POPUP_TITLE).text

    def get_celda_valor(self, fila, columna):
        celda_xpath = f"(//table[@class='table table-striped table-bordered table-hover']/tbody/tr)[{fila}]/td[{columna}]"
        celda = self.wait_for_element((By.XPATH, celda_xpath))
        return celda.text if celda else None

    def get_valor_celda_estatica(self, fila, columna):
        celda_xpath = f"(//h2[normalize-space()='Tabla estática']/following-sibling::table/tbody/tr)[{fila}]/td[{columna}]"
        celda = self.wait_for_element((By.XPATH, celda_xpath))
        return celda.text if celda else None
