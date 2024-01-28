# FastAPI Password Generator
Rest API using FastAPI that allows users to request new passwords based on specified criteria.

1. Install Dependencies:
Ensure that you have Python 3.7 or later installed. Install the required dependencies specified in the requirements.txt file using the following command:

`pip install -r requirements.txt`

2. Run the Application:
Run the FastAPI application using Uvicorn. Open a terminal and navigate to the directory containing your code (main.py). Execute the following command:

`uvicorn main:app --reload`

3. Access the API:
Open your web browser or a tool like httpie or curl and navigate to http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc to explore and test the API interactively. You can also make requests programmatically.

# API Endpoint
## Generate Password

- Endpoint: /generate-password

- Method: POST

- Request Payload:
  - **length** (integer): Length of the password to be generated.
  - **include_uppercase** (optional boolean, default False): Include uppercase letters.
  - **include_digits** (optional boolean, default False): Include digits.
  - **include_special_chars** (optional boolean, default False): Include special characters.

- Sample Request:
  
  `
  {
  "length": 12,
  "include_uppercase": True,
  "include_digits": True,
  "include_special_chars": False
}
`

- Sample Response:

`
{
  "password": "aB3dE!gH1iJ"
}
`

# Testing
To run the provided unit tests, make sure you have pytest installed:

`pip install pytest`

Run the tests with:

`pytest test/test_main.py`
