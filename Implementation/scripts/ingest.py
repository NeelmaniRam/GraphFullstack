import json
import sqlite3

conn = sqlite3.connect("data.db")
cur = conn.cursor()

with open("combined.jsonl") as f:
    for line in f:
        row = json.loads(line)

        # Customer
        if row.get("customer"):
            cur.execute("""
                INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?)
            """, (
                row.get("customer"),
                row.get("businessPartnerFullName"),
                row.get("cityName"),
                row.get("country")
            ))

        # Product
        if row.get("product"):
            cur.execute("""
                INSERT OR IGNORE INTO products VALUES (?, ?, ?)
            """, (
                row.get("product"),
                row.get("productDescription"),
                row.get("productGroup")
            ))

        # Sales Order
        if row.get("salesOrder"):
            cur.execute("""
                INSERT OR IGNORE INTO sales_orders VALUES (?, ?, ?)
            """, (
                row.get("salesOrder"),
                row.get("customer"),
                row.get("creationDate")
            ))

        # Order Item
        if row.get("salesOrderItem"):
            cur.execute("""
                INSERT OR IGNORE INTO sales_order_items VALUES (?, ?, ?)
            """, (
                row.get("salesOrder"),
                row.get("salesOrderItem"),
                row.get("product")
            ))

        # Delivery
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