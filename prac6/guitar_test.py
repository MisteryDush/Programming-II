from guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 5000)
another_guitar = Guitar("Noob's guitar", 2013, 100)

print(f'Gibson L-5 CES get_age() - Expected 100. Got {gibson.get_age()}')
print(f'Another Guitar get_age() - Expected 9. Got {another_guitar.get_age()}')
print(f'Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}')
print(f'Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}')
