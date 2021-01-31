prompt = "\nEnter a toppings you want add on pizza.\nEnter 'quit' to stop: "

while True:
    toppings = input(prompt)
    if toppings.lower() == 'quit':
        break
    print(f"Adding {toppings}")
