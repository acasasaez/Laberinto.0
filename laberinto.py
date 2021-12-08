#representación del laberinto 
laberinto = [
            ["A", "X","X","X","X"],
            ["A","X","A","A", "A"],
            ["A", "X","A","X","A"],
            ["A","A","A", "X","A"],
            ["X","X","X","X","S"]
            ]

muro = ((0,1),(0,2),(0,3),(0,4),(1,1),(2,1),(2,3),(3,3),(4,0), (4,1),(4,2),(4,3))

L1 = laberinto[:1]
L2 = laberinto[1:2]
L3 = laberinto[2:3]
L4 = laberinto[3:4]
L5= laberinto[4:]
def lab():
    for X in laberinto:
        print("ABAJO")
    for A in laberinto:
        print("ARRIBA")
L1 = lab(L1)
L2 = lab(L2)
L3 = lab (L3)
L4 = lab(L4)
L5 = lab (L5)
print (L1,L2,L3,L4,L5)