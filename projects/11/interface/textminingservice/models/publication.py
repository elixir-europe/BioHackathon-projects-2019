class Publication:
    def __init__(self, title=None, year=None, journal_title=None, pmc_id=None, pm_id=None, doi=None, preprint_id=None, other_id=None):
        self.title = title
        self.year = year
        self.journal_title = journal_title
        self.pmc_id = pmc_id
        self.pm_id = str(pm_id)  # pubmed_id
        self.doi = doi
        self.preprint_id = preprint_id
        self.other_id = other_id

    def __repr__(self):
        ids = [("PMC_ID", self.pmc_id), ("PUBMED_ID", self.pm_id), ("DOI", self.doi),
               ("PREPRINT ID", self.preprint_id), ("OTHER ID", self.other_id)]
        return ' '.join([str(id) for id in ids if id[1] is not None])
