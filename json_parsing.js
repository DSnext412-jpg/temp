const fs = require("fs");
console.log("1. Creating directory...");

if (!fs.existsSync("MyData")) {
    fs.mkdirSync("MyData");
    console.log("Directory 'MyData' created.");
} else {
    console.log("Directory 'MyData' already exists.");
}

const student={
    id: 101,
    name: "Rahul",
    course: "M.Sc. Computer Science",
    marks: 85
};

const jsonData = JSON.stringify(student, null, 2);

fs.writeFileSync("MyData/student.json", jsonData);

console.log("Student data written to student.json.");


const data = fs.readFileSync("MyData/student.json", "utf8");
const studentData = JSON.parse(data);

console.log("\nStudent Information:");
console.log("ID:", studentData.id);
console.log("Name:", studentData.name);
console.log("Course:", studentData.course);
console.log("Marks:", studentData.marks);


console.log("\nFiles in MyData directory:");

const files = fs.readdirSync("MyData");

files.forEach(file => {
    console.log(file);
});


if (fs.existsSync("MyData")) {
    fs.renameSync("MyData", "StudentData");
    console.log("\nDirectory renamed from 'MyData' to 'StudentData'.");
}


console.log("\nCurrent directory contents:");

const items = fs.readdirSync(".");

items.forEach(item => {
    console.log(item);
});


if (fs.existsSync("StudentData")) {
    fs.rmSync("StudentData", { recursive: true, force: true });
    console.log("\nDirectory 'StudentData' deleted.");
}
