from unittest import TestCase
from main import create_folder


class TestAPI(TestCase):


# Тест отрицательного ответа: папка не создана
    def test_new_folder(self):
        name_folder = 'test6_name'
        result = create_folder(name_folder)
        expected = 201
        self.assertNotEqual(result, expected)
        print(f'Папка с именем {name_folder} не создана')

# Тест на положительный ответ: папка создана
    def test_have_folder(self):
        name_folder = 'test6_name'
        result = create_folder(name_folder)
        expected = 201
        self.assertEqual(result, expected)
        print(f'Папка с именем {name_folder} создана')