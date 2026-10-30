import pandas as pd
import random
from pathlib import Path
from faker import Faker

fake = Faker()

DATA_DIR = Path("data/generated")

payment_methods = [
    "CARD",
    "BANK_TRANSFER",
    "COD",
    "WALLET"
]

payment_statuses = [
    "SUCCESS",
    "FAILED",
    "PENDING",
    "REFUNDED"
]


def generate_payments():

    orders = pd.read_csv(DATA_DIR / "orders.csv")

    payments = []

    payment_counter = 1

    for _, order in orders.iterrows():

        # Every order receives at least one payment attempt.
        payment = {
            "payment_id": f"PAY{payment_counter:06d}",
            "order_id": order["order_id"],
            "payment_method": random.choice(payment_methods),
            "amount": round(
                order["unit_price"] * order["quantity"], 2
            ),
            "payment_status": random.choices(
                payment_statuses,
                weights=[75, 12, 10, 3]
            )[0],
            "transaction_date": order["order_date"]
        }

        payments.append(payment)
        payment_counter += 1

    # Generate 5,000 additional payment attempts.
    extra_orders = orders.sample(n=5000)

    for _, order in extra_orders.iterrows():

        payment = {
            "payment_id": f"PAY{payment_counter:06d}",
            "order_id": order["order_id"],
            "payment_method": random.choice(payment_methods),
            "amount": round(
                order["unit_price"] * order["quantity"], 2
            ),
            "payment_status": random.choice(
                ["SUCCESS", "FAILED", "PENDING"]
            ),
            "transaction_date": order["order_date"]
        }

        payments.append(payment)
        payment_counter += 1

    df = pd.DataFrame(payments)

    df.to_csv(DATA_DIR / "payments.csv", index=False)

    print(f"Generated {len(df)} payments.")


if __name__ == "__main__":
    generate_payments()