import collections
# Cipher
# Takes a list of words and finds all cipher complete sets
def cipher(words):
  # List of cipher complete sets

  cipher_complete = collections.defaultdict(lambda: [])
  for word in words:
    cipher_complete[get_duplicates(word)].append(word)

  print '-' * 10
  for key in cipher_complete:
    print cipher_complete[key]

# Finds duplicate letters and positions, returns array of tuples containing the positions of duplicate
# letters.
def get_duplicates(word):
  positions = collections.defaultdict(lambda: [])

  for i in range(len(word)):
    positions[word[i]].append(i)

  duplicates = []
  for key in positions:
    duplicates.append(tuple(positions[key]))

  if len(duplicates) > 1:
    duplicates.sort()
  return tuple(duplicates)


cipher(['python', 'java', 'ruby', 'lisp', 'dayo', 'lava', 'laaa', 'sixlet', 'javascript'])
cipher(['aa', 'abc', 'bbde', 'abace', 'asdfds', 'abdedb'])
cipher(['aacc', 'bbdd', 'ecce', 'dd', 'ee'])
