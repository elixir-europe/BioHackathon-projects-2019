$(document).ready(function() {
    window.localStorage.setItem('projectInfo', {});
    window.localStorage.setItem('sampleInfo', []);
    window.localStorage.setItem('analysisInfo', {});
    $('go-btn').click(refSetSearch)
})

const baseURL = "https://gigwa-dev.southgreen.fr/gigwaV2/rest/brapi/v2/"
    //const baseURL = "http://localhost:8081/gigwa2/rest/brapi/v2/"
    //const baseURL = "http://172.16.5.144:59395/Gigwa2/rest/brapi/v2/"
    //const baseURL = "http://172.16.5.144:59395/Gigwa2/rest/ga4gh/"
    //const baseURL = "http://gigwa.southgreen.fr/gigwa/rest/ga4gh/"

function refSetSearch(successCallback) {
    var URL = baseURL + "referencesets"
    var body = {}
    $.ajax({
        url: URL,
        type: 'get',
        //data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: successCallback
    });
}

function variantSetSearch(referenceSetID, successCallback) {
    var URL = baseURL + "search/variantsets"
    var body = { "referenceSetDbIds": [referenceSetID] }
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: successCallback
    });
}

function callSetSearch(variantSetID, successCallback) {
    var URL = baseURL + "search/callsets"
    var body = { "variantSetDbIds": [variantSetID], "pageSize": 10 }
    $.ajax({
        url: URL,
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: successCallback
    });
}

function sampleSearch(sampleDbIds, successCallback) {
    var URL = baseURL + "search/samples"
    var body = {
        "sampleDbIds": sampleDbIds,
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
        success: successCallback
    });
}

function germplasmSearch(germplasmDbIds, successCallback) {
    var URL = baseURL + "search/germplasm"
    var body = {
        "germplasmDbIds": germplasmDbIds,
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
        success: successCallback
    });
}

function goToValidator(samplesJSON, successCallback) {
    const body = samplesJSON;
    $.ajax({
        url: '/validate',
        type: 'post',
        data: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
            'Accept': '*/*'
        },
        dataType: 'json',
        success: successCallback
    });
}