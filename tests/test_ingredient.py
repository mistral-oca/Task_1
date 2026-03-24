import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "ketchup", 50),
        ("FILLING", "cheese", 100),
        ("SAUCE", "", 0),
        ("FILLING", "bacon", 99.9),
    ])
    def test_ingredient_type_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "ketchup", 50),
        ("FILLING", "cheese", 100),
        ("SAUCE", "", 0),
        ("FILLING", "bacon", 99.9),
    ])
    def test_ingredient_name_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.name == name

    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "ketchup", 50),
        ("FILLING", "cheese", 100),
        ("SAUCE", "", 0),
        ("FILLING", "bacon", 99.9),
    ])
    def test_ingredient_price_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.price == price


    @pytest.mark.parametrize("price", [0, 10, 99.9])
    def test_get_price(self, price):
        ingredient = Ingredient("SAUCE", "test", price)

        assert ingredient.get_price() == price


    @pytest.mark.parametrize("name", ["ketchup", "cheese", ""])
    def test_get_name(self, name):
        ingredient = Ingredient("SAUCE", name, 50)

        assert ingredient.get_name() == name


    @pytest.mark.parametrize("ingredient_type", ["SAUCE", "FILLING"])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "test", 50)

        assert ingredient.get_type() == ingredient_type