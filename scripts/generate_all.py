from generate_customers import generate_customers
from generate_products import generate_products
from generate_orders import generate_orders
from generate_payments import generate_payments
from generate_deliveries import generate_deliveries


def generate_all():

    print("\nStarting E-Commerce Data Generation...\n")

    print("Step 1: Generating customers")
    generate_customers()

    print("\nStep 2: Generating products")
    generate_products()

    print("\nStep 3: Generating orders")
    generate_orders()

    print("\nStep 4: Generating payments")
    generate_payments()

    print("\nStep 5: Generating deliveries")
    generate_deliveries()

    print("\nAll datasets generated successfully!")


if __name__ == "__main__":
    generate_all()