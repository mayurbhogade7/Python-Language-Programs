sandwich_orders = ['sandwich 0', 'sandwich 1', 'sandwich 2', 'sandwich 3', 'sandwich 4']
finished_orders = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order}")
    finished_orders.append(order)

print("List of sandwiches: ")
for order in finished_orders:
    print(order)