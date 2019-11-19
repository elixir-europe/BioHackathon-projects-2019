$(document).ready(function() {
    window.localStorage.setItem('submitterDetails', {});
    window.localStorage.setItem('projectInfo', {});
    window.localStorage.setItem('sampleInfo', []);
    window.localStorage.setItem('analysisInfo', {});
    $('go-btn').click(refSetSearch)
})

//const baseURL = "http://172.16.5.144:59395/Gigwa2/rest/ga4gh/"
const baseURL = "http://gigwa.southgreen.fr/gigwa/rest/ga4gh/"

function refSetSearch() {
    var URL = baseURL + "referencesets/search"
    var body = {}
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: function(data, status) {
            console.log(data);
            $('#refSetList').empty();
            $('#refSetList').append('<p class=\"col-sm-8 offset-sm-2\"> Reference Sets </p>')

            for (var refSet of data['referenceSets']) {
                $('#refSetList').append('<div class=\"btn btn-info col-sm-8 offset-sm-2\" onclick=\"variantSetSearch(\'' + refSet['id'] + '\');\">' + refSet['name'] + '</div>')
            }
        }
    });
}

function variantSetSearch(referenceSetID) {
    var URL = baseURL + "variantsets/search"
    var body = { "datasetId": referenceSetID }
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: function(data, status) {
            console.log(data);
            $('#refSetList').empty();
            $('#refSetList').append('<p class=\"col-sm-8 offset-sm-2\"> Variant Sets </p>')
            for (var variantset of data['variantSets']) {
                $('#refSetList').append('<div class=\"btn btn-info col-sm-8 offset-sm-2\" onclick=\"callSetSearch(\'' + variantset['id'] + '\');\">' + variantset['name'] + '</div>')
            }
        }
    });
}

function callSetSearch(variantSetID) {
    var URL = baseURL + "callsets/search"
    var body = { "variantSetId": variantSetID, "pageSize": 10 }
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: function(data, status) {
            console.log(data);
            $('#refSetList').empty();
            $('#refSetList').append('<p class=\"col-sm-8 offset-sm-2\"> Call Sets </p>')
            for (var callSet of data['callSets']) {
                $('#refSetList').append('<div class=\"btn btn-info col-sm-8 offset-sm-2\" onclick=\"variantSearch(\'' + callSet['id'] + '\', \'' + variantSetID + '\');\">' + callSet['name'] + '</div>')
            }
        }
    });
}

function variantSearch(callSetID, variantSetID) {
    var URL = baseURL + "variants/search"
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
        success: function(data, status) {
            console.log(data);
            $('#refSetList').empty();
            $('#refSetList').append('<p class=\"col-sm-8 offset-sm-2\"> Variant </p>')
            for (var variant of data['variants']) {
                $('#refSetList').append('<div class=\"btn btn-info col-sm-8 offset-sm-2\">' + variant['id'] + '</div>')
            }
        }
    });
}