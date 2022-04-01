print("Number of items: ", end='')
number_of_items = int(input())
prices = []
for i in range(0, number_of_items):
    print("Price of item: ", end='')
    price = float(input())
    prices.append(price)
total = 0
for price in prices:
    total += price
if total > 100:
    discount = total / 100 * 10
    final_price = (total - discount)
print(f"Total price of 3 items is ${round(final_price,2)}")
