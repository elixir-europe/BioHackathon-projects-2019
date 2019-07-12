# FAIRifying REDCap Clinical Research Data Collection

**Project Number:** 34

## Research area alignment

- ELIXIR Data Platform

## Team

**Submitter:** Nicola Mulder

### Proponent(s)

- Nicola Mulder

### Lead(s)

- Katherine Johnston
 Mamana Mbiyavanga <Mamana>
 
 Computational Biology Division, University of Cape Town, South Africa

### Nominated participant(s)

- We will seek potential collaborators from the data platform and human/rare disease communities in ELIXIR

## Expected outcomes

- General outcomes:
 -Potentially a paper called “Ten lesson learnt making clinical research databases FAIR”?
 -REDCap “FAIRify” external module (built in PHP and Javscript) publicly available on GitHub for installation (this will be reviewed by REDCap and if it passes validation, will be added to the REDCap public repository of external modules)
 -Project Configuration External Module to collect project meta data which will be incorporated in the “FAIRify” META-META data
 
 Specific output of the hackathon are:
 
 1) An external module in REDCap that allows clinical research database to include all the necessary machine code for machine readable metadata of the REDCap metadata (contained in the Data Dictionary). Perhaps a plugin that makes use of REDCap’s Data Dictionary import facility to import metadata to add to the data dictionary
 META-META data should include:
 -Unique, persistent project identifier and variable ID
 -Location of dataset 
 -Type of dataset
 -Data Use Ontology Code (DUO Code)
 -Participant consent codes (this should be derived from participant data consent component see Item 4.)
 
 2) Data definition code (derived from pre-defined ontology dictionaries used by that project). Type of data source (with specific reference including name and location if possible – data provenance, type of data source would determine the requirements here e.g. direct patient report needs no further information but imported data may need raw data file details, machine details, data processing date etc.)
 
 3) Version Control of the META-META configurations
 
 4) To provide a human readable configuration and output of (1) in the REDCap database, with interactive configuration on the online designer (linking to appropriate web-based ontology definitions of use)
 
 5) Possibly extend the capabilities of the ontology lookup fields in REDCap by storing additional ontology information of data values on input (this may not be necessary)
 
 6) To include a patient consent component into REDCap project. This means provide ontology consent coding to attach to project specific consent requirements, including a participant interactive dashboard – this would be time dependent and possibly not achievable during hacakthon. 
 
 7) To include a project configuration component for clinical research project definition and meta data specifications (to be appended in Item 1 module)

## Expected audience

- REDCap experienced PHP software developers with clinical data management experience or exposure to Ontologies database implementation and FAIR data requirements.

**Number of expected hacking days**: 4

