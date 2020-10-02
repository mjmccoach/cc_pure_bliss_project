from flask import Flask, render_template
from flask import Blueprint

from models.city import City
import repositories.city_repository as city_repository

city_blueprint = Blueprint("city",__name__)