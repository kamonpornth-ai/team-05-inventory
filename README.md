swe-team-05-inventory
ระบบ inventory สำหรับวิชา วิศวกรรมซอฟต์แวร์ในยุค AI
repository นี้ใช้ต่อเนื่องตั้งแต่ Lab 2 ถึง Lab 5 งานแต่ละ Lab แยกอยู่ในโฟลเดอร์ของตัวเอง
	
ผู้จัดทำ	กมลพร ทัศนนิติกร (รหัสนักศึกษา 66332110131-0) , วิพาวัลย์ พลลาภ (รหัสนักศึกษา 66332110169-3)
รูปแบบ	ทีม: 2 คน
ภาษา / เครื่องมือ	Python 3.11+, pytest, pytest-cov, ruff, GitHub Actions
ภาพรวมระบบ
ระบบจัดการสต็อกสินค้าที่พัฒนาต่อยอดมาเป็นลำดับ
Lab 2: โปรแกรม command-line เก็บข้อมูลเป็น JSON/CSV (ดู, เพิ่ม, แก้จำนวน, ค้นหา, ส่งออก CSV)
Lab 3: เพิ่มฟีเจอร์แจ้งเตือนสต็อกต่ำ (Email/SMS จำลองด้วย `print`) และรายงานมูลค่าสต็อกแยกหมวดหมู่ ออกแบบด้วย Spec-Driven Development
Lab 4: ออกแบบ UX/UI ให้ผู้ใช้คลังสินค้า และฝึก code review กับ debug โค้ดที่ AI สร้าง
Lab 5: TDD, refactor โค้ดเดิม และตั้ง CI
ระบบรองรับสินค้า 2 ชนิด คือ สินค้าที่จับต้องได้ (มีจำนวนคงเหลือ ลดเมื่อขาย) และ สินค้าดิจิทัล (เป็นไฟล์ ขายแล้วยอดไม่ลด)
---
โครงสร้าง repository
```text
swe-inventory/
├── README.md
├── TEAM_CHARTER.md                 # Lab 2: บทบาท, branching, WIP limit, AI policy
├── RETRO-SPRINT-1.md               # Lab 2: velocity และ retrospective
├── screenshots/                    # Lab 2 (board) และ Lab 5 (CI เขียว/แดง)
├── inventory-sdd/                  # Lab 3
│   ├── specs/spec.md
│   ├── .ai-rules.md
│   ├── src/                        # models.py, notifiers.py, service.py
│   ├── diagrams/                   # class.md, sequence.md (Mermaid)
│   ├── design_review.md
│   └── AI_ITERATION_LOG.md
├── lab04-ai-coding-ux/             # Lab 4
│   ├── findings-lab04.md
│   ├── persona.md
│   ├── accessibility-review.md
│   ├── code-review.md
│   ├── debug-log.md
│   ├── discount.py
│   ├── assets/                     # wireframe-ai.md, mockup-inventory.drawio
│   └── tests/test_discount.py
├── inventory.py                    # Lab 5: โค้ดหลัก
├── pricing_legacy.py               # Lab 5: โค้ดเดิมที่ต้อง refactor
├── tests/                          # test_inventory.py, test_pricing_legacy.py
├── pyproject.toml                  # ตั้งค่า ruff
├── requirements.txt
├── test-gap.md  coverage-note.md  smells.md  ethics.md
└── .github/workflows/ci.yml        # Lab 5: ruff + pytest + coverage
```
---
งานแต่ละ Lab
Lab 2: จำลอง Sprint แบบ Agile ด้วย GitHub Flow
ทำงานตาม GitHub Flow: issue, branch `feat/<issue>-<ชื่องาน>`, pull request, review, merge
Sprint Goal และ WIP limit อยู่ใน `TEAM_CHARTER.md`
Velocity และ Start-Stop-Continue อยู่ใน `RETRO-SPRINT-1.md`
Velocity Sprint 1: [] points | PR ที่ merge แล้ว: [] PR
Lab 3: Spec-Driven Development และ Context Engineering
เขียน spec ก่อนเขียนโค้ด: `inventory-sdd/specs/spec.md`
ไฟล์กฎโปรเจกต์สำหรับ AI: `inventory-sdd/.ai-rules.md`
เทียบผลก่อนและหลังมี context และบันทึกการแก้ที่ spec: `AI_ITERATION_LOG.md`
ตรวจ SOLID ด้วยตัวเอง และ refactor ด้วย Factory + Observer
Lab 4: UX, Code Review และ Debugging
ส่วนที่ 1: UX และ UI Mockup
Persona หลักคือ "กรณ์" (นามสมมติ) ผู้ดูแลคลังสินค้าไอทีที่มีทักษะเทคโนโลยีสูง แต่เจอปัญหา UI ที่ไม่มี validation และแยกสินค้าจับต้องได้กับดิจิทัลไม่ชัด
Mockup ใช้ชุดสีที่ผ่าน WCAG AA: Primary `#1E40AF`, Success `#15803D`, Warning `#B45309`, Text `#111827`
ส่วนที่ 2 และ 3: AI Coding & Debugging
เปรียบเทียบ prompt สั้นและ prompt ที่แนบ context
ทำ Code Review สำหรับ PR ที่ AI เขียน (`code-review.md`)
Debug โค้ดใน `discount.py` ให้ test ผ่านครบถ้วน
รันเทสต์ของ Lab 4:
```bash
cd lab04-ai-coding-ux
python -m pytest tests/ -v
```
Lab 5: TDD, Refactor และ CI/CD
TDD: เขียน test ให้ไม่ผ่านก่อน (`low_stock_items`) แล้วให้ AI เขียนโค้ดให้ผ่าน พร้อมระบุ edge case ที่ AI ลืมไว้ใน `test-gap.md`
Coverage & Smells: บันทึกผล Coverage ใน `coverage-note.md` และวิเคราะห์ Code Smells ใน `smells.md` สำหรับการ refactor `pricing_legacy.py`
CI/CD: ตั้งค่า GitHub Actions ใน `.github/workflows/ci.yml` รัน `ruff check` และ `pytest` พร้อม `--cov-fail-under=85`
Ethics: แนวปฏิบัติและการใช้ AI อย่างมีจริยธรรมใน `ethics.md`
---
หมายเหตุ
Repository เป็น Public ไม่มีชื่อจริงของผู้ถูกสัมภาษณ์ในไฟล์ใด (Persona ใช้นามสมมติ)
Lab 4 ส่วนที่ 2 และ 3 ใช้โค้ดที่ผู้สอนแจก ไม่ใช่โค้ดหลักของระบบคลังสินค้า
