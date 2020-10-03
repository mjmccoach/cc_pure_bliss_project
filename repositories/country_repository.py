from db.run_sql import run_sql

from models.country import Country

def save(country):
    sql = "INSERT INTO countries(name, continent) VALUES (%s, %s) RETURNING id"
    values = [country.name, country.continent]
    results = run_sql(sql, values)
    country.id = results[0]['id']

    return country

def select_all():
    countries_list = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    
    for row in results:
        country = Country(["name"], ["continent"], [id])
        countries_list.append(country)
    return countries_list

def select(id):
    country = None
    
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['continent'], result['id'])
    return country

def delete_all():

    sql = "DELETE FROM countries"
    results = run_sql(sql)

def delete(id):

    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    