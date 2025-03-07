import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytestmark = pytest.mark.sandbox

#-------------------------------------------------------IS-001
@allure.title("The button displays a Label 3 seconds after being clicked")
@allure.epic("Web UI")
@allure.feature("Button with Dynamic ID")
@allure.story("The text appears 3 seconds after clicking the button with Dynamic ID")
@allure.testcase("IS-001")
def test_boton_id_dinamico_muestra_texto_al_hacer_click(sandbox_page):
    with allure.step("Given I navigate to the sandbox and click the button with Dynamic ID"):
        sandbox_page.navigate_sandbox()
        sandbox_page.click_boton_id_dinamico()
    with allure.step("And I wait for the 3-second delay before the text appears"):
        elemento_texto_oculto = sandbox_page.wait_for_element(
            sandbox_page.HIDDEN_TEXT_LABEL)
    with allure.step("Then I can verify that the button indeed displays a text"):
        texto_esperado = (
            "OMG, aparezco después de 3 segundos de haber hecho click en el botón")
        assert (
            texto_esperado in elemento_texto_oculto.text
        ), "The expected text does not match the found text"

#-------------------------------------------------------IS-002
@allure.title("The button with Dynamic ID changes color on hover.")
@allure.epic("Web UI")
@allure.feature("Button with Dynamic ID")
@allure.story("The button component should change color when hovering over it")
@allure.testcase("IS-002")
@allure.severity(allure.severity_level.TRIVIAL)
def test_boton_id_dinamico_cambiar_color_al_hacer_hover(sandbox_page):
    with allure.step("Given I navigate to the sandbox and verify the button has a default color"):
        sandbox_page.navigate_sandbox()
        boton_id_dinamico = sandbox_page.wait_for_element(
            sandbox_page.DYNAMIC_ID_BUTTON)
        color_before_hover = boton_id_dinamico.value_of_css_property("background-color")
    with allure.step(
        "When I hover over the Dynamic ID button and check its color"):
        sandbox_page.hover_over_dynamic_id_button()
        color_after_hover = boton_id_dinamico.value_of_css_property("background-color")
    with allure.step(
        "Then I can verify that the color before and after hovering are different"):
        assert color_before_hover != color_after_hover

#-------------------------------------------------------IS-003
@allure.title("I can select the checkbox associated with a food item in the food checkboxes component")
@allure.epic("Web UI")
@allure.feature("Food Checkboxes")
@allure.story("The user can select a value from the food checkboxes")
@allure.severity(allure.severity_level.NORMAL)
@allure.testcase("IS-003")
def test_elegir_checkbox(sandbox_page):
    label_text = "Pizza"
    with allure.step("Given I navigate to the sandbox"):
        sandbox_page.navigate_sandbox()
    with allure.step("I can select a food item by clicking the checkbox associated with it"):
        sandbox_page.select_checkbox_with_label(label_text)
        assert sandbox_page.is_checkbox_selected(
            label_text
        ), f"The checkbox for {label_text} is not selected after clicking it."

#-------------------------------------------------------IS-004
@allure.title("I can select a radio button.")
@allure.epic("Web UI")
@allure.feature("Radio Buttons")
@allure.story("The user can select a radio button")
@allure.testcase("IS-004")
@allure.severity(allure.severity_level.NORMAL)
def test_elegir_radio_button(sandbox_page):
    opcion_radio_button = "No"
    with allure.step(f"Given I navigate to the sandbox and select the radio button labeled {opcion_radio_button}"):
        sandbox_page.navigate_sandbox()
        sandbox_page.select_radio_button(opcion_radio_button)
    with allure.step(f"Then I can validate that the {opcion_radio_button} button was correctly selected"):
        assert sandbox_page.is_radio_button_selected(
            opcion_radio_button
        ), f"The radio button '{opcion_radio_button}' is not selected."

#-------------------------------------------------------IS-005
@allure.title("I can select a sport from the Sports dropdown.")
@allure.epic("Web UI")
@allure.feature("Sports Dropdown")
@allure.story("The user can select a sport.")
@allure.testcase("IS-005")
@allure.severity(allure.severity_level.NORMAL)
def test_elegir_deporte_del_dropdown(sandbox_page):
    deporte = "Fútbol"
    with allure.step("Given I navigate to the sandbox"):
        sandbox_page.navigate_sandbox()
    with allure.step(f"I can select {deporte} from the Sports dropdown"):
        sandbox_page.select_deporte(deporte)

#-------------------------------------------------------IS-006
@allure.title("The list of sports in the Sports dropdown is as expected.")
@allure.epic("Web UI")
@allure.feature("Sports Dropdown")
@allure.story("Sports Lists")
@allure.testcase("IS-006")
@allure.severity(allure.severity_level.MINOR)
def test_deporte_dropdown_options(sandbox_page):
    with allure.step("Given I navigate to the sandbox"):
        sandbox_page.navigate_sandbox()
    with allure.step("And I retrieve the list of sports in the dropdown"):
        options = sandbox_page.get_deporte_dropdown_options()
    with allure.step("Then I can validate that the list matches the requirements"):
        expected_options = ["Seleccioná un deporte", "Fútbol", "Tennis", "Basketball"]
        assert all(
            option in options for option in expected_options
        ), "Not all expected options are present in the dropdown"

#-------------------------------------------------------IS-007
@allure.title("The text 'Example Popup' appears inside a popup when clicking the 'Popup' button")
@allure.epic("Web UI")
@allure.feature("Popup")
@allure.story("The user sees a popup when clicking the Popup button")
@allure.testcase("IS-007")
@allure.severity(allure.severity_level.CRITICAL)
def test_popup_title(sandbox_page):
    with allure.step("Given I navigate to the sandbox"):
        sandbox_page.navigate_sandbox()
    with allure.step("And I click the Popup button"):
        sandbox_page.click_boton_popup()
    with allure.step("Then I can validate that the text 'Popup de ejemplo' appears inside the popup"):
        popup_title_text = sandbox_page.get_popup_title_text()
        expected_text = "Popup de ejemplo"

        assert (
            popup_title_text == expected_text
        ), f"The popup text is incorrect, got '{popup_title_text}' instead."

#-------------------------------------------------------IS-008
@allure.title("The dynamic table changes cell values after reloading the page.")
@allure.epic("Web UI")
@allure.feature("Dynamic Table")
@allure.story("The dynamic table changes cell values after page reload.")
@allure.testcase("IS-008")
@allure.severity(allure.severity_level.CRITICAL)
def test_valor_celda_cambia_post_recarga(sandbox_page):
    with allure.step("Given I navigate to the sandbox"):
        sandbox_page.navigate_sandbox()
    with allure.step("And I retrieve the value of a cell as a reference"):
        initial_value = sandbox_page.get_celda_valor(2, 3)
    with allure.step("When I reload the page"):
        sandbox_page.reload_page()
    with allure.step("Then I can see that the cell value has changed"):
        value_post_reload = sandbox_page.get_celda_valor(2, 3)
        assert (
            initial_value != value_post_reload
        ), f"The cell value did not change after reload; still '{initial_value}'."

#-------------------------------------------------------IS-009
@allure.title("The cell values do NOT change after reloading the page for the static table")
@allure.epic("Web UI")
@allure.feature("Static Table")
@allure.story("Cell Behavior")
@allure.testcase("IS-009")
@allure.severity(allure.severity_level.CRITICAL)
@allure.link("https://github.com")
def test_valor_celda_no_cambia_post_recarga(sandbox_page):
    with allure.step("Given I navigate to the sandbox and retrieve a cell value from the static table"):
        sandbox_page.navigate_sandbox()
        initial_value = sandbox_page.get_valor_celda_estatica(2, 3)
    with allure.step("When I reload the page and retrieve the same cell value"):
        sandbox_page.reload_page()
        value_post_reload = sandbox_page.get_valor_celda_estatica(2, 3)
    with allure.step("Then I can verify the value has not changed after the reload"):
        assert (
            initial_value == value_post_reload
        ), f"The cell value changed after reload; was '{initial_value}"
