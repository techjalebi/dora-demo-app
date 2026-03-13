"""Utility functions for OrderFlow."""

import uuid
from datetime import datetime


def format_order_id() -> str:
    """Generate a unique order identifier."""
    ts = datetime.utcnow().strftime("%Y%m%d")
    uid = str(uuid.uuid4())[:8].upper()
    return f"ORD-{ts}-{uid}"


def calculate_total(items: list[dict]) -> float:
    """Sum qty * unit_price across all items, rounded to 2 decimal places."""
    return round(sum(i["qty"] * i["unit_price"] for i in items), 2)


def sanitize_sku(sku: str) -> str:
    """Normalize a SKU string to uppercase, strip whitespace."""
    return sku.strip().upper()
