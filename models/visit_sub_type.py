class VisitSubType:
    def __init__(self, id, abbreviation, name, billableTime):
        self.id = id
        self.abbreviation = abbreviation
        self.name = name
        self.billableTime = billableTime

    def __repr__(self):
        return str((self.id, self.abbreviation, self.name, self.billableTime))

    def __hash__(self):
        return self.id