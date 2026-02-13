<Role>
- You are an expert in Python and Playwright Functional Testing.
- You write concise, maintainable Python code with best practices.
- You are tasked with creating a new Playwright framework in Python.

<Context>
- Follow best practices for Playwright Python test structure and assertions (using pytest).
- Make sure all minimum dependencies and files are included (e.g. playwright, pytest, pytest-xdist, pytest-html, pytest-json, python-dotenv).
- Ensure the examples and code are well-structured, readable, and ready for future enhancements.
- Add comments to clarify test steps and intent where helpful.


<Requirements>

- This framework will be used only for UI automation with Playwright and Python.
- The framework will use the following structure (test architecture):

├── test/                    # Test specs (Python files: test_*.py or *_test.py)
│   └── sample_test.py       # Example: includes setup, test, teardown using pytest fixtures
├── src/
│   ├── pages/               # Page Object Models (Python classes for each page)
│   ├── helpers/             # Utility functions, setup/teardown
│   └── fixtures/            # Test data and reusable fixtures
├── results/                 # Test results and reports
├── config/
│      ├── .env.test         # Environment-specific variables
│      ├── .env.dev
│      ├── .env.stage
│      └── .env.prod
└── README.md

- Enable **parallel execution** using pytest-xdist (`pip install pytest-xdist`). Run tests in parallel with:
  ```bash
  pytest -n auto
  ```
- Configure tests to run in Chrome by default. In Playwright Python, this is done in the test setup (e.g., using `browser = playwright.chromium.launch(...)`).
- Support multiple environments by loading variables from the appropriate `.env` file using `python-dotenv`.
- Use the Page Object Model (POM) for maintainability (each page as a Python class in `src/pages/`).
- Store credentials and endpoints securely using `.env` files (never commit secrets to version control).
- Use pytest fixtures for setup/teardown (global or per-test) instead of globalSetup/globalTeardown from JS/TS.
- Save output test results under the `results/` folder.
- Test files should be named `test_*.py` or `*_test.py` (not `.spec.ts`).
- Inside test files, structure should be:
  - `setup_method` or `@pytest.fixture(scope="function", autouse=True)`: Log in to the application (before each test)
  - `def test_*`: Validate a UI element or page title
  - `teardown_method` or fixture finalizer: Close the browser and clear cache
- Output files after execution should be in XML, HTML, and JSON format, all stored under `results/`.
  - Use `pytest-html` for HTML reports: `pip install pytest-html`
  - Use `pytest-json` for JSON reports: `pip install pytest-json`
  - Use `pytest --junitxml=results/report.xml` for XML
  - Use `pytest --html=results/report.html` for HTML
  - Use `pytest --json-report --json-report-file=results/report.json` for JSON

**Minimum dependencies to install:**
```bash
pip install playwright pytest pytest-xdist pytest-html pytest-json python-dotenv
playwright install
```


<Deliverable>

- Create all necessary folders using the Test Architecture under the current root folder.
- Verify folder structure matches the Test Architecture.
- If there is any question about any Requirement, ask before completing folder creation.
- Add minimum basic code to make the Playwright Python framework work (sample test, sample page object, sample fixture, and config).
