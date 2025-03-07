import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from pages.sandbox_page import SandboxPage
from pages.form_page import FormPage

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Type of browser: chrome, firefox, edge, safari",
    )

@pytest.fixture(scope="session")
def browser(request):
    browser_type = request.config.getoption("--browser").lower()
    if browser_type == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_type == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser_type == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service)
    elif browser_type == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Browser {browser_type} not supported")
    yield driver
    driver.quit()

@pytest.fixture
def sandbox_page(browser):
    return SandboxPage(browser)

@pytest.fixture
def form_page(browser):
    return FormPage(browser)
