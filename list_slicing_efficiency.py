# list_slicing_efficiency.py

# Sample list
sneakers = ["new balances", "jordans", "yeezys", "balenciagas", "nikes"]

# Get the last two fruits
print("Last two sneakers:", sneakers[-2:])  # ['orange', 'mango']

# Get the first three fruits
print("First three sneakers:", sneakers[:3])  # ['apple', 'cherry', 'pineapple']

# Get all but the last fruit
print("All but last sneaker:", sneakers[:-1])  # ['apple', 'cherry', 'pineapple', 'orange']

# Efficiency tip: Avoid slicing if you just need one item
last_sneaker = sneakers[-1]
print("Last sneaker without slicing:", last_sneaker)
