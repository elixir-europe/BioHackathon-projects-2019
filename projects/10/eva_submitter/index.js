// var finalhandler = require('finalhandler');
// var http = require('http');
var serveStatic = require('serve-static');
var express = require('express');
var { ElixirValidator } = require('elixir-jsonschema-validator');
var bodyParser = require("body-parser");

// Serve up public folder
//var serve = serveStatic('public', {'index': ['index.html']});

var app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static('public'));

app.post('/validate', async function(req, res) {
    console.log('step 1');
    var response = await validator(req.body.alias)
        .then((validationResult) => {
            console.log(validationResult);
            res.send(validationResult);
        });
    console.log('step 2');
});


// Listen
app.listen(3000);

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
    let jsonObj = { 'alias': data };
    let validator = new ElixirValidator();
    let validatorResponse = {};
    let validatorMessages = [];
    return validator.validate(jsonSchema, jsonObj).then((validationResult) => {
        validatorResponse = { status: validationResult.validationState };
        console.log(validationResult.validationState);
        for (let errors of validationResult.validationErrors) {
            validatorMessages.push(errors.userFriendlyMessage);
            console.log(errors.userFriendlyMessage)
        }
        validatorResponse.messages = validatorMessages;
        return JSON.stringify(validatorResponse)
    });
}