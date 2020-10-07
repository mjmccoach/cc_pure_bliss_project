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
    bucketlist = bucketlist_repository.select_all()
    countries = country_repository.select_all()

    return render_template("/bucketlist/index.html", countries= countries, bucketlist=bucketlist)

@bucketlist_blueprint.route("/bucketlist/new/<country_id>", methods=["GET"])
def new_item(country_id):
    cities = city_repository.select_all()

    country = country_repository.select(country_id)
    
    return render_template("/bucketlist/new.html", country = country, cities = cities)

@bucketlist_blueprint.route("/bucketlist", methods=["POST"])
def add_item():
    city_id = request.form["city_id"]
    visited = False

    city = city_repository.select(city_id)
    
    
    country_id = request.form["country_id"]
    country = country_repository.select(country_id)

    visited = request.form["visited"]
    bucketlist = Bucketlist(country, city, visited)
    bucketlist_repository.save(bucketlist)
    

    return redirect("/bucketlist")
    

@bucketlist_blueprint.route("/bucketlist/<id>/delete", methods=["POST"])
def delete_bucketlist(id):
    bucketlist_repository.delete(id)
    return redirect ("/bucketlist")

@bucketlist_blueprint.route("/bucketlist/<id>", methods=["GET"])
def view_bucketlist(id):
    bucketlist = bucketlist_repository.select(id)
    return render_template("/bucketlist/view.html", bucketlist = bucketlist)

@bucketlist_blueprint.route("/bucketlist/<id>/edit", methods = ["GET"])
def edit_bucketlist(id):
    bucketlist = bucketlist_repository.select(id)
    return render_template("bucketlist/edit.html", bucketlist = bucketlist)

@bucketlist_blueprint.route("/bucketlist/<id>", methods =["POST"])
def update_bucketlist(id):
    visited = request.form["visited"]
    bucketlist = bucketlist_repository.select(id)
    bucketlist.visited = visited
    
    # bucketlist = Bucketlist(country, city, visited, id)
    bucketlist_repository.update(bucketlist)
    return redirect('/bucketlist')
