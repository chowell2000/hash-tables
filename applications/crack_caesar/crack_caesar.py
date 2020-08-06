# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import os
file = open('ciphertext.txt')

ciphertext = file.read()
file.close()
ignored = ['"',".", "," , ':',';','.','-','+','=','/','|','[',']',"{","}"
                ,"(", ")","*",'^','&', "\ ", "\\", '!', "'", '-', '—', '?', '1']

def letter_count(s):
    for i in ignored:
        s = s.replace(i,"")
    words = s.split()
    count = dict()
    for word in words:
        for i in word:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1

    count = {k: v for k,v in reversed(sorted(count.items(), key=lambda item: item[1]))}
    return count

def decipher(s):
    count = letter_count(s)
    frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    # for x in range(26):
    #     count.values()[x] = frequency[x]
    plainkey = dict(zip(list(count.keys()), frequency))
    print(plainkey)
    # for key in plainkey:
    #     s = s.replace(key, plainkey[key])
    coded = list(s)
    ignored_space = ignored + [" ", '\n']
    # print(ignored_space)
    # print(coded)

    for i in range(len(coded)):

        if coded[i] in ignored_space:
            pass
        else:
            coded[i] = plainkey[coded[i]]
    decoded = "".join(coded)
    return decoded

# txtt = 'The quick brown fox jumped over the lazy turtle'

# print(letter_count(ciphertext))
# print(len(letter_count(ciphertext)))

print(decipher(ciphertext))