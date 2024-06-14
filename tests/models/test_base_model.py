from rito.models import base_model


def test_model_format_attribute_name():
    model = base_model.Model()
    assert model._format_attribute_name("jeSuisProut") == "je_suis_prout"


def test_model_format_attribute_name_UPPER_1ST():
    model = base_model.Model()
    assert model._format_attribute_name("JeSuisProut") == "je_suis_prout"


def test_model_format_attribute_name_CC():
    model = base_model.Model()
    assert model._format_attribute_name("jeSuisCCProut") == "je_suis_cc_prout"


def test_model__repr__():
    model = base_model.Model()
    assert model.__repr__() == "Model()"
