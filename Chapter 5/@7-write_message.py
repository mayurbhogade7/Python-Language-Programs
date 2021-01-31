filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    message = "I love creating new games.\n"
    file_object.write(message)