from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.bucketlist import Bucketlist

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

def save(bucketlist):
    sql = "INSERT INTO bucketlist (city_id, country_id, visited) VALUES (%s, %s, %s) RETURNING id"
    values = (bucketlist.city.id, bucketlist.country.id, bucketlist.visited)
    result = run_sql(sql, values)
    id = result[0]['id']
    bucketlist.id = id

def delete(id):
    sql = "DELETE FROM bucketlist WHERE id = %s"
    values = [id]
    run_sql(sql, values)
   
def update(item):
    sql = "UPDATE bucketlist SET (city_id, country_id, visited) = VALUES (%s, %s, %s) WHERE id = %s"
    values = [bucketlist.city.id, bucketlist.country.id, bucketlist.visited, bucketlist.id]
    run_sql(sql, values)

def select_all():
    bucketlist_items = []

    sql = "SELECT * FROM bucketlist"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = city_repository.select(row['city_id'])
        bucketlist = Bucketlist(country, city, row['visited'], row['id'])

        bucketlist_items.append(bucketlist)
    return bucketlist_items

