from rito.models import base_model

def test_model__repr__():
    model = base_model.Model()
    assert model.__repr__() == "Model()"
