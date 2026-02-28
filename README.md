This is a Pytest Framework created for ReqRes API for all endpoints.
It contains happy path cases for every endpoint.

For this framework you will need

    PYTHON VERSION >= 3.9.6

Follow the below steps to execute the framework:

1. Create .env file with below contents:

    BASE_URI = https://reqres.in

    X_API_KEY=<HERE YOU NEED TO ADD YOUR OWN API KEY GENERATED FROM REQRES WEBSITE>

    API_AUTH_HEADER=x-api-key

    TIMEOUT=30

2. Install the requirements.txt with below commands:

    pip install -r requirements.txt

3. To run the tests, make sure the terminal is pointing to root directory:

    pytest

4. To generate allure reports for the framework, execute the commands in the below order:

    brew install allure -> converts those raw files into the actual HTML dashboard
    pytest
    allure serve reports/allure-results -> This opens a live dashboard in your browser automatically.

** One thing to note — results accumulate across runs. If you want a fresh report each time, clear the folder before running. Always delete the content under the reports/allure-reports before running pytest and allure secure command to get fresh reports. **

