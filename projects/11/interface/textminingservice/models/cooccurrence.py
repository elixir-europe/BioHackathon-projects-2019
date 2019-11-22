class CoOccurrence:
    def __init__(self, entity: str, score: float, entity_type: str = None):
        self.entity = entity
        self.score = score
        self.entity_type = entity_type

    def __repr__(self):
        return f'{self.entity} - {self.entity_type} ({self.score})'

    def as_dict(self):
        d = dict(entity=self.entity, score=self.score,
                 entity_type=self.entity_type)
        return {k: v for k, v in d.items() if v is not None}
