//BASE_URL = 'http://7fccb2cc.ngrok.io';
BASE_URL = 'http://127.0.0.1:5000';

var app = new Vue({
    el: "#container",
    data: {
        entity: "",
        papers: [],
        entities: [],
        graph: []
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
            var url = `${BASE_URL}/getMentions/?entity=${entity}&limit=50`;
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
                    .always(function () {
                    });
            }
        },

        getCooccurrences: function () {
            var that = this;
            var entity = that.entity;
            // var url = "http://127.0.0.1:5000/getCooccurrence/DOID:2841?type=9606";
            var url = `${BASE_URL}/getCooccurrence/${entity}`;
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
        getGraphMentions: function () {
            var that = this;
            var entity = that.entity;
            var url = `${BASE_URL}/getMentions/?entity=${entity}&limit=100&format=cytoscape`;
            // var url = `http://127.0.0.1:5000/getMentions/?entity=${entity}&limit=100&format=cytoscape`;
            this.getGraphData(url);
        },
        getGraphCooccurrences: function () {
            var that = this;
            var entity = that.entity;
            var url = `${BASE_URL}/getCooccurrence/${entity}?limit=100&format=cytoscape`;
            // var url = `http://127.0.0.1:5000/getMentions/?entity=${entity}&limit=100&format=cytoscape`;
            this.getGraphData(url);
        },
        getGraphData: function (url) {
            console.log(url);
            var jqxhr = $.ajax(url)
                .done(function (data) {
                    cy.elements().remove();
                    cy.reset();
                    cy.add(data);
                    var layout = cy.layout({
                        name: 'concentric'
                    });

                    layout.run();
                    that.$set(that, "graph", data);
                    console.log("success graph", data);
                })
                .fail(function () {
                    alert("error");
                })
                .always(function () {
                });
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

var cy = cytoscape({

    container: document.getElementById('cy'), // container to render in

    elements: [],

    style: [
        {
            "selector": "core",
            "style": {
                "selection-box-color": "#AAD8FF",
                "selection-box-border-color": "#8BB0D0",
                "selection-box-opacity": "0.5"
            }
        },
        {
            "selector": "node",
            "style": {
                "width": "mapData(score, 0, 100, 40, 5)",
                "height": "mapData(score, 0, 100, 40, 5)",
                "label": "data(name)",
                "font-size": "12px",
                "text-valign": "center",
                "text-halign": "center",
                "background-color": "#00554e",
                "text-outline-color": "#ffc353",
                "text-outline-width": "2px",
                "color": "#fff",
                "overlay-padding": "6px",
                "z-index": "10"
            }
        },
        {
            "selector": "node[?attr]",
            "style": {
                "shape": "rectangle",
                "background-color": "#aaa",
                "text-outline-color": "#aaa",
                "width": "16px",
                "height": "16px",
                "font-size": "6px",
                "z-index": "1"
            }
        },
        {
            "selector": "node[?query]",
            "style": {
                "background-clip": "none",
                "background-fit": "contain"
            }
        },
        {
            "selector": "node:selected",
            "style": {
                "border-width": "6px",
                "border-color": "#AAD8FF",
                "border-opacity": "0.5",
                "background-color": "#77828C",
                "text-outline-color": "#77828C"
            }
        },
        {
            "selector": "edge",
            "style": {
                "curve-style": "haystack",
                "haystack-radius": "0.5",
                "opacity": "0.4",
                "line-color": "#bbb",
                "width": "mapData(weight, 0, 1, 1, 8)",
                "overlay-padding": "3px"
            }
        },
        {
            "selector": "node.unhighlighted",
            "style": {
                "opacity": "0.2"
            }
        },
        {
            "selector": "edge.unhighlighted",
            "style": {
                "opacity": "0.05"
            }
        },
        {
            "selector": ".highlighted",
            "style": {
                "z-index": "999999",
                "transition-duration": "0.5s"
            }
        },
        {
            "selector": "node.highlighted",
            "style": {
                "border-width": "8px",
                "border-color": "#AAD8FF",
                "border-opacity": "0.85",
                "background-color": "#394855",
                "text-outline-color": "#394855",
                "shadow-blur": "12px",
                "shadow-color": "#000",
                "shadow-opacity": "0.8",
                "shadow-offset-x": "0px",
                "shadow-offset-y": "4px",
                "transition-property": "border-width, border-color, border-opacity, background-color, text-outline-color, shadow-blur, shadow-color, shadow-opacity, shadow-offset-x, shadow-offset-y"
            }
        },
        {
            "selector": "node.start",
            "style": {
                "border-color": "#8FDC97"
            }
        },
        {
            "selector": "node.end",
            "style": {
                "border-color": "#9F4A54"
            }
        },
        {
            "selector": "edge.filtered",
            "style": {
                "opacity": "0"
            }
        },
        {
            "selector": "edge[group = \"coexp\"]",
            "style": {
                "line-color": "#d0b7d5"
            }
        },
        {
            "selector": "edge[group = \"coloc\"]",
            "style": {
                "line-color": "#a0b3dc"
            }
        },
        {
            "selector": "edge[group = \"gi\"]",
            "style": {
                "line-color": "#90e190"
            }
        },
        {
            "selector": "edge[group = \"path\"]",
            "style": {
                "line-color": "#9bd8de"
            }
        },
        {
            "selector": "edge[group = \"pi\"]",
            "style": {
                "line-color": "#eaa2a2"
            }
        },
        {
            "selector": "edge[group = \"predict\"]",
            "style": {
                "line-color": "#f6c384"
            }
        },
        {
            "selector": "edge[group = \"spd\"]",
            "style": {
                "line-color": "#dad4a2"
            }
        },
        {
            "selector": "edge[group = \"spd_attr\"]",
            "style": {
                "line-color": "#D0D0D0"
            }
        },
        {
            "selector": "edge[group = \"reg\"]",
            "style": {
                "line-color": "#D0D0D0"
            }
        },
        {
            "selector": "edge[group = \"reg_attr\"]",
            "style": {
                "line-color": "#D0D0D0"
            }
        },
        {
            "selector": "edge[group = \"user\"]",
            "style": {
                "line-color": "#f0ec86"
            }
        },
        {
            "selector": "node[?social]",
            "style": {
                "width": 30,
                "height": 30,
                "background-image": "data(image)",
                "background-fit": "cover"
            }
        },
        {
            "selector": "node[?social]:selected",
            "style": {
                "border-width": 4,
                "border-opacity": 0.8
            }
        },
        {
            "selector": "edge[?social]",
            "style": {
                "width": 3,
                "line-color": "#888",
                "opacity": 0.4,
                "haystack-radius": 0
            }
        },
        {
            "selector": "edge.highlighted",
            "style": {
                "line-color": "#AAD8FF",
                "width": "10px"
            }
        }
    ]
    ,

    layout: {
        name: 'grid',
        rows: 1
    }

});
