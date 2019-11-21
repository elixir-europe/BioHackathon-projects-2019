class CoOccurrence:
    def __init__(self, entity: str, score: float):
        self.entity = entity
        self.score = score

    def __repr__(self):
        return f'{self.entity} ({self.score})'

    def as_dict(self):
        d = dict(entity=self.entity, score=self.score)
        return {k: v for k, v in d.items() if v is not None}
