# info,job1,20200217,02:01:11,f
'''
PRE-PROCESSING PART
'''

def id_for(text_file_name):
    import csv
    with open(text_file_name) as f:
        a = csv.reader(f, delimiter=',')

        temp_val = []
        for cnt, stuff in enumerate(a):
            temp_val.append(stuff)
    return temp_val


def lets_do_it(pass_the_array):
    temp = {}
    for cnt, st in enumerate(pass_the_array):
        # print(temp)
        if cnt >= 1:
            temp.setdefault(st[1], f'God{cnt}')
            if st[4] == 's':
                # print(567890)
                temp[st[1]] = str(str(cnt) + str(st[1]))
                # print('---->', str(st[0]) + st[1])
                pass_the_array[cnt] = [st[0], st[1], st[2], st[3], st[4], temp[st[1]]]
            else:
                pass_the_array[cnt] = [st[0], st[1], st[2], st[3], st[4], temp[st[1]]]
                temp[st[1]] = ''
    return pass_the_array[1:]


def csv_writer_master(pass_to_write):
    import csv

    with open('modified.csv', mode='w', newline='') as csv_file:
        fieldnames = ['what', 'script_name', 'Date', 'Time', 'status', 'id']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for stud in pass_to_write:
            print(stud[4], '---->')
            writer.writerow({'what': stud[0],
                             'script_name': stud[1],
                             'Date': stud[2],
                             "Time": stud[3],
                             "status": stud[4],
                             "id": stud[5]})


csv_writer_master(lets_do_it(id_for('456.txt')))

for i in lets_do_it(id_for('456.txt')):
    print(i)
