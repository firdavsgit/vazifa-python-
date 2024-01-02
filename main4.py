
number = int(input("son:"))
x =1
while x <= number:
    num = 2**x
    if number >= num:
        print(x, num)
    x += 1