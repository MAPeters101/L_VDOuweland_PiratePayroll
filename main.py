pirates = ["Harry", "Isabel", "Bootstrap Bill", "Morgan", "Powder Joe"]

ducats = 480

share = ducats / len(pirates)

for pirate in pirates:
    print(f"{pirate} gets {share} Ducats.")