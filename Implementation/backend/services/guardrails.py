def is_valid_query(query: str) -> bool:
    allowed_keywords = [
        "order", "delivery", "billing", "invoice",
        "payment", "customer", "product"
    ]
    return any(k in query.lower() for k in allowed_keywords)