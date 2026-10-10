const fs = require("fs");

const path = "sample.txt";

fs.stat(path, (err, stats) => {

    if (err) {
        console.log("Error:", err.message);
        return;
    }

    console.log("===== File Statistics =====");
    console.log("File Size:", stats.size, "bytes");
    console.log("Is File:", stats.isFile());
    console.log("Is Directory:", stats.isDirectory());

    console.log("Creation Time:", stats.birthtime);
    console.log("Access Time:", stats.atime);
    console.log("Modification Time:", stats.mtime);
});