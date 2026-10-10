# 📦 Inventory Management System (Capstone Project)
> **Course Project: Software Engineering in AI Era**  
> **Team:** Team 05  
> **Repository:** [https://github.com/kamonpornth-ai/team-05-inventory](https://github.com/kamonpornth-ai/team-05-inventory)  
> **CI Status:** [![CI](https://github.com/kamonpornth-ai/team-05-inventory/actions/workflows/ci.yml/badge.svg)](https://github.com/kamonpornth-ai/team-05-inventory/actions/workflows/ci.yml)

---

## 1. Project Overview & Problem Statement

### 1.1 ที่มาและความสำคัญ (Problem Statement)
การจัดการคลังสินค้าในธุรกิจยุคปัจจุบันต้องเผชิญกับความท้าทายทั้งในด้านความหลากหลายของประเภทสินค้า (Physical และ Digital Products), ความแม่นยำในการคำนวณมูลค่าและส่วนลดตามปริมาณ (Tiered Pricing), ตลอดจนความเสี่ยงจากสินค้าขาดสต็อกโดยไม่รู้ล่วงหน้า ระบบเดิมมักประสบปัญหาโค้ดที่มีความซับซ้อนสูง (Legacy Code), ขาดการทดสอบอัตโนมัติ และไม่มีการแจ้งเตือนแบบทันท่วงที

### 1.2 วัตถุประสงค์และขอบเขต (Project Scope)
- **In-Scope:**
  - จัดการรายการสินค้า การเพิ่ม ค้นหา และปรับปรุงยอดสต็อกแบบ Real-time
  - รองรับการแจ้งเตือนสต็อกต่ำ (Low Stock Alert) ผ่านสถาปัตยกรรม Observer Pattern (Email, SMS)
  - ระบบประเมินมูลค่าสินค้าคงคลังรวม (Inventory Valuation) แยกตามหมวดหมู่
  - คำนวณราคาและส่วนลดตามหมวดหมู่และปริมาณการสั่งซื้อ (Volume Discount Engine)
  - รองรับ CI/CD Pipeline อัตโนมัติด้วย GitHub Actions พร้อมเกณฑ์ Code Coverage ≥ 85% และ Ruff Linter
- **Out-of-Scope:**
  - การชำระเงินผ่าน Payment Gateway ภายนอก
  - ระบบจัดการการขนส่งและโลจิสติกส์ภายนอก (Third-party Logistics)

---

## 2. Team Members & Roles

| ลำดับ | ชื่อ-นามสกุล | GitHub Account | บทบาทหลัก (Role) | ความรับผิดชอบ |
|:---:|---|---|---|---|
| 1 | Kamonporn Th. | [@kamonpornth-ai](https://github.com/kamonpornth-ai) | Product Owner (PO) | กำหนดวิสัยทัศน์ ดูแล Product Backlog, Acceptance Criteria |
| 2 | Wiphawan Phonlap | [@Wiphawan-Phonlap](https://github.com/Wiphawan-Phonlap) | Scrum Master / Dev | จัดการ Sprint, ทำ Code Review, ดูแล TDD & Refactoring |
| 3 | Kamon | [@kamonpornth-ai](https://github.com/kamonpornth-ai) | Full-stack Developer | ออกแบบ UX/UI Wireframe, Debugging และติดตั้ง CI/CD Pipeline |

---

## 3. Architecture & Design Patterns

ระบบได้รับการออกแบบโดยยึดหลัก **SOLID Principles** และ Design Patterns ที่เหมาะสม:

1. **Observer Pattern (`src/notifiers.py`):**
   - ใช้ `StockObserver` ในการติดตามการเปลี่ยนแปลงของสต็อก
   - รองรับ Multi-channel Notifiers (`EmailNotifier`, `SMSNotifier`) โดยไม่กระทบ Business Logic หลัก
2. **Factory Pattern (`src/notifiers.py`):**
   - ใช้ `NotifierFactory` ในการสร้าง Instance ของ Notifier ตาม Channel ที่ต้องการ
3. **Single Responsibility & Strategy (`pricing.py`):**
   - แยกตรรกะการคำนวณส่วนลดตามประเภทสินค้าและจำนวน (`calculate_bulk_discount`, `calculate_final_price`)

```
               +----------------------+
               |   InventoryService   |
               +----------+-----------+
                          | notifies
                          v
               +----------------------+
               |    StockObserver     | <--- Interface
               +----------+-----------+
                          |
             +------------+------------+
             |                         |
    +--------+--------+       +--------+--------+
    |  EmailNotifier  |       |   SMSNotifier   |
    +-----------------+       +-----------------+
```

---

## 4. Engineering Practices & Deliverables

### 4.1 Agile & GitHub Flow (Lab 2)
- ดำเนินการผ่าน Branching Strategy (`feature/*`), Pull Request Reviews และจัดการ Merge Conflict อย่างเป็นระบบ
- จัดทำ `TEAM_CHARTER.md` และ `RETRO-SPRINT-1.md`

### 4.2 Spec-Driven Development & Context Engineering (Lab 3)
- กำหนด Requirements ชัดเจนผ่าน `specs/spec.md`
- ใช้ `.ai-rules.md` ควบคุม AI ให้เขียนโค้ดตามมาตรฐาน SOLID

### 4.3 UX Design & Evidence-based Debugging (Lab 4)
- วิเคราะห์ Persona และ Customer Journey Map 5 ขั้นตอน
- ออกแบบ ASCII Wireframe รองรับ Accessibility WCAG 2.1 AA
- ตรวจสอบบั๊กแฝง 6 จุดใน `inventory_service.py` และทำ Systematic Debugging 5 ขั้นตอนใน `discount.py`

### 4.4 TDD, Refactoring & Automated CI/CD (Lab 5)
- พัฒนาฟังก์ชันด้วย TDD (Red-Green-Refactor)
- บันทึก Characterization Tests 13 ข้อ และ Refactor Legacy Code สู่ Clean Code
- ติดตั้ง GitHub Actions CI Pipeline รัน Ruff และ Pytest Coverage วัดผลได้ **99.27%**

---

## 5. AI Ethics & Usage Disclosure

ในการพัฒนาระบบ ทีมงานได้ปฏิบัติตามหลักจริยธรรม AI 4 มิติ (ตามรายละเอียดใน `ethics.md`):
1. **Transparancy & Verification:** โค้ดที่สร้างโดย AI ทุกบรรทัดต้องผ่านการตรวจสอบด้วย Human Code Review และ Automated Unit Tests 100%
2. **Data Privacy & Security:** ไม่ส่งข้อมูลส่วนบุคคล (PII) หรือ Credentials เข้าสู่ Public AI Prompts
3. **Bias & Fairness:** ออกแบบระบบให้รองรับผู้ใช้งานหลากหลายระดับความสามารถตามมาตรฐาน WCAG 2.1 AA
4. **Accountability:** สมาชิกในทีมรับผิดชอบต่อผลลัพธ์และความปลอดภัยของซอฟต์แวร์ทั้งหมด
