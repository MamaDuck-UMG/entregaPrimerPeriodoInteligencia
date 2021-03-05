'''
5/03/2021
Integrantes:
Todos los integrantes de 8vo semestre de cibernética uwu
'''

from queue import PriorityQueue  # libreria colas de prioridad
import math  # Para los infinitos
import random #para los valores aleatorios generados
import time #para hacer pruebas con sleep
import networkx as nx #oof, necesito imprimir grafos bonitos
import matplotlib.pyplot as plt #parte de dependencias de networkx
seed = 132334534 #semilla para hacer el display del grafo
contador = 0 #utilizado para contar el numero de nodos adyacentes en la funcion de printNeighbours
valormax=0
def algoritmoRecorrido(n1):  # recibe una cadena de valores
    n0 = n1  # lo cofiguro como un nodo tipo puzzle
    Q = PriorityQueue()  # Q es una cola de prioridad
    aux = 0  # otro indice secundario de prioridad para Q
    Q.put((n0.f, aux, n0))  # la cola de prioridad se manejará mediante los f(n)
    visitados = [] #arreglo que almacena el indice de los nodos visitados
    visitadosAlex = []  #arreglo que almacena los nodos visitados
    while not Q.empty():  # mientras la cola no este vacía
        u = Q.get()  # con el metodo get se guarda en u pero se quita de la cola el elemento
        u = u[2]  # porque una cola de prioridad almacena tuplas de prioridad,contador,nodo
        if u.tag not in visitados:  #si no está en visitados, lo agregamos para no volver a mostrarlo
            visitados.append(u.tag)  # para evitar volverlo a visitar
            visitadosAlex.append(u)  #guardamos un nodo (el nodo actual) en el arreglo para hacer su posterior análisis
        ady = u.expand(u.ady1)  # expand me genera una lista de adyacencia, con heuristica y señalando a su padre, establece costo de 1 al generar neuvo nodo
        for v in ady:  # explorar los vecinos
            #print("Heuristica de ", v.tag, " :", v.h)
            if v.tag not in visitados:  # forma parte del algoritmo A* por la estimación de heurística
                fp = v.h + v.g  # cálculo de funciones
                if fp < v.f:
                    v.f = fp
                    aux = aux + 1  # debo tener un entero antes de insertar un nodo en prioridad
                    valormax=v.f
                    Q.put((-(v.f), aux,
                           v))  # lo colocamos en la cola, para que en cada ciclo se evite agregar uno repetido
    print(visitados)
    return visitadosAlex    #retorna el arreglo


class Nodo:
    w=None
    h = None  # heuristica
    f = math.inf  # f es infinito

    def __init__(self, tag, conexiones, padre, mamaduck, personasconect, tiempoactivos,ady1):  # inicializador
        self.tag = tag
        self.conexiones = conexiones
        self.padre = padre
        self.mamaduck = mamaduck
        self.tiempoactivos = tiempoactivos
        self.ady1 = ady1
        if padre is not None:  # si es un hijo
            self.g = padre.g + 1
        else:  # si es padre
            self.g = 0
            self.f = 0  # su f debe valer 0
        self.h = personasconect
    def expand(self, ady1):  # nos va a decir como explorar el grafo, obtiene la raiz en primera instancia
        ady = []  # aqui guardaremos los adyacentes que son objetos del tipo nodo
        for i in ady1:
            ady.append(Nodo(i.tag, i.conexiones, self, i.mamaduck, i.h, i.tiempoactivos,i.ady1))
        return ady  # retornamos los adyacentes o hijos del nodo expandido
    # find solution
def imprimirGrafo():
    pos = nx.spring_layout(G, seed=seed)  # Semilla utilizada para hacer el display del grafo
    nx.draw(G, with_labels=True, font_weight='bold')#se dibuja el grafo
    plt.show() #se muestra el grafo

def definirAtributos(nodoGrafo):
    #G.nodes[1]['Mama'] = nodoGrafo[0].mamaduck
    x = 1  # se inicializa el ciclo en 1 porque los nodos van de 1 a n
    while x < numNod + 1:  # navega por cada nodo
        G.nodes[x]['connectedPeople'] = nodoGrafo[x-1].h  # le asigna un numero aleatorio del 0 al 10 de mensajes
        G.nodes[x]['tiempoDeConexion'] = nodoGrafo[x-1].conexiones  # le asigna un numero aleatorio del 0 al 10 de horas conectadas
        G.nodes[x]['Mama'] = nodoGrafo[x-1].mamaduck
        x += 1

def imprimirAtributos():
    #print(G.nodes.data()) #para saber datos de mama y de emergencyMessages
    while i < numNod:
        print(G.nodes[i]["connectedPeople"])

def addEdge(nodoGrafo):
    G.add_edge(nodoGrafo[0].tag, nodoGrafo[1].tag)
    G.add_edge(nodoGrafo[0].tag, nodoGrafo[2].tag)
    G.add_edge(nodoGrafo[0].tag, nodoGrafo[3].tag)
    G.add_edge(nodoGrafo[1].tag, nodoGrafo[3].tag)
    G.add_edge(nodoGrafo[1].tag, nodoGrafo[4].tag)
    G.add_edge(nodoGrafo[3].tag, nodoGrafo[2].tag)
    G.add_edge(nodoGrafo[2].tag, nodoGrafo[4].tag)

def printNeighbours(unu):
    contador = 0
    arrayxd = []
    xd = nx.all_neighbors(G, unu)
    for x in xd:
        contador +=1
        arrayxd.append(x)
    return arrayxd

# INT MAIN

G = nx.Graph()  # inicializamos el grafo G
numNod = 5  # numero de nodos del grafo

# AÑADIENDO LOS NODOS AL GRAFO
i = 0  # variable para utiolizar el ciclo while
while i < numNod:  # se añaden los nodos de 1 a n, sabiendo que n es numNod
    G.add_node(int(i + 1))
    i += 1
while True:#se va a estar ejecutando frecuentemente hasta que por consola le indiquemos que se detenga (ctrl+c)

    nodoGrafo = []
    nodoGrafo.append(Nodo(5, None, None, False, random.randrange(1, 20, 1), random.randrange(1, 20, 1), []))
    nodoGrafo.append(Nodo(4, None, None, False, random.randrange(1, 20, 1), random.randrange(1, 20, 1), [nodoGrafo[0]]))
    nodoGrafo.append(Nodo(3, None, None, False, random.randrange(1, 20, 1), random.randrange(1, 20, 1), [nodoGrafo[1]]))
    nodoGrafo.append(Nodo(2, None, None, False, random.randrange(1, 20, 1), random.randrange(1, 20, 1), [nodoGrafo[0],nodoGrafo[1]]))
    nodoGrafo.append(Nodo(1, None, None, True, random.randrange(1, 20, 1), random.randrange(1, 20, 1), [nodoGrafo[3],nodoGrafo[1],nodoGrafo[2]]))
    nodoGrafo.reverse()

    addEdge(nodoGrafo)
    definirAtributos(nodoGrafo)
    imprimirAtributos()
    imprimirGrafo()

    algoritmoRecorrido(nodoGrafo[0])  # iniciamos el algoritmo de A estrella en una variable de objeto
    time.sleep(.2)#cadacierto tiempo irá analizando los nodos


