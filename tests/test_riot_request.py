from rito import riot_request
from rito import errors

import time

import pytest


def test_riotrequest_get_retry_after_value_from_headers_GOOD():
    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key")
    retry_after = riot_r._get_retry_after_value_from_headers(
        headers={"Retry-After": 56}
    )
    assert retry_after == 56


def test_riotrequest_get_retry_after_value_from_headers_ERROR():
    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key")
    retry_after = riot_r._get_retry_after_value_from_headers(
        headers={"Retry-After": "lol"}
    )
    assert retry_after == 10


def test_riotrequest_get_retry_after_value_from_headers_NO_RETRY_AFTER():
    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key")
    retry_after = riot_r._get_retry_after_value_from_headers(headers={})
    assert retry_after == 10


def test_riotrequest_wait_before_try(mocker):
    mocker.patch("time.sleep")

    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key")
    riot_r._wait_before_try(10)

    time.sleep.assert_called_once_with(10)


def test_riotrequest_make_request_GET_2OO(requests_mock):
    # Mocks
    mocked_request = requests_mock.get(
        "https://domain.com?key=value", status_code=200, json={"lol": "xd"}
    )

    # Calls
    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key")
    return_value = riot_r.make_request("https://domain.com", params={"key": "value"})

    # Verifs
    assert return_value == {"lol": "xd"}
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"


def test_riotrequest_make_request_GET_404(requests_mock):
    # Mocks
    mocked_request = requests_mock.get("https://domain.com?key=value", status_code=404)

    # Calls
    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key")
    return_value = riot_r.make_request("https://domain.com", params={"key": "value"})

    # Verifs
    assert return_value is None
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
    mocker.patch("rito.riot_request.RiotRequest._wait_before_try")

    # Calls
    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key")
    return_value = riot_r.make_request("https://domain.com", params={"key": "value"})

    # Verifs
    assert return_value == {"lol": "xd"}
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"
    riot_request.RiotRequest._wait_before_try.assert_called_once_with(seconds=20)


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
    mocker.patch("rito.riot_request.RiotRequest._wait_before_try")

    # Calls
    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key")
    return_value = riot_r.make_request("https://domain.com", params={"key": "value"})

    # Verifs
    assert return_value == {"lol": "xd"}
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"
    riot_request.RiotRequest._wait_before_try.assert_called_once_with(seconds=5)


def test_riotrequest_make_request_GET_500_ERROR(requests_mock, mocker):
    # Mocks
    mocked_request = requests_mock.register_uri(
        "GET",
        "https://domain.com?key=value",
        [{"status_code": 500}, {"status_code": 500}],
    )
    mocker.patch("rito.riot_request.RiotRequest._wait_before_try")

    # Calls
    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key", tries_5xx=1)

    # Verifs
    with pytest.raises(errors.RiotAPIError):
        riot_r.make_request("https://domain.com", params={"key": "value"})
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"
    riot_request.RiotRequest._wait_before_try.assert_called_once_with(seconds=5)


def test_riotrequest_make_request_GET_401(requests_mock, mocker):
    # Mocks
    mocked_request = requests_mock.get("https://domain.com?key=value", status_code=401)

    # Calls
    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key", tries_5xx=1)

    # Verifs
    with pytest.raises(errors.RiotAPIError):
        riot_r.make_request("https://domain.com", params={"key": "value"})
    assert mocked_request.last_request.headers["X-Riot-Token"] == "riot_api_key"
