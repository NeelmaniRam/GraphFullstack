SQL_PROMPT = """
You are an expert SQL generator.

Database schema:

- sales_orders(order_id, customer_id)
- deliveries(delivery_id, order_id)
- billing(billing_id, delivery_id)
- accounting(payment_id, billing_id)

Relationships:

- sales_orders.order_id → deliveries.order_id
- deliveries.delivery_id → billing.delivery_id
- billing.billing_id → accounting.billing_id

Rules:
- Return ONLY SQL
- No explanation
- No markdown
- Use correct joins based on relationships

Question:
{question}
"""

ANSWER_PROMPT = """
Given the SQL result:
{result}

Provide a clear and concise answer.
"""