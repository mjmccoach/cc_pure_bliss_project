import unittest

from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country1 = Country("Japan", "Asia", id)
    
    def test_country_has_name(self):
        self.assertEqual("Japan", self.country1.name)

