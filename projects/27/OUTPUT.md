# Monday 2019-11-18

* discusses BridgeDb<>identifiers.org with Nick, including use of MIRIAM and enhancement of compact identifiers
* Egon, Petros: discussed an attack plan to get the BridgeDb IMS Docker working again
   * worked on updating MySQL, but this requires completion of the `@Tag("mysql")` (the tests time out, a bug)
* Denise: worked on SPARQL to [count how many genes from a list occur in one or more pathways](https://www.wikipathways.org/index.php/Help:WikiPathways_Sparql_queries#Count_how_many_genes_from_a_list_occur_in_one_or_more_pathways)
* Emma: worked on PubChemLite evaluation, benchmarking subsets of [PubChem](https://pubchem.ncbi.nlm.nih.gov/) against [MassBank-data](https://github.com/MassBank/MassBank-data/) (starting with [CASMI2016](http://casmi-contest.org/2016/solutions-cat2+3.shtml))

# Tuesday 2019-11-19

* Travis now runs the tests for BridgeDb git master (but not webservices, mysql)
* PubChemLite benckmark now done for first dataset (Eawag EA) from [MetFrag Relaunched 2016](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-016-0115-9). Reusing downloaded [SI data](https://msbi.ipb-halle.de/~cruttkie/CHIN-D-15-00088/). Coding in R and prelim results encouraging. 
* PubChemLite benchmark now running for Eawag QEx data (see above). tier1 running, tier0 likely a Wed job. 
* New MetFrag COCONUT database [added](https://github.com/sneumann/container-metfrag/pull/3) c/o Maria, FSU Jena
* Worked on getting Validator, queryExpander, and IdentifierMappingService compiling on Travis too
* Worked with Andreas Tille on the Debian package of the [CDK](https://cdk.github.io/)

# Wednesday 2019-11-20

* [schymane](https://github.com/schymane/) fixed legacy [MassBank-data](https://github.com/schymane/MassBank-data) repo issues resulting from dev branch creation after forking with the help of [meier-rene](https://github.com/meier-rene) to do long overdue curation of [CASMI2016 spectra](https://github.com/MassBank/MassBank-data/pull/101).
* PubChemLite benchmark running for Eawag QExPlus data.
* fixed two issues in the rWikiPathways package, after discussions with the Debian Med team (Andreas Tille)
