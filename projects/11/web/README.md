# Introduction to OLS-autocomplete
This is a standalone widget for people to include the OLS autocomplete widget and search box within their own homepage. The widget can be seen in action at the start page of the <a href="https://www.ebi.ac.uk/ols">Ontology Lookup Service (OLS)</a>.

**PLEASE MAKE SURE YOU USE HTTPS INSTEAD OF HTTP URLS IN THE FUTURE FOR EBI WEBSERVICE CALLS**

## How to install the plugin
There are multiple ways to install the plugin:
* Download the javascript file (ols-autocomplete.js) stored in the 'build' folder. Include the file by using normal script tags. See the example html pages for more information
* The plugin in is available as npm module - search for ols-autocomplete or use this link
* The widget is listed on the bio.js website where you could find other interesting .js libraries for biological data


## How to start the plugin
To be able to use the widget, you have to include an html <input> field with some additional information. After the html is set up, the start of the widget in javascript is rather simple. Please check the example in the folder for more information.   
#### HTML
```
<input style="font-weight: normal" size="35" type="text" name="q" data-olswidget="select" data-olsontology="" data-selectpath="https://www.ebi.ac.uk/ols/" olstype="" id="local-searchbox" placeholder="Enter the term you are looking for" class="ac_input"></input>
```
* data-olswidget: The potential values are 'select' or 'multisearch', which leads to different handling of the input. Please check the example to see the difference
* data-olsontology: This can be an empty string '' or can narrow the search for suggestions down to a certain ontology.
* data-selectpath: Stores the base url for the interaction with the webservice. In almost all cases, this is going to be https://www.ebi.ac.uk/ols/
* (data-olstype:)

#### Javascript
To start the plugin, the widget has to be required, an instance has to be Initialized and the plugin then started.
```
<script>
$(document).ready(function() {
  var app = require("ols-autocomplete");
  var instance = new app();
  instance.start()
});
</script>
```
# Dependencies
* **JQuery**: Has to be available when you want to include the plugin (https://jquery.com)
* **handlebars**: Is used, so make sure you include it in your script tags (http://handlebarsjs.com/)
* **typeahead**: Also, the plugin uses typeahead (https://github.com/twitter/typeahead.js/) so make sure you include it as well
Check the examples for correct script tags and links to relevant CDNs. Of course can also host the libs locally and adjust the script tags accordingly  

# Contact
Please <a href="https://github.com/LLTommy/ols-autocomplete">use github</a> to report **bugs**, discuss potential **new features** or **ask questions** in general.

# License
The plugin is released under the Apache License Version 2.0. You can find out more about it at http://www.apache.org/licenses/LICENSE-2.0 or within the license file of the repository.

# If you are interested in this plugin...
...you might also want to have a look at
- the **ols-treeview** package, see <a href="https://github.com/LLTommy/OLS-treeview">github</a> or <a href="https://www.npmjs.com/package/ols-treeview">npm</a>
- the **ols-graphview** package as well, see <a href="https://github.com/LLTommy/OLS-graphview">Github</a> or <a href="https://www.npmjs.com/package/ols-graphview">npm</a>
