alien = {'color': 'green', 'points': 5}
print(alien['color'])
print(alien['points'])

print(f"You just earned {alien['points']} points!")

alien['x_position'] = 0
alien['y_position'] = 25
print(alien)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)

del alien_0['points']
print(alien_0)