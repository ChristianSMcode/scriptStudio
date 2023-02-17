import time

#Dada una matriz de que representa unos nodos y sus conexiones determine si dos nodos estan conectados o no
#Params:
# matriz,node1,node2

node_graph=[
    [0,1,0,0],
    [1,0,1,1],
    [0,1,0,1],
    [0,1,1,0],
]
node_graphv2=[
    [ 0, 1, 0, 1, 1 ],
    [ 1, 0, 1, 0, 0 ],
    [ 0, 1, 0, 1, 0 ],
    [ 1, 0, 1, 0, 1 ],
    [ 1, 0, 0, 1, 0 ]
]

def timer(f):
    def wrapper(*args):
        start_time=time.time()
        result = f(*args)
        print(f'La funcion {f.__name__} a tardado {(time.time() - start_time):.5f} en ejecutarse.')
        return result
    return wrapper


@timer
def find_adjacent(matriz,node1,node2):
    return matriz[node1][node2]

        

if find_adjacent(node_graphv2,1,4) == 1:
    print('Los nodos son adjacentes')
    exit(0)
print('Los nodos no son adyacentes.')

#Aprendido:
# - :.2 sobre un numero me retorna la cantidad de numeros decimales que especifique
# los boleanos true y false en python son equivalentes a 1 y 0 respectivamente.