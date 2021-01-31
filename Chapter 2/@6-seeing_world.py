locations = ['kashmir', 'keral', 'newyork', 'paris', 'london']
print(f"original list: {locations}")

print(f"\nalphabetical order: {sorted(locations)}")
print(f"\n list: {locations}")
print(f"\nreverse alphabetical order: {sorted(locations, reverse=True)}")
print(f"\noriginal list: {locations}")

locations.reverse()
print(f"\nreverse order: {locations}")

locations.reverse()
print(f"\noriginal order: {locations}")

locations.sort()
print(f"\nalphabetical order: {locations}")

locations.sort(reverse=True)
print(f"\nreverse alphabetical order: {locations}")