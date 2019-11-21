var app = new Vue({
  el: "#container",
  data: {
    entity: "",
    papers: []
  },
  methods: {
    //refactor this for a hard coded example for demo
    getPapers: function() {
      this.$set(this, "papers", [
        { text: "Paper 1 Title" },
        { text: "Some Other Paper" },
        { text: "Third Paper Title" }
      ]);
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
