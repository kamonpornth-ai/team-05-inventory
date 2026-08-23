# TEAM_CHARTER.md

## สมาชิกและบทบาท

| ชื่อ | GitHub Username | บทบาท |
|---|---|---|
| kamonporn  | https://github.com/kamonpornth-ai             | Product Owner |
| wiphawan  | https://github.com/Wiphawan-Phonlap         | Scrum Master / Developer |
| kamon | https://github.com/kamonpornth-ai            | Developer |

## Branching Strategy

ทีมใช้ GitHub Flow:
- main branch ต้อง deploy ได้เสมอ ห้าม commit โดยตรง
- ทุก feature ใหม่ต้องสร้าง branch ชื่อ feat/<issue-number>-<short-name>
- ทุก PR ต้องมีคนอื่นในทีมอย่างน้อย 1 คน review และ approve ก่อน merge

## เพดานงานที่ทำพร้อมกัน (WIP limit)
- คอลัมน์ In Progress มีการ์ดพร้อมกันได้ไม่เกิน 3 ใบ (เท่ากับจำนวนคนที่เขียนโค้ดในทีม)
- เมื่อชนเพดาน ห้ามลากการ์ดใหม่เข้ามา ให้ช่วยกันปิดของเดิมหรือรีวิว PR ที่ค้างใน In Review ก่อน

## Sprint Goal (Sprint 1)
Sprint 1 นี้ทีมจะส่งมอบระบบจัดการสต็อกสินค้าที่มีฟังก์ชัน US-01 (ดูรายการ), US-02 (เพิ่มสินค้า) และ US-03 (แก้ไขจำนวนสต็อก) ที่รันได้จริงและผ่าน Acceptance Criteria ครบถ้วน


## AI Usage Policy

- ใช้ AI ช่วยเขียน draft code และ draft commit message ได้
- ทุก commit message ที่ AI generate ต้องอ่านและแก้ให้ตรงกับ diff จริงก่อน commit
- ห้าม copy code จาก AI โดยไม่อ่านและทำความเข้าใจก่อน
- ใช้เฉพาะ AI ที่ไม่มีค่าใช้จ่าย ไม่บังคับซื้อ subscription
