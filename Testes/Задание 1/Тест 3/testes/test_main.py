from main import unic_id
import pytest


class TestCity:

    @pytest.mark.parametrize("sens, expected_result",
                             [
                                 (
                                         {'user1': [1, -1, 1, -2, 6],
                                          'user2': [2, 2, 2, 3],
                                          'user3': [-1, -1, -4, -5]
                                          }, {1, -1, -2, 6, 2, 3, -4, -5}
                                 ),
                                 (
                                         {'user1': [0, 0, 0, 2, 3],
                                          'user2': [0, 2, 3, 0],
                                          'user3': [3, 3, 3, 3]
                                          }, {0, 2, 3}
                                 )
                              ]
                             )
    def test_multiplication(self, sens, expected_result):
        result = unic_id(sens)
        expected = expected_result
        assert result == expected
