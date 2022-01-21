
# O(N**2)

def list_minim_1(lst):
    for i in lst:
        minim = True
        for x in lst:
            if i > x:
                minim = False
        if minim:
            return i


# O(N)

def list_minim_2(lst):
    minim_val = lst[0]
    for i in lst:
        if i < minim_val:
            minim_val = i
    return minim_val

lst1 = [randint(0, 100) for i in range(20)]
print(lst1)
print(list_minim_1(lst1))
print(list_minim_2(lst1))