import networkx as nx
import matplotlib.pyplot as plt
import random
import os
import time
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
def mamaTrue(): #definimos al nodo mamá y a los demás nodos con su respectivo atributo
    G.nodes[1]['Mama'] = True
    x = 2
    while x < numNod + 1:  #navega por cada nodo
        G.nodes[x]['Mama'] = False
        x += 1

def messages():   #funcion para dar numeros aleatorios de mensajes de emergencia a los nodos
    x = 1   #se inicializa el ciclo en 1 porque los nodos van de 1 a n
    while x < numNod + 1:  #navega por cada nodo
        G.nodes[x]['EmergencyMessages'] = random.randint(0, 10) #le asigna un numero aleatorio del 0 al 10 de mensajes
        x += 1

#DEFINIENDO LAS DISTANCIAS ENTRE NODOS A PARTIR DE LAS ARISTAS (EDGES)

def definirDistancias():
    G.add_edges_from([(1, 2), (1, 3), (1, 4)])
    G[1][2]['distance'] = random.randint(0, 10)
    G[1][3]['distance'] = random.randint(0, 10)
    G[1][4]['distance'] = random.randint(0, 10)



#IMPRIMIR DISTANCIAS
def imprimirDistancias():
    print("distancia de 1 a 2 =", G.edges[1, 2])
    print("distancia de 1 a 3 =", G.edges[1, 3])
    print("distancia de 1 a 4 =", G.edges[1, 4])

#IMPRIMIR LOS ATRIBUTOS DE LOS NODOS
def imprimirAtributos():
    print(G.nodes.data()) #para saber datos de mama y de emergencyMessages


#IMPRIMIENDO GRAFO
def imprimirGrafo():
    pos = nx.spring_layout(G, seed=seed)  # Semilla utilizada para hacer el display del grafo
    nx.draw(G, with_labels=True, font_weight='bold')#se dibuja el grafo
    plt.show() #se muestra el grafo
    time.sleep(2)
    #os.close(plt)

def demon():
    while 1:
        mamaTrue()
        messages()
        definirDistancias()
        imprimirDistancias()
        imprimirAtributos()
        imprimirGrafo()


demon()







#añadir funcion para reconocer los nodos con más mensajes y mandar alerta al usuario
#