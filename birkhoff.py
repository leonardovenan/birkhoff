# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:50:28 2019

@author: Leonardo
"""
import matplotlib.pyplot as plt

def n2_2k_1 (x):
    return 2**(2*(x-1))

lista1 = []
lista2 = []
lista23 = [2/3]
lista13 = [1/3]
    
soma = 0

j = 1
k = int(input('Digite o valor de k: '))

#for i in range(onde começa, até onde vai, em qual ondem ele  cresce)

for i in range (j, (k+1)):
    soma = soma + n2_2k_1(i)
    lista1.append((1 + soma)/2**(2*(i)-1))
    lista2.append((1 + soma)/2**(2*i))
    
print("ultimo termo 2k-1: ", lista1[k-1])
print("Ultimo termo 2k: ", lista2[k-1])


fig,ax = plt.subplots()
ax.plot(lista1)
ax.plot(k*lista23, 'r--')
plt.title('2k-1 -> 2/3')

fig2, bx = plt.subplots()
bx.plot(lista2)
bx.plot(k*lista13, 'r--')
plt.title('2k -> 1/3')

plt.show()

#res_n2_2k_1 = (1 + soma)/2**(2*(k)-1)
#res_n2_2k = (1 + soma)/2**(2*k)
#print ("ultimo termo 2k-1: ", res_n2_2k_1)
#print ("Ultimo termo 2k: ", res_n2_2k)