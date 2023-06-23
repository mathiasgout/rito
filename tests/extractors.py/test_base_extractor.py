from rito.extractors import base_extractor


def test_baseextractor():
    assert base_extractor.BaseExtractor.__abstractmethods__
    assert base_extractor.BaseExtractor.extract.__isabstractmethod__ is True
