import pandas as pd
import random
from pathlib import Path
from faker import Faker

fake = Faker()

NUM_PRODUCTS = 1000

OUTPUT_DIR = Path("data/generated")

categories = [
    "Electronics",
    "Clothing",
    "Home & Kitchen",
    "Books",
    "Sports",
    "Beauty",
    "Accessories"
]


def generate_products():

    products = []

    for i in range(1, NUM_PRODUCTS + 1):

        product = {
            "product_id": f"PROD{i:04d}",
            "product_name": fake.catch_phrase(),
            "category": random.choice(categories),
            "price": round(random.uniform(500, 150000), 2),
            "cost_price": round(random.uniform(200, 100000), 2),
            "stock_quantity": random.randint(0, 500),
            "created_at": fake.date_time_between(
                start_date="-2y",
                end_date="now"
            )
        }

        products.append(product)

    df = pd.DataFrame(products)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_DIR / "products.csv", index=False)

    print(f"Generated {len(df)} products.")


if __name__ == "__main__":
    generate_products()