# Python QA Automation Framework

A professional-grade Selenium test automation framework built with **Python, Pytest, and Page Object Model architecture**.

This project demonstrates how a modern QA automation framework is structured for **scalability, maintainability, and CI integration**.

It includes:

- Selenium WebDriver automation
- Page Object Model design pattern
- Centralized configuration
- Parallel test execution
- Logging
- Screenshots on failure
- GitHub Actions CI pipeline
- HTML test reports

This framework simulates how real QA teams structure automation projects in production environments.

---

# Tech Stack

Python  
Pytest  
Selenium WebDriver  
Pytest-xdist (parallel execution)  
Pytest-html (test reports)  
GitHub Actions (CI/CD)

---

# Project Architecture

The framework follows the **Page Object Model (POM)** design pattern.

```
python-qa-automation-framework
│
├── pages
│ ├── base_page.py
│ ├── login_page.py
│ └── search_page.py
│
├── tests
│ ├── test_login.py
│ └── test_search.py
│
├── utils
│ ├── config_reader.py
│ ├── driver_factory.py
│ ├── logger.py
│ └── screenshot_helper.py
│
├── config
│ └── settings.yaml
│
├── .github/workflows
│ └── ci.yml
│
├── requirements.txt
└── README.md
```

---

# Features

## Page Object Model

Each page has its own class containing:

- locators
- actions
- reusable functions

Example:

```
login_page.py
```

Encapsulates login functionality so tests remain clean and readable.

---

## Parallel Test Execution

Tests run in parallel using:

```
pytest -n 2
```

This significantly reduces test execution time in larger test suites.

---

## Centralized Configuration

Framework settings are stored in:

```
config/settings.yaml
```

Example configuration:

```
base_url: https://the-internet.herokuapp.com
browser: chrome
timeout: 10
```

This allows easy environment management.

---

## Logging

The framework includes structured logging for:

- test execution
- debugging
- CI diagnostics

Logs are generated automatically during test runs.

---

## Screenshots on Failure

If a test fails, the framework automatically captures a screenshot.

This helps debug UI failures in CI environments.

---

## HTML Test Reports

Test reports are generated using:

```
pytest-html
```

Example run command:

```
pytest -n 2 -v --html=report.html
```

This produces a visual report showing:

- passed tests
- failed tests
- execution time
- detailed results

---

# Continuous Integration

This project uses **GitHub Actions** to run tests automatically on every push.

CI pipeline includes:

- Python setup
- Chrome installation
- dependency installation
- parallel test execution

Workflow file:

```
.github/workflows/ci.yml
```

---

# Running Tests Locally

## Install dependencies

```
pip install -r requirements.txt
```

## Run tests

```
pytest -v
```

## Run tests in parallel

```
pytest -n 2 -v
```

## Generate HTML report

```
pytest -n 2 -v --html=report.html
```

---

# Example Test

Example login test:

```
def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "secure area" in driver.page_source.lower()
```

---

# Why This Framework Matters

Many Selenium examples online show basic scripts.

This project demonstrates **how automation frameworks are actually built in real engineering environments**, including:

- scalable architecture
- reusable components
- CI integration
- parallel execution
- maintainability

---

# Future Improvements

Possible future upgrades:

- Dockerized test execution
- Allure reporting
- API testing integration
- test data management
- cross-browser testing

---

# Author

Jose Sandoval

Premise Technician → Python Automation Engineer

GitHub:  
https://github.com/je80sand