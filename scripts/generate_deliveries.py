import pandas as pd
import random
from pathlib import Path
from datetime import timedelta

DATA_DIR = Path("data/generated")

couriers = [
    "TCS",
    "Leopards",
    "M&P",
    "Trax",
    "BlueEx"
]

delivery_statuses = [
    "SHIPPED",
    "IN_TRANSIT",
    "DELIVERED",
    "FAILED"
]


def generate_deliveries():

    orders = pd.read_csv(DATA_DIR / "orders.csv")

    # Only orders that haven't been cancelled can be shipped.
    eligible_orders = orders[
        orders["order_status"] != "CANCELLED"
    ]

    selected_orders = eligible_orders.sample(
        n=45000,
        random_state=42
    )

    deliveries = []

    for i, (_, order) in enumerate(
        selected_orders.iterrows(),
        start=1
    ):

        order_date = pd.to_datetime(order["order_date"])

        shipped_at = order_date + timedelta(
            hours=random.randint(2, 48)
        )

        delivery_status = random.choices(
            delivery_statuses,
            weights=[10, 20, 65, 5]
        )[0]

        delivered_at = None

        if delivery_status == "DELIVERED":
            delivered_at = shipped_at + timedelta(
                days=random.randint(1, 7)
            )

        delivery = {
            "delivery_id": f"DEL{i:06d}",
            "order_id": order["order_id"],
            "courier_name": random.choice(couriers),
            "delivery_city": random.choice([
                "Lahore",
                "Karachi",
                "Islamabad",
                "Rawalpindi",
                "Faisalabad",
                "Multan",
                "Peshawar",
                "Quetta"
            ]),
            "delivery_status": delivery_status,
            "shipped_at": shipped_at,
            "delivered_at": delivered_at,
            "shipping_cost": round(
                random.uniform(150, 1000), 2
            )
        }

        deliveries.append(delivery)

    df = pd.DataFrame(deliveries)

    df.to_csv(DATA_DIR / "deliveries.csv", index=False)

    print(f"Generated {len(df)} deliveries.")


if __name__ == "__main__":
    generate_deliveries()