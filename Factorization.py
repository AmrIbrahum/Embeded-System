from time import time


def factorization(n):
    factor_list = []
    for i in range(2, n//2 + 1):
        if i % 2 == 0:
            factor_list.append(i)
    return factor_list


start = time()
n = int(input("N: "))
print(factorization(n))

end = time()
print("Elapsed time: {} seconds".format(end - start))
