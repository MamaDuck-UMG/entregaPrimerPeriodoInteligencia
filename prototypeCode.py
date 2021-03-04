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
numNod = 10 #numero de nodos del grafo
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

def definirPersonasConectadas():   #funcion para dar numeros aleatorios de mensajes de emergencia a los nodos
    x = 1   #se inicializa el ciclo en 1 porque los nodos van de 1 a n
    while x < numNod + 1:  #navega por cada nodo
        G.nodes[x]['connectedPeople'] = random.randint(0, 10) #le asigna un numero aleatorio del 0 al 10 de mensajes
        x += 1

#DEFINIENDO LAS DISTANCIAS ENTRE NODOS A PARTIR DE LAS ARISTAS (EDGES)

G.add_edges_from([(1, 2),
                  (1, 3),
                  (1, 4),
                  (1, 5),
                  (1, 6),
                  (2, 5),
                  (6, 8),
                  (6, 7),
                  (5, 7),
                  (9, 6),
                  (9, 10),
                  (10, 2),
                  (3, 4)])

def intensidadDeSegnal():

    G[1][2]['signalIntensity'] = random.randint(-90, -30)
    G[1][3]['signalIntensity'] = random.randint(-90, -30)
    G[1][4]['signalIntensity'] = random.randint(-90, -30)
    G[1][5]['signalIntensity'] = random.randint(-90, -30)
    G[1][6]['signalIntensity'] = random.randint(-90, -30)
    G[2][5]['signalIntensity'] = random.randint(-90, -30)
    G[6][8]['signalIntensity'] = random.randint(-90, -30)
    G[6][7]['signalIntensity'] = random.randint(-90, -30)
    G[5][7]['signalIntensity'] = random.randint(-90, -30)
    G[9][6]['signalIntensity'] = random.randint(-90, -30)
    G[9][10]['signalIntensity'] = random.randint(-90, -30)
    G[10][2]['signalIntensity'] = random.randint(-90, -30)
    G[3][4]['signalIntensity'] = random.randint(-90, -30)

#IMPRIMIR DISTANCIAS
def imprimirIntensidadDeSegnal():
    print("intensidad de señal de 1 a 2 =", G.edges[1, 2])
    print("intensidad de señal de 1 a 3 =", G.edges[1, 3])
    print("intensidad de señal de 1 a 4 =", G.edges[1, 4])
    print("intensidad de señal de 1 a 5 =", G.edges[1, 5])
    print("intensidad de señal de 1 a 6 =", G.edges[1, 6])
    print("intensidad de señal de 2 a 5 =", G.edges[2, 5])
    print("intensidad de señal de 6 a 8 =", G.edges[6, 8])
    print("intensidad de señal de 6 a 7 =", G.edges[6, 7])
    print("intensidad de señal de 5 a 7 =", G.edges[5, 7])
    print("intensidad de señal de 9 a 6 =", G.edges[9, 6])
    print("intensidad de señal de 9 a 10 =", G.edges[9, 10])
    print("intensidad de señal de 10 a 2 =", G.edges[10, 2])
    print("intensidad de señal de 3 a 4 =", G.edges[3, 4])

#IMPRIMIR LOS ATRIBUTOS DE LOS NODOS
def imprimirAtributos():
    print(G.nodes.data()) #para saber datos de mama y de emergencyMessages


#IMPRIMIENDO GRAFO
def imprimirGrafo():
    pos = nx.spring_layout(G, seed=seed)  # Semilla utilizada para hacer el display del grafo
    nx.draw(G, with_labels=True, font_weight='bold')#se dibuja el grafo
    plt.show() #se muestra el grafo
    #time.sleep(.2)
    #os.close(plt)



def demon():
    #while 1:
        mamaTrue()
        definirPersonasConectadas()
        intensidadDeSegnal()
        imprimirIntensidadDeSegnal()
        imprimirAtributos()
        imprimirGrafo()




demon()




imprimirGrafo()


#añadir funcion para reconocer los nodos con más mensajes y mandar alerta al usuario
#