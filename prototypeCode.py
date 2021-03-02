import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
seed = 13235634 #semilla para hacer el display del grafo


#Documentation
#https://networkx.org/documentation/stable/tutorial.html#nodes
#utilizamos la librería de networkx para inicializar un grafo y modificarlo para después realizarle la búasqueda bidireccional


G = nx.Graph() #inicializamos el grafo G
numNod = 4
#matrixuwu = np.zeros((numNod, numNod))#MATRIZ DE ADYACENCIA

#AÑADIENDO LOS NODOS AL GRAFO
i = 0 #variable para utiolizar el ciclo while
while i < numNod: #se añaden los nodos de 1 a n, sabiendo que n es numNod
    G.add_node(int(i+1))
    i += 1

#DEFINIENDO ATRIBUTOS DE LOS NODOS
G.nodes[1]['Mama'] = True
G.nodes[1]['EmergencyMessages'] = 0
G.nodes[2]['Mama'] = False
G.nodes[2]['EmergencyMessages'] = 5
G.nodes[3]['Mama'] = False
G.nodes[3]['EmergencyMessages'] = 3
G.nodes[4]['Mama'] = False
G.nodes[4]['EmergencyMessages'] = 1



#DEFINIENDO LAS DISTANCIAS ENTRE NODOS A PARTIR DE LAS ARISTAS (EDGES)
G.add_edges_from([(1, 2), (1, 3), (1, 4)])
G[1][2]['distance'] = "15"
G[1][3]['distance'] = "12"
G[1][4]['distance'] = "21"



print("Adiós unu, aquí está tu grafo")

#IMPRIMIR DISTANCIAS
print("distancia de 1 a 2 =", G.edges[1, 2])
print("distancia de 1 a 3 =", G.edges[1, 3])
print("distancia de 1 a 4 =", G.edges[1, 4])

#IMPRIMIR LOS ATRIBUTOS DE LOS NODOS
print(G.nodes.data())

#IMPRIMIENDO GRAFO
pos = nx.spring_layout(G, seed=seed)  # Semilla utilizada para hacer el display del grafo
nx.draw(G, pos=pos) # se dibuja eel grafo
plt.show() #se muestra el grafo



