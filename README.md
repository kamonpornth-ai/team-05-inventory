# swe-team-05-inventory

ระบบ inventory สำหรับวิชา **วิศวกรรมซอฟต์แวร์ในยุค AI** 
repository นี้ใช้ต่อเนื่องตั้งแต่ Lab 2 ถึง Lab 5 งานแต่ละ Lab แยกอยู่ในโฟลเดอร์ของตัวเอง

| | |
|---|---|
| ผู้จัดทำ | [นางสาวกมลพร ทัศนนิติกร] (รหัสนักศึกษา 66332110131-0) , นางสาววิพาวัลย์ พลลาภ (รหัสนักศึกษา 66332110169-3)|
| รูปแบบ | [ทีม: 2 คน] |
| ภาษา / เครื่องมือ | Python 3.11+, pytest, pytest-cov, ruff, GitHub Actions |

## ภาพรวมระบบ

ระบบจัดการสต็อกสินค้าที่พัฒนาต่อยอดมาเป็นลำดับ

- **Lab 2:** โปรแกรม command-line เก็บข้อมูลเป็น JSON/CSV (ดู, เพิ่ม, แก้จำนวน, ค้นหา, ส่งออก CSV)
- **Lab 3:** เพิ่มฟีเจอร์แจ้งเตือนสต็อกต่ำ (Email/SMS จำลองด้วย `print`) และรายงานมูลค่าสต็อกแยกหมวดหมู่ ออกแบบด้วย Spec-Driven Development
- **Lab 4:** ออกแบบ UX/UI ให้ผู้ใช้คลังสินค้า และฝึก code review กับ debug โค้ดที่ AI สร้าง
- **Lab 5:** TDD, refactor โค้ดเดิม และตั้ง CI

ระบบรองรับสินค้า 2 ชนิด คือ **สินค้าที่จับต้องได้** (มีจำนวนคงเหลือ ลดเมื่อขาย) และ **สินค้าดิจิทัล** (เป็นไฟล์ ขายแล้วยอดไม่ลด)

## โครงสร้าง repository

```
swe-inventory-[รหัสนักศึกษา]/
├── README.md
├── TEAM_CHARTER.md              # Lab 2: บทบาท, branching, WIP limit, AI policy
├── RETRO-SPRINT-1.md            # Lab 2: velocity และ retrospective
├── screenshots/                 # Lab 2 (board) และ Lab 5 (CI เขียว/แดง)
├── inventory-sdd/               # Lab 3
│   ├── specs/spec.md
│   ├── .ai-rules.md
│   ├── src/                     # models.py, notifiers.py, service.py, inventory_no_context.py
│   ├── diagrams/                # class.md, sequence.md (Mermaid)
│   ├── design_review.md
│   └── AI_ITERATION_LOG.md
├── lab04-ai-coding-ux/          # Lab 4
│   ├── findings-lab04.md
│   ├── persona.md
│   ├── accessibility-review.md
│   ├── code-review.md
│   ├── debug-log.md
│   ├── discount.py
│   ├── assets/                  # wireframe-ai.md, mockup-inventory.drawio, mockup-link.txt
│   └── tests/test_discount.py
├── inventory.py                 # Lab 5: โค้ดหลัก
├── pricing_legacy.py            # Lab 5: โค้ดเดิมที่ต้อง refactor
├── tests/                       # test_inventory.py, test_pricing_legacy.py
├── pyproject.toml               # ตั้งค่า ruff
├── requirements.txt
├── test-gap.md  coverage-note.md  smells.md  ethics.md   # Lab 5
└── .github/workflows/ci.yml     # Lab 5: ruff + pytest + coverage
```

> ปรับโครงสร้างให้ตรงกับ repository จริง ลบบรรทัดที่ยังไม่มีหรือไม่ได้ใช้

## งานแต่ละ Lab

### Lab 2: จำลอง Sprint แบบ Agile ด้วย GitHub Flow
- ทำงานตาม GitHub Flow: issue, branch `feat/<issue>-<ชื่องาน>`, pull request, review, merge
- Sprint Goal และ WIP limit อยู่ใน `TEAM_CHARTER.md`
- Velocity และ Start-Stop-Continue อยู่ใน `RETRO-SPRINT-1.md`
- Velocity Sprint 1: [__] points | PR ที่ merge แล้ว: [__] PR

### Lab 3: Spec-Driven Development และ Context Engineering
- เขียน spec ก่อนเขียนโค้ด: [`inventory-sdd/specs/spec.md`](inventory-sdd/specs/spec.md)
- ไฟล์กฎโปรเจกต์สำหรับ AI: [`inventory-sdd/.ai-rules.md`](inventory-sdd/.ai-rules.md)
- เทียบผลก่อนและหลังมี context และบันทึกการแก้ที่ spec: [`AI_ITERATION_LOG.md`](inventory-sdd/AI_ITERATION_LOG.md)
- ตรวจ SOLID ด้วยตัวเอง และ refactor ด้วย Factory + Observer

### Lab 4: UX, Code Review และ Debugging

**ส่วนที่ 1 UX และ UI mockup**

| ขั้น | ไฟล์ | สถานะ |
|---|---|---|
| 2 สัมภาษณ์ผู้ใช้ | `findings-lab04.md` | [ ] |
| 3 Persona และ journey map | `persona.md` | [x] |
| 4 Text wireframe (Login, Dashboard, Add Product) | `assets/wireframe-ai.md` | [ ] ทำแล้ว 2 หน้า (Add Product, Dashboard) |
| 5 Mockup อย่างน้อย 2 หน้า | `assets/mockup-inventory.drawio`, `assets/mockup-link.txt` | [ ] |
| 6 ตรวจ accessibility | `accessibility-review.md` | [ ] |

Persona หลักคือ "กรณ์" (นามสมมติ) ผู้ดูแลคลังสินค้าไอทีที่ทักษะเทคโนโลยีสูง แต่เจอปัญหา UI ที่ไม่มี validation และแยกสินค้าจับต้องได้กับดิจิทัลไม่ชัด
Mockup ใช้ชุดสีที่ผ่าน WCAG AA: Primary `#1E40AF`, Success `#15803D`, Warning `#B45309`, Text `#111827`

**ส่วนที่ 2 และ 3**

| ขั้น | ไฟล์ | สถานะ |
|---|---|---|
| 7 เทียบ prompt สั้นกับ prompt ที่แนบ context | `prompt-vs-context.md` | [ ] |
| 8 Review PR ที่ AI เขียน | `code-review.md` | [ ] |
| 10 Debug `discount.py` ให้ test ผ่านครบ | `debug-log.md`, `discount.py` | [ ] |

รัน test ของ Lab 4:

```bash
cd lab04-ai-coding-ux
python -m pytest tests/ -v
```

### Lab 5: TDD, Refactor และ CI/CD
- TDD: เขียน test ให้ไม่ผ่านก่อน (`low_stock_items`) แล้วให้ AI เขียนโค้ดให้ผ่าน
- Edge case ที่ AI ลืม: [`test-gap.md`](test-gap.md)
- Coverage: [`coverage-note.md`](coverage-note.md)
- Refactor `pricing_legacy.py` ด้วย characterization test: [`smells.md`](smells.md)
- CI: [`.github/workflows/ci.yml`](.github/workflows/ci.yml) รัน `ruff check` และ `pytest` พร้อม `--cov-fail-under=85`
- จริยธรรมยุค AI และแนวปฏิบัติการใช้ AI: [`ethics.md`](ethics.md)
- ภาพ CI ผ่านและไม่ผ่าน: `screenshots/ci-green.png`, `screenshots/ci-red.png`

## หมายเหตุ

- repository เป็น Public ไม่มีชื่อจริงของผู้ถูกสัมภาษณ์ในไฟล์ใด (persona ใช้นามสมมติ)
- Lab 4 ส่วนที่ 2 และ 3 ใช้โค้ดที่ผู้สอนแจก (`inventory_service.py`, `discount.py`) ไม่ใช่โค้ดของระบบนี้
