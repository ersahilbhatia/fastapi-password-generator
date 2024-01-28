from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import string
import secrets

app = FastAPI()

class PasswordRequest(BaseModel):
    length: int
    include_uppercase: Optional[bool] = False
    include_digits: Optional[bool] = False
    include_special_chars: Optional[bool] = False

def generate_password(request: PasswordRequest):
    characters = string.ascii_lowercase
    if request.include_uppercase:
        characters += string.ascii_uppercase
    if request.include_digits:
        characters += string.digits
    if request.include_special_chars:
        characters += string.punctuation

    try:
        password = ''.join(secrets.choice(characters) for _ in range(request.length))
        return {"password": password}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid password length or criteria")

@app.post("/generate-password")
def generate_password_endpoint(request: PasswordRequest):
    print(request)
    return generate_password(request)
