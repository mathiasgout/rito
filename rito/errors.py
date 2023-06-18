class RiotAPIError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ExtractorError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
