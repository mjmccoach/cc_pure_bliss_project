from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.country import Country

import repositories.country_repository as country_repository

countries_blueprint = Blueprint("countries",__name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

# @countries_blueprint.route("/countries/new")
# def create_country():
#     country_name = request.form["country.name"]
#     country_contintent = request.form["country.continent"]
#     country_repository.save(country)
#     return redirect ("/countries")