''' THIS WORKS
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

'''


import csv


def id_for(text_file_name):
    with open(text_file_name) as f:
        a = csv.reader(f, delimiter=',')
        temp_val = {}
        for cnt, stuff in enumerate(a):
            if cnt > 1:
                temp_val.setdefault(stuff[1], '')
                temp_val[stuff[1]] = str(stuff[4])
        print(temp_val)

    #
    # for stuff in a:
    #     print(stuff)
    # if stuff[0][1] != '':
    #     temp_val.setdefault(stuff[1], [])
    # else:
    #     break

    # print(a[0])


id_for('123.txt')
