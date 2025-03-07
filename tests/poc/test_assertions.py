import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def test_validar_igualdad_de_texto(driver):
    elemento = driver.find_element_by_id("id_del_boton_comprar")
    texto_esperado = "Comprar Curso"
    assert elemento.text == texto_esperado


def test_validar_contiene_texto(driver):
    elemento = driver.find_element_by_id("id_del_boton_comprar")
    substring_esperado = "substring"
    assert substring_esperado in elemento.text


def test_validar_no_igualdad_de_texto(driver):
    elemento = driver.find_element_by_id("id_del_boton_comprar")
    texto_esperado = "Comprar Curso"
    assert elemento.text != texto_esperado


def test_validar_lista_no_vacia(driver):
    elementos = driver.find_elements_by_class_name("clase_elementos_lista")
    assert len(elementos) > 0


def test_boton_habilitado(driver):
    boton = driver.find_element_by_id("id_boton")
    assert boton.is_enabled()


def test_boton_no_esta_habilitado(driver):
    boton = driver.find_element_by_id("id_boton")
    assert not boton.is_enabled()


def test_boton_visible(driver):
    boton = driver.find_element_by_id("id_boton")
    assert boton.is_displayed()


def test_boton_no_visible(driver):
    boton = driver.find_element_by_id("id_boton")
    assert not boton.is_displayed()


def test_validar_igualdad_de_texto_sitio(driver):
    try:
        elemento = driver.find_element_by_id("id_del_boton_comprar")
        texto_esperado = "Comprar Curso"
        assert elemento.text == texto_esperado
    except NoSuchElementException: # type: ignore
        assert False, "No se pudo encontrar el elemento con el locator proporcionado"
