n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))
m = (n1 + n2)/2
print('A média da sua nota foi {:.1f}'.format(m))
if m >= 6.0: 
    print('Sua média foi ótima')
else: 
    print('Precisa melhorar mais')
# print ('Parabéns' if m >=6 else 'Melhore')