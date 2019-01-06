import json
from flask import url_for
from seppuku.api import SeppukuMessage


def test_seppuku_message_api_post_value_responds_with_key_and_expire_none_and_status_200(client):
    response = client.post(url_for(SeppukuMessage.endpoint), data={'value': 'pytest'})
    assert 200 == response.status_code
    data = json.loads(response.data)
    assert sorted(['key', 'expire']) == sorted(list(data))
    assert data['expire'] is None


def test_seppuku_message_api_post_value_and_valid_expire_responds_with_key_and_expire_and_status_200(client):
    response = client.post(url_for(SeppukuMessage.endpoint), data={'value': 'pytest', 'expire': 600})
    assert 200 == response.status_code
    data = json.loads(response.data)
    assert sorted(['key', 'expire']) == sorted(list(data))
    assert 600 == data['expire']


def test_seppuku_message_api_post_with_no_args_responds_status_400(client):
    response = client.post(url_for(SeppukuMessage.endpoint), data={})
    assert 400 == response.status_code


def test_seppuku_message_api_get_key_after_post_responds_with_value_and_status_200(client):
    post_response = client.post(url_for(SeppukuMessage.endpoint), data={'value': 'pytest'})
    post_data = json.loads(post_response.data)
    get_response = client.get(url_for(SeppukuMessage.endpoint), data={'key': post_data['key']})
    assert 200 == get_response.status_code
    get_data = json.loads(get_response.data)
    # Value and only value
    assert 'value' in get_data
    assert 1 == len(get_data)


def test_seppuku_message_api_get_with_no_args_responds_status_400(client):
    response = client.get(url_for(SeppukuMessage.endpoint), data={})
    assert 400 == response.status_code


def test_seppuku_message_api_get_non_existing_key_responds_status_400(client):
    response = client.get(url_for(SeppukuMessage.endpoint), data={'key': 'pytest'})
    assert 400 == response.status_code