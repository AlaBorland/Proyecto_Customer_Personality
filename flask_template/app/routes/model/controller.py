from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from dotenv import dotenv_values,load_dotenv
from app.services.model.model import model

customer_blueprint = Blueprint("customer", __name__, url_prefix="/Customer_classify")


@customer_blueprint.route("/", methods=["GET", "POST"])
def func():
    m=model()
    return m.Run()
    