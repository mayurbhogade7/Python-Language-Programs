flag = True
places = {}

while flag:
    name = input("Enter your name: ")
    place = input ("Where would you go? ")
    places[name] = place

    repeat = input("Is there any one else for polling (yes/ no) ? ")
    if repeat == 'no':
        flag = False

for name, place in places.items():
    print(f"\n{name} would like to go {place}.")