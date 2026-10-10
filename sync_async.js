
const fs = require("fs");
console.log("===== Synchronous Operation =====");

console.log("1. Start reading file");

const data1 = fs.readFileSync("sample.txt", "utf8");
console.log("2. File contents:", data1);

console.log("3. End of synchronous operation");
console.log("\n===== Asynchronous Operation =====");

console.log("1. Start reading file");
fs.readFile("sample.txt", "utf8", (err, data2) => {
    if (err) {
        console.log("Error:", err);
        return;
    }
    console.log("2. File contents:", data2);
});

console.log("3. End of asynchronous operation");
