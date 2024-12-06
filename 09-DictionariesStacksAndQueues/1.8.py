price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

counter = 0

for item,price in price_list.items():
    print(f"{item}: {price}")
    counter += price
print(f"Total price: {round(counter,2)}\n")

upd_price_lst = {
    'T-shirt': 19.99*0.9,
   'Jeans': 49.99*0.9,
   'Jacket': 89.99*0.9,
   'Sneakers': 59.99*0.9,
   'Hat': 15.99*0.9
}

counter_1 = 0
for item,price in upd_price_lst.items():
    print(f"{item}: {price}")
    counter_1 += price
print(f"Total price after 10% discount: {round(counter_1,2)}")