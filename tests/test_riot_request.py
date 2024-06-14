from rito import riot_request
from rito import errors

import time
from unittest.mock import call

import pytest


def test_riotrequest_make_request_GET_2OO(requests_mock):
    # Mocks
    mocked_request = requests_mock.get("https://domain.com?key=value", status_code=200, json={"lol": "xd"})

    # Calls
    riot_r = riot_request.RiotRequest(
        riot_api_key="riot_api_key", 
        return_none_on_404=True, 
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = riot_r.make_request("https://domain.com", params={"key": "value"})

    # Verifs
    assert return_value == {"lol": "xd"}
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"


def test_riotrequest_make_request_GET_404(requests_mock):
    # Mocks
    mocked_request = requests_mock.get("https://domain.com?key=value", status_code=404)

    # Calls
    riot_r = riot_request.RiotRequest(
        riot_api_key="riot_api_key", 
        return_none_on_404=True, 
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = riot_r.make_request("https://domain.com", params={"key": "value"})

    # Verifs
    assert return_value is None
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"


def test_riotrequest_make_request_GET_404_ERROR(requests_mock):
    # Mocks
    mocked_request = requests_mock.get("https://domain.com?key=value", status_code=404)

    # Calls
    riot_r = riot_request.RiotRequest(
        riot_api_key="riot_api_key", 
        return_none_on_404=False, 
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )

    # Verif
    with pytest.raises(errors.RiotAPIError404):
        riot_r.make_request("https://domain.com", params={"key": "value"})
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"


def test_riotrequest_make_request_GET_429(requests_mock, mocker):
    # Mocks
    mocked_request = requests_mock.register_uri(
        "GET",
        "https://domain.com?key=value",
        [
            {"status_code": 429, "headers": {"Retry-After": "20"}},
            {"status_code": 200, "json": {"lol": "xd"}},
        ],
    )
    mocker.patch("time.sleep")

    # Calls
    riot_r = riot_request.RiotRequest(
        riot_api_key="riot_api_key", 
        return_none_on_404=True, 
        retry_on_rate_limit=True,
        timeout_on_servor_error=10
    )
    return_value = riot_r.make_request("https://domain.com", params={"key": "value"})

    # Verifs
    assert return_value == {"lol": "xd"}
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"
    time.sleep.assert_called_once_with(20)


def test_riotrequest_make_request_GET_429_ERROR(requests_mock, mocker):
    # Mocks
    mocked_request = requests_mock.register_uri(
        "GET",
        "https://domain.com?key=value",
        [
            {"status_code": 429, "headers": {"Retry-After": "20"}},
        ],
    )
    mocker.patch("time.sleep")

    # Calls
    riot_r = riot_request.RiotRequest(
        riot_api_key="riot_api_key", 
        return_none_on_404=True, 
        retry_on_rate_limit=False,
        timeout_on_servor_error=10
    )

    # Verifs
    with pytest.raises(errors.RiotAPIError429):
        riot_r.make_request("https://domain.com", params={"key": "value"})
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"


def test_riotrequest_make_request_GET_500(requests_mock, mocker):
    # Mocks
    mocked_request = requests_mock.register_uri(
        "GET",
        "https://domain.com?key=value",
        [
            {"status_code": 500},
            {"status_code": 200, "json": {"lol": "xd"}},
        ],
    )
    mocker.patch("time.sleep")

    # Calls
    riot_r = riot_request.RiotRequest(
        riot_api_key="riot_api_key", 
        return_none_on_404=True, 
        retry_on_rate_limit=True,
        timeout_on_servor_error=12
    )
    return_value = riot_r.make_request("https://domain.com", params={"key": "value"})

    # Verifs
    assert return_value == {"lol": "xd"}
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"
    time.sleep.assert_called_once_with(10)


def test_riotrequest_make_request_GET_500_TIMEOUT(requests_mock, mocker):
    # Mocks
    mocked_request = requests_mock.register_uri(
        "GET",
        "https://domain.com?key=value",
        [
            {"status_code": 500},
            {"status_code": 500},
        ],
    )
    mocker.patch("time.sleep")

    # Calls
    riot_r = riot_request.RiotRequest(
        riot_api_key="riot_api_key", 
        return_none_on_404=True, 
        retry_on_rate_limit=False,
        timeout_on_servor_error=12
    )

    # Verifs
    with pytest.raises(errors.RiotAPIError5xx):
        riot_r.make_request("https://domain.com", params={"key": "value"})
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"
    time.sleep.assert_has_calls([call(10), call(2)])


def test_riotrequest_make_request_GET_500_ERROR(requests_mock):
    # Mocks
    mocked_request = requests_mock.register_uri(
        "GET",
        "https://domain.com?key=value",
        [
            {"status_code": 500},
        ],
    )

    # Calls
    riot_r = riot_request.RiotRequest(
        riot_api_key="riot_api_key", 
        return_none_on_404=True, 
        retry_on_rate_limit=True,
        timeout_on_servor_error=0
    )

    # Verifs
    with pytest.raises(errors.RiotAPIError5xx):
        riot_r.make_request("https://domain.com", params={"key": "value"})
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"


def test_riotrequest_make_request_GET_401(requests_mock):
    # Mocks
    mocked_request = requests_mock.get("https://domain.com?key=value", status_code=401)

    # Calls
    riot_r = riot_request.RiotRequest(
        riot_api_key="riot_api_key", 
        return_none_on_404=True, 
        retry_on_rate_limit=True,
        timeout_on_servor_error=12
    )

    # Verifs
    with pytest.raises(errors.RiotAPIErrorUnknown):
        riot_r.make_request("https://domain.com", params={"key": "value"})
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"


def test_get_retry_after_value_from_headers_GOOD():
    assert riot_request._get_retry_after_value_from_headers(headers={"Retry-After": "10"}) == 10


def test_get_retry_after_value_from_headers_EXCEPTION():
    assert riot_request._get_retry_after_value_from_headers(headers={"Retry-After": "l"}) == 5
