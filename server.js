const http = require('http');

const server = http.createServer((req, res) => {

    if (req.url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write('<h1>Welcome to Node.js Server</h1>');
        res.write('<p>This is the response to the client request.</p>');
        res.end();

    
    } else {
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.write('<h1>404 - Page Not Found</h1>');
        res.end();
    }
});

server.listen(3000, () => {
    console.log('Server started at http://localhost:3000');
});