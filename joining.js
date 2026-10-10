const path = require('path');

const filePath = path.join('C:', 'Users', 'Student', 'Documents', 'file.txt');
console.log('Joined Path:', filePath);

const absolutePath = path.resolve('Documents', 'file.txt');
console.log('Resolved Path:', absolutePath);

console.log('Directory Name:', path.dirname(filePath));
console.log('File Name:', path.basename(filePath));
console.log('File Extension:', path.extname(filePath));

