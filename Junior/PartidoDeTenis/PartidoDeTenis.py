"""
Un hombre endeudado ha decidido invertir todo el dinero que le queda en una ultima apuesta: 
Una partida de tennis a 3 sets entre dos tenistas de alto renombre, el único problema es que 
no conoce muy bien las reglas del deporte y no podría identificar quien ha ganado el partido. 
Para esto necesita un programa que dados los jugadores denotados como 1 y 2, y dada una secuencia 
que muestra que punto ha ganado cada jugador (e.j 1,2,1,1,2,2,1,1). Diga si le es dada una lista de 
sets (secuencias) quien ha ganado el partido.
------------------------------------------------------------------------------------------------------
Input: n = list()
[[1,2,2,1,2,2],[1,1,2,2,1,2,1,2,2],[1,1,1,1]]
------------------------------------------------------------------------------------------------------
Output: o = int
1
"""

def resultado(n):
    return n[-1][-1]

print(resultado([[1,2,2,1,2,2],[1,1,2,2,1,2,1,2,2],[1,1,1,1]]))