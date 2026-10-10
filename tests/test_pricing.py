"""
Unit & Characterization Tests สำหรับ pricing.py (Refactored Module)
ยืนยันว่าการทำงานของโมดูลใหม่ที่ Refactor แล้วตรงกับพฤติกรรมเดิม 100%
"""
import datetime

import pytest

import pricing


@pytest.fixture(autouse=True)
def reset_globals():
    """ล้างค่า State ก่อนเริ่มทุก Test"""
    pricing.member_points.clear()
    pricing.LOG.clear()
    yield
    pricing.member_points.clear()
    pricing.LOG.clear()


def test_refactored_regular_single_item():
    items = [("ปากกา", 10, 20.0)]
    assert pricing.calc(items) == 214.0


def test_refactored_regular_multiple_items():
    items = [("ปากกา", 10, 20.0), ("สมุด", 5, 50.0)]
    assert pricing.calc(items) == 481.5


def test_refactored_bulk_discount_tier_50():
    items = [("สมุด", 50, 10.0)]
    assert pricing.calc(items) == 508.25


def test_refactored_bulk_discount_tier_100():
    items = [("ยางลบ", 100, 10.0)]
    assert pricing.calc(items) == 963.0


def test_refactored_zero_and_negative_quantity_items():
    items = [("ปากกา", 0, 100.0), ("ดินสอ", -5, 50.0)]
    assert pricing.calc(items) == 0.0


def test_refactored_member_discount_and_points():
    items = [("สายไฟ", 10, 100.0)]
    result = pricing.calc(items, member="Somchai")
    assert result == 1016.50
    assert pricing.member_points["Somchai"] == 9


def test_refactored_member_points_accumulation():
    items1 = [("สายไฟ", 10, 100.0)]
    pricing.calc(items1, member="Somchai")
    items2 = [("สายไฟ", 5, 100.0)]
    pricing.calc(items2, member="Somchai")
    assert pricing.member_points["Somchai"] == 13


def test_refactored_coupon_save50():
    items = [("ปากกา", 10, 20.0)]
    assert pricing.calc(items, coupon="SAVE50") == 160.50


def test_refactored_coupon_half():
    items = [("ปากกา", 10, 20.0)]
    assert pricing.calc(items, coupon="HALF") == 107.0


def test_refactored_coupon_newyear_in_january():
    items = [("ปากกา", 10, 20.0)]
    jan_date = datetime.date(2026, 1, 15)
    assert pricing.calc(items, coupon="NEWYEAR", today=jan_date) == 171.20


def test_refactored_coupon_newyear_outside_january():
    items = [("ปากกา", 10, 20.0)]
    feb_date = datetime.date(2026, 2, 10)
    assert pricing.calc(items, coupon="NEWYEAR", today=feb_date) == 214.0


def test_refactored_negative_total_clamped_to_zero():
    items = [("ปากกา", 1, 30.0)]
    assert pricing.calc(items, coupon="SAVE50") == 0.0


def test_refactored_audit_log_recording():
    items = [("ปากกา", 10, 20.0)]
    res = pricing.calc(items, member="Alice")
    assert len(pricing.LOG) == 1
    assert pricing.LOG[0] == ("Alice", res)
