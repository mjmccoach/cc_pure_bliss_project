from db.run_sql import run_sql

from models.city import City

def save(city):
    sql = "INSERT into cities(name) VALUES (%s) RETURNING id"
    values = [city.name]
    results = run_sql(sql, values)
    city.id = results[0]['id']

    return city

# def select_all():
#     city_list = []
    
#     sql = "SELECT * FROM cities"
#     results = run_sql(sql)

#     for row in results:
#         country = Country(row["id"])
#         city = City(row["name"], row [id], row [visited], country)
#         city_list.append(city)
#     return city

def delete_all():
    
    sql = "DELETE FROM cities"
    results = run_sql(sql)