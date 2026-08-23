# src/inventory_no_context.py
# โค้ดที่สร้างโดย AI ก่อนมีไฟล์ .ai-rules.md (มีปัญหาการออกแบบ / Monolith / ละเมิด SOLID)

class InventorySystem:
    def __init__(self):
        # รวมทุกอย่างไว้ในที่เดียว ไม่แยก Class หรือ Models
        self.products = {
            "P01": {"name": "สายไฟ 2.5 sq.mm", "qty": 20, "price": 120.0, "cat": "Electrical", "threshold": 15},
            "P02": {"name": "คีมปอกสายไฟ", "qty": 10, "price": 250.0, "cat": "Hand Tools", "threshold": 5}
        }
        self.manager_email = "manager@store.com"
        self.manager_phone = "0812345678"

    def issue(self, pid, amount):
        # ปน Business Logic, I/O และ Notification เข้าด้วยกัน (ละเมิด SRP)
        if pid not in self.products:
            print("Error: ไม่พบสินค้า")
            return False
            
        if self.products[pid]["qty"] < amount:
            print("Error: สินค้าคงเหลือไม่พอ")
            return False
            
        self.products[pid]["qty"] -= amount
        print(f"จ่ายสินค้า {self.products[pid]['name']} จำนวน {amount} คงเหลือ {self.products[pid]['qty']}")

        # Hardcode notification channel และ coupling โดยตรง (ละเมิด OCP, DIP)
        if self.products[pid]["qty"] < self.products[pid]["threshold"]:
            print(f"[Email to {self.manager_email}] แจ้งเตือน: สินค้า {self.products[pid]['name']} สต็อกต่ำกว่า {self.products[pid]['threshold']} คงเหลือ {self.products[pid]['qty']}")
            print(f"[SMS to {self.manager_phone}] แจ้งเตือน: สินค้า {self.products[pid]['name']} สต็อกต่ำ!")

        return True

    def report(self):
        # คำนวณและพิมพ์ผลรวมไปพร้อมกัน
        total = 0
        cat_totals = {}
        for p in self.products.values():
            val = p["qty"] * p["price"]
            total += val
            cat = p["cat"]
            cat_totals[cat] = cat_totals.get(cat, 0) + val
            
        print("=== รายงานมูลค่าสต็อก ===")
        for c, val in cat_totals.items():
            print(f"หมวดหมู่ {c}: {val:,.2f} บาท")
        print(f"มูลค่ารวมทั้งหมด: {total:,.2f} บาท")

if __name__ == "__main__":
    inv = InventorySystem()
    inv.issue("P01", 8) # สต็อกเหลือ 12 (< 15) -> แจ้งเตือน
    inv.report()
