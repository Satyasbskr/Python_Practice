# Playwright Python UI Automation Framework

This framework is designed for UI automation using Playwright with Python.

## Structure

- `test/` - Test scenarios (format: scenario_test.py)
- `src/pages/` - Page Object Models
- `src/helpers/` - Utility functions
- `src/fixtures/` - Test data and reusable fixtures
- `results/` - Test results and reports
- `config/` - Environment variables (.env files)

## Environments
- `.env.prod` - Production
- `.env.test` - Test
- `.env.stage` - Stage

## Getting Started
1. **Create a Python Virtual Environment**
	 - Open a terminal at the project root (same level as this README).
	 - Run:
		 ```bash
		 python3 -m venv venv
		 ```
	 - Activate the environment:
		 - On macOS/Linux:
			 ```bash
			 source venv/bin/activate
			 ```
		 - On Windows:
			 ```cmd
			 venv\Scripts\activate
			 ```

2. **Upgrade pip (recommended):**
	 ```bash
	 pip install --upgrade pip
	 ```

3. **Install required libraries:**
	 - Install Playwright and pytest:
		 ```bash
		 pip install playwright pytest
		 ```
	 - (Optional) If you use environment variables from `.env` files:
		 ```bash
		 pip install python-dotenv
		 ```
	 - (Optional) For HTML reports:
		 ```bash
		 pip install pytest-html
		 ```

4. **Install Playwright browsers:**
	 - This step downloads the necessary browser binaries (Chromium, Firefox, WebKit) for Playwright to run tests.
	 - Make sure you have installed Playwright in your virtual environment first (`pip install playwright`).
	 - Run the following command (note the correct spelling: `playwright`, not `playright`):
		 ```bash
		 playwright install
		 ```
	 - If you see a 'command not found' error, ensure your virtual environment is activated and Playwright is installed. You can check by running:
		 ```bash
		 pip show playwright
		 which playwright
		 ```
	 - If `which playwright` does not return a path, try reactivating your virtual environment or reinstalling Playwright:
		 ```bash
		 pip install --force-reinstall playwright
		 ```
	 - For more details, see the [Playwright Python docs](https://playwright.dev/python/docs/intro).

5. Configure environment variables
6. Write tests in `test/` folder

## Parallel Execution
Configure Playwright to run tests in parallel using pytest or Playwright's built-in capabilities.
