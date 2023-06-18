from rito.errors import RiotAPIError

import time
import logging
from typing import Union

import requests


logger = logging.getLogger(__name__)


class RiotRequest:
    def __init__(self, riot_api_key: str, tries_5xx: int = 5) -> None:
        self.tries_5xx = tries_5xx
        self.riot_api_key = riot_api_key

    def make_request(
        self, endpoint: str, params: dict = {}, _trie_5xx: int = 0
    ) -> Union[None, dict]:
        r_get = requests.get(
            endpoint, params=params, headers={"X-Riot-Token": self.riot_api_key}
        )

        if r_get.ok:
            logger.info(f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code})")
            return r_get.json()

        elif r_get.status_code == 404:
            logger.info(f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code})")
            return None

        elif r_get.status_code == 429:
            # Wait before a retry
            retry_after = self._get_retry_after_value_from_headers(r_get.headers)
            logger.info(
                f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code}) (retry in {retry_after} seconds)"
            )
            self._wait_before_try(seconds=retry_after)

            # Redo the request
            return self.make_request(endpoint=endpoint, params=params)

        elif r_get.status_code >= 500:
            if _trie_5xx < self.tries_5xx:
                # Wait before a retry
                logger.info(
                    f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code}) (retry in 5 seconds)"
                )
                self._wait_before_try(seconds=5)

                # Redo the request
                return self.make_request(
                    endpoint=endpoint, params=params, _trie_5xx=_trie_5xx + 1
                )

            raise RiotAPIError(
                f"{r_get.url} (code={r_get.status_code}) (retried={_trie_5xx})"
            )

        else:
            raise RiotAPIError(f"{r_get.url} (code={r_get.status_code}) (retried=0)")

    @staticmethod
    def _get_retry_after_value_from_headers(headers: dict) -> int:
        if "Retry-After" in headers:
            try:
                return int(headers["Retry-After"])
            except Exception:
                pass

        return 10

    @staticmethod
    def _wait_before_try(seconds: int) -> None:
        if seconds > 0:
            time.sleep(seconds)
