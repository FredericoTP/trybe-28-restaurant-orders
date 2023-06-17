from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
import pytest


# Req 1
def test_ingredient():
    new_salmao = Ingredient("salmão")
    new_salmao2 = Ingredient("salmão")
    new_farinha = Ingredient("farinha")

    assert new_salmao.name == "salmão"
    assert new_salmao.__repr__() == "Ingredient('salmão')"
    assert new_salmao.__hash__() == new_salmao2.__hash__()
    assert new_salmao.__hash__() != new_farinha.__hash__()
    assert new_salmao.__eq__(new_salmao2) is True
    assert new_salmao.__eq__(new_farinha) is False
    assert new_salmao.restrictions
    assert isinstance(new_farinha.restrictions, set)

    with pytest.raises(TypeError):
        new_ingredient = Ingredient()
        new_ingredient.name
