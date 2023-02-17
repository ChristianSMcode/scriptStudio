# DESCRIPCION===============================================================================
# Este decorador pasa la funcion f2 como argumento a la funcion escrita en el decorador (f1)
# y la ejecuta el wrapper que es retornado(wrapper porque envuelve la ejecucion de una funcion).
# Seria lo mismo que hacer:
# f1(f2)()
# O tambien lo mismo que:
# x=f1(f2)
# x()
# En caso de querer usar argumentos la funcion wrapper debe recibir *Args y **kargs (puesto que no se sabe cuantos
# ni cuales van a ser los argumentos de diferentes funciones que usen el decorador)
# Tambien se le debe pasar esos argumentos a la funcion dentro del wrapper.La forma de visualizar esto seria:
# f1(f2)('saludos')
# O lo mismo que:
# x=f1(f2)
# x('despedida')
# Y la funcion wrapper se vería así:
# def f1(f2):
#   def wrapper('despedida'):
#       print('started')
#       f2('despedida')
#       print('ended)
#   return wrapper
import time

def f1(f):
    def wrapper(*args,**kargs):
        print('started')
        result = f(*args,**kargs)
        print('ended')
        return result
    return wrapper

def timer(f):
    def wrapper(*args):
        start_time=time.time()
        result = f(*args)
        print(f'Function took: {time.time() - start_time} seconds to execute')
        return result
    return wrapper

@f1 
def f2(string):
    print(string)
#To return solamente ajustar el wrapper para que retorne el valor de la funcion que ejecuta
#despues de haber completado toda su ejecucion
@f1
def add(x,y):
    return x + y

##############################################################################################
print(add(1,2))
f2('Despedida')
#Ejemplo aplicacion real (medir tiempo ejecucion de una funcion):
@timer
def f3(seconds):
    time.sleep(seconds)

f3(3)
##############################################################################################
#Conclusion: un decorador literalmente es codigo que envuelve/decora otra funcion cualquiera.
