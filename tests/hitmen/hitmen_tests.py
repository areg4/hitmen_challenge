import requests
import requests_mock
from django.shortcuts import reverse

URL_REGISTER = 'http://localhost:8080'+ reverse('register_hitman')
URL_HITMEN = 'http://localhost:8080'+ reverse('list_hitmen')
URL_HITMEN_DETAIL = 'http://localhost:8080'+ reverse('detail_hitman', kwargs={'hitman_id':6})


def test_register_hitman(mocker, mock_hitman_registered, mock_register_body):
    mocker.patch(
        'services.hitmen.hitmenService.create_hitman',
        return_value=mock_hitman_registered
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_REGISTER, json=mock_hitman_registered)
        response = requests.post(URL_REGISTER, data=mock_register_body)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 201
    assert response_json['data'] is not None


def test_fail_register_hitman(mocker, mock_hitman_registered_fail, mock_register_body):
    mocker.patch(
        'services.hitmen.hitmenService.create_hitman',
        return_value=mock_hitman_registered_fail
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_REGISTER, json=mock_hitman_registered_fail)
        response = requests.post(URL_REGISTER, data=mock_register_body)
        
    response_json = response.json()
    assert response_json['success'] is False
    assert response_json['status'] == 400


def test_list_hitmen(mocker, mock_list_hitmen_response):
    mocker.patch(
        'services.hitmen.hitmenService.get_list_hitmen',
        return_value=mock_list_hitmen_response
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_HITMEN, json=mock_list_hitmen_response)
        response = requests.get(URL_HITMEN)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 200
    assert response_json['data'] is not None
    
    
def test_hitman_detail(mocker, mock_hitman_response):
    mocker.patch(
        'services.hitmen.hitmenService.get_hitman_detail',
        return_value=mock_hitman_response
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_HITMEN_DETAIL, json=mock_hitman_response)
        response = requests.get(URL_HITMEN_DETAIL)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 200
    assert response_json['data'] is not None
    
    
def test_hitman_detail_not_found(mocker, mock_hitman_response_fail):
    mocker.patch(
        'services.hitmen.hitmenService.get_hitman_detail',
        return_value=mock_hitman_response_fail
    )
    
    with requests_mock.Mocker() as m:
        m.get(URL_HITMEN_DETAIL, json=mock_hitman_response_fail)
        response = requests.get(URL_HITMEN_DETAIL)
        
    response_json = response.json()
    assert response_json['success'] is False
    assert response_json['status'] == 404

