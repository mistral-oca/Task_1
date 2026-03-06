import pytest

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100.0),
            ("white bun", 50.5),
            ("sesame bun", 0),
            ("", 10.0),
        ]
    )
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)

        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize(
        "name",
        [
            "black bun",
            "white bun",
            "",
        ]
    )
    def test_get_name_returns_correct_name(self, name):
        bun = Bun(name, 100.0)

        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "price",
        [
            100.0,
            50.5,
            0,
        ]
    )
    def test_get_price_returns_correct_price(self, price):
        bun = Bun("test bun", price)

        assert bun.get_price() == price