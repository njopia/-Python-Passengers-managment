###########################################################################################################
############################   EVALUACIÓN SUMATIVA N°04 "ARREGLOS, TUPLAS Y DICCIONARIOS"   ###############
############################            DOCENTE: DAVID OSVALDO LARRONDO NARBONA             ###############
###############################################   INTEGRANTES:   ##########################################

##################################          ALAN ANDRES RAMIREZ MANQUEZ           #########################
##################################         NATÁN SALOMÓN JOPIA OLIVARES           #########################
##################################         CRISTIAN JORGE ARAOS MANCILLA          #########################

###########################################################################################################
################################## Analista Programador - INACAP Sede Valparaíso ##########################
###########################################################################################################
import time
import numpy as np
import sys

matriz = np.empty([7,6], dtype='object')
matriz2 = np.empty([7,6], dtype='object')
seleccionados =[]
symbol="\033[1;31m"+"X"+"\033[0m"#Colorear Texto

#Variables de
PreNorm=int(78900)
DescNorm=int(PreNorm*0.15)

PreVip=int(240000)
DescVip=int(PreVip*0.15)

ListadoPasajeros=[]
for i in range(1,43):
    ListadoPasajeros.append([])

def Main():
    Crear_Estructura() 
    MenuInicial()


def Crear_Estructura(): #Determinación de estructura vacía de la matriz (7,6)
    pos=0 #Valor de partida para auto-incremento
    for i in range(7):
        for j in range(6):
            matriz[i][j]= pos+1
            matriz2[i][j]= pos+1
            pos+=1

def Conversion(matriz2, anular): #Re-estructuración temporal de matriz desde 7,6 a 1,46
    matriz2=matriz2.reshape(1,42)
    matriz2[0,anular-1]=anular
    matriz2=matriz2.reshape(7,6)            

def MenuInicial(): #Muestra menú principal
    while True:
        print("""
    (1) VER ASIENTOS DISPONIBLES.
    (2) COMPRAR ASIENTOS.
    (3) ANULAR VUELO.
    (4) MODIFICAR DATOS DE PASAJERO.
    (5) SALIR.
    """)
        op= input("SELECCIONE UNA OPCIÓN:")
        if op=="1":
            header1()
            Mostrar_asientos2(matriz2)
        if op=="2":           
            Seleccion_asientos(matriz, matriz2)
            #SeatSelect()
        if op=="3":
            AnularPasajes(matriz2)
            #SeatSelect()
        if op=="4":
            modificar()
            #SeatSelect()
        if op=="5":
            print("\n \n *****¡DESCONECTADO!***** \n \n")    
            sys.exit()
        else:
            print("OPCIÓN NO VÁLIDA")           

def header1():
        print("\033[0;92m"+"""\n        \t###################\n
              \tASIENTOS DISPONIBLES\n
         (Marcados con X no disponibles)\n
              \t###################\n\033[0m""")

def header2():
        print("\033[0;92m"+"""\n        \t###################\n
              \tCOMPRAR ASIENTOS\n
         (Marcados con X no disponibles)\n
              \t###################\n\033[0m""")

def header3():

         print("\033[0;92m"+"""\n          \t###################\n
              \t    ANULAR VUELO\n
        \t###################\n\033[0m""")


def header4():

         print("\033[0;92m"+"""\n\t              ###################\n
        \t MODIFICAR DATOS DE PASAJERO\n
        \t      ###################\n\033[0m""")

def SeatSelect(): #definición para ahorrar espacio
    print("\n Asientos seleccionados: \n",seleccionados)
    
def Mostrar_asientos2(matriz2):  #(1) VER ASIENTOS DISPONIBLES.
    for i in range(7):
        for j in range(6):
            
            print(matriz2[i][j],"\t", end="  ")
            if (matriz2[i][j])==30:
                print()
                print(("\033[0;33m"+"\n---------------------VIP--------------------"+"\033[0m"))#Colorear Texto
        print("\n")
        #print()


def Seleccion_asientos(matriz, matriz2): #(2) COMPRAR ASIENTOS.
      while True:
        header2() 
        Mostrar_asientos2(matriz2)
        #print(ListadoPasajeros)

        seleccion=int(input("Seleccione asiento (Marcados con X no disponibles):  "))
        if seleccion > 42:
            print(("\033[0;91m"+"\n****OPCIÓN NO VÁLIDA****\nFavor seleccione un asiento válido..."+"\033[0m"))#Colorear Texto
            time.sleep(3)
            break
        elif seleccion < 31:
            print(("\033[0;92m"+f"\nUsted ha seleccionado lo siguiente:\n \nAsiento N°: {seleccion}. \nValor: ${PreNorm}. \n"+"\033[0m"))#Colorear Texto
        else:
            print(("\033[0;92m"+f"\nUsted ha seleccionado lo siguiente:\n \nAsiento N°: {seleccion}. \nValor: ${PreVip}. \n"+"\033[0m"))#Colorear Texto

        
        confirm=int(input("¿Confirma su selección? (1 = Si)/(2 = No)"))
        if confirm == 2:
            Seleccion_asientos(matriz, matriz2)
        elif confirm > 2:
            print(("\033[0;33m"+"\n****OPCIÓN NO VÁLIDA****\nFavor seleccione una opción válida..."+"\033[0m"))#Colorear Texto
            time.sleep(3)
            break
        else:   
            seleccionados.append(seleccion)

            nombre=str(input("Ingrese nombre de pasajero:    "))
            ListadoPasajeros[(seleccion-1)].append(nombre)

            rut=int(input("Ingrese RUT de pasajero:    "))
            ListadoPasajeros[(seleccion-1)].append(rut)

            telefono=int(input("Ingrese N° de telefono de pasajero:    "))
            ListadoPasajeros[(seleccion-1)].append(telefono)

            IsBank=int(input("¿Titular de cuenta pertenece a Banco Inacap? (1 = Si)/(2 = No)"))           
            if IsBank == 1:
                print("\n \n\033[0;33m"+"*****SE HA AGREGADO UN DESCUENTO DEL 15%*****"+"\033[0m\n \n")
                time.sleep(2)
                ListadoPasajeros[(seleccion-1)].append("BancoInacap")
                if seleccion < 31:
                    ListadoPasajeros[(seleccion-1)].append(PreNorm-DescNorm)
                    print(f"Valor del ticket: ${PreNorm-DescNorm}")
                else:
                    ListadoPasajeros[(seleccion-1)].append(PreVip-DescVip)
                    print(f"Valor del ticket: ${PreVip-DescVip}")
            else:
                banco=str(input("Ingrese Banco de pasajero:    "))
                ListadoPasajeros[(seleccion-1)].append(banco)
                if seleccion < 31:
                    ListadoPasajeros[(seleccion-1)].append(PreNorm-DescNorm)
                    print(f"Valor del ticket: ${PreNorm-DescNorm}")
                else:
                    ListadoPasajeros[(seleccion-1)].append(PreVip-DescVip)
                    print(f"Valor del ticket: ${PreVip-DescVip}")
            #print(ListadoPasajeros)
            matriz=np.where(matriz == seleccion, symbol, matriz)
            np.copyto(matriz2, matriz, 'same_kind')

            header2()
            Mostrar_asientos2(matriz2)
            
            #print("Asiento(s) seleccionado(s): \n", seleccionados)    
            #print(ListadoPasajeros)
            again=int(input("¿Desea AGREGAR otro asiento? (1 Si) (2 No)"))
            if again == 2:
                MenuInicial()
            elif again == 1:
                Seleccion_asientos(matriz, matriz2)
            else:
                print(("\033[0;33m"+"\n****OPCIÓN NO VÁLIDA****\nFavor seleccione una opción válida..."+"\033[0m"))#Colorear Texto
                time.sleep(3)
                return matriz

def AnularPasajes(matriz2): #(3) ANULAR VUELO.
    while True:
        header3() 
        Mostrar_asientos2(matriz2)
        anular=int(input("Seleccione asiento a ANULAR: "))
        if ListadoPasajeros[anular-1]==[]:
            print(("\033[0;33m"+"\n****ASIENTO NO DISPONIBLE****\nSelecione otro asiento a anular..."+"\033[0m"))#Colorear Texto
            time.sleep(3)
            break
        else:
            ListadoPasajeros[anular-1]=[]
            Conversion(matriz2,anular)
            Mostrar_asientos2(matriz2)
            print("")
            #print(ListadoPasajeros)
            seleccionados.remove(anular)
            print(("\033[0;33m"+f"\n *****ASIENTO N° {anular} SE HA ANULADO SATISFACTORIAMENTE *****\n"+"\033[0m"))#Colorear Texto
            time.sleep(3)

            AnularOtro=int(input("¿Desea ANULAR otro asiento? (1 Si) (2 No)"))
            if AnularOtro != 1:
                break

def modificar(): #(4) MODIFICAR DATOS DE PASAJERO.
    while True:
        header4() 
        Mostrar_asientos2(matriz2)
        Seleccion=int(input("""\n \n Sub Menu de Informacion y/o Modificacion de Datos:\n
        1)Ver datos de un Asiento:
        2)Modificar Datos :
        3)Salir del Sub Menu
        """))
        if Seleccion==1:
                while True:
                    Numero=int(input("Ingrese Numero de Asiento que consultar: "))
                    if ListadoPasajeros[(Numero-1)]==[]:
                        print(("\033[0;91m"+"\n El asiento selecionado esta vacio, por favor seleccione otro...\n"+"\033[0m"))#Colorear Texto
                        time.sleep(2)
                        break
                    else:
                        print("\033[0;93m"+f"""\n \n \t Datos del Pasajero: N° {Numero} \n
                        1)Nombre: {ListadoPasajeros[(Numero-1)][0]}
                        2)Rut: {ListadoPasajeros[(Numero-1)][1]}
                        3)Telefono: {ListadoPasajeros[(Numero-1)][2]}
                        4)Banco: {ListadoPasajeros[(Numero-1)][3]}
                        5)Valor ticket: ${ListadoPasajeros[(Numero-1)][4]} pesos chilenos (CLP)
                        \n \n\033[0m""")
                        time.sleep(4)
                        break
        if Seleccion==2:
            while True:
                Numero1=int(input("Ingrese Numero de Asiento que desea modificar: "))
                if ListadoPasajeros[Numero1-1]==[]:
                    print(("\033[0;91m"+"\n El asiento selecionado esta vacio, por favor seleccione otro...\n"+"\033[0m"))#Colorear Texto
                    time.sleep(2)
                    break
                else:
                    porRut=int(input("Ingrese Rut para validación de usuario:  "))
                    if ListadoPasajeros[Numero1-1][1]==porRut:
                        while True:    
                            Seleccion=int(input("""Gestión de datos de pasajero:
            1)Modificar nombre de pasajero.
            2)Modificar número telefónico.
            3)Volver al menú anterior.
            """))
                            if Seleccion==1:
                                EditNom=str(input("Ingrese nuevo nombre"))
                                ListadoPasajeros[Numero1-1][0]=EditNom
                                print("\n \n *****MODIFICACIÓN EXITOSA *****\n \n")
                                #print(ListadoPasajeros)   
                            if Seleccion==2:           
                                EditNum=str(input("Ingrese nuevo número telefónico"))
                                ListadoPasajeros[Numero1-1][2]=EditNum
                                print("\n \n *****MODIFICACIÓN EXITOSA *****\n \n")
                                #print(ListadoPasajeros)    
                            if Seleccion==3:
                                modificar()
                    else:
                        #print(f"\n \nRut ingresado ({porRut}) es INCORRECTO. Favor intentar nuevamente...\n \n ")
                        print(("\033[0;91m"+f"\nRut ingresado ({porRut}) es INCORRECTO. Favor intentar nuevamente...\n"+"\033[0m"))#Colorear Texto

                        time.sleep(3)
                        break

        if Seleccion==3:
            MenuInicial()

Main()

#Nota: "Cuando los años pasen y veamos nuestros primeros proyectos; Me gustaría saber que sensación tendremos."