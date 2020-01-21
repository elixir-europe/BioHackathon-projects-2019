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

Our workflow can be subdivided into three separate steps

One of such tools is MINERVA platform [PMID:31074494](https://www.ncbi.nlm.nih.gov/pubmed/31074494), allowing hosting and visual exploration of curated disease maps. Another tool of choice is Hipathia platform, allowing to interpret gene expression and mutation data into perturbations of signaling pathways. We will combine these two platforms with the content-rich DisGeNET resource and with our BioKB text mining platform for identification of evidence supporting a particular RD. We will also scan the contents of publicly available disease maps and OpenTargets for potential information pieces. We will align this bioinformatics setup with available data repositories for RDs, like RD-connect, to enable data-driven search for relevant knowledge. The search and visualization of the results will be implemented using existing building blocks, including the MINERVA plugin architecture.

## Results at the BioHackathon'19

## Summary and outlook
