from flask import Blueprint, jsonify
from web.models import Country

api = Blueprint("api", __name__)

@api.route("/api/getcountries", methods=['GET'])
def get_data():
    countries_data: dict = {"countries" : []}
    countries = Country.query.all()
    for country in countries:
        data: dict = {
            "name": country.name, 
            "users": []
        }
        for user in country.users:
            data["users"].append({
                "name": user.name, 
                "gender": user.gender, 
                "email": user.email
            })
        countries_data["countries"].append(data)
    response = jsonify(countries_data)
    response.access_control_allow_origin = "*"
    return response
