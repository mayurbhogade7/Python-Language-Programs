while True:
    age = input("\nEnter your age. OR \nEnter 'quit' to get out of loop.")
    if str(age) == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif age < 13:
            print("Your ticket price is $10.")
        else:
            print("Your ticket price is $15.")
