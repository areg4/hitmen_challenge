import pytest


@pytest.fixture
def mock_login_response():
    data = {
        "status": 200,
        "success": True,
        "msg": "Login!",
        "data": {
            "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYwMTU5MzEwLCJpYXQiOjE2NjAxNTkwMTAsImp0aSI6IjQ2ZTU5YjQ5MTk5NzQ0NjA4ZWEzOWM4NThmYjVhZTkxIiwidXNlcl9pZCI6MX0.ph7VLHhhQ6oEtyQ0IVIH8KxK5s4O8O2v26aIMKizqT8"
        }
    }
    return data


@pytest.fixture
def mock_login_fail_response():
    data = {
        "status": 400,
        "success": False,
        "msg": "Error de autenticación"
    }
    return data


@pytest.fixture
def mock_body_login():
    data = {
        "email": "gera@assassin.com",
        "password": "123456"
    }
    return data


@pytest.fixture
def mock_body_login_fail():
    data = {
        "email": "ge@assassin.com",
        "password": "1234"
    }
    return data