# Disease and pathway maps for Rare Diseases

**Project Number:** 5

## Research area alignment

- This biohackathon aligns with the following ELIXIR platforms: data, tools and interoperability. ELIXIR communities which may find it relevant are Human Data and Rare Diseases.

## Resources and guidelines

A breakdown of work, suggested resources and approach [can be found here](http://bit.ly/bh-rdmaps).

## Team

**Submitter:** Marek Ostaszewski

### Proponent(s)

- Marek Ostaszewski

### Lead(s)

 - Marek Ostaszewski
 Research Fellow
 Université du Luxembourg
 Luxembourg Centre for Systems Biomedicine (LCSB)
 6, avenue du Swing
 L-4367 Belvaux, Luxembourg
 email: marek.ostaszewski@uni.lu

- Laura I. Furlong
 Research Programme on Biomedical Informatics (GRIB)
 Hospital del Mar Medical Research Institute (IMIM)
 DCEXS, Pompeu Fabra University (UPF)
 Carrer del Dr. Aiguader, 88, 08003 Barcelona, Spain
 email: laura.furlong@upf.edu
 
 - Joaquin Dopazo
 Clinical Bioinformatics Area, Director
 Fundacion Progreso y Salud
 CDCA, Hospital Virgen del Rocío
 c/Manuel Siurot s/n, 
 41013, Sevilla, Spain
 email: joaquin.dopazo@juntadeandalucia.es

### Nominated participant(s)

1. Maria Pena Chilet, expertise in pathway modeling in translational medicine
2. Piotr Gawron, expertise in knowledge visualization and translational medicine data formats

## Expected outcomes

A working prototype of a search and visualization interface that, given the search criteria and, if available, omics data, will scan the considered resources, combine the results into a molecular diagram, which then will become available for visualization in MINERVA and Hipathia platforms, linking the results to the sources in DisGeNET and other repositories. 
 
 A suggested workflow will look as follows:
 1. For a rare disease from Orphanet, retrieve the genes/variants from DisGeNET
 2. Interrogate disease maps via MINERVA to retrieve pathways in which these genes/variants are involved
 3. Identify omics data for the RD from omics data repository (e.g. transcriptomics)
 4. Feed output of 3 and 2 into Hipathia for modelling disease processes
 5. Use MINERVA for visualization of identified disease maps, and/or for integration of retrieved data
 
If successful, we plan to continue this collaboration and aim for at least one bioinformatics paper. We will actively explore the possibility of establishing this search and visualization engine as part of ELIXIR services.

## Expected audience

- Bioinformaticians with expertise in handling clinical data to define and consult use-cases for the RD mechanisms search
- Bioinformaticians skilled in information retrieval, knowledge exchange and systems biology formats (SBML, SBGN, BioPAX) to design and implement the intra-tool pipelines
- Bioinformaticians skilled in omics data retrieval and integration, to design and implement the data-level pipelines, including RD-connect
- Web developers proficient with JavaScript to implement the search and visualization interface based on existing MINERVA plugin architecture

## Confirmed participants

Importantly, the organizers ensure participation of 1 web developer, and the following bioinformaticians: one for clinical data handling, one for knowledge retrieval and exchange and two for omics data handling.

**Number of expected hacking days**: 4

