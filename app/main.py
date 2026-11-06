
from fastapi import FastAPI
from pydantic import BaseModel
from app.accounts import create_account, get_all_accounts

app = FastAPI(
    title="PayCore API",
    description="Payment Transaction Processing System",
    version="1.0.0"
)


class AccountRequest(BaseModel):
    name: str
    email: str


@app.get("/")
def home():
    return {
        "message": "Welcome to PayCore API!",
        "status": "running"
    }


@app.post("/accounts")
def register_account(data: AccountRequest):
    return create_account(data.name, data.email)


@app.get("/accounts")
def list_accounts():
    return get_all_accounts()
