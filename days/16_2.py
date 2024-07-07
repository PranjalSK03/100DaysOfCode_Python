#orettytable is a package installed from http://www.pypi.org
# to draw perfect ASCII tables
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmainder", "Bulbasaur"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])

print(table)