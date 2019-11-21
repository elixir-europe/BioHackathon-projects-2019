var app = new Vue({
  el: "#container",
  data: {
    todos: []
  },
  methods: {
    getPapers: function() {
      this.$set(this, "todos", [
        { text: "Learn JavaScript" },
        { text: "Learn Vue" },
        { text: "Build something awesome" }
      ]);
    }
  }
});
