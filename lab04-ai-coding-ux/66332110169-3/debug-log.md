#Debug Log - Lab 04

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
```
