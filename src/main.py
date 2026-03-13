"""
OrderFlow — main application entry point.
A fictional order management service used as simulation target
for the DORA Reporting Platform demo.
"""

from src.config import settings
from src.utils import format_order_id, calculate_total


def process_order(items: list[dict]) -> dict:
    """Process a list of order items and return an order summary."""
    if not items:
        raise ValueError("Order must contain at least one item")

    total = calculate_total(items)
    order_id = format_order_id()

    return {
        "order_id": order_id,
        "items": items,
        "total": total,
        "currency": settings["currency"],
        "status": "pending",
    }


def get_order_status(order_id: str) -> str:
    """Return the current status of an order."""
    # Stub: in a real app this would query a database
    if not order_id.startswith("ORD-"):
        raise ValueError(f"Invalid order ID format: {order_id}")
    return "pending"


if __name__ == "__main__":
    sample_items = [
        {"sku": "WIDGET-A", "qty": 2, "unit_price": 9.99},
        {"sku": "WIDGET-B", "qty": 1, "unit_price": 24.99},
    ]
    order = process_order(sample_items)
    print(f"Order created: {order['order_id']} — Total: {order['total']}")
