


# O(N)
def poisk_1(company):
    in_max = {}
    list_q = dict(company)
    for i in range(3):
        maximum = max(list_q.items(), key=lambda spisok: spisok[1])
        del list_q[maximum[0]]
        in_max[maximum[0]] = maximum[1]
    print(in_max)

# O(N*logonN)
def poisk_2(company):
    list_dict = list(company.items())
    list_dict.sort(key=lambda i: i[1], reverse=True)
    for i in range(3):
        print(f"{list_dict[i][0]}: {list_dict[i][1]}")

poisk_1(company)
poisk_2(company)

# оптимальное решение будет в первом варианте, + в скорости