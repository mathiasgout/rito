class RiotAPIError404(Exception):
    pass


class RiotAPIError429(Exception):
    pass


class RiotAPIError5xx(Exception):
    pass


class RiotAPIErrorUnknown(Exception):
    pass


class ExtractorError(Exception):
    pass
