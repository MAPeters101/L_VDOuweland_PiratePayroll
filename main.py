from data import TestDataLoader
from data import JSONDataLoader
from payroll import Payroll

loader = TestDataLoader()
#loader = JSONDataLoader()
pirates = loader.load_pirates()

ducats = 100

payroll = Payroll()
shares = payroll.calculate_shares(pirates, ducats)

for share in shares:
    print(f"{share.pirate.role.title} {share.pirate.name}, rank {share.pirate.role.rank} gets share {share.ducats:.2f} Ducats.")

