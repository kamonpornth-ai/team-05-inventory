const fs = require('fs');

function viewInventory() {
    try {
        const data = fs.readFileSync('data.json', 'utf8');
        const products = JSON.parse(data);

        console.log("=== รายการสินค้าทั้งหมด (US-01) ===");
        products.forEach(p => {
            console.log(`รหัส: ${p.id} | ชื่อ: ${p.name} | คงเหลือ: ${p.quantity} ชิ้น`);
        });
    } catch (error) {
        console.log("เกิดข้อผิดพลาดในการอ่านข้อมูล:", error.message);
    }
}

viewInventory();