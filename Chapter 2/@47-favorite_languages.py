favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        print(f"\t{name.title()}, I see you love {favorite_languages[name].title()}!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())
print("\n\n")
polls = ['ketan', 'mayur', 'jen', 'abhishek', 'sarah']

for poll in polls:
    if poll in favorite_languages.keys():
        print(f"{poll} you have already taken the poll.")
    else:
        print(f"{poll} you are invited to take a poll.")