var app = new Vue({
  el: "#container",
  data: {
    entity: "",
    papers: []
  },
  methods: {
    //exmples for demo
    getAsthmaExample: function() {
      var exampleDataJson =
        '[{"info": {"title": "Immunology Select", "year": "2007", "journal_title": "Cell", "pmc_id": null, "pm_id": null, "doi": "10.1016/j.cell.2007.05.012", "preprint_id": null, "other_id": "d7cb2216-bbd6-11e5-8abe-001a4ae51246", "id": "10.1016/j.cell.2007.05.012"}, "score": 1, "resources": ["BioKB"]}, {"info": {"title": "Production and characterisation of monoclonal antibodies to ovine interleukin-5", "year": "2003", "journal_title": "Parasitology International", "pmc_id": null, "pm_id": null, "doi": "10.1016/j.parint.2003.08.003", "preprint_id": null, "other_id": "89c62e0a-bbd4-11e5-9b9d-001a4ae51247", "id": "10.1016/j.parint.2003.08.003"}, "score": 1, "resources": ["BioKB"]}, {"info": {"title": "The Crystal Structure of a Major Dust Mite Allergen Der p 2, and its Biological Implications", "year": "2002", "journal_title": "Journal of Molecular Biology", "pmc_id": null, "pm_id": null, "doi": "10.1016/S0022-2836(02)00027-X", "preprint_id": null, "other_id": "9374c06a-bc3d-11e5-9b9d-001a4ae51247", "id": "10.1016/S0022-2836(02)00027-X"}, "score": 1, "resources": ["BioKB"]}, {"info": {"title": "Interactions between gastrointestinal nematode parasites and diarrhoea in sheep: Pathogenesis and control", "year": null, "journal_title": "The Veterinary Journal", "pmc_id": null, "pm_id": null, "doi": "10.1016/j.tvjl.2011.10.009", "preprint_id": null, "other_id": "0c68359c-bc3e-11e5-ac4e-001a4ae51246", "id": "10.1016/j.tvjl.2011.10.009"}, "score": 1, "resources": ["BioKB"]}, {"info": {"title": "En route to new blockbuster anti-histamines: surveying the offspring of the expanding histamine receptor family", "year": "2011", "journal_title": "Trends in Pharmacological Sciences", "pmc_id": null, "pm_id": null, "doi": "10.1016/j.tips.2011.02.004", "preprint_id": null, "other_id": "bd51727e-bc39-11e5-8d2d-001a4ae51247", "id": "10.1016/j.tips.2011.02.004"}, "score": 1, "resources": ["BioKB"]}]';
      var data = JSON.parse(exampleDataJson);
      this.$set(this, "papers", data);
    },
    getOtherExample: function() {
      var exampleDataJson =
        '[{"info": {"title": "Methylation protects cytidines from AID-mediated deamination", "year": "2005", "journal_title": "Molecular Immunology", "doi": "10.1016/j.molimm.2004.09.007", "other_id": "43bbc250-bc4f-11e5-9b9d-001a4ae51247", "id": "10.1016/j.molimm.2004.09.007"}, "score": 1, "resources": ["BioKB"]}, {"info": {"title": "AID Enzyme-Induced Hypermutation in an Actively Transcribed Gene in Fibroblasts | Science", "year": "2002", "journal_title": "Science", "pm_id": "12065838", "doi": "10.1126/science.1071556", "other_id": "833a4178-cb2b-11e5-a6cd-001a4ae51247", "id": "12065838"}, "score": 1, "resources": ["BioKB"]}, {"info": {"title": "The activation-induced cytidine deaminase (AID) efficiently targets DNA in nucleosomes but only during transcription", "journal_title": "The Journal of Experimental Medicine", "pmc_id": "PMC2715043", "pm_id": "19380635", "doi": "10.1084/jem.20082678", "other_id": "c5603162-bbf8-11e5-9b9d-001a4ae51247", "id": "19380635"}, "score": 1, "resources": ["BioKB"]}]';
      var data = JSON.parse(exampleDataJson);
      this.$set(this, "papers", data);
    },

    getMentions: function() {
      var that = this;
      var entity = that.entity;
      var url = `http://9b9a4973.ngrok.io/getMentions/?entity=${entity}&limit=100`;
      console.log(url);
      var jqxhr = $.ajax(url)
        .done(function(data) {
          data = JSON.parse(data);

          that.$set(that, "papers", data);
          console.log("success", data);
        })
        .fail(function() {
          alert("error");
        })
        .always(function() {});
    }
  }
});
