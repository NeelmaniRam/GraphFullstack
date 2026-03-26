import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from db.database import get_connection

def ingest():
    conn = get_connection()
    cur = conn.cursor()

    with open("../data/combined.jsonl") as f:
        for line in f:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                print("Skipping invalid JSON line")
                continue

            # Customers
            if row.get("customer"):
                cur.execute("""
                    INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?)
                """, (
                    row.get("customer"),
                    row.get("businessPartnerFullName"),
                    row.get("cityName"),
                    row.get("country")
                ))

            # Products
            if row.get("product"):
                cur.execute("""
                    INSERT OR IGNORE INTO products VALUES (?, ?, ?)
                """, (
                    row.get("product"),
                    row.get("productDescription"),
                    row.get("productGroup")
                ))

            # Orders
            if row.get("salesOrder"):
                cur.execute("""
                    INSERT OR IGNORE INTO sales_orders VALUES (?, ?, ?)
                """, (
                    row.get("salesOrder"),
                    row.get("customer"),
                    row.get("creationDate")
                ))

            # Order Items
            if row.get("salesOrderItem"):
                cur.execute("""
                    INSERT OR IGNORE INTO sales_order_items VALUES (?, ?, ?)
                """, (
                    row.get("salesOrder"),
                    row.get("salesOrderItem"),
                    row.get("product")
                ))

            # Deliveries
            if row.get("deliveryDocument"):
                cur.execute("""
                    INSERT OR IGNORE INTO deliveries VALUES (?, ?)
                """, (
                    row.get("deliveryDocument"),
                    row.get("salesOrder")
                ))

            # Billing
            if row.get("billingDocument"):
                cur.execute("""
                    INSERT OR IGNORE INTO billing VALUES (?, ?, ?)
                """, (
                    row.get("billingDocument"),
                    row.get("deliveryDocument"),
                    row.get("netAmount")
                ))

            # Accounting
            if row.get("accountingDocument"):
                cur.execute("""
                    INSERT OR IGNORE INTO accounting VALUES (?, ?, ?)
                """, (
                    row.get("accountingDocument"),
                    row.get("billingDocument"),
                    row.get("amountInCompanyCodeCurrency")
                ))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    ingest()