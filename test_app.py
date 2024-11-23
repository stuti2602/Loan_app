import pytest
import json
import warnings
warnings.filterwarnings("ignore")

from app import app ,ping # import app variable from app.py

@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):
    resp = client.get("/ping")
    # assert is a keyword and it will let you test if the condition in your code is true and if not it will give assertion error.
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Hi there, I'm working with the new API!!"}


def test_prediction(client):
    test_data = {
        "Gender" : "Female",
        "Married" : "Married",
        "ApplicantIncome" : 500000,
        "Credit_History" :"Cleard Debts",
        "LoanAmount" : 500
    }

    resp = client.post("/predict", json=test_data)
    assert resp.status_code == 200
    assert resp.get_json() == {"loan_approval_status":"Approved"}



