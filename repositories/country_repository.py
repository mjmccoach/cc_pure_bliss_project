from db.run_sql import run_sql

from models.country import Country

def save(country):
    sql = "INSERT INTO countries(name, continent) VALUES (%s, %s) RETURNING id"
    values = [country.name, country.continent]
    results = run_sql(sql,values)
    country.id = results[0]('id')

    return country