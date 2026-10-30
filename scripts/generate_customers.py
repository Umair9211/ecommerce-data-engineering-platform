import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Configuration
NUM_CUSTOMERS = 5000

# Pakistani cities
cities = [
    "Lahore",
    "Karachi",
    "Islamabad",
    "Rawalpindi",
    "Faisalabad",
    "Multan",
    "Peshawar",
    "Quetta"
]


def generate_customers():

    customers = []

    for i in range(1, NUM_CUSTOMERS + 1):

        customer = {
            "customer_id": f"CUST{i:04d}",
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.unique.email(),
            "city": random.choice(cities),
            "registration_date": fake.date_time_between(
                start_date="-2y",
                end_date="now"
            )
        }

        customers.append(customer)

    # Convert records into a DataFrame
    df = pd.DataFrame(customers)

    # Export to CSV
    df.to_csv("data/generated/customers.csv", index=False)

    print(f"Successfully generated {len(df)} customers!")


if __name__ == "__main__":
    generate_customers()