a = [(1, 'f'), (2, 's'), (3, 's'), (1, 's'), (2, 'f'), (1, 'f'), (3, 'f')]
temp = {}
# for i in a:


for cnt, st in enumerate(a):
    temp.setdefault(st[0], '')
    if st[1] == 's':
        temp[st[0]] = str(str(cnt) + str(st[0]))
        # print('---->', str(st[0]) + st[1])
        a[cnt] = (st[0], st[1], temp[st[0]])
    else:
        a[cnt] = (st[0], st[1], temp[st[0]])
        temp[st[0]] = ''
# print(temp)
for y in a:
    print(y)
