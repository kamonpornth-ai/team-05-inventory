"""
โมดูลสำหรับกำหนด Data Models ของระบบจัดการสต็อกสินค้า
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Category:
    """ข้อมูลหมวดหมู่สินค้า"""
    id: str
    name: str

@dataclass
class Product:
    """ข้อมูลสินค้าและเกณฑ์แจ้งเตือนสต็อกต่ำ"""
    id: str
    name: str
    category: str
    unit_price: float
    quantity: int = 0
    threshold: int = 10

    def calculate_value(self) -> float:
        """คำนวณมูลค่ารวมของสินค้านี้"""
        return self.quantity * self.unit_price

    def is_low_stock(self) -> bool:
        """ตรวจสอบว่าสต็อกต่ำกว่าเกณฑ์หรือไม่ (น้อยกว่า strictly)"""
        return self.quantity < self.threshold

@dataclass
class StockTransaction:
    """บันทึกประวัติการรับเข้า-จ่ายออกสต็อก"""
    id: str
    product_id: str
    transaction_type: str  # "RECEIVE" หรือ "ISSUE"
    amount: int
    balance_after: int
    timestamp: datetime = datetime.now()
    note: Optional[str] = None
