from db.run_sql import run_sql

from models.city import City
from models.country import Country
from models.bucketlist import Bucketlist

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

def save(item):
    sql = "INSERT INTO bucketlist (city_id, country_id, visited) VALUES (%s, %s, %s) RETURNING id"
    values = (bucketlist.city.id, bucketlist.country.id)
    results = run_sql(sql, values)
    id = result[0]['id']
    bucketlist.id = id

def delete(id):
    sql = "DELETE FROM bucketlist WHERE id = %s"
    
   

