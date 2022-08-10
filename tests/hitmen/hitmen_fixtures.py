import pytest


@pytest.fixture
def mock_list_hitmen_response():
    data = {
        "status": 200,
        "success": True,
        "msg": "List of Hitmen",
        "data": [
            {
            "id": 2,
            "name": "Juan Weed",
            "email": "juan@assassin.com",
            "password": "123456",
            "desc": "El mejor Manager",
            "isActive": "Active",
            "isManager": True,
            "managedBy": None,
            "isBoss": False
            },
            {
            "id": 3,
            "name": "Ezio Auditore",
            "email": "ezio@assassin.com",
            "password": "123456",
            "desc": "El mejor Maestro",
            "isActive": "Active",
            "isManager": True,
            "managedBy": None,
            "isBoss": False
            },
            {
            "id": 4,
            "name": "Jaimito",
            "email": "jaimito@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 1,
            "isBoss": False
            },
            {
            "id": 5,
            "name": "Luis",
            "email": "luis@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 1,
            "isBoss": False
            },
            {
            "id": 6,
            "name": "Pepe",
            "email": "pepe@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 1,
            "isBoss": False
            },
            {
            "id": 7,
            "name": "Antoni",
            "email": "ant@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 2,
            "isBoss": False
            },
            {
            "id": 8,
            "name": "Tete",
            "email": "tete@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 2,
            "isBoss": False
            },
            {
            "id": 9,
            "name": "JK",
            "email": "jk@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 2,
            "isBoss": False
            },
            {
            "id": 10,
            "name": "El Triple",
            "email": "triple@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 3,
            "isBoss": False
            },
            {
            "id": 11,
            "name": "Gemelo",
            "email": "gemelo@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 3,
            "isBoss": False
            },
            {
            "id": 12,
            "name": "Ruso",
            "email": "ruso@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 3,
            "isBoss": False
            },
            {
            "id": 13,
            "name": "Ruso II",
            "email": "ruso2@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 3,
            "isBoss": False
            },
            {
            "id": 14,
            "name": "Ruso Papi",
            "email": "rusopapi@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": True,
            "managedBy": None,
            "isBoss": False
            },
            {
            "id": 1,
            "name": "Gerardo GG",
            "email": "gera@assassin.com",
            "password": "123456",
            "desc": "El mejor asesino",
            "isActive": "Active",
            "isManager": False,
            "managedBy": None,
            "isBoss": True
            }
        ]
        }
    return data


@pytest.fixture
def mock_hitman_response():
    data = {
        "status": 200,
        "success": True,
        "msg": "Hitman detail",
        "data": {
            "id": 6,
            "name": "Pepe",
            "email": "pepe@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "isActive": "Active",
            "isManager": False,
            "managedBy": 1,
            "isBoss": False
        }
    }
    
    return data


@pytest.fixture
def mock_hitman_response_fail():
    data = {
        "status": 404,
        "success": False,
        "msg": "Hitman not found"
    }
    return data


@pytest.fixture
def mock_hitman_registered():
    data = {
        "status": 201,
        "success": True,
        "msg": "Hitman registered!",
        "data": {
            "name": "Rusoooo",
            "email": "rusooo@assassin.com",
            "password": "123456",
            "desc": "El mejor alumno",
            "managedBy": 3
        }
    }
    return data


@pytest.fixture
def mock_register_body():
    data = {
        "name": "Rusoooo",
        "email": "rusooo@assassin.com",
        "desc": "El mejor alumno",
        "managedBy": 3,
        "password": "123456"
    }
    return data


@pytest.fixture
def mock_hitman_registered_fail():
    data = {
        "status": 400,
        "success": False,
        "msg": "Error al dar de alta un Hitman",
        "data": {
            "email": [
            "Ya existe un/a Hitmen con este/a email."
            ],
            "password": [
            "Este campo es requerido."
            ]
        }
    }
    return data
