# Monday 2019-11-18

* discusses BridgeDb<>identifiers.org with Nick, including use of MIRIAM and enhancement of compact identifiers
* Egon, Petros: discussed an attack plan to get the BridgeDb IMS Docker working again
   * worked on updating MySQL, but this requires completion of the `@Tag("mysql")` (the tests time out, a bug)
* Denise: worked on SPARQL to [count how many genes from a list occur in one or more pathways](https://www.wikipathways.org/index.php/Help:WikiPathways_Sparql_queries#Count_how_many_genes_from_a_list_occur_in_one_or_more_pathways). Also started with disease database mappings (from Wikidata).
* Emma: worked on PubChemLite evaluation, benchmarking subsets of [PubChem](https://pubchem.ncbi.nlm.nih.gov/) against [MassBank-data](https://github.com/MassBank/MassBank-data/) (starting with [CASMI2016](http://casmi-contest.org/2016/solutions-cat2+3.shtml))

# Tuesday 2019-11-19

* Travis now runs the tests for BridgeDb git master (but not webservices, mysql)
* PubChemLite benckmark now done for first dataset (Eawag EA) from [MetFrag Relaunched 2016](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-016-0115-9). Reusing downloaded [SI data](https://msbi.ipb-halle.de/~cruttkie/CHIN-D-15-00088/). Coding in R and prelim results encouraging. 
* PubChemLite benchmark now running for Eawag QEx data (see above). tier1 running, tier0 likely a Wed job. 
* New MetFrag COCONUT database [added](https://github.com/sneumann/container-metfrag/pull/3) c/o Maria, FSU Jena
* Worked on getting Validator, queryExpander, and IdentifierMappingService compiling on Travis too
* Worked with Andreas Tille on the Debian package of the [CDK](https://cdk.github.io/)
* Denise: added Disease ONtology, UMLS CUI and Orphanet.

# Wednesday 2019-11-20

* [schymane](https://github.com/schymane/) fixed legacy [MassBank-data](https://github.com/schymane/MassBank-data) repo issues resulting from dev branch creation after forking with the help of [meier-rene](https://github.com/meier-rene) to do long overdue curation of [CASMI2016 spectra](https://github.com/MassBank/MassBank-data/pull/101).
* PubChemLite benchmarking completed for Eawag QExPlus and UFZ data (i.e. all intended datasets at this point).
* [fixed two issues](https://github.com/egonw/rWikiPathways/pull/11) in the rWikiPathways package, after discussions with the Debian Med team (Andreas Tille)
* [NORMAN Suspect List Exchange](https://www.norman-network.com/nds/SLE/) upload feedback to Jeff from PubChem including error fixing my side on [Zenodo-SLE](https://zenodo.org/communities/norman-sle)$
* PubChemLite [tier0 and tier1](https://doi.org/10.5281/zenodo.3548654) released on Zenodo DOI: [10.5281/zenodo.3548654](https://doi.org/10.5281/zenodo.3548654) and [pushed to MetFrag](https://github.com/sneumann/container-metfrag/pull/5)
* Uploaded [Maven packages of Validator](https://github.com/bridgedb/Validator/packages) to GitHub Packages
* Figured out how to use GitHub Tokens securely on Travis-CI (see [this](https://github.com/bridgedb/IdentityMappingService/commit/57529c1ab961d0c3868bf2e661286597f03348b5) and [this](https://github.com/bridgedb/IdentityMappingService/commit/135386dee382d90a2354ae4391267c7deca281f2) and setting GITHUB_USERNAME and GITHUB_TOKEN in Travis)
* Travis now successfully compiles BridgeDb, Validator, queryExpender, and IdentifierMappingServices (closes [#43](https://github.com/elixir-europe/BioHackathon-projects-2019/issues/43))
* [added EDAM ontology annotation](https://salsa.debian.org/java-team/cdk/merge_requests/3) to the Debian libcdk-java package
* Denise: added MeSH descriptor IDs, discussed BridgeDb API with Intermine team.

# Thrusday 2019-11-21
* Denise: added ICD9+10+11.
