import pytest
from scrapper import Json_Builder

@pytest.fixture(scope="module")
def json_builder():
    return Json_Builder("https://supermercado.eroski.es/es/supermercado/2059698-frescos/2059746-carnes-y-aves/")

def test_json_builder_resultado_type(json_builder):
    assert isinstance(json_builder.resultado, dict)

def test_json_builder_item_structure(json_builder):
    for _, item in json_builder.resultado.items():
        assert isinstance(item, dict)
        assert "titulo" in item
        assert "precio" in item
        assert "precio_peso" in item
        assert "img" in item
        assert "estrellas" in item

def test_get_ingredientes(json_builder):
    for _, item in json_builder.resultado.items():
        if "https://" in item["img"]:
            json_builder.SacarDetallesItem(item["img"], item)
            assert "ingredientes" in item

def test_get_instrucciones_conservacion(json_builder):
    for _, item in json_builder.resultado.items():
        if "https://" in item["img"]:
            json_builder.SacarDetallesItem(item["img"], item)
            assert "ins_conservación" in item

def test_get_info_nutricional(json_builder):
    for _, item in json_builder.resultado.items():
        if "https://" in item["img"]:
            json_builder.SacarDetallesItem(item["img"], item)
            assert "nutrientes" in item
