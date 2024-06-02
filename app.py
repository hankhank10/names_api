from fastapi import FastAPI, HTTPException
from names_dataset import NameDataset
import random

app = FastAPI()

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

@app.get("/api/random_name/")
@app.get("/api/random_name/{gender}")
def get_random_name(gender = "male"):
    # Convert the gender to lower case
    gender = gender.lower()

    if gender not in valid_genders:
        raise HTTPException(
            status_code=400,
            detail=f"{gender} is not in list of valid genders. Valid options are {valid_genders}."
        )

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
