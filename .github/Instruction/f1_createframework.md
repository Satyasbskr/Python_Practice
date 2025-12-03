<Role>
-You are an expert in Python and Playwright Functional Testing.
-You write concise, maintainable Python code with strict type safety.
- You are tasked with creating a new Playwright framework

<Context>
-- Follow best practices for Playwright test structure and assertions.
- Make sure all minimum dependencies and files are included (e.g. playwright/test).
- Ensure the examples and code are well-structured, readable, and ready for future enhancements.
- Add comments to clarify test steps and intent where helpful.

<Requirements>

- This framework will be used only for UI automation.
- The framework will use the following structure (test architecture):

├── test/                    # Test specs
│   └── sample.py       # Includes beforeAll, test, afterAll
├── src/
│   ├── pages/               # Page Object Models
│   ├── helpers/             # Utility functions, setup/teardown
│   └── fixtures/            # Test data and reusable fixtures
├── results/                 # Test results and reports
├── config /
|      ├── .env.test                # Environment-specific variables
|      ├── .env.dev
|      ├── .env.stage
|      └── .env.prod
└── README.md

- This framework needs to have code and config created to enable **parallel execution** using Playwright’s built-in capabilities.
- This framework configure tests to run in Chrome using the Desktop Chrome device.
- This framework support multiple environments which will handle different data (baseURLs, credentials like username and password, text validations) based on file selected (see test architecture config folder (e.g. -> .env.test)).
- This framework will use the Page Object Model (POM) for maintainability.
- This framework will store credentials and endpoints securely using .env files.
- This framework will use globalSetup and globalTeardown for environment initialization and cleanup.
- This framework will use save output test results under the "Results/" folder (see test architecture).
- This framework for test cases will implement execution only using test files with format as ".spec.ts"
- Inside the test files we will be dividing the structure as
  - "beforeAll": Log in to the application
  - "test": Validate a UI element or page title
  - "afterAll": Close the browser and clear cache
- The output files generated after execution should be in xml, HTML, and Json format all of them stores under results


<Deliverable>

- Create all necessary folder using the Test Architecture under the current root folder.
- Verify folder structure is same as Test Architecture.
- If there is any question about any Requirement, ask before completing folder creation.
- Make sure minimum basic code to make Playwright framework to work is added
