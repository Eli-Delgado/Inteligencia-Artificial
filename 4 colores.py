#Creo mi grafo con los nodos ya mencionados en el documento. EASTER EGG
grafo = {
    'AGU' : ['JAL', 'ZAC'],
    'BCN' : ['BCS', 'SON'],
    'BCS' : ['BCN'],
    'CAM' : ['ROO', 'TAB', 'YUC'],
    'CHP' : ['OAX', 'TAB', 'VER'],
    'CHH' : ['COA', 'DUR', 'SIN', 'SON'],
    'CMX' : ['MEX', 'MOR'],
    'COA' : ['CHH', 'DUR', 'NLE', 'ZAC'],
    'COL' : ['JAL', 'MIC'],
    'DUR' : ['CHH', 'COA', 'NAY', 'SIN', 'ZAC'],
    'GUA' : ['JAL', 'MIC', 'QUE', 'SLP', 'ZAC'],
    'GRO' : ['MEX', 'MIC', 'MOR', 'OAX', 'PUE'],
    'HID' : ['MEX', 'PUE', 'QUE', 'SLP', 'TLA', 'VER'],
    'JAL' : ['AGU', 'COL', 'GUA', 'MIC', 'NAY', 'ZAC'],
    'MEX' : ['CMX', 'GRO', 'HID', 'MIC', 'MOR', 'PUE', 'QUE', 'TLA'],
    'MIC' : ['COL', 'GUA', 'GRO', 'JAL', 'MEX', 'QUE'],
    'MOR' : ['CMX', 'GRO', 'MEX', 'PUE'],
    'NAY' : ['DUR', 'JAL', 'SIN', 'ZAC'],
    'NLE' : ['COA', 'SLP', 'TAM', 'ZAC'],
    'OAX' : ['CHP', 'GRO', 'PUE', 'VER'],
    'PUE' : ['GRO', 'HID', 'MEX', 'MOR', 'OAX', 'TLA', 'VER'],
    'QUE' : ['GUA', 'HID', 'MEX', 'MIC', 'SLP'],
    'ROO' : ['CAM', 'YUC'],
    'SLP' : ['GUA', 'HID', 'NLE', 'QUE', 'TAM', 'VER', 'ZAC'],
    'SIN' : ['CHH', 'DUR', 'NAY', 'SON'],
    'SON' : ['BCN', 'CHH', 'SIN'],
    'TAB' : ['CAM', 'CHP', 'VER'],
    'TAM' : ['NLE', 'SLP', 'VER'],
    'TLA' : ['HID', 'MEX', 'PUE'],
    'VER' : ['CHP', 'HID', 'OAX', 'PUE', 'SLP', 'TAB', 'TAM'],
    'YUC' : ['CAM', 'ROO'],
    'ZAC' : ['AGU', 'COA', 'DUR', 'GUA', 'JAL', 'NAY', 'NLE', 'SLP']
}
#Creo un diccionario para los colores, incialmente coloco todos con valor de 0
colores = {
    'AGU' : 0,
    'BCN' : 0,
    'BCS' : 0,
    'CAM' : 0,
    'CHP' : 0,
    'CHH' : 0,
    'CMX' : 0,
    'COA' : 0,
    'COL' : 0,
    'DUR' : 0,
    'GUA' : 0,
    'GRO' : 0,
    'HID' : 0,
    'JAL' : 0,
    'MEX' : 0,
    'MIC' : 0,
    'MOR' : 0,
    'NAY' : 0,
    'NLE' : 0,
    'OAX' : 0,
    'PUE' : 0,
    'QUE' : 0,
    'ROO' : 0,
    'SLP' : 0,
    'SIN' : 0,
    'SON' : 0,
    'TAB' : 0,
    'TAM' : 0,
    'TLA' : 0,
    'VER' : 0,
    'YUC' : 0,
    'ZAC' : 0
}


visitado = [] 
cola = []  

#funcion que realiza el algoritmo del BFS
def bfs(visitado, grafo, nodo, colores):
    #Agrego el nodo incial a la lista
    visitado.append(nodo)
    #Agrego el nodo inicial a la cola
    cola.append(nodo)

    #Mientras haya nodos en la cola ejecutamos:
    while cola:
        #Sacamos el primer nodo en la cola
        n = cola.pop(0) 
        #Asignación del color
        colores[n] = asignar_color(n, visitado, grafo, colores)
    
        #Para cada vecino del nodo actual
        for vecino in grafo[n]:
            #Si el vecino no está visitado
            if vecino not in visitado:
                #Agrego vecino a la lista de visitados
                visitado.append(vecino)
                #Agrego vecino a la cola
                cola.append(vecino)

#Función para asignar el color
def asignar_color(n, visitado, grafo, colores):
    colores_no_permitidos = []
    #Busco los colores que ya han sido asignados en los nodos adyacentes
    for nodo in grafo[n]:
        if nodo in visitado:
            #Agrego el color de ese nodo visitado a una lista de colores no permitidos
            colores_no_permitidos.append(colores[nodo])
    for i in range (5):
        #Si uno de los 5 colores no ha sido asignado en los vecinos, lo regreso.
        if (i+1) not in colores_no_permitidos:
         return (i+1)

#Mostramos el mapa
print("\nGrafo del mapa de México: \n")
for llave, lista in grafo.items():
	print(llave, " -> ", lista)

#Asignomos NLE como nodo de inicio
inicio = 'NLE'

#Ejecutamos la funcion bfs para recorrer desde el nodo que pedimos
bfs(visitado, grafo, inicio, colores)
print("\n\n")

#Mostramos lo colores dependiendo del nuemero, 1 = rojo, 2 = amarillo, 3 = verde, 4 = celeste, 5 = morado
print("Colores: \n\n")
for llave in colores:
    print(llave, " : ", end = " ")
    if colores [llave] == 1:
        print("Rojo ")
    elif colores [llave] == 2:
        print("Amarillo ")
    elif colores [llave] == 3:
        print("Verde ")
    elif colores [llave] == 4:
        print("Celeste ")
    elif colores [llave] == 5:
        print("Morado ")



