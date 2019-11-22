var app = new Vue({
  el: "#container",
  data: {
    entity: "",
    papers: [],
    entities: []
  },
  methods: {

    showRipple: function () {
      var x = document.getElementById("lds-ripple");
      x.style.display = "inline-block";
    },
    hideRipple: function () {
      var x = document.getElementById("lds-ripple");
      x.style.display = "none";
    },
    //exmples for demo
    getAsthmaExample: function () {
      this.$set(this, "entity", "DOID:2841");
    },
    getGOExample: function () {
      this.$set(this, "entity", "GO:0002206");
    },
    getMentions: function () {
      var that = this;
      var entity = that.entity;
      var url = `http://7fccb2cc.ngrok.io/getMentions/?entity=${entity}&limit=100`;
      if (!entity) {
        alert("Enter an entity!");
      } else {
        this.showRipple();
        var jqxhr = $.ajax(url)
          .done(function (data) {
            that.hideRipple();
            that.$set(that, "entities", []);
            that.$set(that, "papers", data);
            console.log("success mentions", data);
            that.checkDOIs();
          })
          .fail(function () {
            alert("error");
          })
          .always(function () { });
      }
    },
    getCooccurrences: function () {
      var that = this;
      var entity = that.entity;
      var url = "http://7fccb2cc.ngrok.io/getCooccurrence/DOID:2841?type=9606";
      if (!entity) {
        alert("Enter an entity!");
      } else {
        this.showRipple();
        var jqxhr = $.ajax(url)
          .done(function (data) {
            that.hideRipple();
            that.$set(that, "papers", []);
            that.$set(that, "entities", data);
            console.log("success entities", data);

          })
          .fail(function () {
            alert("error");
          });
      }
    },
    checkDOIs: function () {
      var that = this;
      _.forEach(app.papers, function (paper, idx) {
        if (paper.info.doi == undefined) {
          if (paper.info.pm_id != undefined) {
            that.getDOI(paper.info.pm_id, 'pm_id', idx, that);
          } else if (paper.info.pmc_id != undefined) {
            that.getDOI(paper.info.pm_id, 'pmc_id', idx, that);
          }
        }
      });
    },
    getDOI: function (id, type, pub_index, vue_app) {
      if (type == 'pmc_id') {
        var idtype = "pmcid";
      } else if (type == 'pm_id') {
        var idtype = "pmid";
      } else {
        var idtype = "";
      }

      var url = `https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?tool=my_tool&email=my_email@example.com&ids=${id}&format=json`;

      var jqxhr = $.ajax(url)
        .done(function (data) {
          if (data.records.length > 0) {
            if (data.records[0].doi != undefined) {
              vue_app.$set(vue_app.papers[pub_index].info, 'doi', data.records[0].doi);
            }
          }
        }).fail(function () {
          console.log(`Error for ${id} ${type} ${pub_index} and url ${url}`);
        });

    }
  }
});
