from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction  # noqa: F401, E261, E501

mock_carne = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}


# Req 1
def test_ingredient():
    ingredient = Ingredient("carne")
    ingredient2 = Ingredient("farinha")
    assert ingredient.restrictions == mock_carne
    assert ingredient.name == "carne"
    assert repr(ingredient) == "Ingredient('carne')"
    assert ingredient == ingredient
    assert ingredient != ingredient2
    assert hash(ingredient) == hash(ingredient)
    assert hash(ingredient) != hash(ingredient2)
