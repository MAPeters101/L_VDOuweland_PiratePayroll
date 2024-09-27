pirates = [
    ("Harry", "Captain", 5),
    ("Isabel", "Quatermaster", 3),
    ("Bootstrap Bill", "Mate", 3),
    ("Powder Joe", "Gunner",2),
    ("Four Finger Fritz", "Mate", 2)
]
ducats = 850
sum_of_ranks = sum(rank for name, title, rank in pirates)

for name, title, rank in pirates:
    share = rank / sum_of_ranks * ducats
    print(f"{title} {name} gets {share:.2f} Ducats.")
