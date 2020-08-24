# ICCodeChallenge

iCompaas Coding Challenge

Problem: Create a simple API in flask framework
Functionality: API that takes POST JSON payload
Result: The API should return if the payload input has any characters that could be used to do SQL injection

Created template with form for testing. Also works with POST JSON requests to url '/v1/sanitized/input'. 

Wrote simple JSON tests in pytest.

To run(windows):
```
set FLASK_APP = api
set FLASK_ENV = development
flask run
```
Navigate to 'localhost:5000/v1/santized/input'

Testing
```
python3 -m pytest tests
```
