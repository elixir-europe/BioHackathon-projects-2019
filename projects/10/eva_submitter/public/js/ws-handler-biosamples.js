const baseURLBioSamples = "https://submission-dev.ebi.ac.uk/api/"

function getToken() {
    var URL = "https://explore.api.aai.ebi.ac.uk/auth"
    $.ajax({
        url: URL,
        type: 'get',
        headers: {
            'Authorization': 'Basic cHNlbGJ5OmJhbmdjbG9ja19lYmk=',
            'Accept': '*/*'
        },
        success: function(data, status) {
            window.localStorage.setItem('ebi_token', data);
        },
        error: function(data, status) {
            console.log('error');
            console.log(data);
        }
    });
}

function getTeams(successCallback) {
    var URL = baseURLBioSamples + "user/teams"
    $.ajax({
        url: URL,
        type: 'get',
        headers: {
            'Authorization': 'Bearer ' + window.localStorage.getItem('ebi_token'),
            'Accept': '*/*'
        },
        success: successCallback,
        error: function(data, status) {
            console.log('error');
            console.log(data);
        }
    });
}


function postTeam(successCallback) {
    var URL = baseURLBioSamples + "user/teams"
    var body = {
        "description": "My lab group",
        "centreName": "An Institute"
    }
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Authorization': 'Bearer ' + window.localStorage.getItem('ebi_token'),
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: successCallback
    });
}

function postSubmission(teamName, successCallback) {
    var URL = baseURLBioSamples + "teams/" + teamName + "/submissions";
    var body = {}
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Authorization': 'Bearer ' + window.localStorage.getItem('ebi_token'),
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: successCallback
    });
}

function postSamples(submissionId, sampleObj, successCallback) {
    var URL = baseURLBioSamples + "submissions/" + submissionId + "/contents/samples";
    var body = sampleObj;
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Authorization': 'Bearer ' + window.localStorage.getItem('ebi_token'),
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: successCallback
    });
}