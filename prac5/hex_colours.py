COLOURS = {
    'Absolute Zero': '#0048ba',
    'Acid Green': '#b0bf1a',
    'AliceBlue': '#f0f8ff',
    'Alizarin Crimson': '#e32636',
    'British Racing Green': '#004225',
    'Chestnut': '#954535',
    'UP Maroon': '#7b1113',
    'Van Dyke Brown': '#664228',
    'Volt': '#ceff00'
}

for name in COLOURS:
    print(name.lower())

choice = input('What colour code do you want?').strip().lower()
while choice != 'q':
    for name in COLOURS:
        if choice == name.lower():
            print(f"{name} colour code is {COLOURS[name]}")
            choice = input('What colour code do you want?').strip().lower()
    else:
        print("No such colour available!")
