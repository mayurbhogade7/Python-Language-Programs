requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
if 'pepperoni' in requested_topping:
    print("Adding pipperoni.")
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for toppings in requested_toppings:
    if toppings.lower() == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {toppings}.")

print("\nfinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for toppings in requested_toppings:
        print(f"Adding {toppings}.")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for toppings in requested_toppings:
    if toppings in available_toppings:
        print(f"Adding {toppings}.")
    else:
        print(f"Sorry, we don't have {toppings}.")

print("\nFinished making your pizza!")