

list = [1,3,2,4,4,1]
element = int(input("choose number:"))
def qoshish(lst, element):
    i = 0
    while i < len(lst):
        if lst[i] == element:
            lst.append(lst.pop(i))
        return lst


print(qoshish(list,element))


