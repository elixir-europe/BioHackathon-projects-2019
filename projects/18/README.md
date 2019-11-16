# Implementation and sharing of workflows for personal genomic data on DDBJ's workflow execution system SAPPORO

**Project Number:** 18

## Research area alignment

- Tools and workflow development and deployment
- Cloud computing
- Personal data sharing and analysis

## Team

**Submitter:** Tazro Ohta

### Proponent(s)

- Tazro Ohta

### Lead(s)

- Tazro Ohta

### Nominated participant(s)

![Hiro](http://data.dbcls.jp/~inutano/misc/bh19paris/images/suecharo_paris2018.png)

Hirotaka Suetake [@suecharo](https://github.com/suecharo): Main developer of the SAPPORO system

![Manabu](http://data.dbcls.jp/~inutano/misc/bh19paris/images/manabu_paris2019.png)

Manabu Ishii [@manabuishii](https://github.com/manabuishii): CWL project commiter

![Taz](http://data.dbcls.jp/~inutano/misc/bh19paris/images/inutano_paris2018.png)

Tazro Ohta [@inutano](https://github.com/inutano): SAPPORO project lead

...And you!

## Expected outcomes

- Help people who want to deploy the Sapporo system
  - Requirements: Docker & Docker Compose
- Improve Sapporo system
  - Support runners
    - [x] [cwltool](https://github.com/common-workflow-language/cwltool)
    - [ ] [Toil](https://github.com/BD2KGenomics/toil)
    - [ ] [Cromwell](https://github.com/broadinstitute/cromwell)
    - [ ] [nextflow](http://nextflow.io/)
  - integration of utilities
    - [ ] [CWL-metrics](https://github.com/inutano/cwl-metrics), runtime metrics collection system
    - [ ] [tonkaz](https://github.com/suecharo/tonkaz), a test framework for command line tool
- Test systems with existing workflows
  - [ ] [DAT2-CWL](https://github.com/pitagora-network/dat2-cwl)
  - [ ] [bio-cwl-tools](https://github.com/common-workflow-library/bio-cwl-tools)
  - [ ] [nf.core](https://nf-co.re/)
- Work with the other GA4GH WES implementation
  - Elixir WES by [project number 16](../16/)

## Expected audience

- Data scientists for human genome sequence
- Workflow developers
  - CWL, WDL, nextflow, or other WF languages
- Infrastructure Dev/Ops engineers
  - Container deployment
    - Docker
    - Singularity
  - Public cloud operation
    - AWS batch

**Number of expected hacking days**: 4+
