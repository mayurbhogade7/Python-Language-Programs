guest_list = ['Pratik', 'Shubham', 'Pranit']
message = "you are invited for a dinner by Mayur."
print(f"Number of people invited for a dinner {len(guest_list)}")
print(f"{guest_list[0]} {message}")
print(f"{guest_list[1]} {message}")
print(f"{guest_list[2]} {message}")

print(f"{guest_list[1]} can't make the dinner.")
guest_list[1] = 'ketan'
print(f"\nNumber of people invited for a dinner {len(guest_list)}")
print(f"{guest_list[0]} {message}")
print(f"{guest_list[1]} {message}")
print(f"{guest_list[2]} {message}")

print("I have found a bigger dinner table.")
guest_list.insert(0,'abhishek')
guest_list.insert(3, 'bhushan')
guest_list.append('omkar')

print(f"\nNumber of people invited for a dinner {len(guest_list)}")
print(f"{guest_list[0]} {message}")
print(f"{guest_list[1]} {message}")
print(f"{guest_list[2]} {message}")
print(f"{guest_list[3]} {message}")
print(f"{guest_list[4]} {message}")
print(f"{guest_list[5]} {message}")

print("Sorry friends, I can invite only two people for dinner.")
popped = guest_list.pop()
print(f"{popped} sorry I can't invite you for dinner.")
popped = guest_list.pop()
print(f"{popped} sorry I can't invite you for dinner.")
popped = guest_list.pop()
print(f"{popped} sorry I can't invite you for dinner.")
popped = guest_list.pop()
print(f"{popped} sorry I can't invite you for dinner.")

print(f"\nNumber of people invited for a dinner {len(guest_list)}")
print(f"{guest_list[0]} {message}")
print(f"{guest_list[1]} {message}")

del guest_list[1]
del guest_list[0]
print(guest_list)