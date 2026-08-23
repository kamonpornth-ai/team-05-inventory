const fs = require('fs');
const path = require('path');

const dataFilePath = path.join(__dirname, 'data.json');

function readInventory() {
    try {
        const fileContent = fs.readFileSync(dataFilePath, 'utf8');
        const products = JSON.parse(fileContent);

        return Array.isArray(products) ? products : [];
    } catch (error) {
        if (error.code === 'ENOENT') {
            return [];
        }

        throw error;
    }
}

function saveInventory(products) {
    fs.writeFileSync(dataFilePath, JSON.stringify(products, null, 2), 'utf8');
}

// US-02: เพิ่มสินค้าใหม่
function addItem(id, name, quantity) {
    const products = readInventory();
    const existingProduct = products.find((product) => product.id === id);

    if (existingProduct) {
        console.log('รหัสสินค้าซ้ำ');
        return false;
    }

    products.push({ id, name, quantity });
    saveInventory(products);
    console.log(`เพิ่มสินค้า ${name} (รหัส: ${id}) เรียบร้อย`);
    return true;
}

// US-03: แก้ไข/ปรับปรุงจำนวนสินค้า (รับเข้า หรือ จ่ายออก)
function updateQuantity(id, amount) {
    const products = readInventory();
    const product = products.find((p) => p.id === id);

    if (!product) {
        console.log(`ไม่พบสินค้ารหัส: ${id}`);
        return false;
    }

    if (product.quantity + amount < 0) {
        console.log(`สินค้าคงเหลือไม่พอ (ปัจจุบันมี: ${product.quantity}, ต้องการจ่ายออก: ${Math.abs(amount)})`);
        return false;
    }

    product.quantity += amount;
    saveInventory(products);
    console.log(`อัปเดตสินค้า ${product.name} (รหัส: ${id}) ยอดคงเหลือใหม่คือ: ${product.quantity}`);
    return true;
}

// US-01: ดูรายการสินค้าในระบบ
function viewInventory() {
    try {
        const products = readInventory();

        if (products.length === 0) {
            console.log('ยังไม่มีสินค้าในระบบ');
            return;
        }

        console.log('=== รายการสินค้าในระบบ ===');
        products.forEach((product) => {
            console.log(`id: ${product.id} | name: ${product.name} | quantity: ${product.quantity}`);
        });
    } catch (error) {
        console.log('เกิดข้อผิดพลาดในการอ่านข้อมูล:', error.message);
    }
}

viewInventory();

module.exports = {
    readInventory,
    saveInventory,
    addItem,
    updateQuantity,
    viewInventory,
};
