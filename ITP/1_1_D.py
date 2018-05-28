S = input()
i = int(S)
h = i / 3600
m = (i % 3600) / 60
s = (i % 3600) % 60
print(str(int(h)) + ':' + str(int(m)) + ':' + str(s))
