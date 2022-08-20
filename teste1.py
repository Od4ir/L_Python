x = 603
y = 2

print('x é divisível por y: ', x % y == 0)
print('x é divisível por (y + 1):', x % (y + 1) == 0)

z = int(input('Digite um valor inteiro: '))
if z > 0:
    print('Era positivo: ', z)
else:
    print('Era negativo: ', -z)
