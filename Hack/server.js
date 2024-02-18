const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');
const qs = require('querystring');

// In-memory storage for user accounts (replace with a database in a real application)
const users = [
    { username: 'user1', password: 'password1' },
    { username: 'user2', password: 'password2' }
];

// Create a server
const server = http.createServer((req, res) => {
    // Parse request URL
    const parsedUrl = url.parse(req.url, true);
    const pathname = parsedUrl.pathname;

    if (pathname === '/') {
        // Serve the login page
        fs.readFile(path.join(__dirname, 'user.html'), (err, data) => {
            if (err) {
                res.writeHead(500);
                res.end('Error loading user.html');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data);
            }
        });
    } else if (pathname === '/login' && req.method === 'POST') {
        // Process login form submission
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });
        req.on('end', () => {
            const formData = qs.parse(body);
            const { username, password } = formData;
            // Authenticate user
            const user = users.find(user => user.username === username && user.password === password);
            if (user) {
                 fs.readFile(path.join(__dirname, 'list.html'), (err, data) => {
            if (err) {
                res.writeHead(500);
                res.end('Error loading list.html');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data);
				
            }
        });
            } else {
                res.writeHead(401, { 'Content-Type': 'text/html' });
                res.end('<h1>Unauthorized</h1>');
            }
        });
    }else if (pathname === '/result' && req.method === 'POST') {
		// Process search
        let body = '';
        req.on('data', chunk => {
            body += chunk.toString();
        });
		
        req.on('end', () => {
            const formData = qs.parse(body);
            const { Name,Author,ISBN} = formData;
            
            
               
		
		
		const { exec } = require('child_process');

const pythonFilePath = './show_websites.py';

// Execute the Python file using the 'python' command
exec(`python ${pythonFilePath} `+Name+' '+'#@ '+Author+' #@ '+ISBN, (error, stdout, stderr) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  if (stderr) {
    console.error(`stderr: ${stderr}`);
    return;
  }
  
  res.writeHead(200, { 'Content-Type': 'text/html' });          
  res.end(`
  
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Site List</title>
  
</head>
<body style="background-color: green;">
  <center>
  <form action="/result" method="POST">
        <label for="Name">Book Name:</label><br>
        <input type="text" id="Name" name="Name" ><br>
        <label for="author">Author</label><br>
        <input type="text" id="Author" name="Author" ><br>
        <label for="ISBN">ISBN</label><br>
        <input type="text" id="ISBN" name="ISBN" ><br>
		
        <input type="submit" value="Find">
    </form>
  
  <h1 style="background-color: #FFCC33;">Websites</h1>
  
  <h style="font size: 2px;"> ${stdout}</h2>
      

     
 
  
  </center>
  <center>
  <l2> <img src=https://seeklogo.com/images/G/George_Mason_Patriots-logo-5D994883C6-seeklogo.com.png>    </l2>
  </center>

`);
});

		
		
		
		
        });
	}else {
        // Handle 404 Not Found
        res.writeHead(404, { 'Content-Type': 'text/html' });
        res.end('<h1>404 Not Found</h1>');
    }
});

// Set the port
const port = process.env.PORT || 3000;

// Start the server
server.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
