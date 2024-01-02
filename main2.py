
# list = [1,1,2,-2,5,2,4,4,-1,-2]
# for x in list:
#     if list.count(x) == 1:
#         print(x)

#


list = [1,1,2,-2,5,2,4,4,-1,-2,5]

def find_odd_occurrence(lst):
    i = 0
    while i < len(lst):
        count = 0
        j = 0
        while j < len(lst):
            if lst[i] == lst[j]:
                count += 1
            j += 1

        if count % 2 != 0:
            return lst[i]
        i += 1
print(find_odd_occurrence(list))


