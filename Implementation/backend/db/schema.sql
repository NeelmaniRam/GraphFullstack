CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    country TEXT
);

CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    description TEXT,
    product_group TEXT
);

CREATE TABLE IF NOT EXISTS sales_orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT,
    creation_date TEXT
);

CREATE TABLE IF NOT EXISTS sales_order_items (
    order_id TEXT,
    item_id TEXT,
    product_id TEXT,
    PRIMARY KEY (order_id, item_id)
);

CREATE TABLE IF NOT EXISTS deliveries (
    delivery_id TEXT PRIMARY KEY,
    order_id TEXT
);

CREATE TABLE IF NOT EXISTS billing (
    billing_id TEXT PRIMARY KEY,
    delivery_id TEXT,
    amount REAL
);

CREATE TABLE IF NOT EXISTS accounting (
    accounting_id TEXT PRIMARY KEY,
    billing_id TEXT,
    amount REAL
);