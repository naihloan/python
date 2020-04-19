# Initialize an empty dictionary
player = {}
print(player)

# New game + player
player['name'] = 'Benja'
player['score'] = 0
print(player)

# Increasing points
player['score'] = 5000
print(player)

# Increasing points
player['score'] = 5200
print(player)

# Access a value
# print(player.get('name'))
print(player.get('automata', 'No information'))

# Iterate through dictionary
for key, value in player.items():
    # print(key)
    print(value)

# Eliminate player and score after game
del player['name']
del player['score']
print(player)