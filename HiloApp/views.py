from django.shortcuts import render
import time
import threading

# Create your views here.
datos = []

class hilo:
    # metodo aceptar personas ----------Hilo1
    def personass(personas):
        for person in personas:
            mensajeP = 'Hilo No.1  -  Hola querido ' + person + ' Como estas?'
            print(mensajeP)
            datos.append(mensajeP)
            time.sleep(0.5)

    # metodo asignarle un idlista------- Hilo2
    def asiganarleId(personas):
        i = 1
        for person in personas:
            mensajeId = "Hilo No.2  -  Hola! {}, tu id es {}. ".format(person, i)
            print(mensajeId)
            datos.append(mensajeId)
            i += 1
            time.sleep(0.5)

    # metodo asignar Departamento ---------Hilo3
    def asignarDepartamento(personas, departamentos):
        i = 0
        for departamento in departamentos:
            mensajeC = 'Hilo No.3  -  Ciudad para {}, es: {}.'.format(personas[i], departamento)
            print(mensajeC)
            datos.append(mensajeC)
            i += 1
            time.sleep(0.5)


def index(request):
    t = time.time()
    datos.clear()  # limpiamos los dato[]
    lista = ['Haroldo', 'Edy', 'Santiago', 'Melissa', 'Alejandro']
    departamentos = ['Chimaltenango', 'Comalapa', 'Chimaltenago', 'Chimaltenango', 'Comalapa']
    # --------------------Creando Hilos Para las Personas, sus Id's y departamento----------
    t1 = threading.Thread(target=hilo.personass, args=(lista,))
    t2 = threading.Thread(target=hilo.asiganarleId, args=(lista,))
    t3 = threading.Thread(target=hilo.asignarDepartamento, args=(lista, departamentos))
    # --------------------Iniciamos Los Hilos-----------------------------------------------
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    tiempo = str(time.time() - t)
    print("El tiempo tardado " + str(time.time() - t))
    return render(request, "index.html", {'persona': datos, 'tiemp': tiempo})
