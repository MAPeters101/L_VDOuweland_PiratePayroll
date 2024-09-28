class Share:
    def __init__(self, pirate, ducats):
        self.pirate = pirate
        self.ducats = ducats

class Payroll:
    def calculate_shares(self, crew, ducats):
        sum_of_ranks = sum(pirate.role.rank for pirate in crew)
        return [Share(pirate, pirate.role.rank / sum_of_ranks * ducats) for pirate in crew]
