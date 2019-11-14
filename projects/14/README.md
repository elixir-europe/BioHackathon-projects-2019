# panoptes: Monitor computational workflows in real time

**Project Number:** 14

## Research area alignment

- In alignment with ELIXIR tools and compute platforms

## Team

**Submitter:** Argyrios Alexandros Gardelakos

### Proponent(s)

- Argyrios Alexandros Gardelakos

### Lead(s)

- Argyrios Alexandros Gardelakos
- Georgios Kostoulas

### Nominated participant(s)

- Georgios Ntalaperas, Programmer, Data transformation expert
- Foivos Gypas, Programmer, Bioinformatics expert (Swiss Institute of Bioinformatics)

## Background information

Bioinformaticians and data scientists, rely on computational frameworks (e.g. [snakemake](https://snakemake.readthedocs.io/en/stable/), [nextflow](https://www.nextflow.io/), [CWL](https://www.commonwl.org/), [WDL](https://software.broadinstitute.org/wdl/)) to process, analyze and integrate data of various types. Such frameworks allow scientists to combine software and custom tools of different origin in a unified way, which lets them reproduce the results of others, or reuse the same pipeline on different datasets. One of the fundamental issues is that the majority of the users execute multiple pipelines at the same time, or execute a multistep pipeline for a big number of datasets, or both, making it hard to track the execution of the individual steps or monitor which of the processed datasets are complete. panoptes is a tool that monitors the execution of such workflows.

panoptes is a service that can be used by:
- Data scientists, bioinformaticians, etc. that want to have a general overview of the progress of their pipelines and the status of their jobs
- Administrations that want to monitor their servers
- Web developers that want to integrate the service in bigger web applications

**Note:** panoptes is in early development stage and the first proof of concept server will support only workflows written in [snakemake](https://snakemake.readthedocs.io/en/stable/).

## Expected outcomes

- A working prototype to visualize and monitor the execution of workflows

Please take a look on the [project page of panoptes for the Paris Biohackathon 2019](https://github.com/panoptes-organization/panoptes/projects/1)

## Expected audience

- Bioinformaticians and programmers, but everyone with technical background is more than welcome

Useful skills:
- Programming skills: python, javascript, react.js, flask, web development, databases
- Authentication, authorization, JSON web tokens
- APIs, microservices
- Workflows (snakemake, nextflow, CWL)

**Number of expected hacking days**: 4

## Links

- panoptes github page: https://github.com/panoptes-organization/panoptes/projects/1
- panoptes example workflow: https://github.com/panoptes-organization/snakemake_example_workflow
- panoptes organization: https://github.com/panoptes-organization/
- panoptes video example: https://www.youtube.com/watch?v=Expb3odk0GQ