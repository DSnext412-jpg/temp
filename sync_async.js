
const fs = require("fs");
console.log("synchronous operation");

console.log("1.start reading file");

const data1=fs.readFileSync("sample.txt", "utf8");
console.log("2.file contents:", data1);

console.log("3.end of synchronous operation");
console.log("\nasynchronous operation");

console.log("1.start reading file");
fs.readFile("sample.txt","utf8", (err, data2) => {
    if (err) {
        console.log("error:", err);
        return;
    }
    console.log("2.file contents:", data2);
});

console.log("3.end of asynchronous operation");
