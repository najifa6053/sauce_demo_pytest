# Testing_Sauce_Demo_pytest-


This project demonstrates an example Pytest-based automation suite for the SauceDemo demo e-commerce site using the Page Object Model (POM).
Features:
- Page Object Model for Login, Inventory, Cart, and Checkout pages
- Pytest fixtures for browser lifecycle and login
- Three tests: order confirmation, order cancellation, and checkout details verification
- Use of pytest markers: skip, xfail, flaky, dependency, skipif, parametrize
- Generates test report with pytest-html 


### Step 1: **Clone the project**

Open Terminal:

```bash
git clone https://github.com/najifa6053/Sauce_Demo_Pytest-.git
```

---

### Step 2: **Create and Activate a Virtual Environment**

```bash
py -m venv venv
source venv/scripts/activate
```

### Step 3: **Install Selenium and WebDriver Manager**

```bash
pip install selenium webdriver-manager
```

### Step 4: **Install pytest and pytest html**

```bash
pip install pytest
pip install pytest-html
pip install pytest-dependency
pip install pytest-order
pip install pytest-rerunfailures

```


### Step 5: **Run the Script**

In Terminal: To run a specific file

```bash
pytest <file_name> --html=reports/report.html --self-contained-html

```

In Terminal: To run a all testcases

```bash
pytest --html=reports/report.html --self-contained-html

```

### Notes:
- Tests use `pytest-order` to control execution order. Install with `pip install pytest-order` if needed.
- After a run the HTML report will be created at `reports/report.html`.
- The suite uses Selenium WebDriver. Ensure Chrome and a matching chromedriver are installed and available on PATH.
- You can set HEADLESS=1 environment variable to run the browser in headless mode.
- To see conditional skipping in action, set environment variables such as SKIP_CANCEL=1.
