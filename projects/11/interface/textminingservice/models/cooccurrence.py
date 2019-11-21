class CoOccurrence:
    def __init__(self, entity: str, score: float):
        self.entity = entity
        self.score = score

    def __repr__(self):
        return f'{self.entity} ({self.score})'
