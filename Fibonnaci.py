first_num = 0
second_num = 1

for i in range(10):
    if i < 2:
        print(i)
    else:
        sum = first_num + second_num
        print(sum)
        first_num = second_num
        second_num = sum