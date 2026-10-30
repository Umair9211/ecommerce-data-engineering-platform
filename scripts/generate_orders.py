import pandas as pd
import random
from pathlib import Path
from faker import Faker

fake = Faker()

NUM_ORDERS = 50000

DATA_DIR = Path("data/generated")

order_statuses = [
    "PENDING",
    "CONFIRMED",
    "SHIPPED",
    "DELIVERED",
    "CANCELLED"
]


def generate_orders():

    customers = pd.read_csv(DATA_DIR / "customers.csv")
    products = pd.read_csv(DATA_DIR / "products.csv")

    customer_ids = customers["customer_id"].tolist()
    product_ids = products["product_id"].tolist()

    product_prices = products.set_index("product_id")["price"].to_dict()

    orders = []

    for i in range(1, NUM_ORDERS + 1):

        product_id = random.choice(product_ids)

        quantity = random.randint(1, 5)

        order = {
            "order_id": f"ORD{i:06d}",
            "customer_id": random.choice(customer_ids),
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": product_prices[product_id],
            "order_status": random.choices(
                order_statuses,
                weights=[10, 20, 20, 40, 10]
            )[0],
            "order_date": fake.date_time_between(
                start_date="-1y",
                end_date="now"
            )
        }

        orders.append(order)

    df = pd.DataFrame(orders)

    df.to_csv(DATA_DIR / "orders.csv", index=False)

    print(f"Generated {len(df)} orders.")


if __name__ == "__main__":
    generate_orders()