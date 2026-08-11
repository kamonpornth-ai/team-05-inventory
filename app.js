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

function addItem(id, name, quantity) {
    const products = readInventory();
    const existingProduct = products.find((product) => product.id === id);

    if (existingProduct) {
        console.log('รหัสสินค้าซ้ำ');
        return false;
    }

    products.push({ id, name, quantity });
    saveInventory(products);
    return true;
}

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

// ตัวอย่างการเขียนไฟล์ JSON
// const products = readInventory();
// products.push({ id: 'P004', name: 'ดินสอ', quantity: 20 });
// saveInventory(products);

viewInventory();

module.exports = {
    readInventory,
    saveInventory,
    viewInventory,
    addItem,
};