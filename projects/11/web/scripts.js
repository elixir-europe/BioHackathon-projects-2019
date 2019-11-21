var app = new Vue({
  el: "#container",
  data: {
    entity: "",
    papers: [],
    entities: []
  },
  methods: {
    showRipple: function() {
      var x = document.getElementById("lds-ripple");
      x.style.display = "inline-block";
    },
    hideRipple: function() {
      var x = document.getElementById("lds-ripple");
      x.style.display = "none";
    },
    //exmples for demo
    getAsthmaExample: function() {
      this.$set(this, "entity", "DOID:2841");
    },
    getGOExample: function() {
      this.$set(this, "entity", "GO:0002206");
    },
    getMentions: function() {
      var that = this;
      var entity = that.entity;
      var url = `http://9b9a4973.ngrok.io/getCooccurrence/?entity=${entity}&limit=30`;
      console.log(url);
      if (!entity) {
        alert("Enter an entity!");
      } else {
        this.showRipple();
        var jqxhr = $.ajax(url)
          .done(function(data) {
            that.hideRipple();
            that.$set(that, "entities", data);
            console.log("success", data);
          })
          .fail(function() {
            alert("error");
          })
          .always(function() {});
      }
    },
    getCooccurrences: function() {
      var that = this;
      var entity = that.entity;
      var url = "http://9b9a4973.ngrok.io/getCooccurrence/DOID:2841?type=9606";
      console.log(url);
      if (!entity) {
        alert("Enter an entity!");
      } else {
        this.showRipple();
        var jqxhr = $.ajax(url)
          .done(function(data) {
            that.hideRipple();
            that.$set(that, "entities", data);
            console.log("success", data);
            that.$set(that, "papers", data);
          })
          .fail(function() {
            alert("error");
          })
          .always(function() {});
      }
    }
  }
});
