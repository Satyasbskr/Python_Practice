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
1. Install dependencies
2. Configure environment variables
3. Write tests in `test/` folder

## Parallel Execution
Configure Playwright to run tests in parallel using pytest or Playwright's built-in capabilities.
