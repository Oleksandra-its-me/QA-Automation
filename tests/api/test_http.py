import pytest
import requests
import json
import sys


@pytest.mark.http
def test_first_requests():
    r = requests.get('https://api.github.com/zen')
    print(r.text)

@pytest.mark.http
def test_addition_to_second_request():
    r = requests.get('http://api.github.com/users/defunkt')
    # Ensure the output uses UTF-8 encoding
    sys.stdout.reconfigure(encoding='utf-8')
    print(f"Response Body is {json.dumps(r.json(), ensure_ascii=False)}")

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    # print(f"Response is {r.text}")
    # print(f"Response Body is {r.json()}")
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    # print(f"Response Status code is {r.status_code}")
    assert r.status_code == 200
    # print(f"Response Headers are {r.headers}")
    assert headers['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/oleksandra_ponomarova')
    
    assert r.status_code == 404
