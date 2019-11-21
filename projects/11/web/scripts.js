var app = new Vue({
  el: "#container",
  data: {
    entity: "",
    papers: []
  },
  methods: {
    //refactor this for a hard coded example for demo
    getExample: function() {
      var exampleDataJson =
        '[{"info": {"title": "Immunology Select", "year": "2007", "journal_title": "Cell", "pmc_id": null, "pm_id": null, "doi": "10.1016/j.cell.2007.05.012", "preprint_id": null, "other_id": "d7cb2216-bbd6-11e5-8abe-001a4ae51246", "id": "10.1016/j.cell.2007.05.012"}, "score": 1, "resources": ["BioKB"]}, {"info": {"title": "Production and characterisation of monoclonal antibodies to ovine interleukin-5", "year": "2003", "journal_title": "Parasitology International", "pmc_id": null, "pm_id": null, "doi": "10.1016/j.parint.2003.08.003", "preprint_id": null, "other_id": "89c62e0a-bbd4-11e5-9b9d-001a4ae51247", "id": "10.1016/j.parint.2003.08.003"}, "score": 1, "resources": ["BioKB"]}, {"info": {"title": "The Crystal Structure of a Major Dust Mite Allergen Der p 2, and its Biological Implications", "year": "2002", "journal_title": "Journal of Molecular Biology", "pmc_id": null, "pm_id": null, "doi": "10.1016/S0022-2836(02)00027-X", "preprint_id": null, "other_id": "9374c06a-bc3d-11e5-9b9d-001a4ae51247", "id": "10.1016/S0022-2836(02)00027-X"}, "score": 1, "resources": ["BioKB"]}, {"info": {"title": "Interactions between gastrointestinal nematode parasites and diarrhoea in sheep: Pathogenesis and control", "year": null, "journal_title": "The Veterinary Journal", "pmc_id": null, "pm_id": null, "doi": "10.1016/j.tvjl.2011.10.009", "preprint_id": null, "other_id": "0c68359c-bc3e-11e5-ac4e-001a4ae51246", "id": "10.1016/j.tvjl.2011.10.009"}, "score": 1, "resources": ["BioKB"]}, {"info": {"title": "En route to new blockbuster anti-histamines: surveying the offspring of the expanding histamine receptor family", "year": "2011", "journal_title": "Trends in Pharmacological Sciences", "pmc_id": null, "pm_id": null, "doi": "10.1016/j.tips.2011.02.004", "preprint_id": null, "other_id": "bd51727e-bc39-11e5-8d2d-001a4ae51247", "id": "10.1016/j.tips.2011.02.004"}, "score": 1, "resources": ["BioKB"]}]';
      var data = JSON.parse(exampleDataJson);
      this.$set(this, "papers", data);
    },
    getMentions: function() {
      var that = this;
      var entity = that.entity;
      var url = `http://9b9a4973.ngrok.io/getMentions/?entity=${entity}?limit=100`;
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
