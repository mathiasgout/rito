from rito.errors import RiotAPIError404, RiotAPIError429, RiotAPIError5xx, RiotAPIErrorUnknown

import time
import logging
from typing import Optional

import requests


logger = logging.getLogger(__name__)


class RiotRequest:
    def __init__(
        self, 
        riot_api_key: str, 
        return_none_on_404: bool,
        retry_on_rate_limit: bool, 
        timeout_on_servor_error: int
    ) -> None:
        self.riot_api_key = riot_api_key
        self.return_none_on_404 = return_none_on_404
        self.retry_on_rate_limit = retry_on_rate_limit
        self.timeout_on_servor_error = timeout_on_servor_error

    def make_request(self, endpoint: str, params: dict = {}, _waited: int = 0) -> Optional[dict]:
        r_get = requests.get(endpoint, params=params, headers={"X-Riot-Token": self.riot_api_key})

        if r_get.ok:
            logger.info(f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code})")
            return r_get.json()

        elif r_get.status_code == 404:
            logger.info(f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code})")
            if self.return_none_on_404:
                return None
            raise RiotAPIError404(f"{r_get.url} (code={r_get.status_code}) (retried=0) (waited=0)")

        elif r_get.status_code == 429:
            if self.retry_on_rate_limit:
                retry_after = _get_retry_after_value_from_headers(r_get.headers)

                # Wait before a retry
                logger.info(f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code}) (retry in {retry_after} seconds)")
                time.sleep(retry_after)
                return self.make_request(endpoint=endpoint, params=params)
            
            raise RiotAPIError429(f"{r_get.url} (code={r_get.status_code}) (retried=0) (waited=0)")

        elif r_get.status_code >= 500:
            if self.timeout_on_servor_error > 0:
                retry_after = 10
                if _waited < self.timeout_on_servor_error:
                    if _waited + retry_after >= self.timeout_on_servor_error:
                        retry_after = self.timeout_on_servor_error - _waited
        
                    # Wait before a retry
                    logger.info(f"[HTTP GET Riot API] {r_get.url} (code={r_get.status_code}) (retry in {retry_after} seconds)")
                    time.sleep(retry_after)
                    return self.make_request(endpoint=endpoint, params=params, _waited=_waited + retry_after)

                raise RiotAPIError5xx(f"{r_get.url} (code={r_get.status_code}) (waited={_waited})")
            
            raise RiotAPIError5xx(f"{r_get.url} (code={r_get.status_code}) (waited=0)")

        else:
            raise RiotAPIErrorUnknown(f"{r_get.url} (code={r_get.status_code}) (waited=0)")
        

def _get_retry_after_value_from_headers(headers: dict) -> int:
    if "Retry-After" in headers:
        try:
            return int(headers["Retry-After"])
        except Exception:
            pass

    return 5
