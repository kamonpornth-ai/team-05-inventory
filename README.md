# 📦 team-05-inventory
> **Software Engineering Course Portfolio: Lab 2 ➔ Lab 3 ➔ Lab 4 ➔ Lab 5**

[![CI](https://github.com/kamonpornth-ai/team-05-inventory/actions/workflows/ci.yml/badge.svg)](https://github.com/kamonpornth-ai/team-05-inventory/actions/workflows/ci.yml)
![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)
![Test Coverage](https://img.shields.io/badge/coverage-99.27%25-brightgreen)
![Code Style](https://img.shields.io/badge/code%20style-ruff-000000.svg)

ระบบจัดการสต็อกสินค้า (Inventory Management System) พัฒนาขึ้นในรายวิชาวิศวกรรมซอฟต์แวร์ในยุค AI โดยบูรณาการแนวคิด **Agile/Scrum (GitHub Flow)**, **Spec-Driven Development (SDD)**, **UX/UI Design Thinking**, **Code Review & Debugging**, **Test-Driven Development (TDD)**, **Refactoring Legacy Code**, **Automated CI/CD** และ **จริยธรรมการใช้งาน AI**

---

## 📌 สารบัญ (Table of Contents)
- [ภาพรวมการพัฒนาแต่ละแล็บ (Lab Progress)](#-ภาพรวมการพัฒนาแต่ละแล็บ-lab-progress)
- [โครงสร้างโปรเจกต์ (Project Structure)](#-โครงสร้างโปรเจกต์-project-structure)
- [การติดตั้งและการทดสอบ (Installation & Testing)](#-การติดตั้งและการทดสอบ-installation--testing)
- [สรุปรายละเอียดของแต่ละแล็บ (Lab Breakdown)](#-สรุปรายละเอียดของแต่ละแล็บ-lab-breakdown)
  - [Lab 2: Agile Sprint & GitHub Flow](#lab-2-agile-sprint--github-flow)
  - [Lab 3: Spec-Driven Development & Context Engineering](#lab-3-spec-driven-development--context-engineering)
  - [Lab 4: UX/UI Design, Code Review & Debugging](#lab-4-uxui-design-code-review--debugging)
  - [Lab 5: TDD, Refactor, CI/CD & Ethics](#lab-5-tdd-refactor-cicd--ethics)
- [สมาชิกในทีม (Team Members)](#-สมาชิกในทีม-team-members)

---

## 🚀 ภาพรวมการพัฒนาแต่ละแล็บ (Lab Progress)

| แล็บ | หัวข้อหลัก | ผลลัพธ์สำคัญ | สถานะ |
|---|---|---|:---:|
| **Lab 2** | Agile / Scrum & GitHub Flow | ส่งมอบ US-01 ถึง US-03 ผ่าน Pull Requests, Team Charter, Retro Sprint 1 | ✅ **Completed** |
| **Lab 3** | Spec-Driven Development (SDD) | `.ai-rules.md`, สถาปัตยกรรม SOLID (Observer & Factory Pattern), Mermaid Diagrams | ✅ **Completed** |
| **Lab 4** | UX, Code Review & Debugging | Persona + Journey Map, ASCII Wireframe, ตรวจสอบบั๊ก 6 จุด, Debug `discount.py` | ✅ **Completed** |
| **Lab 5** | TDD, Refactor, CI/CD & Ethics | TDD `low_stock_items`, Refactor `pricing.py`, GitHub Actions CI (Coverage 99.27%), `ethics.md` | ✅ **Completed** |

---

## 📁 โครงสร้างโปรเจกต์ (Project Structure)

```text
team-05-inventory/
├── .github/
│   └── workflows/
│       └── ci.yml                # [Lab 5] GitHub Actions Automated CI Workflow
├── lab04-ai-coding-ux/           # [Lab 4] โฟลเดอร์งาน UX, Code Review และ Debugging
│   ├── findings-lab04.md         # สรุปผลการสัมภาษณ์ผู้ใช้และ Point of View
│   ├── persona.md                # Persona คุณสมชาย พร้อม Journey Map 5 ขั้นตอน
│   ├── accessibility-review.md   # รายงานตรวจ Checklist WCAG 2.1 AA และจุดแก้ AI
│   ├── prompt-vs-context.md      # บันทึกการเปรียบเทียบ Prompt vs Context 2 รอบ
│   ├── code-review.md            # บันทึกการ Review บั๊ก 6 จุดใน inventory_service.py
│   ├── debug-log.md              # บันทึกการ Debug โมดูล discount.py ครบ 5 ขั้นตอน
│   ├── discount.py               # โค้ดคิดส่วนลดฉบับแก้ไขบั๊กแล้ว
│   ├── tests/
│   │   └── test_discount.py      # ชุด Unit Tests สำหรับโมดูล discount.py
│   └── assets/
│       ├── wireframe-ai.md       # Text Wireframe (ASCII) ครบ 3 หน้า
│       └── mockup-link.txt       # ลิงก์ Figma Mockup และ Palette สี WCAG AA
├── specs/
│   └── spec.md                   # [Lab 3] สเปกระบบความต้องการละเอียด (5 User Stories)
├── src/                          # [Lab 3] โค้ดระบบ Inventory ตามหลัก SOLID
│   ├── models.py                 # Domain Models (Product, Category, Transaction)
│   ├── notifiers.py              # Observer Pattern & Factory Notifiers (Email, SMS)
│   ├── service.py                # InventoryService พร้อม Dependency Injection
│   └── inventory_no_context.py   # โค้ด Baseline ก่อนมี Context
├── diagrams/                     # [Lab 3] ไดอะแกรม Mermaid
│   ├── class.md                  # Class Diagram
│   └── sequence.md               # Sequence Diagram
├── tests/                        # [Lab 5] โฟลเดอร์รวมชุดการทดสอบอัตโนมัติ
│   ├── test_inventory.py         # TDD Tests สำหรับ low_stock_items และ Edge Cases
│   ├── test_pricing.py           # Unit Tests สำหรับโมดูล pricing.py (Refactored)
│   └── test_pricing_legacy.py    # Characterization Tests สำหรับ pricing_legacy.py
├── inventory.py                  # [Lab 5] ซอร์สโค้ดหลักระบบจัดการสต็อก
├── pricing.py                    # [Lab 5] โมดูลคิดราคาและส่วนลดฉบับ Refactored (Clean Code)
├── pricing_legacy.py             # [Lab 5] โค้ดเก่าดั้งเดิม (Legacy Code)
├── test-gap.md                   # [Lab 5] ตารางวิเคราะห์ช่องว่างของ Test (Test Gap)
├── coverage-note.md              # [Lab 5] บันทึกผลวิเคราะห์ Code Coverage (99.27%)
├── smells.md                     # [Lab 5] บันทึกรายการ Code Smells 6 ข้อ
├── ethics.md                     # [Lab 5] บทวิเคราะห์จริยธรรม 4 มิติ และแนวปฏิบัติของทีม
├── pyproject.toml                # [Lab 5] การตั้งค่า Ruff Linter และ Pytest Coverage
├── requirements.txt              # [Lab 5] รายการ Dependencies (pytest, pytest-cov, ruff)
├── TEAM_CHARTER.md               # [Lab 2] กฎการทำงานเป็นทีม WIP Limit และ Git Flow
├── RETRO-SPRINT-1.md             # [Lab 2] บันทึก Sprint Retrospective
├── design_review.md              # [Lab 3] ตารางประเมินหลักการ SOLID 5 ข้อ
├── AI_ITERATION_LOG.md           # [Lab 3] บันทึกการปรับปรุง Prompt และ Context 2 รอบ
└── README.md                     # เอกสารอธิบายโครงการฉบับสมบูรณ์
```

---

## 🛠️ การติดตั้งและการทดสอบ (Installation & Testing)

### 1. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

### 2. ตรวจสอบคุณภาพโค้ดด้วย Ruff Linter
```bash
ruff check .
```

### 3. รันชุดการทดสอบอัตโนมัติและวัด Code Coverage (Lab 5)
```bash
pytest tests/ --cov=. --cov-report=term-missing --cov-fail-under=85
```

### 4. รันการทดสอบของ Lab 4
```bash
pytest lab04-ai-coding-ux/tests/ -v
```

---

## 📖 สรุปรายละเอียดของแต่ละแล็บ (Lab Breakdown)

### Lab 2: Agile Sprint & GitHub Flow
* พัฒนาฟังก์ชันการจัดการสต็อกพื้นฐาน (US-01: ดูรายการ, US-02: เพิ่มสินค้า, US-03: ปรับปรุงยอดสต็อก)
* ปฏิบัติตาม **GitHub Flow** ผ่าน Pull Request (#1, #2, #3) พร้อม Code Review และแก้ปัญหา Merge Conflict
* จัดทำข้อตกลงทีมใน `TEAM_CHARTER.md` และสรุปผลใน `RETRO-SPRINT-1.md`

### Lab 3: Spec-Driven Development & Context Engineering
* เขียนสเปกแบบ Given-When-Then ใน `specs/spec.md` (ฟีเจอร์แจ้งเตือนสต็อกต่ำ และรายงานมูลค่าสต็อก)
* ใช้ `.ai-rules.md` ควบคุมคุณภาพและสถาปัตยกรรมของ AI Coding Assistant
* ออกแบบตามหลัก **SOLID ครบทั้ง 5 ข้อ** โดยประยุกต์ใช้ **Observer Pattern** และ **Factory Pattern**
* สรุปผลวิเคราะห์ใน `design_review.md`, `AI_ITERATION_LOG.md` และสร้าง Mermaid Diagrams

### Lab 4: UX/UI Design, Code Review & Debugging
* ทำ Design Thinking สังเคราะห์ Persona คุณสมชาย (ทักษะ 2/5) พร้อม Journey Map 5 ขั้นตอน
* ออกแบบ Text Wireframe (ASCII) 3 หน้า ที่รองรับทั้งสินค้าจริง (Physical) และสินค้าดิจิทัล (Digital)
* ตรวจสอบ Accessibility ตามเกณฑ์ WCAG 2.1 AA และบันทึกจุดแก้ไขข้อผิดพลาดของ AI
* ดำเนินการ **Code Review** โค้ด `inventory_service.py` ตรวจพบบั๊กแฝงครบ 6 จุด (Atomicity, Concurrency Race Condition, Boundary, Division by Zero)
* ดำเนินการ **Debugging แบบมีหลักฐาน 5 ขั้นตอน** แก้ไขบั๊กในโมดูล `discount.py` จน Test ผ่าน 100%

### Lab 5: TDD, Refactor, CI/CD & Ethics
* พัฒนาฟังก์ชัน `low_stock_items(threshold)` ด้วยกระบวนการ **TDD (Red ➔ Green ➔ Refactor)** ครบ 6 Test Cases
* วิเคราะห์ช่องว่างของการทดสอบที่ AI สร้างใน `test-gap.md` และวัด Code Coverage ได้สูงถึง **99.27%**
* วิเคราะห์ Code Smells ของ `pricing_legacy.py` ครบ 6 ข้อใน `smells.md`
* เขียน **Characterization Tests ทั้งหมด 13 ข้อ** เพื่อบันทึกพฤติกรรมเดิมอย่างครบถ้วน
* ทำการ **Refactor** สู่โมดูล `pricing.py` ที่อ่านง่าย มี Type Hints และแยกฟังก์ชันตาม SRP โดย Test ทั้ง 13 ข้อยังผ่าน 100%
* ติดตั้ง **GitHub Actions Automated CI Pipeline** ตรวจสอบ Linting และ Coverage ทุกครั้งที่มีการ Push/PR
* จัดทำบทวิเคราะห์จริยธรรมในยุค AI ครบ 4 มิติ พร้อมข้อตกลงแนวปฏิบัติของทีมใน `ethics.md`

---

## 👥 สมาชิกในทีม (Team Members)

| ลำดับ | ชื่อ-นามสกุล | GitHub Profile | บทบาทในทีม |
|:---:|---|---|---|
| 1 | Kamonporn Th. | [@kamonpornth-ai](https://github.com/kamonpornth-ai) | Product Owner |
| 2 | Wiphawan Phonlap | [@Wiphawan-Phonlap](https://github.com/Wiphawan-Phonlap) | Scrum Master / Developer |
| 3 | Kamon | [@kamonpornth-ai](https://github.com/kamonpornth-ai) | Developer |
