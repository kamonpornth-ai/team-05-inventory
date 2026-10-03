# Debug Log - Lab 04

## 1. Reproduce (ก่อนแก้)

```
============================= test session starts ==============================
platform linux -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0 -- /home/codespace/.python/current/bin/python
cachedir: .pytest_cache
rootdir: /workspaces/team-05-inventory/lab04-ai-coding-ux/66332110169-3
plugins: anyio-4.15.1
collecting ... collected 6 items

tests/test_discount.py::test_apply_discount_basic FAILED                 [ 16%]
tests/test_discount.py::test_apply_discount_zero PASSED                  [ 33%]
tests/test_discount.py::test_bulk_total FAILED                           [ 50%]
tests/test_discount.py::test_average_price PASSED                        [ 66%]
tests/test_discount.py::test_average_price_empty FAILED                  [ 83%]
tests/test_discount.py::test_cheapest_n FAILED                           [100%]

=================================== FAILURES ===================================
__________________________ test_apply_discount_basic ___________________________

    def test_apply_discount_basic():
        # ลด 10% จาก 100 บาท ควรเหลือ 90 บาท
>       assert apply_discount(100.0, 10) == 90.0
E       assert 99.9 == 90.0
E        +  where 99.9 = apply_discount(100.0, 10)

tests/test_discount.py:8: AssertionError
_______________________________ test_bulk_total ________________________________

    def test_bulk_total():
        # (100 + 100 + 100) = 300 ลด 10% ควรเหลือ 270
>       assert bulk_total([100.0, 100.0, 100.0], 10) == 270.0
E       assert 299.9 == 270.0
E        +  where 299.9 = bulk_total([100.0, 100.0, 100.0], 10)

tests/test_discount.py:18: AssertionError
___________________________ test_average_price_empty ___________________________

    def test_average_price_empty():
        # คลังว่างควรได้ 0.0 ไม่ใช่ crash
>       assert average_price([]) == 0.0
               ^^^^^^^^^^^^^^^^^

tests/test_discount.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

prices = []

    def average_price(prices: list) -> float:
        """คืนราคาเฉลี่ยของรายการสินค้า"""
>       return sum(prices) / len(prices)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
E       ZeroDivisionError: division by zero

discount.py:18: ZeroDivisionError
_______________________________ test_cheapest_n ________________________________

    def test_cheapest_n():
        # ถูกสุด 2 รายการของ [50, 10, 30, 20] = [10, 20]
>       assert cheapest_n([50.0, 10.0, 30.0, 20.0], 2) == [10.0, 20.0]
E       assert [20.0] == [10.0, 20.0]
E         
E         At index 0 diff: 20.0 != 10.0
E         Right contains one more item: 20.0
E         
E         Full diff:
E           [
E         -     10.0,
E               20.0,
E           ]

tests/test_discount.py:33: AssertionError
=========================== short test summary info ============================
FAILED tests/test_discount.py::test_apply_discount_basic - assert 99.9 == 90.0
FAILED tests/test_discount.py::test_bulk_total - assert 299.9 == 270.0
FAILED tests/test_discount.py::test_average_price_empty - ZeroDivisionError: ...
FAILED tests/test_discount.py::test_cheapest_n - assert [20.0] == [10.0, 20.0]
========================= 4 failed, 2 passed in 0.04s ==========================


## 2. test_apply_discount_basic
- Assertion ที่เห็น: assert 99.9 == 90.0
- คิดเลขมือ: 10 / 100 = 0.1 แล้ว 100.0 - 0.1 = 99.9 (ตรงกับที่ pytest แสดง)
- ลด 10% จาก 100 บาท ควรหักออก: 10 บาท
- โค้ดหักออกไป: 0.1 บาท
- สมมติฐาน: น่าจะผิดเพราะคำนวณมูลค่าส่วนลดผิด โดยนำเปอร์เซ็นต์ส่วนลด (10) ไปหาร 100 แล้วเอาค่าที่ได้ (0.1) ไปลบออกจากราคาตั้งต้นโดยตรง แทนที่จะนำไปคูณกับราคาตั้งต้นก่อน
- วิธียืนยัน: รันใน terminal 3 คำสั่งโดยไม่แก้ไฟล์ ได้ 0.1, 99.9 และ 90.0 ตามลำดับ แปลว่าสูตรเดิมหักส่วนลดแค่ 0.1 บาท ส่วนสูตรที่คูณ percent กับราคาก่อนหารด้วย 100 ให้ 90.0 ตรงกับ test สมมติฐานถูกต้อง

## 3. test_bulk_total
- Assertion ที่เห็น: assert 299.9 == 270.0
- สมมติฐาน: น่าจะเกิดจาก root cause เดียวกับข้อ 2 เพราะ `bulk_total` เรียก `apply_discount` ข้างใน (ทำให้ลบออกแค่ 0.1 แทนที่จะลบส่วนลด 10%)
- วิธียืนยัน: แก้ `apply_discount` บรรทัดเดียว แล้วรัน test ทั้งชุด ผลคือ `test_bulk_total` ผ่านโดยไม่ได้แก้โค้ดใน `bulk_total` เลย
- ที่ทายไว้: ไม่ได้ทายไว้ก่อนรัน | ผลจริง: ผ่าน (สมมติฐานถูกต้อง)

## 4. test_average_price_empty
- Assertion ที่เห็น: ZeroDivisionError: division by zero
- ผล sum([]) และ len([]): 0 และ 0
- สมมติฐาน: น่าจะผิดเพราะฟังก์ชันไม่ได้เช็กก่อนว่าลิสต์ว่างหรือไม่ เมื่อใส่ลิสต์ว่างเข้ามาจึงเกิดการหารด้วย 0 (`len(prices)` เป็น 0)
- วิธียืนยัน: จำลองการทำงาน `sum([]) / len([])` พบ Error เดียวกัน จากนั้นแก้โค้ดโดยเพิ่มเงื่อนไข `if not prices: return 0.0` ดักไว้ก่อน แล้วรัน pytest ใหม่ พบว่าผ่าน (Passed) สมมติฐานถูกต้อง

## 6. test_cheapest_n
- Assertion ที่เห็น: assert [20.0] == [10.0, 20.0]
- สมมติฐาน: ฟังก์ชันน่าจะใช้ index ในการตัดลิสต์ (Slicing) ผิด โดยเริ่มที่ 1 แทนที่จะเริ่มที่ 0 ทำให้ข้ามค่าที่ถูกที่สุดไป
- วิธียืนยัน: เปิดดูโค้ดพบ `ordered[1:n]` จึงแก้ไขเป็น `ordered[:n]` เพื่อให้เริ่มดึงข้อมูลตั้งแต่ตัวแรกสุด จากนั้นรัน pytest ใหม่ พบว่าผ่านทั้งหมด (6 passed) สมมติฐานถูกต้อง









