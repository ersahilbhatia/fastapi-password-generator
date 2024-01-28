# FastAPI Password Generator
Rest API using FastAPI that allows users to request new passwords based on specified criteria.

## Setup Project

**1. Install Dependencies:**

Clone the project and create a python virtual environment. Use the following command to create and activate virtual environment.

**On Windows**

`python -m venv venv`

`venv\Scripts\activate`

**On macOS or Linux**

`python3 -m venv venv`

`source venv/bin/activate`

 Ensure that you have Python 3.7 or later installed. Install the required dependencies specified in the requirements.txt file using the following command:

`pip install -r requirements.txt`

**2. Run the Application:**

Run the FastAPI application using Uvicorn. Open a terminal and navigate to the directory containing your code (main.py). Execute the following command:

`uvicorn main:app --reload`

**3. Access the API:**

Open Postman tool to access API endpoint http://127.0.0.1:8000/generate-password which is described in the next section.

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
