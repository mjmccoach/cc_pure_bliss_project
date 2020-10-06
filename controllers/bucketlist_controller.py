from flask import Flask, render_template, redirect, request
from flask import Blueprint

from models.city import City
from models.country import Country
from models.bucketlist import Bucketlist

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.bucketlist_repository as bucketlist_repository

bucketlist_blueprint = Blueprint("bucketlist",__name__)

@bucketlist_blueprint.route("/bucketlist")
def bucketlist_home():
    bucketlist_repository.select_all()
    countries = country_repository.select_all()
    return render_template("/bucketlist/index.html", countries= countries)

@bucketlist_blueprint.route("/bucketlist/new/<country_id>", methods=["GET"])
def new_item(country_id):
    cities = city_repository.select_all()

    countries = country_repository.select(country_id)

    return render_template("/bucketlist/new.html", country = countries, cities = cities)

@bucketlist_blueprint.route("/bucketlist", methods = ["POST"])
def add_item(country_id):
    city = request.form["city"]
    country_id = country_repository.select(country_id)
    visted = False

    bucketlist = Bucketlist(city, country, visited, id)
    bucketlist_repository.save(bucketlist)
    
    # country = country_repository.select(country_id)
    # city = city_repository.select_all()
    # bucketlist = bucketlist_repository.select_all()

    return redirect("/bucketlist") 
    # country = country, city= cities, bucketlist = bucketlist)

    
