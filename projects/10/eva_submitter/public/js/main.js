$(document).ready(function () {
    window.localStorage.setItem('projectInfo', {});
    window.localStorage.setItem('sampleInfo', []);
    window.localStorage.setItem('analysisInfo', {});
    $('go-btn').click(refSetSearch)
})

const baseURL = "http://172.16.5.144:59395/Gigwa2/rest/brapi/v2/";
//const baseURL = "http://172.16.5.144:59395/Gigwa2/rest/ga4gh/"
//const baseURL = "http://gigwa.southgreen.fr/gigwa/rest/ga4gh/"

function refSetSearch() {
    var URL = baseURL + "referencesets"
    var body = {};
    $.ajax({
        url: URL,
        type: 'get',
        //data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: function (data, status) {
            console.log(data);
            $('#mainPanel').empty();
            $('#mainPanel').append('<p class=\"col-sm-8 offset-sm-2\"> Reference Sets </p>')

            for (var refSet of data['result']['data']) {
                var id = refSet['referenceSetDbId'];
                var name = refSet['referenceSetName'];
                $('#mainPanel').append('<div class=\"btn btn-info col-sm-8 offset-sm-2\" onclick=\"variantSetSearch(\'' + id + '\');\">' + name + '</div>')
            }
        }
    });
}

function variantSetSearch(referenceSetID) {
    var URL = baseURL + "variantsets/search"
    var body = {"datasetId": referenceSetID}
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: function (data, status) {
            console.log(data);
            $('#mainPanel').empty();
            $('#mainPanel').append('<p class=\"col-sm-8 offset-sm-2\"> Variant Sets </p>')
            for (var variantset of data['variantSets']) {
                $('#mainPanel').append('<div class=\"btn btn-info col-sm-8 offset-sm-2\" onclick=\"callSetSearch(\'' + variantset['id'] + '\');\">' + variantset['name'] + '</div>')
            }
        }
    });
}

function callSetSearch(variantSetID) {
    var URL = baseURL + "callsets/search";
    var body = {"variantSetId": variantSetID, "pageSize": 10}
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: function (data, status) {
            console.log(data);
            $('#mainPanel').empty();
            $('#mainPanel').append('<p class=\"col-sm-8 offset-sm-2\"> Call Sets </p>')
            for (var callSet of data['callSets']) {
                $('#mainPanel').append('<div class=\"btn btn-info col-sm-8 offset-sm-2\" onclick=\"variantSearch(\'' + callSet['id'] + '\', \'' + variantSetID + '\');\">' + callSet['name'] + '</div>')
            }
        }
    });
}

function variantSearch(callSetID, variantSetID) {
    var URL = baseURL + "variants/search";
    var body = {
        "callSetIds": [callSetID],
        "variantSetId": variantSetID,
        "pageSize": 10
    }
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: function (data, status) {
            console.log(data);
            $('#mainPanel').empty();
            $('#mainPanel').append('<p class=\"col-sm-8 offset-sm-2\"> Variant </p>')
            for (var variant of data['variants']) {
                $('#mainPanel').append('<div class=\"btn btn-info col-sm-8 offset-sm-2\">' + variant['id'] + '</div>')
            }
        }
    });
}

function setSubbmitterDetails() {
    var formData = {};
    formData.lastName = document.getElementById("lastName").value;
    formData.firstName = document.getElementById("firstName").value;
    formData.phoneNumber = document.getElementById("phoneNumber").value;
    formData.email = document.getElementById("email").value;
    formData.laboratory = document.getElementById("laboratory").value;
    formData.center = document.getElementById("center").value;
    formData.address = document.getElementById("address").value;
    console.log('formData');
    console.log(formData);
    var myJsonData = JSON.stringify(formData);
    window.localStorage.setItem('submitterDetails', formData);
    refSetSearch();

}


function goToValidator() {
    const body = {alias : "MTB1"};
    $.ajax({
        url: '/validate',
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: function (data, status) {
            console.log(data);
            // $('#mainPanel').append('<p class=\"col-sm-8 offset-sm-2\"> Valid </p>')

        }
    });
}