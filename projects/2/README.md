# bio.tools & EDAM drop-in hackathon & discussions

**Project Number:** 2

## Research area alignment

- Aligns with ELIXIR Tools Platform and other end-users of bio.tools and EDAM ontology.

## Team

**Submitter:** Jon Ison

### Proponent(s)

- Jon Ison

### Lead(s)

- Jon Ison
- Hans Ienasescu

### Nominated participant(s)

- Hans Ienasescu, (bio.tools expert)
- Alban Gaignard (ELIXIR-FR)

## Priorities (set during the hackathon)

1. **ELIXIR Tools platform ecosystem** - gathering technical requirements from the tools platform and stakeholders. Planning.
2. **Tool information profiles** - to specifies which tool attributes - defined in biotoolsSchema - should be specified within a set of tool descriptions, e.g. from a project, institute, ELIXIR node *etc.*
3. **Bioschema tool profile** - settle this 
4. **Bioschema data dump and embedding** - dump of Bioschema (schema.org) metadata for all tools in *bio.tools*. Embed schema.org mark-up in *bio.tools*
5. **biotoolsSchema & bio.tools updates** - *e.g.* support for organisational IDs
6. **bio.tools subdomains** (discussion) more flexible / sustainable ways to define *bio.tools* subdomain content





## Expected outcomes

At least a couple of the following:

For implementation:
 1. Improving the EDAM Formats subontology:
    - Technical quality assurance tests and user guidelines 
    - Validator for quality control 
    - Curation to bring things up to standard
 2. Using bio.tools & EDAM to curate complex online tools, e.g. [RSAT](http://rsat01.biologie.ens.fr/rsa-tools/RSAT_home.cgi).
 3. Improved support for bio.tools Dockerisation process (especially Windows) and local development environment.
 
Discussion & planning:
 1. Technical planning and ideas around task queues and scheduling for maintenance and housekeeping of bio.tools (e.g. Celery).
 2. Engage with communities (national, scientific and projects) on how to improve EDAM for their applications.
    - French tool developers & providers describing their tools for the IFB catalogue.
 3. How to leverage EDAM conceptual relationships within software catalogues (bio.tools, IFB catalogue) to improve content quality and optimise the registration process.
 4. Discussions around GitHub-based content management architecture.
    - continuous integration of bio.tools with GitHub
    - managing pull requests in a sustainable way, e.g. for high volume of automatically generated entries

## Expected audience

- programmers (Python, Django REST Framework, Python Celery), software tool developers, ontologists, technical project managers

**Number of expected hacking days**: 4

