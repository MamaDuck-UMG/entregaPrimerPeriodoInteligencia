# Primer Periodo Inteligencia Artificial

## Objetivos

- Implementar una algoritmo para nuestro sistema que facilite el analisis de nuestra red Mama Duck
- Aplicar los conceptos y algoritmos vistos en la materia de manera practica

## Funcionamiento

Nuestro algoritmo utiliza una variante de **A-star** también conocido como A*. Nuestra versión no busca ningún nodo en específico pero nos permite recorrerlo para poder analizar la información de este.
Por cada nodo visitado, realizamos algunos análisis y cálculos con sus nodos vecinos para crear alertas útiles para los administradores del sistema. 

## Modulos

Nuestro proyecto utiliza los siguientes modulos:

- PriorityQueue
- math
- random
- time
- networkx
- matplotlib