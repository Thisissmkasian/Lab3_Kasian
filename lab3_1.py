"""
Надрукувати усі двоцифрові числа, сума квадратів цифр яких
ділиться на n націло. Число n - ціле число, яке вводить користувач.

Автор: КАСЬЯН М.А.

"""

n = int(input("Введіть значення n: "))
for i in range(10, 100):
   if not (i**2 % 10 + i**2 // 10 % 10 + i**2 // 100 % 10 + i**2 // 1000) % n:
       print(i, end=' ')