from guitar import Guitar

guitars = []
print('My guitars!')
name = 'default'
while True:
    name = input('Name: ')
    if not name:
        break
    year = int(input('Year: '))
    cost = int(input('Cost: '))
    print(f'{name} ({year}) : ${cost} added.')
    guitars.append(Guitar(name, year, cost))

for i, guitar in enumerate(guitars, 1):
    vintage_str = " (vintage)" if guitar.is_vintage() else ""
    print(f'Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost}{vintage_str}')
