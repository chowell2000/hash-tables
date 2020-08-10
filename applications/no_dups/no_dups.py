def no_dups(s):
    words = s.split()
    dupeless = dict()
    for word in words:
        if word not in dupeless.keys():
            dupeless[word] = word
    strings = [i for i in dupeless.keys()]
    return ' '.join(strings)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))