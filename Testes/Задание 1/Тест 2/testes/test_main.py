from main import max_sales
import pytest


class TestCity:

    @pytest.mark.parametrize("sens, expected_result", [({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 299,
                                                         'email': 42, 'ok': 98}, 'google'), ({'facebook': 55,
                                                         'yandex': 120, 'vk': 125, 'google': 99,
                                                         'email': 42, 'ok': 98}, 'vk')])
    def test_multiplication(self, sens, expected_result):
        result = max_sales(sens)
        expected = expected_result
        assert result == expected

