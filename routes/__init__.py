from flask import Blueprint, jsonify
from flask_pymongo import PyMongo
from models import mongo

routes = Blueprint('routes', __name__)
db = mongo.db
from .account import *
from .menu import *

