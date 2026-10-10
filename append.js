const fs = require("fs");

fs.writeFile("student.txt","Hello this is slip 23",(err)=>{
                 
                                      if(err) throw err;
                                   console.log("file created and data written");

  fs.readFile('student.txt', 'utf8', (err, data) => {
        if (err) throw err;

        console.log('2. File contents:', data);


fs.appendFile('student.txt', '\nWelcome to Node JS programming.', (err) => {
            if (err) throw err;

            console.log('3. Data appended successfully.');

   		});
        });

 });

