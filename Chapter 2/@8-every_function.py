lang = ['c', 'c++', 'python', 'java', 'curl', 'sql']
print(lang[2])
lang[4] = 'php'
print(lang)

lang.append('curl')
print(lang)

lang.insert(3,'html')
print(lang)

print(f"length: {len(lang)}")

del lang[len(lang)-1]
print(lang)

popped = lang.pop()
print(f"recently popped {popped}")

popped = lang.pop(3)
print(f"I am {popped}")

lang.remove('c')
print(lang)

lang.sort()
print(f"sorted list: {lang}")

lang.sort(reverse=True)
print(f"reverse sorted order: {lang}")

print(sorted(lang))
print(sorted(lang, reverse=True))

lang.reverse()
print(lang)