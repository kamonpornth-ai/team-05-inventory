"""
Characterization Tests สำหรับ pricing_legacy.py
มีหน้าที่บันทึกพฤติกรรมจริงของโค้ดเดิมทุกกรณี ก่อนเริ่มการ Refactor
"""
import datetime

import pytest

import pricing_legacy


@pytest.fixture(autouse=True)
def reset_globals():
    """ล้างค่า Global State (member_points และ LOG) ก่อนเริ่มทุก Test Case"""
    pricing_legacy.member_points.clear()
    pricing_legacy.LOG.clear()
    yield
    pricing_legacy.member_points.clear()
    pricing_legacy.LOG.clear()


# =====================================================================
# 1. กลุ่มราคาปกติ (Regular Price - No Discount)
# =====================================================================

def test_regular_single_item():
    """สินค้า 1 รายการ จำนวนปกติ ไม่ใช้สิทธิ์ใด ๆ (ภาษี 7%)"""
    # 10 * 20.0 = 200.0 -> + 7% VAT = 214.0
    items = [("ปากกา", 10, 20.0)]
    assert pricing_legacy.calc(items) == 214.0


def test_regular_multiple_items():
    """สินค้าหลายรายการ จำนวนปกติ"""
    # (10 * 20.0) + (5 * 50.0) = 200 + 250 = 450.0 -> + 7% VAT = 481.5
    items = [("ปากกา", 10, 20.0), ("สมุด", 5, 50.0)]
    assert pricing_legacy.calc(items) == 481.5


# =====================================================================
# 2. กลุ่มซื้อจำนวนมาก (Tiered Bulk Quantity Discounts)
# =====================================================================

def test_bulk_discount_tier_50():
    """จำนวน 50 ชิ้นพอดี -> ได้รับส่วนลด 5% เฉพาะรายการนั้น"""
    # 50 * 10.0 = 500.0 * 0.95 = 475.0 -> + 7% VAT = 508.25
    items = [("สมุด", 50, 10.0)]
    assert pricing_legacy.calc(items) == 508.25


def test_bulk_discount_tier_100():
    """จำนวน 100 ชิ้นพอดี -> ได้รับส่วนลด 10% เฉพาะรายการนั้น"""
    # 100 * 10.0 = 1000.0 * 0.90 = 900.0 -> + 7% VAT = 963.0
    items = [("ยางลบ", 100, 10.0)]
    assert pricing_legacy.calc(items) == 963.0


# =====================================================================
# 3. กลุ่มจำนวนเป็นศูนย์หรือติดลบ (Zero and Negative Quantities)
# =====================================================================

def test_zero_and_negative_quantity_items():
    """รายการที่มีจำนวน <= 0 จะถูกข้าม ไม่นำมาคิดราคา"""
    items = [("ปากกา", 0, 100.0), ("ดินสอ", -5, 50.0)]
    assert pricing_legacy.calc(items) == 0.0


# =====================================================================
# 4. กลุ่มสมาชิก (Member Discount and Point Accrual)
# =====================================================================

def test_member_discount_and_points():
    """สมาชิกได้รับส่วนลด 5% และสะสมแต้ม 1 แต้มต่อ 100 บาท (คำนวณก่อนภาษี)"""
    # 10 * 100.0 = 1000.0 -> ลดสมาชิก 5% = 950.0 -> แต้ม = int(950/100) = 9
    # ยอดรวมหลังภาษี = 950 * 1.07 = 1016.50
    items = [("สายไฟ", 10, 100.0)]
    result = pricing_legacy.calc(items, member="Somchai")
    assert result == 1016.50
    assert pricing_legacy.member_points["Somchai"] == 9


def test_member_points_accumulation():
    """สมาชิกซื้อซ้ำ แต้มต้องสะสมต่อเนื่อง"""
    items1 = [("สายไฟ", 10, 100.0)] # 9 แต้ม
    pricing_legacy.calc(items1, member="Somchai")
    items2 = [("สายไฟ", 5, 100.0)]  # 5 * 100 = 500 * 0.95 = 475 -> 4 แต้ม
    pricing_legacy.calc(items2, member="Somchai")
    assert pricing_legacy.member_points["Somchai"] == 13


# =====================================================================
# 5. กลุ่มคูปองส่วนลด (Coupon Codes)
# =====================================================================

def test_coupon_save50():
    """คูปอง SAVE50: ลด 50 บาทตรง ๆ"""
    # 10 * 20.0 = 200.0 -> - 50 = 150.0 -> + 7% VAT = 160.50
    items = [("ปากกา", 10, 20.0)]
    assert pricing_legacy.calc(items, coupon="SAVE50") == 160.50


def test_coupon_half():
    """คูปอง HALF: ลด 50%"""
    # 10 * 20.0 = 200.0 -> * 0.5 = 100.0 -> + 7% VAT = 107.0
    items = [("ปากกา", 10, 20.0)]
    assert pricing_legacy.calc(items, coupon="HALF") == 107.0


def test_coupon_newyear_in_january():
    """คูปอง NEWYEAR: ลด 20% เมื่อใช้วันที่อยู่ในเดือนมกราคม (month == 1)"""
    # 10 * 20.0 = 200.0 -> * 0.8 = 160.0 -> + 7% VAT = 171.20
    items = [("ปากกา", 10, 20.0)]
    jan_date = datetime.date(2026, 1, 15)
    assert pricing_legacy.calc(items, coupon="NEWYEAR", today=jan_date) == 171.20


def test_coupon_newyear_outside_january():
    """คูปอง NEWYEAR: ไม่ได้รับส่วนลดถ้าไม่ได้อยู่ในเดือนมกราคม"""
    # 10 * 20.0 = 200.0 -> ไม่ลด = 200.0 -> + 7% VAT = 214.0
    items = [("ปากกา", 10, 20.0)]
    feb_date = datetime.date(2026, 2, 10)
    assert pricing_legacy.calc(items, coupon="NEWYEAR", today=feb_date) == 214.0


# =====================================================================
# 6. กลุ่มยอดติดลบและการปัดเศษ (Negative Clamping & Rounding)
# =====================================================================

def test_negative_total_clamped_to_zero():
    """หากส่วนลดมากกว่าราคาสินค้า ยอดรวมจะถูกปรับเป็น 0 (ไม่ติดลบ)"""
    # 1 * 30.0 = 30.0 -> - 50 = -20.0 -> ปรับเป็น 0.0 -> VAT = 0.0
    items = [("ปากกา", 1, 30.0)]
    assert pricing_legacy.calc(items, coupon="SAVE50") == 0.0


# =====================================================================
# 7. กลุ่มการบันทึก Log (Audit Log Side-effect)
# =====================================================================

def test_audit_log_recording():
    """ฟังก์ชัน calc ต้องบันทึกประวัติการคำนวณลงใน LOG ทุกครั้ง"""
    items = [("ปากกา", 10, 20.0)]
    res = pricing_legacy.calc(items, member="Alice")
    assert len(pricing_legacy.LOG) == 1
    assert pricing_legacy.LOG[0] == ("Alice", res)
