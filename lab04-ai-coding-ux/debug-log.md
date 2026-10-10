# บันทึกการ Debugging แบบมีหลักฐาน (Debug Log)

## รายการ Test ที่ไม่ผ่านและการวิเคราะห์ Root Cause ครบ 5 ขั้นตอน

### 1. Test ที่ไม่ผ่าน: `test_apply_discount_basic`
- **1. Reproduce:** `pytest tests/test_discount.py -v` -> `assert apply_discount(100.0, 10) == 90.0` เกิด `AssertionError: assert 99.9 == 90.0`
- **2. Traceback:** `discount.py:4` ใน `apply_discount`
- **3. สมมติฐาน:** สูตรคำนวณส่วนลดผิดพลาด โดยใช้ `price - percent / 100` ซึ่งเป็นการลบด้วยเศษส่วนตรง ๆ แทนที่จะเป็นการหักเปอร์เซ็นต์ออกจากราคา
- **4. การยืนยัน:** คำนวณ `100 - (10/100) = 99.9` ซึ่งตรงกับค่าที่ Traceback แสดงผลจริง
- **5. Root Cause & การแก้:** แก้สูตรเป็น `return price * (1.0 - (percent / 100.0))`

---

### 2. Test ที่ไม่ผ่าน: `test_bulk_total`
- **1. Reproduce:** `assert bulk_total([100.0, 100.0, 100.0], 10) == 270.0` เกิด `AssertionError: assert 299.9 == 270.0`
- **2. Traceback:** `discount.py:12` เรียก `apply_discount(total, discount_percent)`
- **3. สมมติฐาน:** เป็นผลกระทบต่อเนื่องมาจากสูตรคำนวณส่วนลดที่ผิดใน `apply_discount`
- **4. การยืนยัน:** เมื่อแก้ฟังก์ชัน `apply_discount` แล้ว test ข้อนี้ผ่านทันที
- **5. Root Cause & การแก้:** แก้ไขที่ฟังก์ชันต้นทาง `apply_discount`

---

### 3. Test ที่ไม่ผ่าน: `test_average_price_empty`
- **1. Reproduce:** `assert average_price([]) == 0.0` เกิด `ZeroDivisionError: division by zero`
- **2. Traceback:** `discount.py:17` ใน `average_price`: `return sum(prices) / len(prices)`
- **3. สมมติฐาน:** โค้ดไม่ได้ดักจับกรณี `prices` เป็น List ว่าง (`len == 0`) ทำให้เกิดการหารด้วยศูนย์
- **4. การยืนยัน:** ตรวจสอบความยาวของ `prices` ถ้าเป็น 0 ให้คืนค่า `0.0` ทันที
- **5. Root Cause & การแก้:** แก้เป็น `return sum(prices) / len(prices) if prices else 0.0`

---

### 4. Test ที่ไม่ผ่าน: `test_cheapest_n`
- **1. Reproduce:** `assert cheapest_n([50.0, 10.0, 30.0, 20.0], 2) == [10.0, 20.0]` เกิด `AssertionError: assert [20.0] == [10.0, 20.0]`
- **2. Traceback:** `discount.py:23` ใน `cheapest_n`: `return ordered[1:n]`
- **3. สมมติฐาน:** Slice ขอบเขตผิด โดยเริ่มที่ Index `1` ทำให้ข้ามตัวที่ถูกที่สุดตัวแรก (Index 0) ไป
- **4. การยืนยัน:** `sorted([50, 10, 30, 20]) = [10, 20, 30, 50]` ตัดช่วง `[1:2]` ได้ผลลัพธ์เป็น `[20]` ตัวเดียว
- **5. Root Cause & การแก้:** แก้ไข Slice เป็น `return ordered[:n]`
