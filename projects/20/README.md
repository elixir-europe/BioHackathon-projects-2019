# Improving the interoperability of the core intrinsically disordered protein (IDP) resource

## Research area alignment

- tools, compute, data, personal data sharing e.g. EGA/JGA

## Team

### Proponent(s)

- Tazro Ohta

### Lead(s)

- Tazro Ohta

### Nominated participant(s)

- Hirotaka Suetake, main developer of the SAPPORO system
 Manabu Ishii, CWL project commiter 
 Tazro Ohta, SAPPORO project lead

## Expected outcomes

- This proposal is based on the idea of sharing workflows, so the outcomes may vary with the people we can work with. If we could have audiences who already have workflows that analyze the personal genomic data, we will describe them in CWL, and then test on our system running on DDBJ's HPC platform. We can help to package tools in containers for that as well, but it will be more productive if there were the BioConda/BioContainers team and/or the Elixir tool registry team. We already have CWL workflows that run on our system, so we can share our workflows and test if they are truly portable when there is a workflow execution platform team such as Galaxy. Our system can run workflows for non-human data as well, so we can import and test the workflows already described in CWL such as the MGnify workflow developed by the EBI Metagenome team or pgap pipeline developed by NCBI. We would be happy to present our system in details and help to deploy if there were people interested in having a similar system on their computing platform.

## Expected audience

- Developers who are familiar with workflow languages such as CWL
 Data producers who are interested in sharing personal genome data

**Number of expected hacking days**: 4

