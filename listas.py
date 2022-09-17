# Listas usam [] colchetes;
A = [1, 2, 3, 4, 'Porquinho']
print(A)

A = A + [8, 9, 10, 'Cachorrinho']
print(A)

# Caso deseje somar Listas com o comando sum é necessário colocar [] dentro dos parênteses;
B = sum([ [1,2,3], [4,5,6], [7,8,9]], [])
print(B)

# Também é possível escrever listas com o for e condições usando o if;
C = [x*y for x in [1, 2, 3, 4] for y in {-1} if x < 4]
print(C)

C = [x*y for x in [1, 2, 3, 4] for y in {-1, -2} if x < 4]
print(C)

C = [x*y for x in [1, 2, 3, 4, 5] for y in [100, 200] if x <= 4]
print(C)

# Lista de listas:
D = [[x, y] for x in ['A', 'B', 'C'] for y in [1, 2, 3]]
print(D)

# Lista de Conjuntos: 
E = [{x, y, z} for x in [1, 2] for y in {100, 200} for z in ['A', 'B', 'C', 4] if z != 4]
print(E)