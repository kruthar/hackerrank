import sys

#word = sys.stdin.next().strip()[::-1]
word = 'sbcnzxqnrygkocahxjebvueaawwcythjdrhvizqsshgtwdolmillxpshxpxqrywkivceufclhydhshrklkphajbftuapiocjlcthfirhgaohfysqjolssbzhbovdstbyqdpnjbpfmgqrzfctcwcrztvgbegunarvecseoulabaonguckqbtrvuagreyclyjytpvozqdnhldlnsocenuzksawirgsbjobpldjdlrxbricrauuksbmecvvwagnnacaqghmjpzrlsvlpbbcuaddgvlhvuvkxexjcfhxrodmcwlrzyyiksuksshhonahsyzbbprwuitmoyoqurtqsaslevgvpfbzkkhgcnpjdpseuiylluvdetsqssbrxpiclxxvosuqipsqvvwsezhl'[::-1]

letters = sorted(word)[::2]
letters_dict = dict()
word_dict = dict()

for letter in letters:
    letters_dict[letter] = letters_dict.get(letter, 0) + 1

for w in word:
    word_dict[w] = word_dict.get(w, 0) + 1

result = ''

last_accepted = 0
for i in range(0, len(word)):
    if len(letters) == 0:
        break

    if word[i] == 'd':
        pass
    if word[i] == letters[0]:
        result += word[i]
        letters_dict[word[i]] = letters_dict.get(word[i]) - 1
        letters.remove(word[i])
        last_accepted = i
    elif letters_dict[word[i]] > 0 and letters_dict[word[i]] >= word_dict.get(word[i], 0):
        temp_result = ''
        temp_dict = dict()
        max_letter = word[i]#chr(ord(word[i]) - 1)
        role_back = i

        while role_back > last_accepted:
            if word[role_back] <= max_letter and letters_dict[word[role_back]] - temp_dict.get(word[role_back], 0) > 0:
                temp_result = word[role_back] + temp_result
                temp_dict[word[role_back]] = temp_dict.get(word[role_back], 0) + 1
                max_letter = word[role_back]
            role_back -= 1

        if len(temp_result) == 1 or temp_result < word[i]:
            for let in temp_result:
                letters_dict[let] = letters_dict.get(let) - 1
                letters.remove(let)
            result += temp_result
            last_accepted = i

    word_dict[word[i]] = word_dict.get(word[i], 0) - 1

print result
