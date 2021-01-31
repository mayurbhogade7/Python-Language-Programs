person_0 = {'first_name': 'mayur', 'last_name': 'bhogade', 'age': 20, 'city': 'pune'}
person_1= {'first_name': 'ketan', 'last_name': 'puranik', 'age': 20, 'city': 'latur'}
person_2 = {'first_name': 'omkar', 'last_name': 'sonawane', 'age': 21, 'city': 'satara'}

peoples = [person_0, person_1, person_2]
count = 1
for people in peoples:
    print(f"\n{count}.")
    count = count + 1

    for p,q in people.items():
        print(f"{p.title()}: {q}")
