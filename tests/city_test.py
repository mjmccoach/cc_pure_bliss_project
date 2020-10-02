import unittest

from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city1 = City("Tokyo", False, id)

    def test_city_has_name(self):
        self.assertEqual("Tokyo", self.city1.name)