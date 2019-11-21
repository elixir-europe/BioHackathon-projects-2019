# Implementation of Bioschema for Orphanet and Orphadata

**Project Number:** 15

## Orphanet DEV environment links (not public, need VPN)
Nb: JSON-LD is displayed in the page to show it (=> will be put into script tags obviously)

Nb: real implementation will need a new constructor within the framework engine (to optimize integration)

Nb: it works (=> possible to search different drugs, tradename, genes, diseases...)

Tradename example (http://dev.orpha.net/hanauer/consor4.01/www/cgi-bin/Drugs_Search.php?lng=EN&data_id=2583&Substance=VINCERINONE&Typ=Med&title=VINCERINONE&data_type=Product)

Drugs example (http://dev.orpha.net/hanauer/consor4.01/www/cgi-bin/Drugs_Search.php?lng=EN&data_id=2082&Tradename=Alpha-tocotrienol-quinone&Typ=Sub&title=Alpha-tocotrienol%20quinone&data_type=Product)

Gene example (http://dev.orpha.net/hanauer/consor4.01/www/cgi-bin/Disease_Genes.php?lng=EN&data_id=20738&Disease_Disease_Genes_diseaseGroup=brca1&Disease_Disease_Genes_diseaseType=Gen&MISSING%20CONTENT=BRCA1-associated-protein-1---BAP1&search=Disease_Genes_Simple&title=BRCA1%20associated%20protein%201%20-%20BAP1)

Disease example (http://dev.orpha.net/hanauer/consor4.01/www/cgi-bin/Disease_Search.php?lng=EN&data_id=91&Disease_Disease_Search_diseaseGroup=rett&Disease_Disease_Search_diseaseType=Pat&Disease(s)/group%20of%20diseases=Rett-syndrome&title=Rett%20syndrome&search=Disease_Search_Simple)

Disease HPO annotations example (http://dev.orpha.net/hanauer/consor4.01/www/cgi-bin/Disease_HPOTerms.php?lng=EN&data_id=8&Disease_Disease_HPOTerms_diseaseGroup=canavan&Disease_Disease_HPOTerms_diseaseType=Pat&Disease(s)/group%20of%20diseases=Canavan-disease&title=Canavan%20disease&search=Disease_HPOTerms_Simple)


## Docker image of Orphadata's FAIRdatapoint almost setup

Giving a machine readable access to Orphadata's datasets

Need look&feel customisation

## Research area alignment

- Elxir Core Data Resources
 Rare disease Elixir Communities
 Federated Data

## Team

**Submitter:** Marc Hanauer

### Proponent(s)

- Marc Hanauer

### Lead(s)

- Marc Hanauer
 David Lagorce
 
 ## Background information
---
Orphanet is a website dedicated to rare diseases, providing several kind of information such nomenclature, classifications, textual information, disorders/genes relations and also dedicated resources in the field (Experts centres, Diagnostic tests, clinical trials, orphandrugs, registries and biobanks, supports groups etc.) for more than 40 countries. 
The site has a huge audience, around 2 million unique visitors/month and 8 languages. 
![Orphanet](https://raw.githubusercontent.com/elixir-europe/BioHackathon/master/interoperability/Development%20of%20a%20catalog%20of%20federated%20SPARQL%20queries%20in%20the%20field%20of%20Rare%20Diseases/images/Orphanet.png)

The database content is linked to the Orphanet nomenclature

![Orphanet_Map](https://github.com/elixir-europe/BioHackathon/blob/master/interoperability/Development%20of%20a%20catalog%20of%20federated%20SPARQL%20queries%20in%20the%20field%20of%20Rare%20Diseases/images/ORPHANET-map.png)

and we provide several dataset, also accessible on our platform Orphadata https://www.orphadata.org

![Orphadata](https://github.com/elixir-europe/BioHackathon/raw/master/interoperability/Development%20of%20a%20catalog%20of%20federated%20SPARQL%20queries%20in%20the%20field%20of%20Rare%20Diseases/images/Screenshot_Orphadata.png)

Orphanet produce also the Orphanet Rare Diseases Ontology and clinical description of diseases using HPO ontology. Each disease concept has a unique, stable, identifier (Orphacode) which could be used to identify diseases in health information system. The orphacode has been integrated in several countries.
![Codification](https://github.com/elixir-europe/BioHackathon/raw/master/interoperability/Development%20of%20a%20catalog%20of%20federated%20SPARQL%20queries%20in%20the%20field%20of%20Rare%20Diseases/images/map-codificationOrpha2018.jpg)

### Nominated participant(s)

- Rajaram Kaliyaperumal (FAIR expert)
 Celine Rousselot (Orphanet PHP dev lead)
 David Lagorce (Orphanet/Orphadata project manager & Dev)
 Marc Hanauer (Orphanet CTO)
 
 (Please note: no travel fundings for Rousselot, Lagorce and Hanauer, only accommodation)

## Expected outcomes

- Improve interoperability of our core data resources
 FAIRdatapoint avalaible

## Expected audience

- FAIR expert
 PHP dev. (Orphanet's website)
 data model (RDF/Ontology)

**Number of expected hacking days**: 4

## Existing Repo
Orphanet website https://github.com/Orphanet/orphanet_website_biohack2019

Orphadata website https://github.com/davidlagorce/orphadata_website_biohack2019
