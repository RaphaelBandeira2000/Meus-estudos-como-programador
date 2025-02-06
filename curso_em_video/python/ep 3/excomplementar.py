elemento1 = int(input('digite o primeiro elemento: '))
elemento2 = int(input('digite o segundo elemento: '))
sub = elemento1 - elemento2
list = []
for i in range(elemento2, elemento1):
    list.append(i)
for num in list:
    sub_num = num +1
mult = sub_num * num
div = mult / 2
print (f"{div:.0f}")