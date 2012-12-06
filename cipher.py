# Cipher
# Takes a list of words and finds all cipher complete sets
def cipher(words):
  # List of cipher complete sets
  cipher_complete_sets = []

  remaining_words = set(words)

  while len(remaining_words) > 0:
    word = remaining_words.pop()
    cipher_complete_set = set([word])

    to_delete = set()
    for other in remaining_words:
      if is_cipher_complete(word, other):
        cipher_complete_set.add(other)
        to_delete.add(other)

    remaining_words -= to_delete

    cipher_complete_sets.append(cipher_complete_set)

  print cipher_complete_sets


# Returns true if the 2 words are cipher complete false otherwise
def is_cipher_complete(word1, word2):
  if len(word1) != len(word2):
    return False

  cipher = {}
  for i in range(len(word1)):
    if word1[i] in cipher and cipher[word1[i]] != word2[i]:
      # One key mapping to two different letters, can't be a cipher
      return False
    elif not word1[i] in cipher:
      cipher[word1[i]] =  word2[i]

  if len(cipher.values()) > len(set(cipher.values())):
      # Not unique values, therefore not a one-to-one mapping
      return False

  return True

cipher(['python', 'java', 'ruby', 'lisp', 'dayo', 'lava', 'laaa', 'sixlet', 'javascript'])
cipher(['aa', 'abc', 'bbde', 'abace', 'asdfds'])
cipher(['aa', 'bb', 'cc', 'dd', 'ee'])
