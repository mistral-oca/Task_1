import pytest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from database import Database
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_returns_all_buns(self):
        db = Database()
        buns = db.available_buns()

        assert isinstance(buns, list)
        assert all(isinstance(bun, Bun) for bun in buns)
        assert len(buns) == 3

        names_prices = [(bun.get_name(), bun.get_price()) for bun in buns]
        expected = [("black bun", 100), ("white bun", 200), ("red bun", 300)]
        assert names_prices == expected

    def test_available_ingredients_returns_all_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert isinstance(ingredients, list)
        assert all(isinstance(ing, Ingredient) for ing in ingredients)
        assert len(ingredients) == 6

        types_names_prices = [(ing.get_type(), ing.get_name(), ing.get_price()) for ing in ingredients]
        expected = [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300),
        ]
        assert types_names_prices == expected