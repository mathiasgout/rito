from rito import riot_request


def test_riotrequest_get_retry_after_value_from_headers():
    riot_r = riot_request.RiotRequest(riot_api_key="riot_api_key")
    retry_after = riot_r._get_retry_after_value_from_headers(
        headers={"Retry-After": 10}
    )
    assert retry_after == 10
