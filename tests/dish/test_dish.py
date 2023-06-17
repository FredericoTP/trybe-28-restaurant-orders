from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    new_farofa = Dish("Farofa", 10)
    new_farofa2 = Dish("Farofa", 10)
    new_feijoada = Dish("Feijoada", 23)

    farinha = Ingredient("farinha")
    bacon = Ingredient("bacon")

    assert new_farofa.name == "Farofa"
    assert new_farofa.__repr__() == "Dish('Farofa', R$10.00)"
    assert new_farofa.__eq__(new_farofa2) is True
    assert new_farofa.__eq__(new_feijoada) is False
    assert new_farofa.__hash__() == new_farofa2.__hash__()
    assert new_farofa.__hash__() != new_feijoada.__hash__()

    new_farofa.add_ingredient_dependency(farinha, 2)
    new_farofa.add_ingredient_dependency(bacon, 3)

    assert new_farofa.get_ingredients() == {farinha, bacon}
    assert new_farofa.get_restrictions()

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Farofa", "a")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Farofa", -1)
