var serveStatic = require('serve-static');
var express = require('express');
var { ElixirValidator } = require('elixir-jsonschema-validator');
var bodyParser = require('body-parser');
var request = require('request');

var app = express();

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static('public'));

app.post('/validate', async function(req, res) {
    console.log(req.body);
    var responseList = [];
    for (var sample of req.body) {
        var response = await validator(sample)
            .then((validationResult) => {
                responseList.push(validationResult)
            })
    }
    res.send(responseList);
});


// Listen
app.listen(3000);

let jsonSchema;
request('https://raw.githubusercontent.com/FAIRsharing/mircat/mircat-ebiusi/miappe/schema/biological_material_schema.json', function(error, response, body) {
    if (!error && response.statusCode == 200) {
        jsonSchema = JSON.parse(body);
    }
});

function validator(data) {
    console.log('Doing validation...');
    console.log(data);
    let jsonObj = data;
    let validator = new ElixirValidator();
    let validatorResponse = {};
    let validatorMessages = [];
    return validator.validate(jsonSchema, jsonObj).then((validationResult) => {
        validatorResponse = { status: validationResult.validationState };
        console.log(validationResult.validationState);
        for (let errors of validationResult.validationErrors) {
            let enrichedMessage = 'The biological material ID: ' + data.biological_material_ID + ' ' + errors.userFriendlyMessage;
            validatorMessages.push(enrichedMessage);
            console.log(errors.userFriendlyMessage)
        }
        validatorResponse.messages = validatorMessages;
        return validatorResponse
    });
}