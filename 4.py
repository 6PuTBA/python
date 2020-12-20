digit = int(input("Введите целое положительное число:"))
max_dig = 0
while digit // 10 > 0:
    if max_dig < digit % 10:
        max_dig = digit % 10
    digit //= 10
print(max_dig)
