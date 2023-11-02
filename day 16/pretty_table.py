import prettytable

table = prettytable.PrettyTable()

table.add_column("Pokèmon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)