# Conjuntos utilizam as chaves {};
# Conjuntos não possuem elementos repetidos, se ocorrer eles tornam-se o mesmo;
# Conjuntos, Listas e Tuplas não podem ser elementos de  Conjuntos;
A = {1, 1+2, 3, 'A'}
print(A)

# A função len retorna o número de elementos do Conjunto A;
print(len(A))

# A função sum retorna a soma dos elementos do Conjunto B; 
B = {1, 2, 3, 5}
print(sum(B))
# Colocando um número junto de B, a soma comça a partir desse número;
print(sum(B, 100))

# As "perguntas" in e not in servem para verificar a presença de um elemento em um conjunto;
print(1 in B)
print(789 in B)
print(2.5 not in A)

# União de Conjuntos: | e Intersecção de Conjuntos: &;
C = {1, 2, 3, 4, 'PÃO'}
D = {'CAVALO', 89, 2, 3, 100}
print(C | D)
print(C & D)

# A.add(x) adiciona um elemento x;
# A.remove(x) remove um elemento x;
print(C)
C.add('ROSA')
C.remove(3)
print(C)

# "update" atualiza o conjunto adicionando uma série de elementos
E = {1, 2, 3}
print(E)
E.update({78, 79, 80})
print(E)

# Outra forma de descrever conjuntos usando for e condições com o if;
F = {x + 4 for x in {1, 2, 3}}
print(F)

G = {x - 100 for x in {1002, 432, 890, 34} if x > 100 and x < 1002}
print(G)

H = {x + y for x in {0, 2, 4, 8} for y in {-1, -2, -3, -4, -5} if y >-2}
print(H)
