"""
โมดูลคำนวณราคาและส่วนลดของระบบ Inventory (Refactored Clean Code Version)
ผ่านการ Refactor จาก pricing_legacy.py โดยยึดหลัก Clean Code, SOLID และ Type Hints
โดยยังคงพฤติกรรมและการทำงานเดิมไว้ครบถ้วน 100% ตาม Characterization Tests
"""
from __future__ import annotations

import datetime

# =====================================================================
# ค่าคงที่ทางธุรกิจ (Named Business Constants)
# =====================================================================
DEFAULT_TAX_RATE: float = 0.07

BULK_DISCOUNT_TIER_1_QTY: int = 50
BULK_DISCOUNT_TIER_1_MULTIPLIER: float = 0.95  # ลด 5%

BULK_DISCOUNT_TIER_2_QTY: int = 100
BULK_DISCOUNT_TIER_2_MULTIPLIER: float = 0.90  # ลด 10%

MEMBER_DISCOUNT_MULTIPLIER: float = 0.95        # สมาชิกลด 5%
MEMBER_POINTS_SPEND_PER_POINT: int = 100       # 1 แต้มต่อ 100 บาท

# State ระดับโมดูลเพื่อ Backward Compatibility กับระบบเดิม
member_points: dict[str, int] = {}
LOG: list[tuple[str | None, float]] = []


# =====================================================================
# Helper Functions แยกตาม Single Responsibility Principle (SRP)
# =====================================================================

def calculate_item_subtotal(name: str, quantity: int, unit_price: float) -> float:
    """
    คำนวณราคาย่อยของสินค้าแต่ละรายการ พร้อมคิดส่วนลดซื้อส่ง (Bulk Discount)
    """
    if quantity <= 0:
        return 0.0

    subtotal = quantity * unit_price
    if quantity >= BULK_DISCOUNT_TIER_2_QTY:
        subtotal *= BULK_DISCOUNT_TIER_2_MULTIPLIER
    elif quantity >= BULK_DISCOUNT_TIER_1_QTY:
        subtotal *= BULK_DISCOUNT_TIER_1_MULTIPLIER

    return subtotal


def calculate_cart_subtotal(items: list[tuple[str, int, float]]) -> float:
    """คำนวณยอดรวมของสินค้าทั้งหมดในตะกร้า"""
    total = 0.0
    for item in items:
        name, quantity, price = item[0], item[1], item[2]
        total += calculate_item_subtotal(name, quantity, price)
    return total


def apply_member_discount_and_points(
    total: float,
    member: str | None,
    points_repo: dict[str, int]
) -> float:
    """คำนวณส่วนลดสมาชิกและบันทึกแต้มสะสม"""
    if member is None:
        return total

    if member not in points_repo:
        points_repo[member] = 0

    discounted_total = total * MEMBER_DISCOUNT_MULTIPLIER
    points_repo[member] += int(discounted_total / MEMBER_POINTS_SPEND_PER_POINT)
    return discounted_total


def apply_coupon_discount(
    total: float,
    coupon: str | None,
    today: datetime.date | None = None
) -> float:
    """คำนวณส่วนลดตามเงื่อนไขของรหัสคูปอง"""
    if coupon is None:
        return total

    if coupon == "SAVE50":
        return total - 50.0
    elif coupon == "HALF":
        return total * 0.5
    elif coupon == "NEWYEAR":
        check_date = today if today is not None else datetime.date.today()
        if check_date.month == 1:
            return total * 0.8

    return total


def apply_tax_and_rounding(total: float, tax_rate: float = DEFAULT_TAX_RATE) -> float:
    """ปรับยอดไม่ให้ติดลบ บวกภาษีมูลค่าเพิ่ม และปัดเศษทศนิยม 2 ตำแหน่ง"""
    if total < 0.0:
        total = 0.0

    with_tax = total + (total * tax_rate)
    return round(with_tax, 2)


# =====================================================================
# Main Calculation Entrypoint
# =====================================================================

def calc(
    items: list[tuple[str, int, float]],
    member: str | None = None,
    coupon: str | None = None,
    today: datetime.date | None = None
) -> float:
    """
    คำนวณราคาสุทธิหลังหักส่วนลดทุกประเภทและรวมภาษี
    
    Args:
        items: รายการสินค้า list ของ tuple (ชื่อ, จำนวน, ราคาต่อหน่วย)
        member: ชื่อสมาชิก (ถ้ามี)
        coupon: รหัสคูปอง (ถ้ามี)
        today: วันที่สำหรับเช็คสิทธิ์คูปอง (ถ้าไม่ระบุใช้วันนี้)
        
    Returns:
        ราคาสุทธิหลังรวมภาษีและปัดเศษ 2 ตำแหน่ง
    """
    # 1. ยอดรวมสินค้าพร้อมส่วนลดซื้อส่ง
    total = calculate_cart_subtotal(items)

    # 2. ส่วนลดสมาชิกและสะสมแต้ม
    total = apply_member_discount_and_points(total, member, member_points)

    # 3. ส่วนลดคูปอง
    total = apply_coupon_discount(total, coupon, today)

    # 4. ปรับยอดไม่ให้ติดลบ บวกภาษี และปัดเศษ
    final_price = apply_tax_and_rounding(total, DEFAULT_TAX_RATE)

    # 5. บันทึก Transaction Log
    LOG.append((member, final_price))

    return final_price
