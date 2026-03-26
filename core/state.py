class TimetableState:
    def __init__(self, assignments=None):
        self.assignments = assignments or {}

    def copy(self):
        return TimetableState(self.assignments.copy())