fav_pizzas = ['paneer pizza', 'chicken pizza', 'pepperoni pizza', 'veg pizza']
for pizza in fav_pizzas:
    print(pizza)
    print(f"I like {pizza}.")
print("I really love pizza!")

friend_pizzas = fav_pizzas[:]

fav_pizzas.append('cheese pizza')
friend_pizzas.append('non-veg pizza')

print("My favorite pizzas are:")
for pizza in fav_pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)