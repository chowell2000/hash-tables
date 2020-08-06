# Your code here

# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import operator
file = open('robin.txt')

s = file.read()
file.close()
ignored = ['"',".", "," , ':',';','.','-','+','=','/','|','[',']',"{","}"
                ,"(", ")","*",'^','&', "\ ", "\\", '!', "'", '-', '—', '?', '1']

def word_count(s):
    # ignored = ['"',".", "," , ':',';','.','-','+','=','/','|','[',']',"{","}","(", ")","*",'^','&', "\ ", "\\"]
    for i in ignored:
        s = s.replace(i,"")
    words = s.lower().split()
    count = dict()
    for word in words:
        if word in count.keys():
            count[word] += 1
        else:
            count[word] = 1

    # return count


    count = {k: v for k,v in reversed(sorted(count.items(), key=operator.itemgetter(0)))}
    count = {k: v for k,v in reversed(sorted(count.items(), key=operator.itemgetter(1)))}
    for key in count:
        graph = 'X'*count[key]
        print("{:>15} {}".format(key, graph))
    return count


print(word_count(s))