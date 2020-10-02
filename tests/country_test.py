import unittest

from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country1 = Country("Japan", "Asia", id)
    
    def test_country_has_name(self):
        self.assertEqual("Japan", self.country1.name)

    def test_country_has_continent(self):
        self.assertEqual("Asia", self.country1.continent)
    
    def test_country_has_id(self):
        self.assertEqual(id, self.country1.id)