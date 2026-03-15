![CI](https://github.com/je80sand/python-qa-automation-framework/actions/workflows/ci.yml/badge.svg)

# Python QA Automation Framework

# Python QA Automation Framework

A scalable Selenium + Pytest automation framework built using the Page Object Model.  
This project demonstrates how modern QA teams design automated UI test frameworks.

---

## Features

- Selenium WebDriver automation
- Pytest test runner
- Page Object Model (POM)
- Data-driven testing using JSON
- HTML test reports
- Automatic screenshot capture on failure
- Parameterized test execution
- WebDriver Manager integration

---

## Project Structure

```
python-qa-automation-framework
│
├── pages
│ └── login_page.py
│
├── tests
│ ├── test_login.py
│ └── test_search.py
│
├── utils
│ ├── driver_factory.py
│ ├── config_reader.py
│ └── screenshot_helper.py
│
├── test_data
│ └── test_users.json
│
├── reports
│ ├── report.html
│ └── screenshots/
│
├── conftest.py
├── pytest.ini
└── requirements.txt
```

---

## Technologies Used

- Python
- Selenium
- Pytest
- WebDriver Manager

---

## Running The Tests

Install dependencies:

```
pip install -r requirements.txt
```

Run tests:

```
pytest -v
```

Generate HTML report:

```
pytest --html=reports/report.html
```

---

## Example Test Coverage

The framework currently includes login tests for:

- Valid login
- Invalid login

The tests are **data-driven using JSON**, allowing multiple scenarios to run automatically.

---

## Author

Jose Sandoval  
GitHub: https://github.com/je80sand