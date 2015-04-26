def get_word(str, sep=" "):
    word = []
    i = 0
    while str[i] != "\n" and str[i] != sep:
        word.append(str[i])
        i = i + 1
    return ''.join(word)

f = open("dictionary.txt")

d = {}

while True:
    s = f.readline()
    if not s: break
    word = get_word(s, ":")
    attrs = []

    a = len(word) + 1
    while a != len(s):
        attr = get_word(s[a:len(s)], " ")
        attrs.append(attr)
        a += len(attr) + 1

    for k in attrs:
       
        if k in d:
            d[k].append(word)
        else:
            d[k] = [word]

attribute = input("Choose attribute:")
if attribute in d:
    print(d[attribute])
else:
    print("No attribute exist!")

f.close()

