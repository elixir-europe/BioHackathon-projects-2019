// var finalhandler = require('finalhandler');
// var http = require('http');
var serveStatic = require('serve-static');
var express = require('express');
var {ElixirValidator} = require('elixir-jsonschema-validator');
var bodyParser = require("body-parser");

// Serve up public folder
//var serve = serveStatic('public', {'index': ['index.html']});

var app = express();

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.use(express.static('public'));

app.post('/validate', (req, res) => {
    res.send(validator(req.body.alias));

});


// Listen
app.listen(3000);

function generateFile() {
    console.log('generate file');
}


let jsonSchema = {
    $schema: "http://json-schema.org/draft-07/schema#",
    type: "object",
    properties: {
        alias: {
            description: "A sample unique identifier in a submission.",
            type: "string"
        }
    },
    required: ["alias"]
};

function validator(data) {
    console.log('Doing validation...');
    let jsonObj = {'alias': data};
    let validator = new ElixirValidator();
    let validatorResponse = {};
    let validatorMessages =[];
    validator.validate(jsonSchema, jsonObj).then((validationResult) => {
        validatorResponse={status: validationResult.validationState};
        console.log(validationResult.validationState);
        for (let errors of validationResult.validationErrors) {
            validatorMessages.push(errors.userFriendlyMessage);
            console.log(errors.userFriendlyMessage)
        }
        validatorResponse.messages = validatorMessages;
        return JSON.stringify(validatorResponse)
    });
}