# AI Iteration Log: บันทึกการพัฒนาด้วย Spec-Driven & Context Engineering

## 1. ข้อมูลเครื่องมือ AI ที่ใช้
- **AI Model / Assistant:** Gemini 3.7 / Antigravity Agent
- **วัตถุประสงค์:** ฝึกการควบคุมคุณภาพผลลัพธ์ของ AI ผ่าน Spec และ Context Rule โดยไม่แก้โค้ดด้วยมือ

---

## 2. ตารางเปรียบเทียบผลลัพธ์ ก่อน vs หลัง มี Context (.ai-rules.md)

| มิติการเปรียบเทียบ | ก่อนมี Context (`src/inventory_no_context.py`) | หลังมี Context (`src/models.py`, `src/notifiers.py`, `src/service.py`) |
|---|---|---|
| **โครงสร้างไฟล์ / การแยกหน้าที่** | รวมทุกอย่างไว้ในไฟล์เดียว (Monolith) Class เดียวทำทุกหน้าที่ | แยกไฟล์ชัดเจนตามหน้าที่ (`models`, `notifiers`, `service`) ตามหลัก SRP |
| **Type Hints & Docstrings** | ไม่มี Type Hints และไม่มี Docstrings | มี Type Hints ครบทุก Signature พร้อม Docstring ภาษาไทย |
| **ความผูกพันของโค้ด (Coupling)** | `InventorySystem` ผูกติดกับ Email/SMS โดยตรง (Hardcoded) | `InventoryService` รับ Abstraction ผ่าน Dependency Injection (DIP) |
| **การขยายระบบ (Extensibility)** | ถ้าเพิ่มช่องทางใหม่ต้องแก้โค้ดเก่า (ละเมิด OCP) | เพิ่ม Notifier คลาสใหม่ได้ทันทีผ่าน Observer Pattern |
| **การจัดการ Config** | Hardcode เบอร์โทรและอีเมลไว้ในคลาส | รับ Parameter และ Metadata แบบไดนามิก |

---

## 3. บันทึกรอบการปรับปรุง (Iteration Cycles)

### 🔁 รอบที่ 1: การจัดการเงื่อนไข Threshold เท่ากันพอดี (Edge Case)
* **ปัญหาที่พบ:** AI ตีความคำว่า "สต็อกต่ำกว่าเกณฑ์" เป็น `<= threshold` ทำให้เมื่อสต็อกเหลือ 15 เท่ากับ threshold พอดี ระบบกลับส่งแจ้งเตือน
* **การวิเคราะห์สาเหตุ:** เกิดจาก `specs/spec.md` ในตอนแรกเขียนว่า "เมื่อสต็อกต่ำกว่า threshold" โดยไม่ได้ระบุเงื่อนไขทางคณิตศาสตร์ที่ชัดเจน
* **การแก้ไขที่ต้นทาง (Spec):** เพิ่ม Acceptance Criteria กรณี Edge Case ใน `specs/spec.md`:
  > *"Scenario: จ่ายสินค้าโดยสต็อกหลังจ่ายเท่ากับ threshold พอดี -> สต็อกคงเหลือเท่า threshold พอดี และระบบต้องไม่ส่งการแจ้งเตือน"*
* **ผลลัพธ์หลังแก้ไข:** AI ปรับปรุงโค้ดเป็น `quantity < threshold` อย่างถูกต้อง และผ่านเงื่อนไขทุกกรณี

---

### 🔁 รอบที่ 2: การแยกส่วนการแจ้งเตือนตามหลัก SOLID (DIP & OCP)
* **ปัญหาที่พบ:** ในรอบแรก โค้ดของ `InventoryService` มีคำสั่ง `EmailNotifier().send()` อยู่ภายในคลาส ทำให้เกิด High Coupling
* **การวิเคราะห์สาเหตุ:** `.ai-rules.md` ยังไม่ได้ระบุข้อห้ามเรื่องการสร้าง Concrete Notifier ภายใน Service อย่างชัดเจน
* **การแก้ไขที่ต้นทาง (Context):** เพิ่มกฎใน `.ai-rules.md`:
  > *"ห้ามให้ `InventoryService` รู้จัก Concrete Class ของ Notifier โดยตรง ให้ใช้ Observer Pattern และรับผ่าน Constructor (Dependency Injection)"*
* **ผลลัพธ์หลังแก้ไข:** AI ทำการ Refactor โค้ดใหม่ โดยใช้ **Observer Pattern** และ **Factory Pattern** ทำให้โค้ดผ่านเกณฑ์ SOLID ครบ 5 ข้อ

---

## 4. สรุปประวัติ Prompts สำคัญที่ใช้

```text
[Prompt 1 - Spec Review]:
"ฉันกำลังทำ Spec-Driven Development ช่วยรีวิว spec ด้านล่างนี้ในฐานะ senior software engineer ตอบเป็นภาษาไทย โดยชี้เฉพาะจุดที่:
1. acceptance criteria ข้อใดยัง "กำกวม" หรือ "ไม่ testable"
2. มี requirement ใดที่ขัดแย้งกันเองหรือซ้ำซ้อน
3. มี edge case สำคัญใดที่ spec ยังไม่ครอบคลุม (เช่น จ่ายเท่ากับ threshold พอดี)
อย่าเพิ่งเขียนโค้ด ให้เสนอเป็น checklist สั้น ๆ ว่าควรแก้ spec ตรงไหน [spec.md]"

[Prompt 2 - No Context Test]:
"จาก spec นี้ ช่วยเขียนโค้ด Python สำหรับฟีเจอร์แจ้งเตือนสต็อกต่ำ และรายงานมูลค่าสต็อกสินค้า
[spec.md]"

[Prompt 3 - Context-Driven Implementation]:
"คุณคือ AI coding agent ของโปรเจกต์นี้ ทำตามกฎใน .ai-rules.md อย่างเคร่งครัด
implement ฟีเจอร์ตาม spec ด้านล่าง โดยแยกไฟล์ตามที่กฎกำหนด (models / notifiers / service)
ทุก acceptance criteria ใน spec ต้อง implement ครบ
[.ai-rules.md]
---
[spec.md]"

[Prompt 4 - Refactor with Factory & Observer]:
"จากโค้ดใน models.py, notifiers.py, service.py ช่วยสร้าง:
1. Class Diagram เป็น Mermaid (classDiagram) แสดง class, attribute, method, visibility และความสัมพันธ์ (composition, dependency, realization)
2. Sequence Diagram เป็น Mermaid (sequenceDiagram) แสดง flow เมื่อพนักงานจ่ายสินค้าจนสต็อกต่ำกว่า threshold ตั้งแต่ InventoryService.issue_stock() จนถึงการเรียก notifier.send()"

[Prompt 5: สั่ง AI Refactor]
"จากผลการตรวจ SOLID design นี้ละเมิด OCP และ DIP เพราะ InventoryService มี coupling กับ notifier ช่วย refactorfy ดังนี้
1. ใช้ Factory pattern: NotifierFactory.create(channel_type, destination) คืน Notifier instance
2. InventoryService รับ Notifier ผ่าน constructor (Dependency Injection)
3. รองรับหลายปลายทางพร้อมกันด้วย Observer pattern: InventoryService เก็บ list ของ observer และเรียก notify ทุกตัวเมื่อสต็อกต่ำกว่า threshold โดยไม่รู้ว่าแต่ละ observer เป็นช่องทางอะไร
อย่าแก้ business logic การคำนวณสต็อก ให้แก้เฉพาะส่วน notification"
