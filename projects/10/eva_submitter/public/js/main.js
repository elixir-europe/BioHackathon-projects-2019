$(document).ready(function() {
    refSetSearch();
})

function refSetSearch() {

    $('#start-btn').click(function() {
        var URL = "http://gigwa.southgreen.fr/gigwa/rest/ga4gh/referencesets/search"
        var body = {}
        $.post(URL, JSON.stringify(body), function(data, status) {
            alert(status);
            console.log(data);
        });
    })
}