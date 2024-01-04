class Train:
    def __init__(self):
        self.schedules = []

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def display_info(self):
        return ", ".join(self.schedules)    