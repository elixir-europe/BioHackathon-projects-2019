$(document).ready(function() {})

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

    setItemStorage('submitterDetails', formData);

    var sampleDetails = {};
    refSetSearch(
        function(data, status) {

            console.log(data);

            $('#mainPanel').empty();
            $('#mainPanel').append('<p class=\"col-sm-8 offset-sm-2\"> Reference Sets </p>')

            var refernceSets = {}

            for (var refSet of data['result']['data']) {
                var id = refSet['referenceSetDbId'];
                var name = refSet['referenceSetName'];
                refernceSets[id] = refSet;
                $('#mainPanel').append('\
                    <div \
                    class=\"btn btn-info col-sm-8 offset-sm-2\" \
                    onclick=\"setReferenceSet(\'' + id + '\');\">' +
                    name + '</div>')
            }

            setItemStorage('refernceSetsRaw', refernceSets);
        }
    );

}

function setReferenceSet(referenceSetId) {
    console.log(getItemStorage('refernceSetsRaw'));
    var referenceSet = getItemStorage('refernceSetsRaw')[referenceSetId];
    setItemStorage('refernceSet', referenceSet);

    variantSetSearch(referenceSet['referenceSetDbId'], function(data, status) {
        console.log(data);

        $('#mainPanel').empty();
        $('#mainPanel').append('<p class=\"col-sm-8 offset-sm-2\"> Variant Sets </p>')

        var variantSets = {};

        for (var variantSet of data['result']['data']) {
            var id = variantSet['variantSetDbId'];
            var name = variantSet['variantSetName'];
            variantSets[id] = variantSet;
            $('#mainPanel').append('<div \
            class=\"btn btn-info col-sm-8 offset-sm-2\" \
            onclick=\"setVariantSet(\'' + id + '\');\">' +
                name + '</div>')

        }

        setItemStorage('variantSetsRaw', variantSets);
    })
}

function setVariantSet(variantSetId) {
    var variantSet = getItemStorage('variantSetsRaw')[variantSetId];
    setItemStorage('variantSet', variantSet);

    gatherSampleData(variantSet['variantSetDbId']);
}

function gatherSampleData(variantSetId) {

    $('#mainPanel').empty();
    $('#mainPanel').append('<div class="row"><div id="loading-log" class="col-xs-6"></div><img id="loading-gif" class="col-xs-6" src="images/spinner.gif" /></div>')
    $('#loading-log').append('<p class=\"col-xs-12\"> Gathering Sample Data </p>')

    callSetSearch(variantSetId, function(data, status) {
        console.log(data);

        var callSets = {};
        var sampleDbIds = [];

        for (var callSet of data['result']['data']) {
            callSets[callSet['callSetDbId']] = callSet;
            sampleDbIds.push(callSet['sampleDbId']);
        }

        setItemStorage('callSets', callSets);
        $('#loading-log').append('<p class=\"col-xs-12\">' + Object.keys(callSets).length + ' Call Sets Found </p>')

        sampleSearch(sampleDbIds, function(data, status) {

            console.log(data);

            var samples = {};
            var germplasmDbIds = [];

            for (var sample of data['result']['data']) {
                samples[sample['sampleDbId']] = sample;
                germplasmDbIds.push(sample['germplasmDbId']);
            }

            setItemStorage('samples', samples);
            $('#loading-log').append('<p class=\"col-xs-12\">' + Object.keys(samples).length + ' Samples Found </p>')

            germplasmSearch(germplasmDbIds, function(data, status) {
                console.log(data);

                var germplasmList = {};

                for (var germplasm of data['result']['data']) {
                    germplasmList[germplasm['germplasmDbId']] = germplasm;
                }

                setItemStorage('germplasmList', germplasmList);
                $('#loading-log').append('<p class=\"col-xs-12\">' + Object.keys(germplasmList).length + ' Germplasm Found </p>')

                var sampleObjs = packageSampleData();
                goToValidator(sampleObjs, function(data, status) {

                    $('#loading-log').append('<p class=\"col-xs-12\"> Finished </p>')
                    $('#loading-gif').remove();
                });
            });
        });
    });
}

function packageSampleData() {
    var callSets = getItemStorage('callSets');
    var samples = getItemStorage('samples');
    var germplasmList = getItemStorage('germplasmList');
    var sampleObjs = [];
    for (var callSetDbId of Object.keys(callSets)) {
        var callSet = callSets[callSetDbId];
        var sample = samples[callSet['sampleDbId']];
        var germplasm = germplasmList[sample['germplasmDbId']];
        var sampleObj = {};

        if (callSet['callSetDbId'])
            sampleObj.biological_material_ID = callSet['callSetDbId'];

        if (sample['sampleDescription'])
            sampleObj.material_source_description = sample['sampleDescription'];

        if (germplasm['germplasmGenus'])
            sampleObj.genus = germplasm['germplasmGenus'];
        if (germplasm['germplasmSpecies'])
            sampleObj.species = germplasm['germplasmSpecies'];
        if (germplasm['subtaxa'])
            sampleObj.infraspecific_name = germplasm['subtaxa'];
        if (germplasm['germplasmPreprocessing'])
            sampleObj.biological_material_preprocessing = germplasm['germplasmPreprocessing'];
        if (germplasm['instituteCode'] && germplasm['accessionNumber'])
            sampleObj.material_source_ID = germplasm['instituteCode'] + ':' + germplasm['accessionNumber'];
        if (germplasm['germplasmPUI'])
            sampleObj.material_source_DOI = germplasm['germplasmPUI'];
        //if (germplasm['taxonIds'] && germplasm['taxonIds'][0] && germplasm['taxonIds'][0]['sourceName'] && germplasm['taxonIds'][0]['taxonId'])
        sampleObj.organism = 'test';
        //sampleObj.organism = germplasm['taxonIds'][0]['sourceName'] + ':' + germplasm['taxonIds'][0]['taxonId'];
        if (germplasm['germplasmOrigin'] && germplasm['germplasmOrigin'][0]) {
            var germplasmOrigin = germplasm['germplasmOrigin'][0];
            if (germplasmOrigin['latitudeDecimal'])
                sampleObj.biological_material_latitude = germplasmOrigin['latitudeDecimal'];
            if (germplasmOrigin['longitudeDecimal'])
                sampleObj.biological_material_longitude = germplasmOrigin['longitudeDecimal'];
            if (germplasmOrigin['altitude'])
                sampleObj.biological_material_altitude = germplasmOrigin['altitude'];
            if (germplasmOrigin['coordinateUncertainty'])
                sampleObj.biological_material_coordinate_uncertainty = germplasmOrigin['coordinateUncertainty'];
            if (germplasmOrigin['latitudeDecimal'])
                sampleObj.material_source_latitude = germplasmOrigin['latitudeDecimal'];
            if (germplasmOrigin['longitudeDecimal'])
                sampleObj.material_source_longitude = germplasmOrigin['longitudeDecimal'];
            if (germplasmOrigin['altitude'])
                sampleObj.material_source_altitude = germplasmOrigin['altitude'];
            if (germplasmOrigin['coordinateUncertainty'])
                sampleObj.material_source_coordinate_uncertainty = germplasmOrigin['coordinateUncertainty'];
        }
        sampleObjs.push(sampleObj);
    }
    console.log(sampleObjs);
    return sampleObjs;
}

function setItemStorage(key, value) {
    window.localStorage.setItem(key, JSON.stringify(value));
}

function getItemStorage(key) {
    var obj = JSON.parse(window.localStorage.getItem(key));
    return obj;
}