current_users = ['mayur', 'john', 'alex', 'jack', 'ketan']
new_users = ['John', 'amit', 'bhushan', 'alex', 'kalis']

for user in new_users:
    if user.lower() in current_users:
        print(f"username: {user} is already taken. Please enter new one.")
    else:
        print(f"username: {user} is available.")
