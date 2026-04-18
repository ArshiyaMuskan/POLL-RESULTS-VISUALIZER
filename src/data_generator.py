import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_advanced_data(n=500):
    np.random.seed(42)

    # -----------------------------
    # COUNTRY + REGION MAPPING
    # -----------------------------
    country_region = {
        "USA": "North America",
        "Canada": "North America",
        "UK": "Europe",
        "Germany": "Europe",
        "India": "Asia",
        "China": "Asia",
        "Japan": "Asia",
        "Australia": "Oceania",
        "Brazil": "South America",
        "South Africa": "Africa"
    }

    countries = list(country_region.keys())

    # -----------------------------
    # OTHER COLUMNS
    # -----------------------------
    questions = [
        "Favorite Product",
        "Preferred Platform",
        "Satisfaction Level"
    ]

    product_options = ["Product A", "Product B", "Product C"]
    platform_options = ["Mobile App", "Website", "Tablet"]
    satisfaction_options = ["Satisfied", "Neutral", "Dissatisfied"]

    age_groups = ["18-25", "26-35", "36-50", "50+"]
    genders = ["Male", "Female", "Other"]
    income_levels = ["Low", "Medium", "High"]

    # -----------------------------
    # DATE GENERATION
    # -----------------------------
    start_date = datetime(2024, 1, 1)

    data = []

    for i in range(n):
        country = np.random.choice(countries)
        region = country_region[country]
        question = np.random.choice(questions)

        # Conditional options based on question
        if question == "Favorite Product":
            option = np.random.choice(product_options, p=[0.4, 0.35, 0.25])
        elif question == "Preferred Platform":
            option = np.random.choice(platform_options)
        else:
            option = np.random.choice(satisfaction_options, p=[0.6, 0.25, 0.15])

        row = {
            "Respondent_ID": i + 1,
            "Date": start_date + timedelta(days=np.random.randint(0, 180)),
            "Country": country,
            "Region": region,
            "Question": question,
            "Option_Selected": option,
            "Age_Group": np.random.choice(age_groups),
            "Gender": np.random.choice(genders),
            "Income_Level": np.random.choice(income_levels)
        }

        data.append(row)

    df = pd.DataFrame(data)

    # Save dataset
    df.to_csv("data/advanced_poll_data.csv", index=False)

    print("✅ Advanced global dataset created!")

if __name__ == "__main__":
    generate_advanced_data()