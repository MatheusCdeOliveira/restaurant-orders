from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction
import pytest

mock_restrictions = {
    Restriction.ANIMAL_DERIVED,
    Restriction.ANIMAL_MEAT,
}


# Req 2
def test_dish():
    dish1 = Dish("Strogonoff", 24.90)
    dish2 = Dish("Escondidinho", 22.90)
    ingredient = Ingredient("frango")

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Strogonoff", "24")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Strogonoff", -1)

    assert dish1.name == "Strogonoff"
    assert dish1.price == 24.90
    assert dish1.recipe == {}
    assert repr(dish1) == "Dish('Strogonoff', R$24.90)"
    assert dish1 == dish1
    assert dish1 != dish2
    assert hash(dish1) == hash(dish1)
    assert hash(dish1) != hash(dish2)
    assert dish1.get_restrictions() == set()

    dish1.add_ingredient_dependency(ingredient, 2)

    assert dish1.recipe == {Ingredient("frango"): 2}
    assert dish1.get_restrictions() == mock_restrictions
    assert dish1.get_ingredients() == set(dish1.recipe.keys())
