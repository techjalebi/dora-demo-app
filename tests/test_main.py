"""Tests for OrderFlow core logic."""

import pytest
from src.main import process_order, get_order_status
from src.utils import calculate_total, format_order_id, sanitize_sku


def test_process_order_success():
    items = [{"sku": "WIDGET-A", "qty": 2, "unit_price": 9.99}]
    order = process_order(items)
    assert order["order_id"].startswith("ORD-")
    assert order["total"] == 19.98
    assert order["status"] == "pending"


def test_process_order_empty_raises():
    with pytest.raises(ValueError):
        process_order([])


def test_calculate_total():
    items = [
        {"sku": "A", "qty": 3, "unit_price": 10.00},
        {"sku": "B", "qty": 1, "unit_price": 5.50},
    ]
    assert calculate_total(items) == 35.50


def test_format_order_id_format():
    oid = format_order_id()
    parts = oid.split("-")
    assert parts[0] == "ORD"
    assert len(parts) == 3


def test_sanitize_sku():
    assert sanitize_sku("  widget-a  ") == "WIDGET-A"


def test_get_order_status_invalid_id():
    with pytest.raises(ValueError):
        get_order_status("INVALID123")
