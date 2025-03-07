# 🐍 Selenium Automation Project with Pytest & Allure

## 🌐 English Version

## 📖 Project Overview
This is a **Test Automation Project** developed using **Python, Selenium, Pytest, and Allure Reports**. The project focuses on automating **several test cases** for a sample web application, following the **Page Object Model (POM)** design pattern to ensure better scalability and maintainability.

---

## 🛠️ Tools & Technologies
- Python 3.x
- Selenium WebDriver
- Pytest
- Allure Report

---

## 📂 Project Structure
```
project-root/
│-- pages/                # Page Objects (locators and actions)
│-- tests/                 # Test cases (pytest)
│-- utils/                  # Utilities (configuration, helpers, etc.)
│-- conftest.py            # Pytest fixtures/hooks
│-- pytest.ini              # Pytest configuration
│-- requirements.txt       # Project dependencies
│-- README.md               # This file
```
---

## 🚀 Installation & Setup
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd project-root
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    .\venv\Scripts\activate    # Windows
    ```

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## ✅ Running Tests
### Run all test cases:
```bash
pytest
```

### Run tests marked as 'form':
```bash
pytest -m form
```

### Run a specific test file:
```bash
pytest tests/test_001_login.py
```

---

## 📊 Allure Reports
### Run tests and generate Allure results:
```bash
pytest --alluredir=allure-results
```

### Open Allure report:
```bash
allure serve allure-results
```

---

## 🔗 Useful Additional Commands
- Run tests with detailed output:
```bash
pytest -v
```

- Run only failed tests from previous execution:
```bash
pytest --lf
```

- Customize pytest execution with markers (example `form` marker):
```bash
pytest -m form -v
```

---

---

# 🐍 Proyecto de Automatización con Selenium, Pytest y Allure

## 🌐 Versión en Español

## 📖 Descripción del Proyecto
Este es un **Proyecto de Automatización de Pruebas** desarrollado con **Python, Selenium, Pytest y Allure Reports**. El objetivo es automatizar **varios casos de prueba** para una aplicación web de ejemplo, siguiendo el patrón de diseño **Page Object Model (POM)** para facilitar el mantenimiento y la escalabilidad.

---

## 🛠️ Herramientas y Tecnologías
- Python 3.x
- Selenium WebDriver
- Pytest
- Allure Report

---

## 📂 Estructura del Proyecto
```
project-root/
│-- pages/                # Objetos de página (localizadores y acciones)
│-- tests/                 # Casos de prueba (pytest)
│-- utils/                  # Utilidades (configuración, helpers, etc.)
│-- conftest.py            # Fixtures/Hooks de pytest
│-- pytest.ini              # Configuración de pytest
│-- requirements.txt       # Dependencias del proyecto
│-- README.md               # Este archivo
```

---

## 🚀 Instalación y Configuración
1. Clonar el repositorio:
    ```bash
    git clone <repository-url>
    cd project-root
    ```

2. Crear y activar un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    .\venv\Scripts\activate    # Windows
    ```

3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```

---

## ✅ Ejecución de Pruebas
### Ejecutar todos los casos de prueba:
```bash
pytest
```

### Ejecutar solo pruebas marcadas como 'form':
```bash
pytest -m form
```

### Ejecutar un archivo específico:
```bash
pytest tests/test_001_login.py
```

---

## 📊 Reportes con Allure
### Ejecutar pruebas y generar resultados para Allure:
```bash
pytest --alluredir=allure-results
```

### Abrir el reporte de Allure:
```bash
allure serve allure-results
```

---

## 🔗 Comandos Adicionales Útiles
- Ejecutar pruebas con salida detallada:
```bash
pytest -v
```

- Ejecutar solo pruebas fallidas de la ejecución previa:
```bash
pytest --lf
```

- Personalizar la ejecución usando marcadores (ejemplo 'form'):
```bash
pytest -m form -v
```

---