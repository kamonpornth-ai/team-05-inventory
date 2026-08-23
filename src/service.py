"""
โมดูลสำหรับจัดการ Business Logic ของระบบสต็อกสินค้า (Inventory Service)
"""
import os
import sys

# รองรับการรันจากทั้ง root directory และจากภายในโฟลเดอร์ src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from typing import Dict, List, Optional, Tuple
from datetime import datetime
import uuid

try:
    from src.models import Product, StockTransaction
    from src.notifiers import Notifier, NotifierFactory
except ModuleNotFoundError:
    from models import Product, StockTransaction
    from notifiers import Notifier, NotifierFactory

class InventoryService:
    """Service จัดการสต็อกสินค้าตามหลัก SOLID และ Observer Pattern"""

    def __init__(self, observers: Optional[List[Notifier]] = None):
        """
        สร้าง InventoryService พร้อมรับ Dependency Observers
        
        Args:
            observers: รายการผู้รับการแจ้งเตือน (Notifiers)
        """
        self._products: Dict[str, Product] = {}
        self._transactions: List[StockTransaction] = []
        self._observers: List[Notifier] = observers or []

    def attach_observer(self, observer: Notifier) -> None:
        """เพิ่มผู้รับการแจ้งเตือนใหม่ (Observer)"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach_observer(self, observer: Notifier) -> None:
        """ถอดผู้รับการแจ้งเตือนออก"""
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify_low_stock(self, product: Product) -> None:
        """กระจายการแจ้งเตือนไปยัง Observers ทุกตัวเมื่อสต็อกต่ำกว่าเกณฑ์"""
        message = f"แจ้งเตือน: สต็อกสินค้า '{product.name}' ต่ำกว่าเกณฑ์ขั้นต่ำ!"
        metadata = {
            "product_id": product.id,
            "product_name": product.name,
            "current_stock": product.quantity,
            "threshold": product.threshold
        }
        for observer in self._observers:
            observer.send(message, metadata)

    def add_product(self, product: Product) -> None:
        """เพิ่มสินค้าใหม่เข้าระบบ"""
        if product.id in self._products:
            raise ValueError(f"รหัสสินค้าซ้ำ: {product.id}")
        self._products[product.id] = product

    def get_product(self, product_id: str) -> Optional[Product]:
        """ค้นหาข้อมูลสินค้าตาม ID"""
        return self._products.get(product_id)

    def receive_stock(self, product_id: str, amount: int, note: Optional[str] = None) -> bool:
        """
        บันทึกการรับสินค้าเข้าสต็อก
        
        Args:
            product_id: รหัสสินค้า
            amount: จำนวนที่รับเข้า (ต้องมากกว่า 0)
        """
        if amount <= 0:
            raise ValueError("จำนวนรับเข้าต้องมากกว่า 0")

        product = self._products.get(product_id)
        if not product:
            raise KeyError(f"ไม่พบสินค้ารหัส: {product_id}")

        product.quantity += amount
        
        # บันทึกประวัติ Transaction
        tx = StockTransaction(
            id=str(uuid.uuid4())[:8],
            product_id=product_id,
            transaction_type="RECEIVE",
            amount=amount,
            balance_after=product.quantity,
            note=note
        )
        self._transactions.append(tx)
        return True

    def issue_stock(self, product_id: str, amount: int, note: Optional[str] = None) -> bool:
        """
        บันทึกการจ่ายสินค้าออกจากสต็อก พร้อมเช็คการแจ้งเตือนสต็อกต่ำ
        
        Args:
            product_id: รหัสสินค้า
            amount: จำนวนที่จ่ายออก (ต้องมากกว่า 0)
        """
        if amount <= 0:
            raise ValueError("จำนวนจ่ายออกต้องมากกว่า 0")

        product = self._products.get(product_id)
        if not product:
            raise KeyError(f"ไม่พบสินค้ารหัส: {product_id}")

        if product.quantity < amount:
            return False  # ปฏิเสธรายการเนื่องจากสต็อกไม่พอ (ไม่ให้ติดลบ)

        product.quantity -= amount
        
        # บันทึกประวัติ Transaction
        tx = StockTransaction(
            id=str(uuid.uuid4())[:8],
            product_id=product_id,
            transaction_type="ISSUE",
            amount=amount,
            balance_after=product.quantity,
            note=note
        )
        self._transactions.append(tx)

        # ตรวจสอบเงื่อนไขสต็อกต่ำ (Strictly less than threshold)
        if product.is_low_stock():
            self._notify_low_stock(product)

        return True

    def calculate_valuation_report(self) -> Tuple[Dict[str, float], float]:
        """
        คำนวณมูลค่าสต็อกสินค้าแยกตามหมวดหมู่และยอดรวมทั้งสิ้น
        
        Returns:
            Tuple[Dict[category_name, category_total_value], grand_total_value]
        """
        category_totals: Dict[str, float] = {}
        grand_total: float = 0.0

        for product in self._products.values():
            val = product.calculate_value()
            grand_total += val
            category_totals[product.category] = category_totals.get(product.category, 0.0) + val

        return category_totals, grand_total

if __name__ == "__main__":
    # 1. เตรียม Observers ผ่าน Factory
    email_obs = NotifierFactory.create("email", "manager@eng-store.com")
    sms_obs = NotifierFactory.create("sms", "089-999-8888")

    # 2. เริ่มต้น Service พร้อม Dependency Injection
    service = InventoryService(observers=[email_obs, sms_obs])

    # 3. เพิ่มสินค้า
    service.add_product(Product(id="P01", name="สายไฟ 2.5 sq.mm", category="Electrical", unit_price=120.0, quantity=20, threshold=15))
    service.add_product(Product(id="P02", name="คีมปอกสายไฟ", category="Hand Tools", unit_price=250.0, quantity=10, threshold=5))

    print("--- ทดสอบจ่ายสินค้าให้สต็อกต่ำกว่าเกณฑ์ ---")
    service.issue_stock("P01", 8) # เดิม 20 จ่าย 8 เหลือ 12 (< 15) -> Trigger Alerts!

    print("\n--- รายงานมูลค่าสต็อกแยกตามหมวดหมู่ ---")
    cat_totals, grand_total = service.calculate_valuation_report()
    for cat, total in cat_totals.items():
        print(f"หมวดหมู่ {cat}: {total:,.2f} บาท")
    print(f"มูลค่ารวมทั้งสิ้น: {grand_total:,.2f} บาท")
