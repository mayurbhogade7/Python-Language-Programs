pet_0 = {'pet name': 'dog', 'owner name': 'jack'}
pet_1 = {'pet name': 'cat', 'owner name': 'kalis'}
pet_2 = {'pet name': 'horse', 'owner name': 'mayur'}

pets = [pet_0, pet_1, pet_2]

count = 1
for pet in pets:
    print(f"\n{count}.")
    count = count + 1
    for p,q in pet.items():
        print(f"{p}: {q}")