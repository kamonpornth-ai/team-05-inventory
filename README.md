# 📦 team-05-inventory
> **Software Engineering Course: Lab 2 ➔ Lab 3 Development**

ระบบจัดการสต็อกร้านเครื่องเขียนแบบง่าย รันผ่าน Command Line Interface (CLI) บันทึกและอ่านข้อมูลผ่านไฟล์ JSON พัฒนาโดยเน้นกระบวนการทำงานเป็นทีมแบบ Agile/Scrum, GitHub Flow และการทดสอบระบบ

---

## 📌 สารบัญ (Table of Contents)
- [ภาพรวมการพัฒนา (Lab Progress)](#-ภาพรวมการพัฒนา-lab-progress)
- [ฟีเจอร์ของระบบ (Features)](#-ฟีเจอร์ของระบบ-features)
- [Acceptance Criteria (AC)](#-acceptance-criteria-ac)
- [โครงสร้างโปรเจกต์ (Project Structure)](#-โครงสร้างโปรเจกต์-project-structure)
- [เทคโนโลยีที่ใช้ (Tech Stack)](#-เทคโนโลยีที่ใช้-tech-stack)
- [การติดตั้งและการใช้งาน (Installation & Usage)](#-การติดตั้งและการใช้งาน-installation--usage)
- [ข้อกำหนดการทำงานของทีม (Team Workflow)](#-ข้อกำหนดการทำงานของทีม-team-workflow)

---

## 🚀 ภาพรวมการพัฒนา (Lab Progress)

* **Lab 2 (Sprint 1)**: ส่งมอบฟีเจอร์หลัก (Must Have) US-01 ถึง US-03 พร้อมวางรากฐาน GitHub Flow, Project Board และ Team Charter
* **Lab 3 (Sprint 2 / Ongoing)**: ปรับปรุงโครงสร้างโค้ด (Refactoring), เพิ่มการเขียน Unit Test / Integration Test และพัฒนาฟีเจอร์เพิ่มเติม (US-04, US-05)

---

## ✨ ฟีเจอร์ของระบบ (Features)

- 📋 **US-01: ดูรายการสินค้าทั้งหมด (List Items)** *(Implemented in Lab 2)*
  - แสดงรหัส ชื่อ และจำนวนคงเหลือของสินค้าทุกรายการ
  - แสดงข้อความเตือนเมื่อยังไม่มีสินค้าในระบบ
- ➕ **US-02: เพิ่มสินค้าใหม่ (Add Item)** *(Implemented in Lab 2)*
  - เพิ่มสินค้าพร้อมรหัส ชื่อ และจำนวนเริ่มต้น
  - มีระบบตรวจสอบและปฏิเสธการเพิ่มสินค้ารหัสซ้ำ
- ✏️ **US-03: แก้ไขจำนวนสินค้า (Update Stock)** *(Implemented in Lab 2)*
  - อัปเดตยอดคงเหลือเมื่อมีการรับเข้าหรือจ่ายออก[cite: 1]
  - ป้องกันการจ่ายออกเกินจำนวนที่มีอยู่ในสต็อก (ป้องกันสต็อกติดลบ)[cite: 1]
- 🔍 **US-04: ค้นหาสินค้า (Search Item)** *(Planned for Lab 3)*[cite: 1]
- 📤 **US-05: ส่งออกรายงาน CSV (Export CSV)** *(Planned for Lab 3)*[cite: 1]

---

## ✅ Acceptance Criteria (AC)

| User Story | เงื่อนไขการตรวจรับงาน (Acceptance Criteria)[cite: 1] | สถานะ |
|---|---|---|
| **US-01**[cite: 1] | • **AC-1:** มีสินค้าอย่างน้อย 1 รายการ $\rightarrow$ แสดงชื่อ รหัส และจำนวนคงเหลือครบ[cite: 1]<br>• **AC-2:** ยังไม่มีสินค้า $\rightarrow$ แสดงข้อความ *"ยังไม่มีสินค้าในระบบ"*[cite: 1] | **Done (Lab 2)**[cite: 1] |
| **US-02**[cite: 1] | • **AC-1:** ยังไม่มีรหัสนี้ $\rightarrow$ บันทึกสินค้าใหม่ และแสดงเมื่อเรียก list[cite: 1]<br>• **AC-2:** สินค้ารหัสซ้ำ $\rightarrow$ ปฏิเสธและแสดง *"รหัสสินค้าซ้ำ"* โดยไม่เขียนทับ[cite: 1] | **Done (Lab 2)**[cite: 1] |
| **US-03**[cite: 1] | • **AC-1:** ยอดคงเหลือไม่ติดลบ $\rightarrow$ อัปเดตยอดคงเหลือเป็นค่าใหม่และบันทึกทันที[cite: 1]<br>• **AC-2:** จ่ายออกมากกว่าคงเหลือ $\rightarrow$ แสดง *"จำนวนคงเหลือไม่พอ"* ยอดไม่เปลี่ยน[cite: 1] | **Done (Lab 2)**[cite: 1] |

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

```text
team-05-inventory/
├── inventory.py          # ซอร์สโค้ดหลักของระบบจัดการสต็อก
├── inventory.json        # ไฟล์เก็บข้อมูลสินค้า (JSON Database)
├── tests/                # โฟลเดอร์สำหรับไฟล์ทดสอบ (Lab 3)
│   └── test_inventory.py
├── TEAM_CHARTER.md       # กฎการทำงานเป็นทีม WIP Limit และ Branching Strategy
├── RETRO-SPRINT-1.md     # บันทึก Retrospective ของ Lab 2 (Sprint 1)
├── RETRO-SPRINT-2.md     # บันทึก Retrospective ของ Lab 3 (Sprint 2)
└── README.md             # เอกสารอธิบายโครงการ