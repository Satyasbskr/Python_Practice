<Role>
-You are an expert in Python and Playwright Functional Testing.
-You write concise, maintainable Python code with strict type safety.
- You are tasked to create some automation test scripts using a new Playwright framework.

<Context>
- Follow best practices for Playwright test structure and assertions.
- Ensure the examples and code are well-structured, readable, and ready for future enhancements.
- Add comments to clarify test steps and intent where helpful.

<Requirements>
- The scripts will always be using the following base URL: https://www.kroger.com/
- To successfully login we need to use USERNAME and PASSWORD located inside the config files (e.g. ".env.prod")
- You need to implement best practices to create the following steps using Page Object Model and also considering current architecture established in framework:
  - Go to base URL.
  - Home Page
    - Seek and click "Sign In" top-navigation menu button => locator (id: "WelcomeButton-A11Y-FOCUS-ID")
    - Validate "Welcome Sign In button" is displayed and click on it => locator (data-testid: "WelcomeMenuButtonSignIn")
  - Sign In Page
    - Click on Email Address input box and fill the corresponding USERNAME value (found in .env file) => locator (id: "signInName")
    - Click on password input box and fill the corresponding PASSWORD value (found in .env file) => locator (id: "forgotPassword")
    - Verify "Keep me signed in" checkbox is selected => locator (id: "kr_remember_me_adi_true")
      - If checkbox is not selected, then we should select it.
    - Click on "Sign In" button to continue => locator (id: "continue")
- We need to connect the pages files to the test files using fixture file strategy to avoid basic import (use reference: https://playwright.dev/docs/test-fixtures).
- On each of the "page.py" files you need to implement the following POM internal structure:
  - Define locators variable type (e.g. 'private readonly signInTopNavigationMenu: Locator')
  - Define the constructor and inside set all locators value (e.g. "this.subMenuSignInButton = page.getByTestId('WelcomeMenuButtonSignIn');")
  - Finally define, necessary steps to acomplish certain task (e.g successfully login to app), you can add any annotations needed to understand functionality.
  - Verify all libraries are correctly imported.
  - The files created in test folder (make sure you use pre-established name-convention) should include the following:
    - Include "test.description" cause we will be grouping positive and negative scenarios together.
    - Include under "test()" add a title format easy to identify the test cases (e.g. UI-XXX - Summary).
    - Implement tags strategy that will help us to execute only certain scenarios (e.g. only positive sign in)
    - Make sure that steps created on pages files are imported using fixture strategy (use reference: https://playwright.dev/docs/test-fixtures).
      - Create a fixture Python file under the following folder: "src/fixtures/" (create folder if not present)

<Deliverable>
- Create 2 "page.py" files for screens: "Home Page" and "SignIn Page" under the path "src/pages/" (create folder if not present).
- Create one new test file to store all Login scenarios.
- Implement changes directly on the current folders and files we have in root folder. Keep in mind framework structure.