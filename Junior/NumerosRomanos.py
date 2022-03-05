"""
Ejercicio 1 :
Un historiador con mucho tiempo de sobra quiere escribir como los antiguos romanos, 
para esto ha dedicado incalculables horas de su tiempo a aprender su idioma y sus costumbres, 
pero no ha logrado aprender su sistema numérico, frustrado y aburrido decide buscar a un programador 
que pueda dado una entrada en números arábigos (1 ,2 ,3 ,… ) retornarle una salida en su equivalente 
en romano (I ,II ,III ,… ).
RECUERDA:
1:"I",
5:"V",
10:"X",
50:"L",
100:"C",
500:"D",
1000:"M"
------------------------------------------------------------------------------------------------------
Input: n = int
1
2
3
4
------------------------------------------------------------------------------------------------------
Output: o = String
I
II
III
IV
"""

import random

def traductor(n):
    lista = {"M": 1000,            
            "CM": 900,            
            "D": 500,            
            "CD": 400,            
            "C": 100,            
            "XC":90,       
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
            }
    if(lista.get(n)!=None):
        return lista.get(n)
    else:
        res = ""
        for i in lista:
            while n>= lista.get(i):
                res = res + i
                n = n-lista.get(i)
        return res

x = random.randrange(0,500)
print(x)
print(traductor(x))
