import sys

#word = sys.stdin.next().strip()[::-1]
word = 'djjcddjggbiigjhfghehhbgdigjicafgjcehhfgifadihiajgciagicdahcbajjbhifjiaajigdgdfhdiijjgaiejgegbbiigida'[::-1]

# adigiibbgegjeiagjjiidhfdgdgijaaijfihbjjabchadcigaicgjaihidafigfhhecjgfacijgidgbhhehgfhjgiibggjddcjjd
# a             a              aa        abc   cig icgj ihid fi    e j f  ijgidgbhhehgfhjgiibggjdd jjd
# This is the sorted letter set of A.
# Subsequently this is also the lexicographically smallest permutation,
# but may not be possible given the word.
letters = sorted(word)[::2]
print word[::-1]
letters_dict = dict()
word_dict = dict()

for letter in letters:
    letters_dict[letter] = letters_dict.get(letter, 0) + 1

for w in word:
    word_dict[w] = word_dict.get(w, 0) + 1

result = ''
result_dict = dict()

seen_dict = dict()
for i in range(0, len(word)):
    if len(letters) == 0:
        break

    if word[i] == letters[0]:
        result += word[i]
        result_dict[word[i]] = result_dict.get(word[i], 0) + 1
        letters_dict[word[i]] = letters_dict.get(word[i]) - 1
        letters.remove(word[i])
    elif letters_dict[word[i]] > 0 and letters_dict[word[i]] == seen_dict.get(word[i], 0):
        result += word[i]
        result_dict[word[i]] = result_dict.get(word[i], 0) + 1
        letters_dict[word[i]] = letters_dict.get(word[i]) - 1
        letters.remove(word[i])
    else:
        seen_dict[word[i]] = seen_dict.get(word[i], 0) + 1

    word_dict[word[i]] = word_dict.get(word[i], 0) - 1

print result

