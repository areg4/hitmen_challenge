import requests
import requests_mock
from django.shortcuts import reverse


URL_LOGIN = 'http://localhost:8080'+ reverse('token_obtain_pair')


def test_login(mocker, mock_login_response, mock_body_login):
    mocker.patch(
        'services.login.get_token',
        return_value=mock_login_response
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_LOGIN, json=mock_login_response)
        response = requests.post(URL_LOGIN, data=mock_body_login)
        
    response_json = response.json()
    assert response_json['status'] is 200
    assert response_json['data'] is not None
    assert response_json['success'] is True
    
    
def test_login_fail(mocker, mock_login_fail_response, mock_body_login_fail):
    mocker.patch(
        'services.login.get_token',
        return_value = mock_login_fail_response
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_LOGIN, json=mock_login_fail_response)
        response = requests.post(URL_LOGIN, data=mock_body_login_fail)
        
    response_json = response.json()
    assert response_json['status'] == 400
    assert 'data' not in response_json
    assert response_json['success'] is False
    
    