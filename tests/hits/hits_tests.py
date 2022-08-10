import requests
import requests_mock
from django.shortcuts import reverse

URL_CREATE_HIT = 'http://localhost:8080'+ reverse('register_hit')
URL_HITS = 'http://localhost:8080'+ reverse('list_hits')
URL_HIT_DETAIL = 'http://localhost:8080'+ reverse('hit_detail', kwargs={'hit_id':21})


def test_create_hit(mocker, mock_create_hit, mock_create_hit_body):
    mocker.patch(
        'services.hits.hitsService.create_hit',
        return_value=mock_create_hit
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_CREATE_HIT, json=mock_create_hit)
        response = requests.post(URL_CREATE_HIT, data=mock_create_hit_body)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 201
    assert response_json['data'] is not None
    
    
def test_create_hit_fail(mocker, mock_create_hit_fail, mock_create_hit_body):
    mocker.patch(
        'services.hits.hitsService.create_hit',
        return_value=mock_create_hit_fail
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_CREATE_HIT, json=mock_create_hit_fail)
        response = requests.post(URL_CREATE_HIT, data=mock_create_hit_body)
        
    response_json = response.json()
    assert response_json['success'] is False
    assert response_json['status'] == 400


def test_list_hits(mocker, mock_list_hits):
    mocker.patch(
        'services.hits.hitsService.list_hits',
        return_value=mock_list_hits
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_HITS, json=mock_list_hits)
        response = requests.post(URL_HITS)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 200
    assert response_json['data'] is not None


def test_hit_detail(mocker, mock_hit_detail):
    mocker.patch(
        'services.hits.hitsService.get_hit_detail',
        return_value=mock_hit_detail
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_HIT_DETAIL, json=mock_hit_detail)
        response = requests.post(URL_HIT_DETAIL)
        
    response_json = response.json()
    assert response_json['success'] is True
    assert response_json['status'] == 200
    assert response_json['data'] is not None
    
    
def test_hit_detail_not_found(mocker, mock_hit_not_found):
    mocker.patch(
        'services.hits.hitsService.get_hit_detail',
        return_value=mock_hit_not_found
    )
    
    with requests_mock.Mocker() as m:
        m.post(URL_HIT_DETAIL, json=mock_hit_not_found)
        response = requests.post(URL_HIT_DETAIL)
        
    response_json = response.json()
    assert response_json['success'] is False
    assert response_json['status'] == 404
