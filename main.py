from pirates import Captain
from pirates import Quartermaster
from pirates import Officer
from pirates import CannonOperator

pirates = [
    Captain("Harry"),
    Quartermaster("Isabel"),
    Officer("Bootstrap Bill"),
    CannonOperator("Powder Joe"),
    Officer("Four Finger Fritz"),
    CannonOperator("Lady Joyce")
]
ducats = 920
sum_of_ranks = sum(pirate.rank for pirate in pirates)

for pirate in pirates:
    share = pirate.rank / sum_of_ranks * ducats
    print(f"{pirate.title} {pirate.name} gets {share:.2f} Ducats.")

