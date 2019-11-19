class Publication:
    def __init__(self, pmc_id=None, pm_id=None, doi=None, preprint_id=None, other_id=None):
        self.pmc_id = pmc_id
        self.pm_id = pm_id
        self.doi = doi
        self.preprint_id = preprint_id
        self.other_id = other_id