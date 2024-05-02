import pytest1
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_sign_up():
    # Test valid sign-up data
    sign_up_data = {"name": "John Doe", "username": "johndoe", "email": "johndoe@example.com", "password": "password123"}
    response = client.post("/signup", json=sign_up_data)
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}

    # Test sign-up with existing username
    response = client.post("/signup", json=sign_up_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Username already exists"}

    # Test sign-up with existing email
    sign_up_data["username"] = "anotherusername"
    response = client.post("/signup", json=sign_up_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already exists"}

def test_login():
    # Test valid login
    login_data = {"username": "johndoe", "password": "password123"}
    response = client.post("/login", json=login_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}

    # Test login with invalid password
    login_data["password"] = "wrongpassword"
    response = client.post("/login", json=login_data)
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect password"}

    # Test login with non-existent user
    login_data["username"] = "nonexistentuser"
    response = client.post("/login", json=login_data)
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

if __name__ == "__main__":
    pytest.main()
