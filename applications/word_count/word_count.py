def word_count(s):
    ignored = ['"',".", "," , ':',';','.','-','+','=','/','|','[',']',"{","}","(", ")","*",'^','&', "\ ", "\\"]
    for i in ignored:
        s = s.replace(i,"")
    words = s.lower().split()
    count = dict()
    for word in words:
        if word in count.keys():
            count[word] += 1
        else:
            count[word] = 1

    return count



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))