var finalhandler = require('finalhandler');
var http = require('http');
var serveStatic = require('serve-static');
var express = require('express')

// Serve up public folder
var serve = serveStatic('public', { 'index': ['index.html'] });

const app = express();

app.use(express.static('public'))

app.get('/generate-file', (req, res) => {
    generateFile();
})

// Listen
app.listen(3000);

function generateFile() {
    console.log('generate file');
}