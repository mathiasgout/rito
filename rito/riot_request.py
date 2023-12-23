from rito.errors import RiotAPIError

import time
import logging
from typing import Union

import requests


logger = logging.getLogger(__name__)


class RiotRequest:
    def __init__(self, riot_api_key: str, timeout: int = 300, tries_max: int = 5) -> None:
        self.riot_api_key = riot_api_key
        self.timeout = timeout
        self.tries_max = tries_max

    def make_request(self, endpoint: str, params: dict = {}, _tries: int = 0, _waited: int = 0) -> Union[None, dict]:
        r_get = requests.get(endpoint, params=params, headers={"X-Riot-Token": self.riot_api_key})

        if r_get.ok:
            logger.info(f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code})")
            return r_get.json()

        elif r_get.status_code == 404:
            logger.info(f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code})")
            return None

        elif (r_get.status_code == 429) or (r_get.status_code >= 500):
            retry_after = self._get_retry_after_value_from_headers(r_get.headers)

            if (_tries < self.tries_max) and (_waited < self.timeout):
                if _waited + retry_after >= self.timeout:
                    retry_after = self.timeout - _waited

                # Wait before a retry
                logger.info(f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code}) (retry in {retry_after} seconds)")
                self._wait_before_try(seconds=retry_after)

                # Redo the request
                return self.make_request(
                    endpoint=endpoint,
                    params=params,
                    _tries=_tries + 1,
                    _waited=_waited + retry_after,
                )

            raise RiotAPIError(f"{r_get.url} (code={r_get.status_code}) (retried={_tries}) (waited={_waited})")

        else:
            raise RiotAPIError(f"{r_get.url} (code={r_get.status_code}) (retried=0) (waited=0)")

    @staticmethod
    def _get_retry_after_value_from_headers(headers: dict) -> int:
        if "Retry-After" in headers:
            try:
                return int(headers["Retry-After"])
            except Exception:
                pass

        return 5

    @staticmethod
    def _wait_before_try(seconds: int) -> None:
        if seconds > 0:
            time.sleep(seconds)
