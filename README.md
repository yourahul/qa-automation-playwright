# QA Automation Framework

Automation testing framework built using Python, Playwright and Pytest.

## Features
- UI automation: login, signup, add-to-cart  
- API testing  
- Database validation (SQLite + SQL)  
- HTML test report  
- Page Object Model structure  
- GitHub Actions CI

## Tech Stack
Python, Playwright, Pytest, SQL (SQLite), GitHub Actions

## Run Locally

Clone the repo:
```bash
git clone https://github.com/yourahul/qa-automation-playwright.git
cd qa-automation-playwright
```

Install dependencies:
```bash
pip install -r requirements.txt
python -m playwright install
```

Run tests:
```bash
pytest
```

Generate HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

## CI/CD
Tests run automatically on GitHub Actions on every push.

## Author
Rahul U
