from main import geo_city
import pytest


class TestCity:

    @pytest.mark.parametrize("sens, expected_result", [
            (
                [
                    {'1': ['q', 'Россия']}, {'2': ['d', 'Россия']}, {'3': ['w', 'Франция']}, {'4': ['e', 'Австрия']}
                ], ['q', 'd']
            ),
            (
                [
                    {'один': ['1', 'Россия']}, {'два': ['2', 'Россия']}, {'три': ['3', 'Ф']},
                    {'четыре': ['4', 'Россия']}
                ], ['1', '2', '4'])
            ])
    def test_multiplication(self, sens, expected_result):
        result = geo_city(sens)
        expected = expected_result
        assert result == expected

