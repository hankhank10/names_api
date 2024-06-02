from flask import Flask, jsonify, abort
from names_dataset import NameDataset
import random

app = Flask(__name__)

nd = NameDataset()

valid_genders = ["male", "female"]

country = "GB"
first_name_count = 200
second_name_count = 800

first_names_female = nd.get_top_names(
    n=first_name_count,
    gender="Female",
    use_first_names=True,
    country_alpha2=country
)[country]['F']

first_names_male = nd.get_top_names(
    n=first_name_count,
    gender="Male",
    use_first_names=True,
    country_alpha2=country
)[country]['M']

second_names = nd.get_top_names(
    n=second_name_count,
    use_first_names=False,
    country_alpha2=country
)[country]

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/api/random_name/<string:gender>", methods=['GET'])
def get_random_name(gender):
    # Convert the gender to lower case
    gender = gender.lower()

    if gender not in valid_genders:
        return {
            "status": "error",
            "message": "Invalid gender provided",
            "valid_options": valid_genders
        }, 400

    if gender == "male":
        first_name = random.choice (first_names_male)
    
    if gender == "female":
        first_name = random.choice(first_names_female)

    second_name = random.choice(second_names)

    return {
        "status": "success",
        "first_name": first_name,
        "second_name": second_name
    }

if __name__ == "__main__":
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8090
    )