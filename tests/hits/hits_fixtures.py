import pytest


@pytest.fixture
def mock_list_hits():
    data = {
        "status": 200,
        "success": True,
        "msg": "List of Hits",
        "data": [
            {
            "id": 19,
            "assignee": 3,
            "desc": "Urgente",
            "target": "Lic",
            "status": "ASSIGNED",
            "created_by": 1
            },
            {
            "id": 20,
            "assignee": 3,
            "desc": "Urgente",
            "target": "Lic",
            "status": "ASSIGNED",
            "created_by": 1
            },
            {
            "id": 21,
            "assignee": 10,
            "desc": "Urgente",
            "target": "Lic",
            "status": "ASSIGNED",
            "created_by": 3
            },
            {
            "id": 22,
            "assignee": 10,
            "desc": "string",
            "target": "string",
            "status": "ASSIGNED",
            "created_by": 3
            }
        ]
    }
    
    return data


@pytest.fixture
def mock_hit_detail():
    data = {
        "status": 200,
        "success": True,
        "msg": "Hit details",
        "data": {
            "id": 21,
            "assignee": 10,
            "desc": "Urgente",
            "target": "Lic",
            "status": "ASSIGNED",
            "created_by": 3
        }
    }
    return data


@pytest.fixture
def mock_hit_not_found():
    data = {
        "status": 404,
        "success": False,
        "msg": "Hit not found"
    }
    
    return data


@pytest.fixture
def mock_create_hit_fail():
    data = {
        "status": 400,
        "success": False,
        "msg": "Error al crear un Hit",
        "data": {
            "assignee": [
            "No puede asignar a este Hitman"
            ]
        }
    }
    
    return data


@pytest.fixture
def mock_create_hit():
    data = {
        "status": 201,
        "success": True,
        "msg": "Hit created!",
        "data": {
            "assignee": 10,
            "desc": "Urgente",
            "target": "Lic",
            "status": "ASSIGNED",
            "created_by": 3
        }
    }
    return data


@pytest.fixture
def mock_create_hit_body():
    data = {
        "assignee": 10,
        "desc": "Urgente",
        "target": "Lic",
        "status": "ASSIGNED",
        "created_by": 1
    }
    return data
