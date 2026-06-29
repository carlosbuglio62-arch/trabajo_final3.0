import csv
import os
dataset=[
    {"pais":"Argentina",
     "poblacion":45000000,
     "superficie":2780400,
     "continente":"America"
    },
    {"pais":"Alemania",
     "poblacion":93000000,
     "superficie":375000,
     "continente":"Europa"
    },
    {"pais":"España",
     "poblacion":47000000,
     "superficie":505000,
     "continente":"Europa"
    },
    {"pais":"Japon",
     "poblacion":125000000,
     "superficie":377500,
     "continente":"Asia"
    }
]

def crear_paises(nombre_archivo,datos):
    campos=["pais","poblacion","superficie","continente"]
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor=csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)

def enlistar_paises(nombre_archivo):
    lista=[]
    with open(nombre_archivo, mode='r', encoding="utf-8") as archivo:
        lector=csv.DictReader(archivo)
        for fila in lector:
            fila["poblacion"]=int(fila["poblacion"])
            fila["superficie"]=int(fila["superficie"])
            lista.append(fila)
    return(lista)

def agregar_pais(lista):
    pais=input("ingrese nuevo pais: ")
    for fila in lista:
        if pais.lower()==fila["pais"].lower():
            print("no se aceptan valores repetidos")
            return
    if pais=="":
        print("no se aceptan valores vacios")
        return
    else:
        try:
            poblacion=int(input("ingrese poblacion: "))
            if poblacion<=0:
                print("poblacion debe ser un entero positivo")
                return
            superficie=int(input("ingrese superficie: "))
            if superficie<=0:
                print("superficie debe ser un entero positivo")
                return
        except ValueError:
            print("ingrese un numero valido")
            return
        continente=input("ingrese continente: ")
        if continente=="":
            print("no se aceptan valores vacios")
            return
        else:
            nuevo_pais={
            "pais":pais,
            "poblacion":poblacion,
            "superficie":superficie,
            "continente":continente}
            lista.append(nuevo_pais)

def buscar_pais(lista):
    pais=input("ingrese pais: ")
    for fila in lista:
        if pais.lower()==fila["pais"].lower():
            print(f"pais: {fila["pais"]}  poblacion: {fila["poblacion"]} hab.")
            print(f"superficie: {fila["superficie"]} km2   continente: {fila["continente"]}")
            return
    print(pais," no se halla")

def modificar_poblacion(lista):
    pais=input("ingrese pais: ")
    for fila in lista:
        if pais.lower()==fila["pais"].lower():
            try:
                nueva_poblacion=int(input("ingrese nueva poblacion: "))
                if nueva_poblacion<=0:
                    print("poblacion debe ser un entero positivo")
                    return
                elif nueva_poblacion=="":
                    print("poblacion debe ser no vacio")
                    return
                else:
                    fila["poblacion"]=nueva_poblacion
                    return
            except ValueError:
                print("ingrese un numero valido")
                return
    print(pais," no se halla")

def modificar_superficie(lista):
    pais=input("ingrese pais: ")
    for fila in lista:
        if pais.lower()==fila["pais"].lower():
            try:
                nueva_superficie=int(input("ingrese nueva superficie: "))
                if nueva_superficie<=0:
                    print("superficie debe ser un entero positivo")
                    return
                elif nueva_superficie=="":
                    print("superficie debe ser no vacio")
                    return
                else:
                    fila["superficie"]=nueva_superficie
                    return
            except ValueError:
                print("ingrese un numero valido")
                return
    print(pais," no se halla")

def filtrar_por_poblacion(lista):
    try:
        limite=int(input("paises que superan los (hab.)"))
        if limite<=0:
            print("el limite debe ser positivo")
            return
    except ValueError:
        print("ingrese un numero valido")
        return
    encontrados=False
    print(f"paises con mas de {limite} habitantes")
    for fila in lista:
        if fila["poblacion"]>limite:
            print(f"pais: {fila["pais"]} poblacion: {fila["poblacion"]} h.")
            print(f"superficie: {fila["superficie"]} km2  continente: {fila["continente"]}")
            encontrados=True
    if not encontrados:
        print("no hay paises que cumplan esa condicion")

def filtrar_por_superficie(lista):
    try:
        limite=int(input("paises que no llegan a (KM2) "))
        if limite<=0:
            print("el limite debe ser positivo")
            return
    except ValueError:
        print("ingrese un numero valido")
        return
    encontrados=False
    print(f"paises con menos de {limite} km2")
    for fila in lista:
        if fila["superficie"]<limite:
            print(f"pais: {fila["pais"]}  poblacion: {fila["poblacion"]} h.")
            print(f"superficie: {fila["superficie"]} km2  continente: {fila["continente"]}")
            encontrados=True
    if not encontrados:
        print("no hay paises que cumplan esa condicion")

def filtrar_por_continente(lista):
    encontrados=False
    continente=input("ingrese continente")
    if continente=="":
        print("continente debe ser no vacio")
        return
    for fila in lista:
        if continente.lower()==fila["continente"].lower():
            print(f"pais: {fila["pais"]}   poblacion: {fila["poblacion"]} h.")
            print(f"superficie: {fila["superficie"]} km2   continente {fila["continente"]}")
            encontrados=True
    if not encontrados:
        print("no hay paises que pertenezcan a ",continente)



def guardar_paises(nombre_archivo,lista):
    campos=["pais","poblacion","superficie","continente"]
    with open(nombre_archivo, mode='w', newline="", encoding="utf-8") as archivo:
        escritor=csv.DictWriter(archivo,fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(lista)

def ordenamientos(lista):
    opcion="8"
    while opcion!="7":
        print("1: ordenados por poblacion (asc)")
        print("2: ordenados por poblacion (desc)")
        print("3: ordenados por superficie (asc)")
        print("4: ordenados por superficie (desc)")
        print("5: ordenados alfabeticamente (asc)")
        print("6: ordenados alfabeticamente (desc)")
        print("7: salir")
        opcion=input("ingrese opcion: ")
        if opcion=="1":
            lista_ordenada=sorted(lista, key=lambda x: x["poblacion"])
            mostrar_paises(lista_ordenada)
        elif opcion=="2":
            lista_ordenada=sorted(lista, key=lambda x: x["poblacion"], reverse=True)
            mostrar_paises(lista_ordenada)
        elif opcion=="3":
            lista_ordenada=sorted(lista, key=lambda x: x["superficie"])
            mostrar_paises(lista_ordenada)
        elif opcion=="4":
            lista_ordenada=sorted(lista, key=lambda x: x["superficie"], reverse=True)
            mostrar_paises(lista_ordenada)
        elif opcion=="5":
            lista_ordenada=sorted(lista, key=lambda x: x["pais"].lower())
            mostrar_paises(lista_ordenada)
        elif opcion=="6":
            lista_ordenada=sorted(lista, key=lambda x: x["pais"].lower(), reverse=True)
            mostrar_paises(lista_ordenada)

def estadisticas(lista):
    min_pob=1000000000
    max_pob=0
    pob=0
    sup=0
    contador=0
    america=0
    asia=0
    africa=0
    europa=0
    oceania=0
    for fila in lista:
        if fila["continente"].lower()=="america":
            america+=1
        elif fila["continente"].lower()=="asia":
            asia+=1
        elif fila["continente"].lower()=="africa":
            africa+=1
        elif fila["continente"].lower()=="europa":
            europa+=1
        elif fila["continente"].lower()=="oceania":
            oceania+=1
        if fila["poblacion"]>max_pob:
            max_pob=fila["poblacion"]
            paismax=fila["pais"]
        if fila["poblacion"]<min_pob:
            min_pob=fila["poblacion"]
            paismin=fila["pais"]
        pob+=fila["poblacion"]
        sup+=fila["superficie"]
        contador+=1
    print(f"pais mas poblado: {paismax} habitantes: {max_pob}")
    print(f"pais menos poblado: {paismin} habitantes: {min_pob}")
    prompob=round(pob/contador)
    promsup=round(sup/contador)
    print(f"poblacion promedio por pais: {prompob} habitantes")
    print(f"superficie promedio por pais: {promsup} km2")
    print("paises por continente:")
    print(f"America:{america}   Asia:{asia}   Africa:{africa}   Europa:{europa}   Oceania:{oceania}")

def mostrar_paises(mi_lista):
    for fila in mi_lista:
        print(f"pais: {fila["pais"]}   poblacion: {fila["poblacion"]} hab.")
        print(f"superficie: {fila["superficie"]} km2   continente: {fila["continente"]}")


DIRECTORIO_ACTUAL=os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO=os.path.join(DIRECTORIO_ACTUAL,"Datos.txt")
#lo ideal es crear_paises solo una vez, luego trabajar con el archivo actualizado
crear_paises(RUTA_ARCHIVO,dataset)
mi_lista=enlistar_paises(RUTA_ARCHIVO)
opcion=10
while opcion!="0":
    print("1: agregar pais")
    print("2: buscar pais")
    print("3: modificar poblacion de un pais")
    print("4: modificar superficie de un pais")
    print("5: filtrar paises por poblacion")
    print("6: filtrar paises por superficie")
    print("7: filtrar paises por continente")
    print("8: ordenamientos")
    print("9: estadisticas")
    print("10:mostrar paises")
    print("0: salir")
    opcion=input("ingrese opcion: ")
    if opcion=="1":
        agregar_pais(mi_lista)
    elif opcion=="2":
        buscar_pais(mi_lista)
    elif opcion=="3":
        modificar_poblacion(mi_lista)
    elif opcion=="4":
        modificar_superficie(mi_lista)
    elif opcion=="5":
        filtrar_por_poblacion(mi_lista)
    elif opcion=="6":
        filtrar_por_superficie(mi_lista)
    elif opcion=="7":
        filtrar_por_continente(mi_lista)
    elif opcion=="8":
        ordenamientos(mi_lista)
    elif opcion=="9":
        estadisticas(mi_lista)
    elif opcion=="10":
        mostrar_paises(mi_lista)
guardar_paises(RUTA_ARCHIVO,mi_lista)