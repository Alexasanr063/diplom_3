# Stellar Burgers Test Automation

Selenium-based test automation project for [Stellar Burgers](https://stellarburgers.nomoreparties.site) web application.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run with reports
pytest --alluredir=allure-results -v
allure serve allure-results
```

## Project Structure

- `api/` - API interaction classes (UserAPI, OrderAPI)
- `pages/` - Page Object Model classes  
- `locators/` - Element locators
- `tests/` - Test files
- `config.py` - URLs, endpoints, test data

## Test Approach

**Hybrid API + UI Testing:**
- API layer for fast test setup/data creation
- UI layer for user experience validation
- Page Object Model with Allure reporting
- Chrome WebDriver automation

## Key Commands

```bash
pytest tests/test_main_page.py    # Specific test file
pytest -v                        # Verbose output
pytest tests/test_api_integration.py  # API tests
```

## Architecture

- **BasePage** - Common Selenium operations
- **Page Classes** - Inherit from BasePage, contain page-specific methods
- **API Classes** - Handle REST API interactions
- **Test Fixtures** - Browser setup, user authentication
- **Allure Integration** - Enhanced test reporting