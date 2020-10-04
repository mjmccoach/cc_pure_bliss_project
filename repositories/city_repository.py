from db.run_sql import run_sql

from models.city import City
from models.country import Country

import repositories.country_repository as country_repository

def save(city):
    sql = "INSERT into cities(name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id

    return city 

def select_all():
    city_list = []
    
    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row["id"])
        city = City(["name"], country , ['visited'], [id])
        city_list.append(city)
    return city_list

def delete_all():
    
    sql = "DELETE FROM cities"
    results = run_sql(sql)

def delete(id):

    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)


def update(city):
    
    sql = "UPDATE cities SET (name, country, visited) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.country, city.visited]
    print(values)
    result = run_sql(sql, values)