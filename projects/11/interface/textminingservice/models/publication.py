class Publication:
    PUBMED_BASE_URL = "https://www.ncbi.nlm.nih.gov/pubmed/{}"

    def __init__(self, title=None, year=None, journal_title=None, pmc_id=None, pm_id=None, doi=None, preprint_id=None,
                 other_id=None):
        self.title = title
        self.year = year
        self.journal_title = journal_title
        self.pmc_id = pmc_id
        if pm_id is not None:
            self.pm_id = str(pm_id)  # pubmed_id
        else:
            self.pm_id = None
        self.doi = doi
        self.preprint_id = preprint_id
        self.other_id = other_id

    @property
    def id(self):
        return self.pm_id or self.pmc_id or self.doi or self.preprint_id or self.other_id

    @property
    def uri(self):
        if self.pm_id:
            return Publication.PUBMED_BASE_URL.format(self.pm_id)
        return None

    def __repr__(self):
        ids = [("PMC_ID", self.pmc_id), ("PUBMED_ID", self.pm_id), ("DOI", self.doi),
               ("PREPRINT ID", self.preprint_id), ("OTHER ID", self.other_id)]
        return ' '.join([str(id) for id in ids if id[1] is not None])

    def as_dict(self):
        return dict(
            title=self.title,
            year=self.year,
            journal_title=self.journal_title,
            pmc_id=self.pmc_id,
            pm_id=self.pm_id,
            doi=self.doi,
            preprint_id=self.preprint_id,
            other_id=self.other_id,
            id=self.id
        )
