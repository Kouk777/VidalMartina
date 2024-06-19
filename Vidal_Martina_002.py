https://github.com/Kouk777/VidalMartina.git

import csv
lista=[]

def confirmar(resp):
    if resp=="si":
        return 1
    if resp=="no":
        return 2
    
def validación(puntos,lista):
    if puntos>=0 and puntos<=150:
            valido=True
    else:
            valido=False
            print("Puntos no válidos...")
            puntos=int(input("Ingrese los puntos nuevamente : "))
            print("")
          
    
def estadisticas():
    cont=0
    acum=0
    punt=0
    for x in lista:
        cont=cont+1
        acum=int(acum+x[2])
    prom=acum/cont
    print("El promedio de puntos es de = "),prom)
    for x in lista:
        p=x[2]
        if punt<p:
            punt=x[2]
    print("La mayor cantidad de puntos fueron : ",punt)
        
while(True):
    print("-.-.- MENÚ PRINCIPAL -.-.-")
    print("1.- Agregar equipo.")
    print("2.- Listar equipo.")
    print("3.- Actualizar nombre de equipo por id.")
    print("4.- Generar Base de datos.")
    print("5.- Cargar Base de datos.")
    print("6.- Estadísticas.")
    print("0.- Salir.")
    print("")
    
    op=int(input("Seleccione una opción : "))

    if op==1:
           print("")
           print("-.- AGREGAR EQUIPO -.-")
           print("")
           n_jug=int(input("Ingrese el número del equipo : "))
           nombre=input("Ingrese el nombre del equipo : ")
           puntos=int(input("Ingrese los puntos del equipo : "))
           validación(puntos,lista)
           if puntos<=0 and puntos >=40:
                   categoria="Amateur"
           elif puntos<=41 and puntos>=80:
                   categoria="Principiante"
           elif puntos<=81 and puntos >=120:
                   categoria="Avanzado"
           elif puntos>=121 and puntos=150:
                   categoria="Idolos"
           nueva_lista=[n_jug,nombre,puntos,categoria]
           lista.append(nueva_lista)
           print("")
           print("Nuevo equipo agregado correctamente")
                     
    elif op==2:
        print("")
        print("-.- LISTAR EQUIPOS -.-")
        print("")
        for i in lista:
            print("N° Equipo : ",i[0],"Nombre : ",i[1],"Puntos : ",i[2],"Categoría : ",i[3])
            print("-----------------")
    elif op==3:
        encontrado=False
        print("-.- ACTUALIZAR NOMBRE DE EQUIPO -.-")
        n_eq=int(input("Ingrese el N° del equipo que desea actualizar : "))
        for i in lista:
            if n_eq==i[0]:
                print("- DATOS DEL EQUIPO QUE DESEA ACTUALIZAR -")
                print("N° Equipo : ",i[0],"Nombre : ",i[1],"Puntos : ",i[2],"Categoría",i[3])
                resp=input("Confirma la actualización del equipo? (si/no)").lower()
                r=confirmar(resp)
                if r:
                    nv_nom=input("Ingrese el nuevo nombre del equipo : ")
                    i[1]=nv_nom
                    print("Equipo actualizado con éxito!!")
                    encontrado=True
                else:
                    print("Actualización cancelada !!")
                break
    elif op==4:
        print("")
        print("-.- GENERAR BASE DE DATOS -.-")
        print("")
        with open('bbdd_equipos.csv','w',newline='')as bbdd_equipos:
            escritor_csv=csv.writer(bbdd_equipos)
            escritor_csv.writerow(['N° EQUIPO','NOMBRE EQUIPO','PUNTOS','CATEGORIA'])
            escritor_csv.writerows(lista)
            print("ARCHIVO CSV GENERADO CORRECTAMENTE !")
            print("...")
    elif op==5:
        print("")
        print("-.- CARGAR BASE DE DATOS -.-")
        print("")
        with open('bbdd_equipos.csv','r',newline='')as bbdd_equipos:
            lector_csv=csv.reader(bbdd_equipos)
            for x in lector_csv:
                lista.append(x)
                lista.pop(0)
            print("ARCHIVO CSV CARGADO CORRECTAMENTE !")
            print("...")
    elif op==6:
        print("")
        print("-.- ESTADÍSTICAS -.-")
        estadisticas()
        print("")
    elif op==0:
        print("")
        print("HA SALIDO DEL MENÚ...HASTA LUEGO ;P")
        print("...")
        break
    else:
        print("")
        print("Seleccione una opción válida...")
        print("")
           
            
               
