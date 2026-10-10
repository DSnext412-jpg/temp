const fs = require('fs');

fs.writeFile('student.txt', 'Hello, this is Node.js.', (err) => {
    if (err) throw err;

    console.log('1. File created and data written successfully.');
    fs.readFile('student.txt', 'utf8', (err, data) => {
        if (err) throw err;

        console.log('2. File contents:', data);
        fs.appendFile('student.txt', '\nWelcome to asynchronous programming.', (err) => {
            if (err) throw err;

            console.log('3. Data appended successfully.');
            fs.rename('student.txt', 'student_new.txt', (err) => {
                if (err) throw err;
                console.log('4. File renamed successfully.');

              });
        });
    });
});

console.log('5. Program continues while file operations are performed...');