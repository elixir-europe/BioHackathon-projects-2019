# Disease and pathway maps for Rare Diseases

## Authors
 - **Submitter and proponent:** Marek Ostaszewski
 - **Leads:** Marek Ostaszewski, Laura I. Furlong, Joaquin Dopazo
 - **Nominated participants:** Maria Pena Chilet, Piotr Gawron
 - **Participants:** Janet Pinero, Marina Esteban, Jose Luis Fernandez, David Hoksza, Vincenza Colonna
 
### LCSB, University of Luxembourg, Luxembourg
 - Piotr Gawron (0000-0002-9328-8052)
 - David Hoksza (0000-0003-4679-0557)
 - Marek Ostaszewski (0000-0003-1473-370X)

### University Pompeu Fabra, Barcelona, Spain
 - Laura I. Furlong (0000-0002-9383-528X)
 - Janet Pinero (0000-0003-1244-7654)
 
### Fundacion Progreso y Salud, Sevilla, Spain
 - Joaquin Dopazo (0000-0003-3318-120X)
 - Maria Pena Chilet (0000-0002-6445-9617)
 - Marina Esteban (0000-0003-2632-9587)
 - Jose Luis Fernandez ()
  
### Institute of Genetics and Biophysics, National Research Council of Italy
 - Vincenza Colonna (0000-0002-3966-0474)


## Abstract

## Introduction

Investigation of causal mechanisms behind Rare Diseases (RDs) is challenging, as these disorders are nor prevalent enough to be represented in major bioinformatics resources or pathway databases. At the same time, a number of disease-focused resources are developed which could offer insights into specific rare diseases, if searched systematically. During BioHackathon'19 we based on an existing, rich, open source/open access infrastructure focused on disease-related mechanisms. We focused on repositories with well-defined APIs to facilitate their integration. 

We streamlined different tools and platforms to enable pan-resource searches for specific questions of the field of RD research. We based on standardized definitions and encoding of disease phenotypes, supported the search process with high-throughput data, whenever applicable. Using these searches, we retrieved genes and variants relevant for the disease mechanisms. Using these relevant genes and variants, we identified enriched, publicly available pathway databases and disease maps, togehter with text mining results, to combine them into a custom disease map, generated on-the-fly. This way, a researcher is able to define an RD of choice, or encode its phenotype, to generate a relevant disease map prototype for further refinement.

## Approach and resources

Our workflow can be subdivided into three, conceptually separate steps:

1. Getting data about the disease context for a given RD
2. Creating a network of known mechanisms from a set of selected repositories
3. Producing an online, interactive map prototype

### Disease context
In order to introduce disease context, we focused on two major resources: OrphaNet ([orpha.net](https://www.orpha.net)) and Human Phenotype Ontology (HPO) [PMID:27899602](https://www.ncbi.nlm.nih.gov/pubmed/27899602). Unique identifiers of OrphaNet allow to identify an RD, and if this disease is still not classified, it is possible to identify a proximal OrphaNet id by similarity of HPO terms.

For given OrphaNet identifers, we obtained the list of relevant genes and variants by combining: i) gene-disease mapping of OrphaNet, ii) gene-disease and variant-disease mapping of DisGeNET [PMID:25877637](https://www.ncbi.nlm.nih.gov/pubmed/25877637) ([disgenet.org](https://www.disgenet.org)), iii) variant-disease mapping of OpenTargets platform [PMID:30462303](https://www.ncbi.nlm.nih.gov/pubmed/30462303) ([opentargets.org](https://www.opentargets.org)) and iii) variant-disease mapping of ClinVar ([www.ncbi.nlm.nih.gov/clinvar/](https://www.ncbi.nlm.nih.gov/clinvar/)). Importantly, disease-associated variants were filtered for rarity using population allele frequencies obtained from Ensembl Variant Effect Predictor (VEP) ([www.ensembl.org/info/docs/tools/vep/](https://www.ensembl.org/info/docs/tools/vep/)).

In parallel, for same OrphaNet identifers, we searched ArrayExpress [PMID:30357387](https://www.ncbi.nlm.nih.gov/pubmed/30357387) ([www.ebi.ac.uk/arrayexpress/](https://www.ebi.ac.uk/arrayexpress/)) and Gene Expression Omnibus [PMID:27008011](https://www.ncbi.nlm.nih.gov/pubmed/27008011) ([www.ncbi.nlm.nih.gov/geo/](http://www.ncbi.nlm.nih.gov/geo/)) to retrieve a list of Differentially Expressed Genes (DEGs), to extend the the set of disease-associated genes.

### Network of mechanisms
The disease-relevant list of genes and variants was then used to construct a network of mechanisms using three different resources: disease maps, pathways and text mining.

Disease maps offer standardized and diagrammatic description of disease mechanisms [PMID:29872544](https://www.ncbi.nlm.nih.gov/pubmed/29872544), and with the help of Gene Set Enrichment Analysis can be queried for areas of significance for a given gene list [PMID:31074494](https://www.ncbi.nlm.nih.gov/pubmed/31074494). These areas can be exported together with their layout information, thanks to the capabilities of Systems Biology Markup Language to support layout and render information, and functionalities of the MINERVA Platform [PMID:31273380](https://www.ncbi.nlm.nih.gov/pubmed/31273380).

Another set of resources that support building the network of mechanisms are pathway databases. They also offer diagrammatic description of mechanisms in molecular biology, but less relevant to a particular disease. Nevertheless, they area a valuable resource and can be evaluated using enrichment. We focused on WikiPathways [PMID:29136241](https://www.ncbi.nlm.nih.gov/pubmed/29136241) ([wikipathways.org](https://wikipathways.org)).

Finally, to fetch potentially novel interactions between the preselected genes, we used String [PMID:30476243](https://www.ncbi.nlm.nih.gov/pubmed/30476243) ([string-db.org](https://string-db.org/)). As these interactions are non-directional and may contain noise, we relied on the OmniPath resource [PMID:27898060](https://www.ncbi.nlm.nih.gov/pubmed/27898060) to increase reliability, and to obtain directionality and sign of interaction.

### Interactive prototype

One of such tools is MINERVA platform [PMID:31074494](https://www.ncbi.nlm.nih.gov/pubmed/31074494), allowing hosting and visual exploration of curated disease maps. Another tool of choice is Hipathia platform, allowing to interpret gene expression and mutation data into perturbations of signaling pathways. We will combine these two platforms with the content-rich DisGeNET resource and with our BioKB text mining platform for identification of evidence supporting a particular RD. We will also scan the contents of publicly available disease maps and OpenTargets for potential information pieces. We will align this bioinformatics setup with available data repositories for RDs, like RD-connect, to enable data-driven search for relevant knowledge. The search and visualization of the results will be implemented using existing building blocks, including the MINERVA plugin architecture.

## Results at the BioHackathon'19

## Summary and outlook
