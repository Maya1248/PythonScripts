txt = str(input(">"))
t = ""

for i in range(len(txt)):
    t += txt[i]
    print(t)
for i in range(len(txt)):
    t = t[0:len(txt)-i]
    print(t)
