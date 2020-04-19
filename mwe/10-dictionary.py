# Creating a simple dictionary
song = {
    'artist' : 'Metallica', # key and value
    'song' : 'Enter Sandman',
    'release' : 1992
}

# Access dictionary's elements
# print(song['song'])
print(song['release'])

# Mix with string
release = song['release']

print(f'I am listening to this nice old {release} song.')
# print(f'Hello {song['release']}.')

# Add new values
song['playlist'] = 'Heavy Metal'
print(song)

# Replace existing value: if exists, replaces
song['song'] = 'Seek & Destroy'
print(song)

# Erase an entry
del song['release']
print(song)