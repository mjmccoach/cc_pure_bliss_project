from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.country import Country

import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries",__name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)


@countries_blueprint.route("/countries/new", methods=["GET"])
def new_country():
    return render_template("countries/new.html")

@countries_blueprint.route("/countries", methods=["POST"])
def add_country():
    
    name = request.form["name"]
    continent = request.form["continent"]
    
    country = Country(name, continent)

    country_repository.save(country)
    return redirect ("/countries")

@countries_blueprint.route("/countries/<id>", methods= ["GET"])
def view_country(id):
    country = country_repository.select(id)
    return render_template("/countries/view.html", country = country)

@countries_blueprint.route("/countries/<id>/edit", methods= ["GET"])
def edit_country(id):
    country = country_repository.select(id)
    
    return render_template("/countries/edit.html", country = country)

@countries_blueprint.route("/countries/<id>", methods= ["POST"])
def update_city(id):
    name = request.form["name"]
    continent = request.form["continent"]

    country = Country(name, continent, id)
    country_repository.update(country)
    return redirect('/countries')
