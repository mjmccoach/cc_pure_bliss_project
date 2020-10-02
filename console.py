import pdb

from models.city import City
from models.country import Country

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository


country1 = Country("Germany", "Europe")
country_repository.save(country1)

country2 = Country("South Korea", "Asia")
country_repository.save(country2)

country3 = Country("New Zealand", "Oceania")
country_repository.save(country3)

pdb.set_trace()
