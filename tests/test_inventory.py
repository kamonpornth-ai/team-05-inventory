"""
Unit tests สำหรับคลาส Inventory ใน inventory.py
ประกอบด้วย:
1. TDD tests สำหรับเมธอด low_stock_items (6 กรณี)
2. Unit tests และ Edge cases สำหรับเมธอด sell และเมธอดพื้นฐาน
"""
import pytest
from inventory import Inventory, InventoryItem


# =====================================================================
# ส่วนที่ 1: TDD tests สำหรับ low_stock_items(threshold) ครบ 6 กรณี
# =====================================================================

def test_low_stock_items_all_above_threshold():
    """กรณีที่ 1: สินค้าทุกรายการมีจำนวนมากกว่า threshold -> คืน list ว่าง"""
    inv = Inventory()
    inv.add_item("สินค้า A", 15, 100.0)
    inv.add_item("สินค้า B", 20, 200.0)
    assert inv.low_stock_items(10) == []


def test_low_stock_items_exact_threshold():
    """กรณีที่ 2: มีสินค้าที่จำนวนเท่ากับ threshold พอดี -> ต้องถูกนับรวมด้วย (<= threshold)"""
    inv = Inventory()
    inv.add_item("สินค้า A", 10, 100.0)
    inv.add_item("สินค้า B", 25, 200.0)
    assert inv.low_stock_items(10) == ["สินค้า A"]


def test_low_stock_items_multiple_sorted_by_name():
    """กรณีที่ 3: มีสินค้าเข้าเกณฑ์หลายรายการ -> ผลลัพธ์ต้องเรียงตามชื่อ ไม่ใช่ตามลำดับที่เพิ่ม"""
    inv = Inventory()
    inv.add_item("ยางลบ", 3, 10.0)
    inv.add_item("กรรไกร", 5, 50.0)
    inv.add_item("ดินสอ", 2, 15.0)
    inv.add_item("สมุด", 20, 30.0)
    # ทั้ง ยางลบ (3), กรรไกร (5), ดินสอ (2) เข้าเกณฑ์ threshold=5
    # ต้องเรียงตามตัวอักษร: กรรไกร, ดินสอ, ยางลบ
    assert inv.low_stock_items(5) == ["กรรไกร", "ดินสอ", "ยางลบ"]


def test_low_stock_items_empty_inventory():
    """กรณีที่ 4: คลังว่าง -> คืน list ว่าง ไม่ใช่ error"""
    inv = Inventory()
    assert inv.low_stock_items(10) == []


def test_low_stock_items_threshold_zero():
    """กรณีที่ 5: threshold เป็น 0 -> คืนเฉพาะสินค้าที่เหลือ 0 ชิ้น"""
    inv = Inventory()
    inv.add_item("สินค้า หมด", 0, 100.0)
    inv.add_item("สินค้า เหลือ 1", 1, 100.0)
    assert inv.low_stock_items(0) == ["สินค้า หมด"]


def test_low_stock_items_negative_threshold():
    """กรณีที่ 6: threshold ติดลบ -> คืน list ว่าง เนื่องจากสินค้าไม่สามารถมีสต็อกติดลบได้"""
    inv = Inventory()
    inv.add_item("สินค้า A", 0, 100.0)
    inv.add_item("สินค้า B", 10, 200.0)
    assert inv.low_stock_items(-1) == []


# =====================================================================
# ส่วนที่ 2: Unit tests และ Edge cases สำหรับเมธอด sell และฟังก์ชันพื้นฐาน
# =====================================================================

def test_sell_basic_success():
    """กรณีปกติ: ขายสำเร็จ ยอดสต็อกลดลงตามจำนวน"""
    inv = Inventory()
    inv.add_item("ปากกา", 50, 10.0)
    remaining = inv.sell("ปากกา", 20)
    assert remaining == 30


def test_sell_exact_all_remaining():
    """Edge case 1 (ค่าขอบ): ขายเท่ากับจำนวนคงเหลือทั้งหมด -> สต็อกเหลือ 0 พอดี"""
    inv = Inventory()
    inv.add_item("ปากกา", 10, 10.0)
    remaining = inv.sell("ปากกา", 10)
    assert remaining == 0


def test_sell_zero_amount():
    """Edge case 2 (ค่าที่ไม่ควรรับ): ขายจำนวน 0 -> ต้อง raise ValueError"""
    inv = Inventory()
    inv.add_item("ปากกา", 10, 10.0)
    with pytest.raises(ValueError, match="จำนวนที่ขายต้องมากกว่าศูนย์"):
        inv.sell("ปากกา", 0)


def test_sell_negative_amount():
    """Edge case 3 (ค่าที่ไม่ควรรับ): ขายจำนวนติดลบ -> ต้อง raise ValueError"""
    inv = Inventory()
    inv.add_item("ปากกา", 10, 10.0)
    with pytest.raises(ValueError, match="จำนวนที่ขายต้องมากกว่าศูนย์"):
        inv.sell("ปากกา", -5)


def test_sell_insufficient_stock():
    """Edge case 4 (ค่าที่ไม่ควรรับ): ขายเกินจำนวนคงเหลือ -> ต้อง raise ValueError"""
    inv = Inventory()
    inv.add_item("ปากกา", 5, 10.0)
    with pytest.raises(ValueError, match="ไม่เพียงพอสำหรับการขาย"):
        inv.sell("ปากกา", 10)


def test_sell_non_existent_item():
    """Edge case 5 (เส้นทาง error): ขายสินค้าที่ไม่มีในระบบ -> ต้อง raise KeyError"""
    inv = Inventory()
    with pytest.raises(KeyError, match="ไม่พบสินค้า"):
        inv.sell("สินค้าผี", 1)


# =====================================================================
# ส่วนที่ 3: Unit tests สำหรับ InventoryItem, add_item, restock, get_total_value
# =====================================================================

def test_inventory_item_validation():
    """ทดสอบ validation ของ InventoryItem"""
    with pytest.raises(ValueError, match="ชื่อสินค้าต้องไม่ว่างเปล่า"):
        InventoryItem("", 10, 100.0)
    with pytest.raises(ValueError, match="จำนวนสินค้าต้องไม่ติดลบ"):
        InventoryItem("A", -1, 100.0)
    with pytest.raises(ValueError, match="ราคาต้องมากกว่าศูนย์"):
        InventoryItem("A", 10, 0.0)


def test_add_item_duplicate():
    """ทดสอบเพิ่มสินค้าซ้ำชื่อเดิม -> ต้อง raise ValueError"""
    inv = Inventory()
    inv.add_item("สมุด", 10, 20.0)
    with pytest.raises(ValueError, match="มีอยู่ในระบบแล้ว"):
        inv.add_item("สมุด", 5, 20.0)


def test_restock_success_and_errors():
    """ทดสอบ restock ทั้งกรณีปกติและ error cases"""
    inv = Inventory()
    inv.add_item("สมุด", 10, 20.0)
    assert inv.restock("สมุด", 15) == 25
    with pytest.raises(KeyError):
        inv.restock("ไม่มี", 5)
    with pytest.raises(ValueError):
        inv.restock("สมุด", 0)


def test_get_total_value():
    """ทดสอบคำนวณมูลค่ารวมทั้งหมด"""
    inv = Inventory()
    assert inv.get_total_value() == 0.0
    inv.add_item("A", 10, 50.0)  # 500
    inv.add_item("B", 5, 100.0)  # 500
    assert inv.get_total_value() == 1000.0
