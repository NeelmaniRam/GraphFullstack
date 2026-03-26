import networkx as nx
from db.database import get_connection

def build_graph():
    G = nx.DiGraph()
    conn = get_connection()
    cur = conn.cursor()

    # Customer → Orders
    for order_id, customer_id in cur.execute("SELECT order_id, customer_id FROM sales_orders"):
        G.add_edge(f"C_{customer_id}", f"O_{order_id}")

    # Orders → Items
    for order_id, item_id in cur.execute("SELECT order_id, item_id FROM sales_order_items"):
        G.add_edge(f"O_{order_id}", f"OI_{order_id}_{item_id}")

    # Items → Products
    for order_id, item_id, product_id in cur.execute("SELECT order_id, item_id, product_id FROM sales_order_items"):
        G.add_edge(f"OI_{order_id}_{item_id}", f"P_{product_id}")

    # Orders → Deliveries
    for delivery_id, order_id in cur.execute("SELECT delivery_id, order_id FROM deliveries"):
        G.add_edge(f"O_{order_id}", f"D_{delivery_id}")

    # Delivery → Billing
    for billing_id, delivery_id in cur.execute("SELECT billing_id, delivery_id FROM billing"):
        G.add_edge(f"D_{delivery_id}", f"B_{billing_id}")

    # Billing → Accounting
    for accounting_id, billing_id in cur.execute("SELECT accounting_id, billing_id FROM accounting"):
        G.add_edge(f"B_{billing_id}", f"A_{accounting_id}")

    conn.close()
    return G