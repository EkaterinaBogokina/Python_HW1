# Задача 2: Найдите сумму цифр трехзначного числа.

a = int (input ("enter 3-digits number "))
sum_1 = 0
while a > 0:
    n = a%10
    sum_1 = sum_1+n
    a = a//10
print(sum_1)


