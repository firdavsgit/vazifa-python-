first = int(input("1-day KM"))
y = int(input("all KM"))

def find_day(first,y):
    num = (first*10)//100
    for x in range(first,y+1):
        x = x + num
        return x


print(find_day(first,y))








