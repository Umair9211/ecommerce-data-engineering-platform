import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/generated")


def validate_primary_key(df, column, dataset):

    duplicates = df[column].duplicated().sum()

    if duplicates > 0:
        print(f"FAILED: {dataset} has {duplicates} duplicate IDs")
    else:
        print(f"PASSED: {dataset} primary key is unique")


def validate_foreign_key(child_df, child_column,
                          parent_df, parent_column, dataset):

    invalid = ~child_df[child_column].isin(parent_df[parent_column])

    invalid_count = invalid.sum()

    if invalid_count > 0:
        print(f"FAILED: {dataset} has {invalid_count} invalid foreign keys")
    else:
        print(f"PASSED: {dataset} foreign keys are valid")


def main():

    customers = pd.read_csv(DATA_DIR / "customers.csv")
    products = pd.read_csv(DATA_DIR / "products.csv")
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    payments = pd.read_csv(DATA_DIR / "payments.csv")
    deliveries = pd.read_csv(DATA_DIR / "deliveries.csv")

    print("\n--- PRIMARY KEY VALIDATION ---\n")

    validate_primary_key(customers, "customer_id", "Customers")
    validate_primary_key(products, "product_id", "Products")
    validate_primary_key(orders, "order_id", "Orders")
    validate_primary_key(payments, "payment_id", "Payments")
    validate_primary_key(deliveries, "delivery_id", "Deliveries")

    print("\n--- FOREIGN KEY VALIDATION ---\n")

    validate_foreign_key(
        orders, "customer_id",
        customers, "customer_id",
        "Orders -> Customers"
    )

    validate_foreign_key(
        orders, "product_id",
        products, "product_id",
        "Orders -> Products"
    )

    validate_foreign_key(
        payments, "order_id",
        orders, "order_id",
        "Payments -> Orders"
    )

    validate_foreign_key(
        deliveries, "order_id",
        orders, "order_id",
        "Deliveries -> Orders"
    )


if __name__ == "__main__":
    main()