


list = [10,20,30,40,60]
while True:
    def find_percent(list):
        foiz = int(input("foiz kirit:"))
        i = 0
        while i < len(list):
            answer = (list[i]*foiz)/100
            i += 1
            print(answer)

    find_percent(list)
