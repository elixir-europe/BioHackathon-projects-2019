# Semantic recommendation system for life sciences publications

Authors

- Mustafa Anıl Tuncel (0000-0003-0317-2556)
- Toshiyuki T. Yokoyama (0000-0002-7345-6397)
- Ivan Topolsky (0000-0002-7561-0810)
- Kim Philipp Jablonski (0000-0002-4166-4343)
- Qiong Lin (0000-0002-7964-6191)
- Andreas Steffen

## Introduction

Keeping up with the recent advancements in science is a challenge. BioRxiv.org, the largest biology-focused preprint server had received 37,648 preprints by the end of November 2018 with a submission rate of over 2100 publications in October 2018 [1]. Retrieving the relevant scientific documents based on a text-based query is hard to achieve due to the unstructured nature of scientific publications. Use of domain-specific ontologies has the potential to improve over the current approaches by organising it into knowledge. The scientists at the European Organization for Nuclear Research (CERN) have developed INSPIRE information system which represents domain knowledge for high-energy physics specific scientific literature and provides a platform to enable scientists to access most relevant content to their research [2]. In the field of bioinformatics, EDAM ontology is developed for domain knowledge modelling [3]. Nevertheless, the corresponding information system is amiss. To this extent, we developed Quack<sup>2</sup>, a semantic recommender system for life sciences publications. Quack<sup>2</sup> has been built during the European Biohackathon 2019 event.

## System architecture

The system applies the event stream listener we developed during the European Biohackathon 2018 to retrieve scientific publications in real-time using the bioRxiv Twitter feed. We extract meta- and semantic-information from these publications using a custom-built parser, as well as EDAMmap [4]. The resulting RDF graph is converted to a property graph using Graph to Graph Mapping Language (G2GML) [5]. The property graph enables downstream analytical operations and algorithms such as centrality detection and recommendation to be performed. Finally, we provide a friendly user interface that allows users to find relevant research items in the search space of semantically annotated publications.

In order to test the efficiency and robustness of our system, we ran it on a single board computer (SBC) -- a Raspberry Pi 3B+. 
Our system showed resilience in this low spec environment. This gave us a reasonable expectation of its performance on more powerful hardware once we try scaling it to a huge data set and a large number of concurrent users.

## References

1. Abdill, R. J., & Blekhman, R. (2019). Meta-Research: Tracking the popularity and outcomes of all bioRxiv preprints. ELife, 8, e45133.
2. Ivanov, R., & Raae, L. (2010). INSPIRE: a new scientific information system for HEP. In Journal of Physics: Conference Series (Vol. 219, No. 8, p. 082010). IOP Publishing.
3. Ison, J., Kalaš, M., Jonassen, I., Bolser, D., Uludag, M., McWilliam, H., Malone, J., Lopez, R., Pettifer, S. and Rice, P. (2013). EDAM: an ontology of bioinformatics operations, types of data and identifiers, topics and formats. Bioinformatics, 29(10): 1325-1332.
4. Jaaniso, E. (2016). EDAMmap. https://github.com/edamontology/edammap.
5. Matsumoto, S., Yamanaka, R., & Chiba, H. (2018). Mapping RDF graphs to property graphs. arXiv preprint arXiv:1812.01801.
