# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Modulos
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import random
import pickle
from reportlab.pdfgen import canvas
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Clases
class Pila:
    def __init__(self):
        self.elementos = []

    def vacía(self):
        """Retorna True si está vacía"""
        return not bool(self.elementos)

    def meter(self, elemento):
        """Agrega un elemento al final de la pila"""
        self.elementos.append(elemento)
    def sacar(self):
        """Remueve el último elemento en entrar"""
        return self.elementos.pop()

    def final(self):
        """retorna el último en entrar"""
        return self.elementos[-1]

    def cantidad(self):
        """número de elementos en la pila"""
        return len(self.elementos)
class Top:
    def __init__(self):
        self.elementos = []
    def meter(self, elemento,tiempo,modalidad):
        """Agrega un elemento al final de la pila y ordena"""
        self.elementos.append([elemento,tiempo])
        sorted(self.elementos, key=lambda x:x[1])
        
    def parcial(self, cantidad):
        if cantidad==0:
            return self.elementos
        if cantidad in range(1,101):
            return self.elementos[:cantidad-1]
    def concatenar(self, lista_nueva):
        self.elementos=self.elementos+lista_nueva
        sorted(self.elementos, key=lambda x:x[1])
        return self.elementos
        
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Definición de variables iniciales requeridas para las funciones
menú = tk.Tk()
menú.title("Juego Sudoku")
menú.geometry("{}x{}+{}+{}".format(370, 382, int((menú.winfo_screenwidth() / 2) - (370 / 2)),
                                   int((menú.winfo_screenheight() / 2) - (382 / 2)))) #decide el tamaño, la posición y algunos otros atributos del diseño de pantalla que vamos a crear.

partidas_iniciales=open("archivos\\documentos\\sudoku2021configuración.dat","wb")
pickle.dump({"reloj":1,"dificultad":0,"horas":0,"minutos":0,"segundos":0,"cantidad_Top":0,"símbolos":["1","2","3","4","5","6","7","8","9"],"símbolos_rbotón":1},partidas_iniciales)                    
partidas_iniciales.close()

configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
configu=pickle.load(configuración_de_archivo) 
configuración_de_archivo.close()                    
fácilTop=Top()
intermedioTop=Top()
difícilTop=Top()
tiempo_expirado=0
guardado=[]
cuadrí_cargando=[]
cargando=False
playreloj=False
jugadas_viejas=Pila()
jugadas_nuevas=Pila()
partida=0
tablero=[]
anterior=0
cantidad_top=0
elección=""
reloj = 0
temporizador = configu["horas"]*3600+configu["minutos"]*60+configu["segundos"]
horas = 0
minutos = 0
segundos = 0
configuración_reloj = tk.IntVar()
configuración_reloj.set(1)
dificultad = tk.IntVar()
dificultad.set(0)
configuración_valores= tk.IntVar()
configuración_valores.set(1)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# indica si el juego inicio
jugando = False
hay_reloj = False
hay_temporizador = False
menú.resizable(width=False, height=False)
menú.config(bg="white")
imagen = tk.PhotoImage(file="archivos\\imagenes\\imagen_menú.png")
imagen.config(width="500",height="500")
fondo = tk.Label(menú, image=imagen)
fondo.config(image=imagen)
fondo.place(x=70, y=70)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

###################################################
#           SECCIÓN DE FUNCIONES                  #
###################################################
def jugar():
    global grid, reloj,guardado,cargando #globales
    configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
    configu=pickle.load(configuración_de_archivo) 
    configuración_de_archivo.close()
    horas=configu["horas"]
    minutos=configu["minutos"]
    segundos=configu["segundos"]
    dificultad=configu["dificultad"]
    configuración_reloj=configu["reloj"]
    configuración_valores=configu['símbolos_rbotón']
    reloj = 0 # se define la variable reloj
    # Esconde el menú
    menú.withdraw()
    # Con top level se crea una ventana secundaria donde se van a ingresar los datos del juego
    ventana_principal_juego = tk.Toplevel()
    
    elección=""
    # se deshabilitan todos los botones
    # Aparecen numeros según la partida escogida del diccionario en configuración
    def invertir(m):
        resultado=[[],[],[],[],[],[],[],[],[]]
        for fila in range(len(m)):
            for elemento in range(len(m[fila])):
                resultado[elemento].append(m[fila][elemento])
        return resultado
    def escoger_partida(partida):
        global tablero
        configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
        configu=pickle.load(configuración_de_archivo) 
        configuración_de_archivo.close()
        partidas_iniciales=open("archivos\\documentos\\sudoku2021partidas.dat","rb")
        lista_diccionarios_partidas=pickle.load(partidas_iniciales)
        partidas_iniciales.close()
        diccionario_fácil=lista_diccionarios_partidas[0]
        diccionario_intermedio=lista_diccionarios_partidas[1]
        diccionario_difícil=lista_diccionarios_partidas[2]
        if configu["dificultad"]==0:
            tablero=diccionario_fácil[list(diccionario_fácil.keys())[partida]]
            for fila in range(9):
                for columna in range(9):
                    if tablero[fila][columna]=="1":
                        tablero[fila][columna]=configu["símbolos"][0]
                    if tablero[fila][columna]=="2":
                        tablero[fila][columna]=configu["símbolos"][1]
                    if tablero[fila][columna]=="3":
                        tablero[fila][columna]=configu["símbolos"][2]
                    if tablero[fila][columna]=="4":
                        tablero[fila][columna]=configu["símbolos"][3]
                    if tablero[fila][columna]=="5":
                        tablero[fila][columna]=configu["símbolos"][4]
                    if tablero[fila][columna]=="6":
                        tablero[fila][columna]=configu["símbolos"][5]
                    if tablero[fila][columna]=="7":
                        tablero[fila][columna]=configu["símbolos"][6]
                    if tablero[fila][columna]=="8":
                        tablero[fila][columna]=configu["símbolos"][7]
                    if tablero[fila][columna]=="9":
                        tablero[fila][columna]=configu["símbolos"][8]
        elif configu["dificultad"]==1:
            tablero=diccionario_intermedio[list(diccionario_intermedio.keys())[partida]]
            for fila in range(9):
                for columna in range(9):
                    if tablero[fila][columna]=="1":
                        tablero[fila][columna]=configu["símbolos"][0]
                    if tablero[fila][columna]=="2":
                        tablero[fila][columna]=configu["símbolos"][1]
                    if tablero[fila][columna]=="3":
                        tablero[fila][columna]=configu["símbolos"][2]
                    if tablero[fila][columna]=="4":
                        tablero[fila][columna]=configu["símbolos"][3]
                    if tablero[fila][columna]=="5":
                        tablero[fila][columna]=configu["símbolos"][4]
                    if tablero[fila][columna]=="6":
                        tablero[fila][columna]=configu["símbolos"][5]
                    if tablero[fila][columna]=="7":
                        tablero[fila][columna]=configu["símbolos"][6]
                    if tablero[fila][columna]=="8":
                        tablero[fila][columna]=configu["símbolos"][7]
                    if tablero[fila][columna]=="9":
                        tablero[fila][columna]=configu["símbolos"][8]
        elif configu["dificultad"]==2:
            tablero=diccionario_difícil[list(diccionario_difícil.keys())[partida]]
            for fila in range(9):
                for columna in range(9):
                    if tablero[fila][columna]=="1":
                        tablero[fila][columna]=configu["símbolos"][0]
                    if tablero[fila][columna]=="2":
                        tablero[fila][columna]=configu["símbolos"][1]
                    if tablero[fila][columna]=="3":
                        tablero[fila][columna]=configu["símbolos"][2]
                    if tablero[fila][columna]=="4":
                        tablero[fila][columna]=configu["símbolos"][3]
                    if tablero[fila][columna]=="5":
                        tablero[fila][columna]=configu["símbolos"][4]
                    if tablero[fila][columna]=="6":
                        tablero[fila][columna]=configu["símbolos"][5]
                    if tablero[fila][columna]=="7":
                        tablero[fila][columna]=configu["símbolos"][6]
                    if tablero[fila][columna]=="8":
                        tablero[fila][columna]=configu["símbolos"][7]
                    if tablero[fila][columna]=="9":
                        tablero[fila][columna]=configu["símbolos"][8]
    
    ventana_principal_juego.title("Juego Sudoku") #Titulo de la ventana
    ventana_principal_juego.geometry("{}x{}+{}+{}".format(700, 500, int((menú.winfo_screenwidth() / 2) - (382 / 2)),
                                                          int((menú.winfo_screenheight() / 2) - (360 / 2)))) #decide el tamaño, la posición y algunos otros atributos del diseño de pantalla que vamos a crear.

    ventana_principal_juego.resizable(width=False, height=False)  #crea una ventana de tamaño fijo
    ventana_principal_juego.config(bg="#8c004b") #se define el color

    frame = tk.Frame(ventana_principal_juego) 
    frame.place(x=0, y=45) #coloca en una posición específica en el widget principal.
    frame.config(width="1", height="1") #Alto y ancho en píxeles
    
    lblJugador = tk.Label(ventana_principal_juego, text="Jugador:", bd=3, bg="#8c004b", fg="black",
                          font=("Century", 11)) 
    lblJugador.place(x=0, y=0)

    lblClock = tk.Label(ventana_principal_juego, bg="#8c004b", font=("Century", 16))
    lblClock.place(x=300, y=0)
    
    lblTimer = tk.Label(ventana_principal_juego, bg="#8c004b", font=("Century", 16))
    lblTimer.place(x=300, y=0)

    
        
    # Label que dibuja  la matriz
            
    grid = [[tk.Button(frame, width=2, height=1, borderwidth=2, relief="solid", font=("Century", 18)) for i in
             range(9)] for j in range(9)] #organiza los widgets en una estructura similar a una tabla en el widget principal.
    num00=grid[0][0]
    num01=grid[0][1]
    num02=grid[0][2]
    num03=grid[0][3]
    num04=grid[0][4]
    num05=grid[0][5]
    num06=grid[0][6]
    num07=grid[0][7]
    num08=grid[0][8]
    num10=grid[1][0]
    num11=grid[1][1]
    num12=grid[1][2]
    num13=grid[1][3]
    num14=grid[1][4]
    num15=grid[1][5]
    num16=grid[1][6]
    num17=grid[1][7]
    num18=grid[1][8]
    num20=grid[2][0]
    num21=grid[2][1]
    num22=grid[2][2]
    num23=grid[2][3]
    num24=grid[2][4]
    num25=grid[2][5]
    num26=grid[2][6]
    num27=grid[2][7]
    num28=grid[2][8]
    num30=grid[3][0]
    num31=grid[3][1]
    num32=grid[3][2]
    num33=grid[3][3]
    num34=grid[3][4]
    num35=grid[3][5]
    num36=grid[3][6]
    num37=grid[3][7]
    num38=grid[3][8]
    num40=grid[4][0]
    num41=grid[4][1]
    num42=grid[4][2]
    num43=grid[4][3]
    num44=grid[4][4]
    num45=grid[4][5]
    num46=grid[4][6]
    num47=grid[4][7]
    num48=grid[4][8]
    num50=grid[5][0]
    num51=grid[5][1]
    num52=grid[5][2]
    num53=grid[5][3]
    num54=grid[5][4]
    num55=grid[5][5]
    num56=grid[5][6]
    num57=grid[5][7]
    num58=grid[5][8]
    num60=grid[6][0]
    num61=grid[6][1]
    num62=grid[6][2]
    num63=grid[6][3]
    num64=grid[6][4]
    num65=grid[6][5]
    num66=grid[6][6]
    num67=grid[6][7]
    num68=grid[6][8]
    num70=grid[7][0]
    num71=grid[7][1]
    num72=grid[7][2]
    num73=grid[7][3]
    num74=grid[7][4]
    num75=grid[7][5]
    num76=grid[7][6]
    num77=grid[7][7]
    num78=grid[7][8]
    num80=grid[8][0]
    num81=grid[8][1]
    num82=grid[8][2]
    num83=grid[8][3]
    num84=grid[8][4]
    num85=grid[8][5]
    num86=grid[8][6]
    num87=grid[8][7]
    num88=grid[8][8]

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# validaciones de cada elemento del tablero y funciones dependientes de la variable elección para establecer cambios en los textos de
# los botones


    def func00():
        global elección,jugadas_viejas
        anterior=num00["text"]
        color_anterior=num00["bg"]
        num00.config(text=elección)
        def cerrar_advertencia00(event):
            habilitar_botones()
            num00.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num00.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia00)
        elif num00["bg"]!="#02ac66":
            deshabilitar_botones()
            num00.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia00)
        elif [num00["text"],num01["text"],num02["text"],num10["text"],num11["text"],num12["text"],num20["text"],num21["text"],num22["text"]].count(num00["text"])>1:
            deshabilitar_botones()
            num00.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia00)

        elif [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"]].count(num00["text"])>1:
            deshabilitar_botones()
            num00.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia00)
                    
        elif [num00["text"],num10["text"],num20["text"],num30["text"],num40["text"],num50["text"],num60["text"],num70["text"],num80["text"]].count(num00["text"])>1:
            deshabilitar_botones()
            num00.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia00)
        else:
            jugadas_viejas.meter([num00,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func01():
        global elección,jugadas_viejas
        anterior=num01["text"]
        color_anterior=num01["bg"]
        num01.config(text=elección)
        def cerrar_advertencia01(event):
            habilitar_botones()
            num01.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num01.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia01)
        elif num01["bg"]!="#02ac66":
            deshabilitar_botones()
            num01.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia01)

        elif [num00["text"],num01["text"],num02["text"],num10["text"],num11["text"],num12["text"],num20["text"],num21["text"],num22["text"]].count(num01["text"])>1:
            deshabilitar_botones()
            num01.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia01)

        elif [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"]].count(num01["text"])>1:
            deshabilitar_botones()
            num01.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia01)
                    
        elif [num01["text"],num11["text"],num21["text"],num31["text"],num41["text"],num51["text"],num61["text"],num71["text"],num81["text"]].count(num01["text"])>1:
            deshabilitar_botones()
            num01.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia01)
        else:
            jugadas_viejas.meter([num01,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func02():
        global elección,jugadas_viejas
        anterior=num02["text"]
        color_anterior=num02["bg"]
        num02.config(text=elección)
        def cerrar_advertencia02(event):
            habilitar_botones()
            num02.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num02.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia02)
        elif num02["bg"]!="#02ac66":
            deshabilitar_botones()
            num02.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia02)
        elif [num00["text"],num01["text"],num02["text"],num10["text"],num11["text"],num12["text"],num20["text"],num21["text"],num22["text"]].count(num02["text"])>1:
            deshabilitar_botones()
            num02.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia02)


        elif [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"]].count(num02["text"])>1:
            deshabilitar_botones()
            num02.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia02)
                    
        elif [num02["text"],num12["text"],num22["text"],num32["text"],num42["text"],num52["text"],num62["text"],num72["text"],num82["text"]].count(num02["text"])>1:
            deshabilitar_botones()
            num02.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia02)
        else:
            jugadas_viejas.meter([num02,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func03():
        global elección,jugadas_viejas
        anterior=num03["text"]
        color_anterior=num03["bg"]
        num03.config(text=elección)
        def cerrar_advertencia03(event):
            habilitar_botones()
            num03.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num03.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia03)
        elif num03["bg"]!="#02ac66":
            deshabilitar_botones()
            num03.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia03)
        elif [num03["text"],num04["text"],num05["text"],num13["text"],num14["text"],num15["text"],num23["text"],num24["text"],num25["text"]].count(num03["text"])>1:
            deshabilitar_botones()
            num03.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia03)

        elif [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"]].count(num03["text"])>1:
            deshabilitar_botones()
            num03.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia03)
                    
        elif [num03["text"],num13["text"],num23["text"],num33["text"],num43["text"],num53["text"],num63["text"],num73["text"],num83["text"]].count(num03["text"])>1:
            deshabilitar_botones()
            num03.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia03)
        else:
            jugadas_viejas.meter([num03,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func04():
        global elección,jugadas_viejas
        anterior=num04["text"]
        color_anterior=num04["bg"]
        num04.config(text=elección)
        def cerrar_advertencia04(event):
            habilitar_botones()
            num04.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num04.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia04)
        elif num04["bg"]!="#02ac66":
            deshabilitar_botones()
            num04.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia04)

        elif [num03["text"],num04["text"],num05["text"],num13["text"],num14["text"],num15["text"],num23["text"],num24["text"],num25["text"]].count(num04["text"])>1:
            deshabilitar_botones()
            num04.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia04)

        elif [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"]].count(num04["text"])>1:
            deshabilitar_botones()
            num04.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia04)
                    
        elif [num04["text"],num14["text"],num24["text"],num34["text"],num44["text"],num54["text"],num64["text"],num74["text"],num84["text"]].count(num04["text"])>1:
            deshabilitar_botones()
            num04.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia04)
        else:
            jugadas_viejas.meter([num04,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func05():
        global elección,jugadas_viejas
        anterior=num05["text"]
        color_anterior=num05["bg"]
        num05.config(text=elección)
        def cerrar_advertencia05(event):
            habilitar_botones()
            num05.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num05.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia05)
        elif num05["bg"]!="#02ac66":
            deshabilitar_botones()
            num05.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia05)
        elif [num03["text"],num04["text"],num05["text"],num13["text"],num14["text"],num15["text"],num23["text"],num24["text"],num25["text"]].count(num05["text"])>1:
            deshabilitar_botones()
            num05.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia05)


        elif [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"]].count(num05["text"])>1:
            deshabilitar_botones()
            num05.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia05)
                    
        elif [num05["text"],num15["text"],num25["text"],num35["text"],num45["text"],num55["text"],num65["text"],num75["text"],num85["text"]].count(num05["text"])>1:
            deshabilitar_botones()
            num05.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia05)
        else:
            jugadas_viejas.meter([num05,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func06():
        global elección,jugadas_viejas
        anterior=num06["text"]
        color_anterior=num06["bg"]
        num06.config(text=elección)
        def cerrar_advertencia06(event):
            habilitar_botones()
            num06.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num06.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia06)
        elif num06["bg"]!="#02ac66":
            deshabilitar_botones()
            num06.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia06)
        elif [num06["text"],num07["text"],num08["text"],num16["text"],num17["text"],num18["text"],num26["text"],num27["text"],num28["text"]].count(num06["text"])>1:
            deshabilitar_botones()
            num06.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia06)

        elif [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"]].count(num06["text"])>1:
            deshabilitar_botones()
            num06.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia06)
                    
        elif [num06["text"],num16["text"],num26["text"],num36["text"],num46["text"],num56["text"],num66["text"],num76["text"],num86["text"]].count(num06["text"])>1:
            deshabilitar_botones()
            num06.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia06)
        else:
            jugadas_viejas.meter([num06,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func07():
        global elección,jugadas_viejas
        anterior=num07["text"]
        color_anterior=num07["bg"]
        num07.config(text=elección)
        def cerrar_advertencia07(event):
            habilitar_botones()
            num07.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num07.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia07)
        elif num07["bg"]!="#02ac66":
            deshabilitar_botones()
            num07.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia07)

        elif [num06["text"],num07["text"],num08["text"],num16["text"],num17["text"],num18["text"],num26["text"],num27["text"],num28["text"]].count(num07["text"])>1:
            deshabilitar_botones()
            num07.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia07)

        elif [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"]].count(num07["text"])>1:
            deshabilitar_botones()
            num07.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia07)
                    
        elif [num07["text"],num17["text"],num27["text"],num37["text"],num47["text"],num57["text"],num67["text"],num77["text"],num87["text"]].count(num07["text"])>1:
            deshabilitar_botones()
            num07.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia07)
        else:
            jugadas_viejas.meter([num07,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func08():
        global elección,jugadas_viejas
        anterior=num08["text"]
        color_anterior=num08["bg"]
        num08.config(text=elección)
        def cerrar_advertencia08(event):
            habilitar_botones()
            num08.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num08.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia08)
        elif num08["bg"]!="#02ac66":
            deshabilitar_botones()
            num08.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia08)
        elif [num06["text"],num07["text"],num08["text"],num16["text"],num17["text"],num18["text"],num26["text"],num27["text"],num28["text"]].count(num08["text"])>1:
            deshabilitar_botones()
            num08.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia08)


        elif [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"]].count(num08["text"])>1:
            deshabilitar_botones()
            num08.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia08)
                    
        elif [num08["text"],num18["text"],num28["text"],num38["text"],num48["text"],num58["text"],num68["text"],num78["text"],num88["text"]].count(num08["text"])>1:
            deshabilitar_botones()
            num08.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia08)
        else:
            jugadas_viejas.meter([num08,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func10():
        global elección,jugadas_viejas
        anterior=num10["text"]
        color_anterior=num10["bg"]
        num10.config(text=elección)
        def cerrar_advertencia10(event):
            habilitar_botones()
            num10.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num10.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia10)
        elif num10["bg"]!="#02ac66":
            deshabilitar_botones()
            num10.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia10)
            
        elif [num00["text"],num01["text"],num02["text"],num10["text"],num11["text"],num12["text"],num20["text"],num21["text"],num22["text"]].count(num10["text"])>1:
            deshabilitar_botones()
            num10.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia10)

        elif [num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"]].count(num10["text"])>1:
            deshabilitar_botones()
            num10.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia10)
                    
        elif [num00["text"],num10["text"],num20["text"],num30["text"],num40["text"],num50["text"],num60["text"],num70["text"],num80["text"]].count(num10["text"])>1:
            deshabilitar_botones()
            num10.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia10)
        else:
            jugadas_viejas.meter([num10,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func11():
        global elección,jugadas_viejas
        anterior=num11["text"]
        color_anterior=num11["bg"]
        num11.config(text=elección)
        def cerrar_advertencia11(event):
            habilitar_botones()
            num11.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num11.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia11)
        elif num11["bg"]!="#02ac66":
            deshabilitar_botones()
            num11.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia11)
            
        elif [num00["text"],num01["text"],num02["text"],num10["text"],num11["text"],num12["text"],num20["text"],num21["text"],num22["text"]].count(num11["text"])>1:
            deshabilitar_botones()
            num11.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia11)

        elif [num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"]].count(num11["text"])>1:
            deshabilitar_botones()
            num11.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia11)
                    
        elif [num01["text"],num11["text"],num21["text"],num31["text"],num41["text"],num51["text"],num61["text"],num71["text"],num81["text"]].count(num11["text"])>1:
            deshabilitar_botones()
            num11.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia11)
        else:
            jugadas_viejas.meter([num11,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func12():
        global elección,jugadas_viejas
        anterior=num12["text"]
        color_anterior=num12["bg"]
        num12.config(text=elección)
        def cerrar_advertencia12(event):
            habilitar_botones()
            num12.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num12.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia12)
        elif num12["bg"]!="#02ac66":
            deshabilitar_botones()
            num12.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia12)

        elif [num00["text"],num01["text"],num02["text"],num10["text"],num11["text"],num12["text"],num20["text"],num21["text"],num22["text"]].count(num12["text"])>1:
            deshabilitar_botones()
            num12.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia12)

        elif [num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"]].count(num12["text"])>1:
            deshabilitar_botones()
            num12.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia12)
                    
        elif [num02["text"],num12["text"],num22["text"],num32["text"],num42["text"],num52["text"],num62["text"],num72["text"],num82["text"]].count(num12["text"])>1:
            deshabilitar_botones()
            num12.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia12)
        else:
            jugadas_viejas.meter([num12,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func13():
        global elección,jugadas_viejas
        anterior=num13["text"]
        color_anterior=num13["bg"]
        num13.config(text=elección)
        def cerrar_advertencia13(event):
            habilitar_botones()
            num13.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num13.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia13)
        elif num13["bg"]!="#02ac66":
            deshabilitar_botones()
            num13.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia13)
            
        elif [num03["text"],num04["text"],num05["text"],num13["text"],num14["text"],num15["text"],num23["text"],num24["text"],num25["text"]].count(num13["text"])>1:
            deshabilitar_botones()
            num13.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia13)

        elif [num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"]].count(num13["text"])>1:
            deshabilitar_botones()
            num13.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia13)
                    
        elif [num03["text"],num13["text"],num23["text"],num33["text"],num43["text"],num53["text"],num63["text"],num73["text"],num83["text"]].count(num13["text"])>1:
            deshabilitar_botones()
            num13.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia13)
        else:
            jugadas_viejas.meter([num13,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func14():
        global elección,jugadas_viejas
        anterior=num14["text"]
        color_anterior=num14["bg"]
        num14.config(text=elección)
        def cerrar_advertencia14(event):
            habilitar_botones()
            num14.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num14.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia14)
        elif num14["bg"]!="#02ac66":
            deshabilitar_botones()
            num14.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia14)
            
        elif [num03["text"],num04["text"],num05["text"],num13["text"],num14["text"],num15["text"],num23["text"],num24["text"],num25["text"]].count(num14["text"])>1:
            deshabilitar_botones()
            num14.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia14)

        elif [num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"]].count(num14["text"])>1:
            deshabilitar_botones()
            num14.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia14)
                    
        elif [num04["text"],num14["text"],num24["text"],num34["text"],num44["text"],num54["text"],num64["text"],num74["text"],num84["text"]].count(num14["text"])>1:
            deshabilitar_botones()
            num14.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia14)
        else:
            jugadas_viejas.meter([num14,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func15():
        global elección,jugadas_viejas
        anterior=num15["text"]
        color_anterior=num15["bg"]
        num15.config(text=elección)
        def cerrar_advertencia15(event):
            habilitar_botones()
            num15.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num15.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia15)
        elif num15["bg"]!="#02ac66":
            deshabilitar_botones()
            num15.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia15)

        elif [num03["text"],num04["text"],num05["text"],num13["text"],num14["text"],num15["text"],num23["text"],num24["text"],num25["text"]].count(num15["text"])>1:
            deshabilitar_botones()
            num15.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia15)

        elif [num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"]].count(num15["text"])>1:
            deshabilitar_botones()
            num15.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia15)
                    
        elif [num05["text"],num15["text"],num25["text"],num35["text"],num45["text"],num55["text"],num65["text"],num75["text"],num85["text"]].count(num15["text"])>1:
            deshabilitar_botones()
            num15.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia15)
        else:
            jugadas_viejas.meter([num15,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func16():
        global elección,jugadas_viejas
        anterior=num16["text"]
        color_anterior=num16["bg"]
        num16.config(text=elección)
        def cerrar_advertencia16(event):
            habilitar_botones()
            num16.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num16.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia16)
        elif num16["bg"]!="#02ac66":
            deshabilitar_botones()
            num16.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia16)
            
        elif [num06["text"],num07["text"],num08["text"],num16["text"],num17["text"],num18["text"],num26["text"],num27["text"],num28["text"]].count(num16["text"])>1:
            deshabilitar_botones()
            num16.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia16)

        elif [num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"]].count(num16["text"])>1:
            deshabilitar_botones()
            num16.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia16)
                    
        elif [num06["text"],num16["text"],num26["text"],num36["text"],num46["text"],num56["text"],num66["text"],num76["text"],num86["text"]].count(num16["text"])>1:
            deshabilitar_botones()
            num16.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia16)
        else:
            jugadas_viejas.meter([num16,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func17():
        global elección,jugadas_viejas
        anterior=num17["text"]
        color_anterior=num17["bg"]
        num17.config(text=elección)
        def cerrar_advertencia17(event):
            habilitar_botones()
            num17.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num17.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia17)
        elif num17["bg"]!="#02ac66":
            deshabilitar_botones()
            num17.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia17)
            
        elif [num06["text"],num07["text"],num08["text"],num16["text"],num17["text"],num18["text"],num26["text"],num27["text"],num28["text"]].count(num17["text"])>1:
            deshabilitar_botones()
            num17.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia17)

        elif [num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"]].count(num17["text"])>1:
            deshabilitar_botones()
            num17.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia17)
                    
        elif [num07["text"],num17["text"],num27["text"],num37["text"],num47["text"],num57["text"],num67["text"],num77["text"],num87["text"]].count(num17["text"])>1:
            deshabilitar_botones()
            num17.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia17)
        else:
            jugadas_viejas.meter([num17,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func18():
        global elección,jugadas_viejas
        anterior=num18["text"]
        color_anterior=num18["bg"]
        num18.config(text=elección)
        def cerrar_advertencia18(event):
            habilitar_botones()
            num18.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num18.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia18)
        elif num18["bg"]!="#02ac66":
            deshabilitar_botones()
            num18.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia18)

        elif [num06["text"],num07["text"],num08["text"],num16["text"],num17["text"],num18["text"],num26["text"],num27["text"],num28["text"]].count(num18["text"])>1:
            deshabilitar_botones()
            num18.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia18)

        elif [num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"]].count(num18["text"])>1:
            deshabilitar_botones()
            num18.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia18)
                    
        elif [num08["text"],num18["text"],num28["text"],num38["text"],num48["text"],num58["text"],num68["text"],num78["text"],num88["text"]].count(num18["text"])>1:
            deshabilitar_botones()
            num18.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia18)
        else:
            jugadas_viejas.meter([num18,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func20():
        global elección,jugadas_viejas
        anterior=num20["text"]
        color_anterior=num20["bg"]
        num20.config(text=elección)
        def cerrar_advertencia20(event):
            habilitar_botones()
            num20.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num20.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia20)
        elif num20["bg"]!="#02ac66":
            deshabilitar_botones()
            num20.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia20)

        elif [num00["text"],num01["text"],num02["text"],num10["text"],num11["text"],num12["text"],num20["text"],num21["text"],num22["text"]].count(num20["text"])>1:
            deshabilitar_botones()
            num20.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia20)

        elif [num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"]].count(num20["text"])>1:
            deshabilitar_botones()
            num20.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia20)
                    
        elif [num00["text"],num10["text"],num20["text"],num30["text"],num40["text"],num50["text"],num60["text"],num70["text"],num80["text"]].count(num20["text"])>1:
            deshabilitar_botones()
            num20.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia20)
        else:
            jugadas_viejas.meter([num20,anterior])



        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func21():
        global elección,jugadas_viejas
        anterior=num21["text"]
        color_anterior=num21["bg"]
        num21.config(text=elección)
        def cerrar_advertencia21(event):
            habilitar_botones()
            num21.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num21.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia21)
        elif num21["bg"]!="#02ac66":
            deshabilitar_botones()
            num21.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia21)

        elif [num00["text"],num01["text"],num02["text"],num10["text"],num11["text"],num12["text"],num20["text"],num21["text"],num22["text"]].count(num21["text"])>1:
            deshabilitar_botones()
            num21.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia21)

        elif [num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"]].count(num21["text"])>1:
            deshabilitar_botones()
            num21.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia21)
                    
        elif [num01["text"],num11["text"],num21["text"],num31["text"],num41["text"],num51["text"],num61["text"],num71["text"],num81["text"]].count(num21["text"])>1:
            deshabilitar_botones()
            num21.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia21)
        else:
            jugadas_viejas.meter([num21,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func22():
        global elección,jugadas_viejas
        anterior=num22["text"]
        color_anterior=num22["bg"]
        num22.config(text=elección)
        def cerrar_advertencia22(event):
            habilitar_botones()
            num22.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num22.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia22)
        elif num22["bg"]!="#02ac66":
            deshabilitar_botones()
            num22.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia22)
        elif [num00["text"],num01["text"],num02["text"],num10["text"],num11["text"],num12["text"],num20["text"],num21["text"],num22["text"]].count(num22["text"])>1:
            deshabilitar_botones()
            num22.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia22)

        elif [num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"]].count(num22["text"])>1:
            deshabilitar_botones()
            num22.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia22)
                    
        elif [num02["text"],num12["text"],num22["text"],num32["text"],num42["text"],num52["text"],num62["text"],num72["text"],num82["text"]].count(num22["text"])>1:
            deshabilitar_botones()
            num22.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia22)
        else:
            jugadas_viejas.meter([num22,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
            
    def func23():
        global elección,jugadas_viejas
        anterior=num23["text"]
        color_anterior=num23["bg"]
        num23.config(text=elección)
        def cerrar_advertencia23(event):
            habilitar_botones()
            num23.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num23.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia23)
        elif num23["bg"]!="#02ac66":
            deshabilitar_botones()
            num23.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia23)

        elif [num03["text"],num04["text"],num05["text"],num13["text"],num14["text"],num15["text"],num23["text"],num24["text"],num25["text"]].count(num23["text"])>1:
            deshabilitar_botones()
            num23.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia23)

        elif [num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"]].count(num23["text"])>1:
            deshabilitar_botones()
            num23.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia23)
                    
        elif [num03["text"],num13["text"],num23["text"],num33["text"],num43["text"],num53["text"],num63["text"],num73["text"],num83["text"]].count(num23["text"])>1:
            deshabilitar_botones()
            num23.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia23)
        else:
            jugadas_viejas.meter([num23,anterior])



        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func24():
        global elección,jugadas_viejas
        anterior=num24["text"]
        color_anterior=num24["bg"]
        num24.config(text=elección)
        def cerrar_advertencia24(event):
            habilitar_botones()
            num24.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num24.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia24)
        elif num24["bg"]!="#02ac66":
            deshabilitar_botones()
            num24.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia24)

        elif [num03["text"],num04["text"],num05["text"],num13["text"],num14["text"],num15["text"],num23["text"],num24["text"],num25["text"]].count(num24["text"])>1:
            deshabilitar_botones()
            num24.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia24)

        elif [num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"]].count(num24["text"])>1:
            deshabilitar_botones()
            num24.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia24)
                    
        elif [num04["text"],num14["text"],num24["text"],num34["text"],num44["text"],num54["text"],num64["text"],num74["text"],num84["text"]].count(num24["text"])>1:
            deshabilitar_botones()
            num24.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia24)
        else:
            jugadas_viejas.meter([num24,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func25():
        global elección,jugadas_viejas
        anterior=num25["text"]
        color_anterior=num25["bg"]
        num25.config(text=elección)
        def cerrar_advertencia25(event):
            habilitar_botones()
            num25.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num25.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia25)
        elif num25["bg"]!="#02ac66":
            deshabilitar_botones()
            num25.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia25)
        elif [num03["text"],num04["text"],num05["text"],num13["text"],num14["text"],num15["text"],num23["text"],num24["text"],num25["text"]].count(num25["text"])>1:
            deshabilitar_botones()
            num25.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia25)

        elif [num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"]].count(num25["text"])>1:
            deshabilitar_botones()
            num25.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia25)
                    
        elif [num05["text"],num15["text"],num25["text"],num35["text"],num45["text"],num55["text"],num65["text"],num75["text"],num85["text"]].count(num25["text"])>1:
            deshabilitar_botones()
            num25.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia25)
        else:
            jugadas_viejas.meter([num25,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
            
    def func26():
        global elección,jugadas_viejas
        anterior=num26["text"]
        color_anterior=num26["bg"]
        num26.config(text=elección)
        def cerrar_advertencia26(event):
            habilitar_botones()
            num26.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num26.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia26)
        elif num26["bg"]!="#02ac66":
            deshabilitar_botones()
            num26.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia26)

        elif [num06["text"],num07["text"],num08["text"],num16["text"],num17["text"],num18["text"],num26["text"],num27["text"],num28["text"]].count(num26["text"])>1:
            deshabilitar_botones()
            num26.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia26)

        elif [num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"]].count(num26["text"])>1:
            deshabilitar_botones()
            num26.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia26)
                    
        elif [num06["text"],num16["text"],num26["text"],num36["text"],num46["text"],num56["text"],num66["text"],num76["text"],num86["text"]].count(num26["text"])>1:
            deshabilitar_botones()
            num26.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia26)
        else:
            jugadas_viejas.meter([num26,anterior])



        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func27():
        global elección,jugadas_viejas
        anterior=num27["text"]
        color_anterior=num27["bg"]
        num27.config(text=elección)
        def cerrar_advertencia27(event):
            habilitar_botones()
            num27.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num27.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia27)
        elif num27["bg"]!="#02ac66":
            deshabilitar_botones()
            num27.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia27)

        elif [num06["text"],num07["text"],num08["text"],num16["text"],num17["text"],num18["text"],num26["text"],num27["text"],num28["text"]].count(num27["text"])>1:
            deshabilitar_botones()
            num27.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia27)

        elif [num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"]].count(num27["text"])>1:
            deshabilitar_botones()
            num27.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia27)
                    
        elif [num07["text"],num17["text"],num27["text"],num37["text"],num47["text"],num57["text"],num67["text"],num77["text"],num87["text"]].count(num27["text"])>1:
            deshabilitar_botones()
            num27.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia27)
        else:
            jugadas_viejas.meter([num27,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func28():
        global elección,jugadas_viejas
        anterior=num28["text"]
        color_anterior=num28["bg"]
        num28.config(text=elección)
        def cerrar_advertencia28(event):
            habilitar_botones()
            num28.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num28.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia28)
        elif num28["bg"]!="#02ac66":
            deshabilitar_botones()
            num28.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia28)
        elif [num06["text"],num07["text"],num08["text"],num16["text"],num17["text"],num18["text"],num26["text"],num27["text"],num28["text"]].count(num28["text"])>1:
            deshabilitar_botones()
            num28.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia28)

        elif [num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"]].count(num28["text"])>1:
            deshabilitar_botones()
            num28.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia28)
                    
        elif [num08["text"],num18["text"],num28["text"],num38["text"],num48["text"],num58["text"],num68["text"],num78["text"],num88["text"]].count(num28["text"])>1:
            deshabilitar_botones()
            num28.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia28)
        else:
            jugadas_viejas.meter([num28,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
            
    def func30():
        global elección,jugadas_viejas
        anterior=num30["text"]
        color_anterior=num30["bg"]
        num30.config(text=elección)
        def cerrar_advertencia30(event):
            habilitar_botones()
            num30.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num30.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia30)
        elif num30["bg"]!="#02ac66":
            deshabilitar_botones()
            num30.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia30)
        elif [num30["text"],num31["text"],num32["text"],num40["text"],num41["text"],num42["text"],num50["text"],num51["text"],num52["text"]].count(num30["text"])>1:
            deshabilitar_botones()
            num30.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia30)

        elif [num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"]].count(num30["text"])>1:
            deshabilitar_botones()
            num30.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia30)
                    
        elif [num00["text"],num10["text"],num20["text"],num30["text"],num40["text"],num50["text"],num60["text"],num70["text"],num80["text"]].count(num30["text"])>1:
            deshabilitar_botones()
            num30.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia30)
        else:
            jugadas_viejas.meter([num30,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func31():
        global elección,jugadas_viejas
        anterior=num31["text"]
        color_anterior=num31["bg"]
        num31.config(text=elección)
        def cerrar_advertencia31(event):
            habilitar_botones()
            num31.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num31.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia31)
        elif num31["bg"]!="#02ac66":
            deshabilitar_botones()
            num31.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia31)

        elif [num30["text"],num31["text"],num32["text"],num40["text"],num41["text"],num42["text"],num50["text"],num51["text"],num52["text"]].count(num31["text"])>1:
            deshabilitar_botones()
            num31.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia31)

        elif [num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"]].count(num31["text"])>1:
            deshabilitar_botones()
            num31.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia31)
                    
        elif [num01["text"],num11["text"],num21["text"],num31["text"],num41["text"],num51["text"],num61["text"],num71["text"],num81["text"]].count(num31["text"])>1:
            deshabilitar_botones()
            num31.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia31)
        else:
            jugadas_viejas.meter([num31,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func32():
        global elección,jugadas_viejas
        anterior=num32["text"]
        color_anterior=num32["bg"]
        num32.config(text=elección)
        def cerrar_advertencia32(event):
            habilitar_botones()
            num32.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num32.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia32)
        elif num32["bg"]!="#02ac66":
            deshabilitar_botones()
            num32.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia32)
        elif [num30["text"],num31["text"],num32["text"],num40["text"],num41["text"],num42["text"],num50["text"],num51["text"],num52["text"]].count(num32["text"])>1:
            deshabilitar_botones()
            num32.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia32)


        elif [num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"]].count(num32["text"])>1:
            deshabilitar_botones()
            num32.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia32)
                    
        elif [num02["text"],num12["text"],num22["text"],num32["text"],num42["text"],num52["text"],num62["text"],num72["text"],num82["text"]].count(num32["text"])>1:
            deshabilitar_botones()
            num32.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia32)
        else:
            jugadas_viejas.meter([num32,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func33():
        global elección,jugadas_viejas
        anterior=num33["text"]
        color_anterior=num33["bg"]
        num33.config(text=elección)
        def cerrar_advertencia33(event):
            habilitar_botones()
            num33.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num33.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia33)
        elif num33["bg"]!="#02ac66":
            deshabilitar_botones()
            num33.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia33)
        elif [num33["text"],num34["text"],num35["text"],num43["text"],num44["text"],num45["text"],num53["text"],num54["text"],num55["text"]].count(num33["text"])>1:
            deshabilitar_botones()
            num33.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia33)

        elif [num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"]].count(num33["text"])>1:
            deshabilitar_botones()
            num33.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia33)
                    
        elif [num03["text"],num13["text"],num23["text"],num33["text"],num43["text"],num53["text"],num63["text"],num73["text"],num83["text"]].count(num33["text"])>1:
            deshabilitar_botones()
            num33.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia33)
        else:
            jugadas_viejas.meter([num33,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func34():
        global elección,jugadas_viejas
        anterior=num34["text"]
        color_anterior=num34["bg"]
        num34.config(text=elección)
        def cerrar_advertencia34(event):
            habilitar_botones()
            num34.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num34.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia34)
        elif num34["bg"]!="#02ac66":
            deshabilitar_botones()
            num34.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia34)

        elif [num33["text"],num34["text"],num35["text"],num43["text"],num44["text"],num45["text"],num53["text"],num54["text"],num55["text"]].count(num34["text"])>1:
            deshabilitar_botones()
            num34.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia34)

        elif [num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"]].count(num34["text"])>1:
            deshabilitar_botones()
            num34.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia34)
                    
        elif [num04["text"],num14["text"],num24["text"],num34["text"],num44["text"],num54["text"],num64["text"],num74["text"],num84["text"]].count(num34["text"])>1:
            deshabilitar_botones()
            num34.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia34)
        else:
            jugadas_viejas.meter([num34,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func35():
        global elección,jugadas_viejas
        anterior=num35["text"]
        color_anterior=num35["bg"]
        num35.config(text=elección)
        def cerrar_advertencia35(event):
            habilitar_botones()
            num35.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num35.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia35)
        elif num35["bg"]!="#02ac66":
            deshabilitar_botones()
            num35.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia35)
        elif [num33["text"],num34["text"],num35["text"],num43["text"],num44["text"],num45["text"],num53["text"],num54["text"],num55["text"]].count(num35["text"])>1:
            deshabilitar_botones()
            num35.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia35)


        elif [num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"]].count(num35["text"])>1:
            deshabilitar_botones()
            num35.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia35)
                    
        elif [num05["text"],num15["text"],num25["text"],num35["text"],num45["text"],num55["text"],num65["text"],num75["text"],num85["text"]].count(num35["text"])>1:
            deshabilitar_botones()
            num35.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia35)
        else:
            jugadas_viejas.meter([num35,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func36():
        global elección,jugadas_viejas
        anterior=num36["text"]
        color_anterior=num36["bg"]
        num36.config(text=elección)
        def cerrar_advertencia36(event):
            habilitar_botones()
            num36.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num36.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia36)
        elif num36["bg"]!="#02ac66":
            deshabilitar_botones()
            num36.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia36)
        elif [num36["text"],num37["text"],num38["text"],num46["text"],num47["text"],num48["text"],num56["text"],num57["text"],num58["text"]].count(num36["text"])>1:
            deshabilitar_botones()
            num36.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia36)

        elif [num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"]].count(num36["text"])>1:
            deshabilitar_botones()
            num36.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia36)
                    
        elif [num06["text"],num16["text"],num26["text"],num36["text"],num46["text"],num56["text"],num66["text"],num76["text"],num86["text"]].count(num36["text"])>1:
            deshabilitar_botones()
            num36.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia36)
        else:
            jugadas_viejas.meter([num36,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func37():
        global elección,jugadas_viejas
        anterior=num37["text"]
        color_anterior=num37["bg"]
        num37.config(text=elección)
        def cerrar_advertencia37(event):
            habilitar_botones()
            num37.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num37.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia37)
        elif num37["bg"]!="#02ac66":
            deshabilitar_botones()
            num37.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia37)

        elif [num36["text"],num37["text"],num38["text"],num46["text"],num47["text"],num48["text"],num56["text"],num57["text"],num58["text"]].count(num37["text"])>1:
            deshabilitar_botones()
            num37.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia37)

        elif [num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"]].count(num37["text"])>1:
            deshabilitar_botones()
            num37.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia37)
                    
        elif [num07["text"],num17["text"],num27["text"],num37["text"],num47["text"],num57["text"],num67["text"],num77["text"],num87["text"]].count(num37["text"])>1:
            deshabilitar_botones()
            num37.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia37)
        else:
            jugadas_viejas.meter([num37,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func38():
        global elección,jugadas_viejas
        anterior=num38["text"]
        color_anterior=num38["bg"]
        num38.config(text=elección)
        def cerrar_advertencia38(event):
            habilitar_botones()
            num38.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num38.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia38)
        elif num38["bg"]!="#02ac66":
            deshabilitar_botones()
            num38.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia38)
        elif [num36["text"],num37["text"],num38["text"],num46["text"],num47["text"],num48["text"],num56["text"],num57["text"],num58["text"]].count(num38["text"])>1:
            deshabilitar_botones()
            num38.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia38)


        elif [num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"]].count(num38["text"])>1:
            deshabilitar_botones()
            num38.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia38)
                    
        elif [num08["text"],num18["text"],num28["text"],num38["text"],num48["text"],num58["text"],num68["text"],num78["text"],num88["text"]].count(num38["text"])>1:
            deshabilitar_botones()
            num38.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia38)
        else:
            jugadas_viejas.meter([num38,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func40():
        global elección,jugadas_viejas
        anterior=num40["text"]
        color_anterior=num40["bg"]
        num40.config(text=elección)
        def cerrar_advertencia40(event):
            habilitar_botones()
            num40.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num40.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia40)
        elif num40["bg"]!="#02ac66":
            deshabilitar_botones()
            num40.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia40)
            
        elif [num30["text"],num31["text"],num32["text"],num40["text"],num41["text"],num42["text"],num50["text"],num51["text"],num52["text"]].count(num40["text"])>1:
            deshabilitar_botones()
            num40.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia40)

        elif [num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"]].count(num40["text"])>1:
            deshabilitar_botones()
            num40.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia40)
                    
        elif [num00["text"],num10["text"],num20["text"],num30["text"],num40["text"],num50["text"],num60["text"],num70["text"],num80["text"]].count(num40["text"])>1:
            deshabilitar_botones()
            num40.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia40)
        else:
            jugadas_viejas.meter([num40,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func41():
        global elección,jugadas_viejas
        anterior=num41["text"]
        color_anterior=num41["bg"]
        num41.config(text=elección)
        def cerrar_advertencia41(event):
            habilitar_botones()
            num41.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num41.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia41)
        elif num41["bg"]!="#02ac66":
            deshabilitar_botones()
            num41.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia41)
            
        elif [num30["text"],num31["text"],num32["text"],num40["text"],num41["text"],num42["text"],num50["text"],num51["text"],num52["text"]].count(num41["text"])>1:
            deshabilitar_botones()
            num41.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia41)

        elif [num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"]].count(num41["text"])>1:
            deshabilitar_botones()
            num41.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia41)
                    
        elif [num01["text"],num11["text"],num21["text"],num31["text"],num41["text"],num51["text"],num61["text"],num71["text"],num81["text"]].count(num41["text"])>1:
            deshabilitar_botones()
            num41.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia41)
        else:
            jugadas_viejas.meter([num41,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func42():
        global elección,jugadas_viejas
        anterior=num42["text"]
        color_anterior=num42["bg"]
        num42.config(text=elección)
        def cerrar_advertencia42(event):
            habilitar_botones()
            num42.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num42.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia42)
        elif num42["bg"]!="#02ac66":
            deshabilitar_botones()
            num42.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia42)

        elif [num30["text"],num31["text"],num32["text"],num40["text"],num41["text"],num42["text"],num50["text"],num51["text"],num52["text"]].count(num42["text"])>1:
            deshabilitar_botones()
            num42.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia42)

        elif [num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"]].count(num42["text"])>1:
            deshabilitar_botones()
            num42.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia42)
                    
        elif [num02["text"],num12["text"],num22["text"],num32["text"],num42["text"],num52["text"],num62["text"],num72["text"],num82["text"]].count(num42["text"])>1:
            deshabilitar_botones()
            num42.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia42)
        else:
            jugadas_viejas.meter([num42,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func43():
        global elección,jugadas_viejas
        anterior=num43["text"]
        color_anterior=num43["bg"]
        num43.config(text=elección)
        def cerrar_advertencia43(event):
            habilitar_botones()
            num43.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num43.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia43)
        elif num43["bg"]!="#02ac66":
            deshabilitar_botones()
            num43.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia43)
            
        elif [num33["text"],num34["text"],num35["text"],num43["text"],num44["text"],num45["text"],num53["text"],num54["text"],num55["text"]].count(num43["text"])>1:
            deshabilitar_botones()
            num43.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia43)

        elif [num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"]].count(num43["text"])>1:
            deshabilitar_botones()
            num43.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia43)
                    
        elif [num03["text"],num13["text"],num23["text"],num33["text"],num43["text"],num53["text"],num63["text"],num73["text"],num83["text"]].count(num43["text"])>1:
            deshabilitar_botones()
            num43.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia43)
        else:
            jugadas_viejas.meter([num43,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func44():
        global elección,jugadas_viejas
        anterior=num44["text"]
        color_anterior=num44["bg"]
        num44.config(text=elección)
        def cerrar_advertencia44(event):
            habilitar_botones()
            num44.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num44.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia44)
        elif num44["bg"]!="#02ac66":
            deshabilitar_botones()
            num44.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia44)
            
        elif [num33["text"],num34["text"],num35["text"],num43["text"],num44["text"],num45["text"],num53["text"],num54["text"],num55["text"]].count(num44["text"])>1:
            deshabilitar_botones()
            num44.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia44)

        elif [num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"]].count(num44["text"])>1:
            deshabilitar_botones()
            num44.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia44)
                    
        elif [num04["text"],num14["text"],num24["text"],num34["text"],num44["text"],num54["text"],num64["text"],num74["text"],num84["text"]].count(num44["text"])>1:
            deshabilitar_botones()
            num44.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia44)
        else:
            jugadas_viejas.meter([num44,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func45():
        global elección,jugadas_viejas
        anterior=num45["text"]
        color_anterior=num45["bg"]
        num45.config(text=elección)
        def cerrar_advertencia45(event):
            habilitar_botones()
            num45.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num45.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia45)
        elif num45["bg"]!="#02ac66":
            deshabilitar_botones()
            num45.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia45)

        elif [num33["text"],num34["text"],num35["text"],num43["text"],num44["text"],num45["text"],num53["text"],num54["text"],num55["text"]].count(num45["text"])>1:
            deshabilitar_botones()
            num45.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia45)

        elif [num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"]].count(num45["text"])>1:
            deshabilitar_botones()
            num45.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia45)
                    
        elif [num05["text"],num15["text"],num25["text"],num35["text"],num45["text"],num55["text"],num65["text"],num75["text"],num85["text"]].count(num45["text"])>1:
            deshabilitar_botones()
            num45.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia45)
        else:
            jugadas_viejas.meter([num45,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func46():
        global elección,jugadas_viejas
        anterior=num46["text"]
        color_anterior=num46["bg"]
        num46.config(text=elección)
        def cerrar_advertencia46(event):
            habilitar_botones()
            num46.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num46.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia46)
        elif num46["bg"]!="#02ac66":
            deshabilitar_botones()
            num46.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia46)
            
        elif [num36["text"],num37["text"],num38["text"],num46["text"],num47["text"],num48["text"],num56["text"],num57["text"],num58["text"]].count(num46["text"])>1:
            deshabilitar_botones()
            num46.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia46)

        elif [num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"]].count(num46["text"])>1:
            deshabilitar_botones()
            num46.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia46)
                    
        elif [num06["text"],num16["text"],num26["text"],num36["text"],num46["text"],num56["text"],num66["text"],num76["text"],num86["text"]].count(num46["text"])>1:
            deshabilitar_botones()
            num46.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia46)
        else:
            jugadas_viejas.meter([num46,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func47():
        global elección,jugadas_viejas
        anterior=num47["text"]
        color_anterior=num47["bg"]
        num47.config(text=elección)
        def cerrar_advertencia47(event):
            habilitar_botones()
            num47.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num47.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia47)
        elif num47["bg"]!="#02ac66":
            deshabilitar_botones()
            num47.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia47)
            
        elif [num36["text"],num37["text"],num38["text"],num46["text"],num47["text"],num48["text"],num56["text"],num57["text"],num58["text"]].count(num47["text"])>1:
            deshabilitar_botones()
            num47.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia47)

        elif [num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"]].count(num47["text"])>1:
            deshabilitar_botones()
            num47.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia47)
                    
        elif [num07["text"],num17["text"],num27["text"],num37["text"],num47["text"],num57["text"],num67["text"],num77["text"],num87["text"]].count(num47["text"])>1:
            deshabilitar_botones()
            num47.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia47)
        else:
            jugadas_viejas.meter([num47,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func48():
        global elección,jugadas_viejas
        anterior=num48["text"]
        color_anterior=num48["bg"]
        num48.config(text=elección)
        def cerrar_advertencia48(event):
            habilitar_botones()
            num48.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num48.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia48)
        elif num48["bg"]!="#02ac66":
            deshabilitar_botones()
            num48.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia48)

        elif [num36["text"],num37["text"],num38["text"],num46["text"],num47["text"],num48["text"],num56["text"],num57["text"],num58["text"]].count(num48["text"])>1:
            deshabilitar_botones()
            num48.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia48)

        elif [num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"]].count(num48["text"])>1:
            deshabilitar_botones()
            num48.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia48)
                    
        elif [num08["text"],num18["text"],num28["text"],num38["text"],num48["text"],num58["text"],num68["text"],num78["text"],num88["text"]].count(num48["text"])>1:
            deshabilitar_botones()
            num48.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia48)
        else:
            jugadas_viejas.meter([num48,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func50():
        global elección,jugadas_viejas
        anterior=num50["text"]
        color_anterior=num50["bg"]
        num50.config(text=elección)
        def cerrar_advertencia50(event):
            habilitar_botones()
            num50.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num50.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia50)
        elif num50["bg"]!="#02ac66":
            deshabilitar_botones()
            num50.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia50)

        elif [num30["text"],num31["text"],num32["text"],num40["text"],num41["text"],num42["text"],num50["text"],num51["text"],num52["text"]].count(num50["text"])>1:
            deshabilitar_botones()
            num50.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia50)

        elif [num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"]].count(num50["text"])>1:
            deshabilitar_botones()
            num50.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia50)
                    
        elif [num00["text"],num10["text"],num20["text"],num30["text"],num40["text"],num50["text"],num60["text"],num70["text"],num80["text"]].count(num50["text"])>1:
            deshabilitar_botones()
            num50.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia50)
        else:
            jugadas_viejas.meter([num50,anterior])



        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func51():
        global elección,jugadas_viejas
        anterior=num51["text"]
        color_anterior=num51["bg"]
        num51.config(text=elección)
        def cerrar_advertencia51(event):
            habilitar_botones()
            num51.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num51.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia51)
        elif num51["bg"]!="#02ac66":
            deshabilitar_botones()
            num51.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia51)

        elif [num30["text"],num31["text"],num32["text"],num40["text"],num41["text"],num42["text"],num50["text"],num51["text"],num52["text"]].count(num51["text"])>1:
            deshabilitar_botones()
            num51.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia51)

        elif [num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"]].count(num51["text"])>1:
            deshabilitar_botones()
            num51.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia51)
                    
        elif [num01["text"],num11["text"],num21["text"],num31["text"],num41["text"],num51["text"],num61["text"],num71["text"],num81["text"]].count(num51["text"])>1:
            deshabilitar_botones()
            num51.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia51)
        else:
            jugadas_viejas.meter([num51,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func52():
        global elección,jugadas_viejas
        anterior=num52["text"]
        color_anterior=num52["bg"]
        num52.config(text=elección)
        def cerrar_advertencia52(event):
            habilitar_botones()
            num52.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num52.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia52)
        elif num52["bg"]!="#02ac66":
            deshabilitar_botones()
            num52.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia52)
        elif [num30["text"],num31["text"],num32["text"],num40["text"],num41["text"],num42["text"],num50["text"],num51["text"],num52["text"]].count(num52["text"])>1:
            deshabilitar_botones()
            num52.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia52)

        elif [num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"]].count(num52["text"])>1:
            deshabilitar_botones()
            num52.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia52)
                    
        elif [num02["text"],num12["text"],num22["text"],num32["text"],num42["text"],num52["text"],num62["text"],num72["text"],num82["text"]].count(num52["text"])>1:
            deshabilitar_botones()
            num52.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia52)
        else:
            jugadas_viejas.meter([num52,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
            
    def func53():
        global elección,jugadas_viejas
        anterior=num53["text"]
        color_anterior=num53["bg"]
        num53.config(text=elección)
        def cerrar_advertencia53(event):
            habilitar_botones()
            num53.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num53.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia53)
        elif num53["bg"]!="#02ac66":
            deshabilitar_botones()
            num53.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia53)

        elif [num33["text"],num34["text"],num35["text"],num43["text"],num44["text"],num45["text"],num53["text"],num54["text"],num55["text"]].count(num53["text"])>1:
            deshabilitar_botones()
            num53.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia53)

        elif [num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"]].count(num53["text"])>1:
            deshabilitar_botones()
            num53.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia53)
                    
        elif [num03["text"],num13["text"],num23["text"],num33["text"],num43["text"],num53["text"],num63["text"],num73["text"],num83["text"]].count(num53["text"])>1:
            deshabilitar_botones()
            num53.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia53)
        else:
            jugadas_viejas.meter([num53,anterior])



        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func54():
        global elección,jugadas_viejas
        anterior=num54["text"]
        color_anterior=num54["bg"]
        num54.config(text=elección)
        def cerrar_advertencia54(event):
            habilitar_botones()
            num54.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num54.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia54)
        elif num54["bg"]!="#02ac66":
            deshabilitar_botones()
            num54.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia54)

        elif [num33["text"],num34["text"],num35["text"],num43["text"],num44["text"],num45["text"],num53["text"],num54["text"],num55["text"]].count(num54["text"])>1:
            deshabilitar_botones()
            num54.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia54)

        elif [num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"]].count(num54["text"])>1:
            deshabilitar_botones()
            num54.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia54)
                    
        elif [num04["text"],num14["text"],num24["text"],num34["text"],num44["text"],num54["text"],num64["text"],num74["text"],num84["text"]].count(num54["text"])>1:
            deshabilitar_botones()
            num54.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia54)
        else:
            jugadas_viejas.meter([num54,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func55():
        global elección,jugadas_viejas
        anterior=num55["text"]
        color_anterior=num55["bg"]
        num55.config(text=elección)
        def cerrar_advertencia55(event):
            habilitar_botones()
            num55.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num55.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia55)
        elif num55["bg"]!="#02ac66":
            deshabilitar_botones()
            num55.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia55)
        elif [num33["text"],num34["text"],num35["text"],num43["text"],num44["text"],num45["text"],num53["text"],num54["text"],num55["text"]].count(num55["text"])>1:
            deshabilitar_botones()
            num55.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia55)

        elif [num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"]].count(num55["text"])>1:
            deshabilitar_botones()
            num55.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia55)
                    
        elif [num05["text"],num15["text"],num25["text"],num35["text"],num45["text"],num55["text"],num65["text"],num75["text"],num85["text"]].count(num55["text"])>1:
            deshabilitar_botones()
            num55.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia55)
        else:
            jugadas_viejas.meter([num55,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
            
    def func56():
        global elección,jugadas_viejas
        anterior=num56["text"]
        color_anterior=num56["bg"]
        num56.config(text=elección)
        def cerrar_advertencia56(event):
            habilitar_botones()
            num56.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num56.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia56)
        elif num56["bg"]!="#02ac66":
            deshabilitar_botones()
            num56.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia56)

        elif [num36["text"],num37["text"],num38["text"],num46["text"],num47["text"],num48["text"],num56["text"],num57["text"],num58["text"]].count(num56["text"])>1:
            deshabilitar_botones()
            num56.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia56)

        elif [num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"]].count(num56["text"])>1:
            deshabilitar_botones()
            num56.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia56)
                    
        elif [num06["text"],num16["text"],num26["text"],num36["text"],num46["text"],num56["text"],num66["text"],num76["text"],num86["text"]].count(num56["text"])>1:
            deshabilitar_botones()
            num56.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia56)
        else:
            jugadas_viejas.meter([num56,anterior])



        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func57():
        global elección,jugadas_viejas
        anterior=num57["text"]
        color_anterior=num57["bg"]
        num57.config(text=elección)
        def cerrar_advertencia57(event):
            habilitar_botones()
            num57.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num57.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia57)
        elif num57["bg"]!="#02ac66":
            deshabilitar_botones()
            num57.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia57)

        elif [num36["text"],num37["text"],num38["text"],num46["text"],num47["text"],num48["text"],num56["text"],num57["text"],num58["text"]].count(num57["text"])>1:
            deshabilitar_botones()
            num57.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia57)

        elif [num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"]].count(num57["text"])>1:
            deshabilitar_botones()
            num57.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia57)
                    
        elif [num07["text"],num17["text"],num27["text"],num37["text"],num47["text"],num57["text"],num67["text"],num77["text"],num87["text"]].count(num57["text"])>1:
            deshabilitar_botones()
            num57.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia57)
        else:
            jugadas_viejas.meter([num57,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func58():
        global elección,jugadas_viejas
        anterior=num58["text"]
        color_anterior=num58["bg"]
        num58.config(text=elección)
        def cerrar_advertencia58(event):
            habilitar_botones()
            num58.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num58.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia58)
        elif num58["bg"]!="#02ac66":
            deshabilitar_botones()
            num58.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia58)
        elif [num36["text"],num37["text"],num38["text"],num46["text"],num47["text"],num48["text"],num56["text"],num57["text"],num58["text"]].count(num58["text"])>1:
            deshabilitar_botones()
            num58.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia58)

        elif [num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"]].count(num58["text"])>1:
            deshabilitar_botones()
            num58.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia58)
                    
        elif [num08["text"],num18["text"],num28["text"],num38["text"],num48["text"],num58["text"],num68["text"],num78["text"],num88["text"]].count(num58["text"])>1:
            deshabilitar_botones()
            num58.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia58)
        else:
            jugadas_viejas.meter([num58,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
            
    def func60():
        global elección,jugadas_viejas
        anterior=num60["text"]
        color_anterior=num60["bg"]
        num60.config(text=elección)
        def cerrar_advertencia60(event):
            habilitar_botones()
            num60.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num60.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia60)
        elif num60["bg"]!="#02ac66":
            deshabilitar_botones()
            num60.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia60)
        elif [num60["text"],num61["text"],num62["text"],num70["text"],num71["text"],num72["text"],num80["text"],num81["text"],num82["text"]].count(num60["text"])>1:
            deshabilitar_botones()
            num60.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia60)

        elif [num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"]].count(num60["text"])>1:
            deshabilitar_botones()
            num60.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia60)
                    
        elif [num00["text"],num10["text"],num20["text"],num30["text"],num40["text"],num50["text"],num60["text"],num70["text"],num80["text"]].count(num60["text"])>1:
            deshabilitar_botones()
            num60.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia60)
        else:
            jugadas_viejas.meter([num60,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func61():
        global elección,jugadas_viejas
        anterior=num61["text"]
        color_anterior=num61["bg"]
        num61.config(text=elección)
        def cerrar_advertencia61(event):
            habilitar_botones()
            num61.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num61.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia61)
        elif num61["bg"]!="#02ac66":
            deshabilitar_botones()
            num61.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia61)

        elif [num60["text"],num61["text"],num62["text"],num70["text"],num71["text"],num72["text"],num80["text"],num81["text"],num82["text"]].count(num61["text"])>1:
            deshabilitar_botones()
            num61.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia61)

        elif [num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"]].count(num61["text"])>1:
            deshabilitar_botones()
            num61.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia61)
                    
        elif [num01["text"],num11["text"],num21["text"],num31["text"],num41["text"],num51["text"],num61["text"],num71["text"],num81["text"]].count(num61["text"])>1:
            deshabilitar_botones()
            num61.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia61)
        else:
            jugadas_viejas.meter([num61,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func62():
        global elección,jugadas_viejas
        anterior=num62["text"]
        color_anterior=num62["bg"]
        num62.config(text=elección)
        def cerrar_advertencia62(event):
            habilitar_botones()
            num62.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num62.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia62)
        elif num62["bg"]!="#02ac66":
            deshabilitar_botones()
            num62.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia62)
        elif [num60["text"],num61["text"],num62["text"],num70["text"],num71["text"],num72["text"],num80["text"],num81["text"],num82["text"]].count(num62["text"])>1:
            deshabilitar_botones()
            num62.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia62)


        elif [num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"]].count(num62["text"])>1:
            deshabilitar_botones()
            num62.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia62)
                    
        elif [num02["text"],num12["text"],num22["text"],num32["text"],num42["text"],num52["text"],num62["text"],num72["text"],num82["text"]].count(num62["text"])>1:
            deshabilitar_botones()
            num62.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia62)
        else:
            jugadas_viejas.meter([num62,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func63():
        global elección,jugadas_viejas
        anterior=num63["text"]
        color_anterior=num63["bg"]
        num63.config(text=elección)
        def cerrar_advertencia63(event):
            habilitar_botones()
            num63.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num63.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia63)
        elif num63["bg"]!="#02ac66":
            deshabilitar_botones()
            num63.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia63)
        elif [num63["text"],num64["text"],num65["text"],num73["text"],num74["text"],num75["text"],num83["text"],num84["text"],num85["text"]].count(num63["text"])>1:
            deshabilitar_botones()
            num63.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia63)

        elif [num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"]].count(num63["text"])>1:
            deshabilitar_botones()
            num63.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia63)
                    
        elif [num03["text"],num13["text"],num23["text"],num33["text"],num43["text"],num53["text"],num63["text"],num73["text"],num83["text"]].count(num63["text"])>1:
            deshabilitar_botones()
            num63.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia63)
        else:
            jugadas_viejas.meter([num63,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func64():
        global elección,jugadas_viejas
        anterior=num64["text"]
        color_anterior=num64["bg"]
        num64.config(text=elección)
        def cerrar_advertencia64(event):
            habilitar_botones()
            num64.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num64.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia64)
        elif num64["bg"]!="#02ac66":
            deshabilitar_botones()
            num64.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia64)

        elif [num63["text"],num64["text"],num65["text"],num73["text"],num74["text"],num75["text"],num83["text"],num84["text"],num85["text"]].count(num64["text"])>1:
            deshabilitar_botones()
            num64.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia64)

        elif [num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"]].count(num64["text"])>1:
            deshabilitar_botones()
            num64.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia64)
                    
        elif [num04["text"],num14["text"],num24["text"],num34["text"],num44["text"],num54["text"],num64["text"],num74["text"],num84["text"]].count(num64["text"])>1:
            deshabilitar_botones()
            num64.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia64)
        else:
            jugadas_viejas.meter([num64,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func65():
        global elección,jugadas_viejas
        anterior=num65["text"]
        color_anterior=num65["bg"]
        num65.config(text=elección)
        def cerrar_advertencia65(event):
            habilitar_botones()
            num65.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num65.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia65)
        elif num65["bg"]!="#02ac66":
            deshabilitar_botones()
            num65.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia65)
        elif [num63["text"],num64["text"],num65["text"],num73["text"],num74["text"],num75["text"],num83["text"],num84["text"],num85["text"]].count(num65["text"])>1:
            deshabilitar_botones()
            num65.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia65)


        elif [num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"]].count(num65["text"])>1:
            deshabilitar_botones()
            num65.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia65)
                    
        elif [num05["text"],num15["text"],num25["text"],num35["text"],num45["text"],num55["text"],num65["text"],num75["text"],num85["text"]].count(num65["text"])>1:
            deshabilitar_botones()
            num65.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia65)
        else:
            jugadas_viejas.meter([num65,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func66():
        global elección,jugadas_viejas
        anterior=num66["text"]
        color_anterior=num66["bg"]
        num66.config(text=elección)
        def cerrar_advertencia66(event):
            habilitar_botones()
            num66.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num66.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia66)
        elif num66["bg"]!="#02ac66":
            deshabilitar_botones()
            num66.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia66)
        elif [num66["text"],num67["text"],num68["text"],num76["text"],num77["text"],num78["text"],num86["text"],num87["text"],num88["text"]].count(num66["text"])>1:
            deshabilitar_botones()
            num66.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia66)

        elif [num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"]].count(num66["text"])>1:
            deshabilitar_botones()
            num66.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia66)
                    
        elif [num06["text"],num16["text"],num26["text"],num36["text"],num46["text"],num56["text"],num66["text"],num76["text"],num86["text"]].count(num66["text"])>1:
            deshabilitar_botones()
            num66.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia66)
        else:
            jugadas_viejas.meter([num66,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func67():
        global elección,jugadas_viejas
        anterior=num67["text"]
        color_anterior=num67["bg"]
        num67.config(text=elección)
        def cerrar_advertencia67(event):
            habilitar_botones()
            num67.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num67.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia67)
        elif num67["bg"]!="#02ac66":
            deshabilitar_botones()
            num67.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia67)

        elif [num66["text"],num67["text"],num68["text"],num76["text"],num77["text"],num78["text"],num86["text"],num87["text"],num88["text"]].count(num67["text"])>1:
            deshabilitar_botones()
            num67.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia67)

        elif [num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"]].count(num67["text"])>1:
            deshabilitar_botones()
            num67.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia67)
                    
        elif [num07["text"],num17["text"],num27["text"],num37["text"],num47["text"],num57["text"],num67["text"],num77["text"],num87["text"]].count(num67["text"])>1:
            deshabilitar_botones()
            num67.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia67)
        else:
            jugadas_viejas.meter([num67,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func68():
        global elección,jugadas_viejas
        anterior=num68["text"]
        color_anterior=num68["bg"]
        num68.config(text=elección)
        def cerrar_advertencia68(event):
            habilitar_botones()
            num68.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num68.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia68)
        elif num68["bg"]!="#02ac66":
            deshabilitar_botones()
            num68.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia68)
        elif [num66["text"],num67["text"],num68["text"],num76["text"],num77["text"],num78["text"],num86["text"],num87["text"],num88["text"]].count(num68["text"])>1:
            deshabilitar_botones()
            num68.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia68)


        elif [num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"]].count(num68["text"])>1:
            deshabilitar_botones()
            num68.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia68)
                    
        elif [num08["text"],num18["text"],num28["text"],num38["text"],num48["text"],num58["text"],num68["text"],num78["text"],num88["text"]].count(num68["text"])>1:
            deshabilitar_botones()
            num68.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia68)
        else:
            jugadas_viejas.meter([num68,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func70():
        global elección,jugadas_viejas
        anterior=num70["text"]
        color_anterior=num70["bg"]
        num70.config(text=elección)
        def cerrar_advertencia70(event):
            habilitar_botones()
            num70.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num70.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia70)
        elif num70["bg"]!="#02ac66":
            deshabilitar_botones()
            num70.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia70)
            
        elif [num60["text"],num61["text"],num62["text"],num70["text"],num71["text"],num72["text"],num80["text"],num81["text"],num82["text"]].count(num70["text"])>1:
            deshabilitar_botones()
            num70.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia70)

        elif [num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"]].count(num70["text"])>1:
            deshabilitar_botones()
            num70.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia70)
                    
        elif [num00["text"],num10["text"],num20["text"],num30["text"],num40["text"],num50["text"],num60["text"],num70["text"],num80["text"]].count(num70["text"])>1:
            deshabilitar_botones()
            num70.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia70)
        else:
            jugadas_viejas.meter([num70,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func71():
        global elección,jugadas_viejas
        anterior=num71["text"]
        color_anterior=num71["bg"]
        num71.config(text=elección)
        def cerrar_advertencia71(event):
            habilitar_botones()
            num71.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num71.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia71)
        elif num71["bg"]!="#02ac66":
            deshabilitar_botones()
            num71.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia71)
            
        elif [num60["text"],num61["text"],num62["text"],num70["text"],num71["text"],num72["text"],num80["text"],num81["text"],num82["text"]].count(num71["text"])>1:
            deshabilitar_botones()
            num71.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia71)

        elif [num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"]].count(num71["text"])>1:
            deshabilitar_botones()
            num71.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia71)
                    
        elif [num01["text"],num11["text"],num21["text"],num31["text"],num41["text"],num51["text"],num61["text"],num71["text"],num81["text"]].count(num71["text"])>1:
            deshabilitar_botones()
            num71.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia71)
        else:
            jugadas_viejas.meter([num71,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func72():
        global elección,jugadas_viejas
        anterior=num72["text"]
        color_anterior=num72["bg"]
        num72.config(text=elección)
        def cerrar_advertencia72(event):
            habilitar_botones()
            num72.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num72.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia72)
        elif num72["bg"]!="#02ac66":
            deshabilitar_botones()
            num72.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia72)

        elif [num60["text"],num61["text"],num62["text"],num70["text"],num71["text"],num72["text"],num80["text"],num81["text"],num82["text"]].count(num72["text"])>1:
            deshabilitar_botones()
            num72.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia72)

        elif [num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"]].count(num72["text"])>1:
            deshabilitar_botones()
            num72.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia72)
                    
        elif [num02["text"],num12["text"],num22["text"],num32["text"],num42["text"],num52["text"],num62["text"],num72["text"],num82["text"]].count(num72["text"])>1:
            deshabilitar_botones()
            num72.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia72)
        else:
            jugadas_viejas.meter([num72,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func73():
        global elección,jugadas_viejas
        anterior=num73["text"]
        color_anterior=num73["bg"]
        num73.config(text=elección)
        def cerrar_advertencia73(event):
            habilitar_botones()
            num73.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num73.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia73)
        elif num73["bg"]!="#02ac66":
            deshabilitar_botones()
            num73.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia73)
            
        elif [num63["text"],num64["text"],num65["text"],num73["text"],num74["text"],num75["text"],num83["text"],num84["text"],num85["text"]].count(num73["text"])>1:
            deshabilitar_botones()
            num73.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia73)

        elif [num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"]].count(num73["text"])>1:
            deshabilitar_botones()
            num73.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia73)
                    
        elif [num03["text"],num13["text"],num23["text"],num33["text"],num43["text"],num53["text"],num63["text"],num73["text"],num83["text"]].count(num73["text"])>1:
            deshabilitar_botones()
            num73.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia73)
        else:
            jugadas_viejas.meter([num73,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func74():
        global elección,jugadas_viejas
        anterior=num74["text"]
        color_anterior=num74["bg"]
        num74.config(text=elección)
        def cerrar_advertencia74(event):
            habilitar_botones()
            num74.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num74.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia74)
        elif num74["bg"]!="#02ac66":
            deshabilitar_botones()
            num74.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia74)
            
        elif [num63["text"],num64["text"],num65["text"],num73["text"],num74["text"],num75["text"],num83["text"],num84["text"],num85["text"]].count(num74["text"])>1:
            deshabilitar_botones()
            num74.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia74)

        elif [num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"]].count(num74["text"])>1:
            deshabilitar_botones()
            num74.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia74)
                    
        elif [num04["text"],num14["text"],num24["text"],num34["text"],num44["text"],num54["text"],num64["text"],num74["text"],num84["text"]].count(num74["text"])>1:
            deshabilitar_botones()
            num74.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia74)
        else:
            jugadas_viejas.meter([num74,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func75():
        global elección,jugadas_viejas
        anterior=num75["text"]
        color_anterior=num75["bg"]
        num75.config(text=elección)
        def cerrar_advertencia75(event):
            habilitar_botones()
            num75.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num75.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia75)
        elif num75["bg"]!="#02ac66":
            deshabilitar_botones()
            num75.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia75)

        elif [num63["text"],num64["text"],num65["text"],num73["text"],num74["text"],num75["text"],num83["text"],num84["text"],num85["text"]].count(num75["text"])>1:
            deshabilitar_botones()
            num75.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia75)

        elif [num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"]].count(num75["text"])>1:
            deshabilitar_botones()
            num75.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia75)
                    
        elif [num05["text"],num15["text"],num25["text"],num35["text"],num45["text"],num55["text"],num65["text"],num75["text"],num85["text"]].count(num75["text"])>1:
            deshabilitar_botones()
            num75.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia75)
        else:
            jugadas_viejas.meter([num75,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func76():
        global elección,jugadas_viejas
        anterior=num76["text"]
        color_anterior=num76["bg"]
        num76.config(text=elección)
        def cerrar_advertencia76(event):
            habilitar_botones()
            num76.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num76.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia76)
        elif num76["bg"]!="#02ac66":
            deshabilitar_botones()
            num76.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia76)
            
        elif [num66["text"],num67["text"],num68["text"],num76["text"],num77["text"],num78["text"],num86["text"],num87["text"],num88["text"]].count(num76["text"])>1:
            deshabilitar_botones()
            num76.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia76)

        elif [num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"]].count(num76["text"])>1:
            deshabilitar_botones()
            num76.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia76)
                    
        elif [num06["text"],num16["text"],num26["text"],num36["text"],num46["text"],num56["text"],num66["text"],num76["text"],num86["text"]].count(num76["text"])>1:
            deshabilitar_botones()
            num76.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia76)
        else:
            jugadas_viejas.meter([num76,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func77():
        global elección,jugadas_viejas
        anterior=num77["text"]
        color_anterior=num77["bg"]
        num77.config(text=elección)
        def cerrar_advertencia77(event):
            habilitar_botones()
            num77.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num77.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia77)
        elif num77["bg"]!="#02ac66":
            deshabilitar_botones()
            num77.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia77)
            
        elif [num66["text"],num67["text"],num68["text"],num76["text"],num77["text"],num78["text"],num86["text"],num87["text"],num88["text"]].count(num77["text"])>1:
            deshabilitar_botones()
            num77.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia77)

        elif [num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"]].count(num77["text"])>1:
            deshabilitar_botones()
            num77.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia77)
                    
        elif [num07["text"],num17["text"],num27["text"],num37["text"],num47["text"],num57["text"],num67["text"],num77["text"],num87["text"]].count(num77["text"])>1:
            deshabilitar_botones()
            num77.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia77)
        else:
            jugadas_viejas.meter([num77,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func78():
        global elección,jugadas_viejas
        anterior=num78["text"]
        color_anterior=num78["bg"]
        num78.config(text=elección)
        def cerrar_advertencia78(event):
            habilitar_botones()
            num78.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num78.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia78)
        elif num78["bg"]!="#02ac66":
            deshabilitar_botones()
            num78.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia78)

        elif [num66["text"],num67["text"],num68["text"],num76["text"],num77["text"],num78["text"],num86["text"],num87["text"],num88["text"]].count(num78["text"])>1:
            deshabilitar_botones()
            num78.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia78)

        elif [num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"]].count(num78["text"])>1:
            deshabilitar_botones()
            num78.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia78)
                    
        elif [num08["text"],num18["text"],num28["text"],num38["text"],num48["text"],num58["text"],num68["text"],num78["text"],num88["text"]].count(num78["text"])>1:
            deshabilitar_botones()
            num78.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia78)
        else:
            jugadas_viejas.meter([num78,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func80():
        global elección,jugadas_viejas
        anterior=num80["text"]
        color_anterior=num80["bg"]
        num80.config(text=elección)
        def cerrar_advertencia80(event):
            habilitar_botones()
            num80.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num80.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia80)
        elif num80["bg"]!="#02ac66":
            deshabilitar_botones()
            num80.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia80)

        elif [num60["text"],num61["text"],num62["text"],num70["text"],num71["text"],num72["text"],num80["text"],num81["text"],num82["text"]].count(num80["text"])>1:
            deshabilitar_botones()
            num80.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia80)

        elif [num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count(num80["text"])>1:
            deshabilitar_botones()
            num80.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia80)
                    
        elif [num00["text"],num10["text"],num20["text"],num30["text"],num40["text"],num50["text"],num60["text"],num70["text"],num80["text"]].count(num80["text"])>1:
            deshabilitar_botones()
            num80.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia80)
        else:
            jugadas_viejas.meter([num80,anterior])



        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func81():
        global elección,jugadas_viejas
        anterior=num81["text"]
        color_anterior=num81["bg"]
        num81.config(text=elección)
        def cerrar_advertencia81(event):
            habilitar_botones()
            num81.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num81.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia81)
        elif num81["bg"]!="#02ac66":
            deshabilitar_botones()
            num81.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia81)

        elif [num60["text"],num61["text"],num62["text"],num70["text"],num71["text"],num72["text"],num80["text"],num81["text"],num82["text"]].count(num81["text"])>1:
            deshabilitar_botones()
            num81.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia81)

        elif [num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count(num81["text"])>1:
            deshabilitar_botones()
            num81.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia81)
                    
        elif [num01["text"],num11["text"],num21["text"],num31["text"],num41["text"],num51["text"],num61["text"],num71["text"],num81["text"]].count(num81["text"])>1:
            deshabilitar_botones()
            num81.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia81)
        else:
            jugadas_viejas.meter([num81,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func82():
        global elección,jugadas_viejas
        anterior=num82["text"]
        color_anterior=num82["bg"]
        num82.config(text=elección)
        def cerrar_advertencia82(event):
            habilitar_botones()
            num82.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num82.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia82)
        elif num82["bg"]!="#02ac66":
            deshabilitar_botones()
            num82.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia82)
        elif [num60["text"],num61["text"],num62["text"],num70["text"],num71["text"],num72["text"],num80["text"],num81["text"],num82["text"]].count(num82["text"])>1:
            deshabilitar_botones()
            num82.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia82)

        elif [num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count(num82["text"])>1:
            deshabilitar_botones()
            num82.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia82)
                    
        elif [num02["text"],num12["text"],num22["text"],num32["text"],num42["text"],num52["text"],num62["text"],num72["text"],num82["text"]].count(num82["text"])>1:
            deshabilitar_botones()
            num82.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia82)
        else:
            jugadas_viejas.meter([num82,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
            
    def func83():
        global elección,jugadas_viejas
        anterior=num83["text"]
        color_anterior=num83["bg"]
        num83.config(text=elección)
        def cerrar_advertencia83(event):
            habilitar_botones()
            num83.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num83.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia83)
        elif num83["bg"]!="#02ac66":
            deshabilitar_botones()
            num83.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia83)

        elif [num63["text"],num64["text"],num65["text"],num73["text"],num74["text"],num75["text"],num83["text"],num84["text"],num85["text"]].count(num83["text"])>1:
            deshabilitar_botones()
            num83.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia83)

        elif [num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count(num83["text"])>1:
            deshabilitar_botones()
            num83.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia83)
                    
        elif [num03["text"],num13["text"],num23["text"],num33["text"],num43["text"],num53["text"],num63["text"],num73["text"],num83["text"]].count(num83["text"])>1:
            deshabilitar_botones()
            num83.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia83)
        else:
            jugadas_viejas.meter([num83,anterior])



        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func84():
        global elección,jugadas_viejas
        anterior=num84["text"]
        color_anterior=num84["bg"]
        num84.config(text=elección)
        def cerrar_advertencia84(event):
            habilitar_botones()
            num84.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num84.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia84)
        elif num84["bg"]!="#02ac66":
            deshabilitar_botones()
            num84.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia84)

        elif [num63["text"],num64["text"],num65["text"],num73["text"],num74["text"],num75["text"],num83["text"],num84["text"],num85["text"]].count(num84["text"])>1:
            deshabilitar_botones()
            num84.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia84)

        elif [num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count(num84["text"])>1:
            deshabilitar_botones()
            num84.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia84)
                    
        elif [num04["text"],num14["text"],num24["text"],num34["text"],num44["text"],num54["text"],num64["text"],num74["text"],num84["text"]].count(num84["text"])>1:
            deshabilitar_botones()
            num84.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia84)
        else:
            jugadas_viejas.meter([num84,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func85():
        global elección,jugadas_viejas
        anterior=num85["text"]
        color_anterior=num85["bg"]
        num85.config(text=elección)
        def cerrar_advertencia85(event):
            habilitar_botones()
            num85.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num85.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia85)
        elif num85["bg"]!="#02ac66":
            deshabilitar_botones()
            num85.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia85)
        elif [num63["text"],num64["text"],num65["text"],num73["text"],num74["text"],num75["text"],num83["text"],num84["text"],num85["text"]].count(num85["text"])>1:
            deshabilitar_botones()
            num85.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia85)

        elif [num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count(num85["text"])>1:
            deshabilitar_botones()
            num85.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia85)
                    
        elif [num05["text"],num15["text"],num25["text"],num35["text"],num45["text"],num55["text"],num65["text"],num75["text"],num85["text"]].count(num85["text"])>1:
            deshabilitar_botones()
            num85.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia85)
        else:
            jugadas_viejas.meter([num85,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
            
    def func86():
        global elección,jugadas_viejas
        anterior=num86["text"]
        color_anterior=num86["bg"]
        num86.config(text=elección)
        def cerrar_advertencia86(event):
            habilitar_botones()
            num86.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num86.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia86)
        elif num86["bg"]!="#02ac66":
            deshabilitar_botones()
            num86.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia86)

        elif [num66["text"],num67["text"],num68["text"],num76["text"],num77["text"],num78["text"],num86["text"],num87["text"],num88["text"]].count(num86["text"])>1:
            deshabilitar_botones()
            num86.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia86)

        elif [num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count(num86["text"])>1:
            deshabilitar_botones()
            num86.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia86)
                    
        elif [num06["text"],num16["text"],num26["text"],num36["text"],num46["text"],num56["text"],num66["text"],num76["text"],num86["text"]].count(num86["text"])>1:
            deshabilitar_botones()
            num86.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia86)
        else:
            jugadas_viejas.meter([num86,anterior])



        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func87():
        global elección,jugadas_viejas
        anterior=num87["text"]
        color_anterior=num87["bg"]
        num87.config(text=elección)
        def cerrar_advertencia87(event):
            habilitar_botones()
            num87.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num87.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia87)
        elif num87["bg"]!="#02ac66":
            deshabilitar_botones()
            num87.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia87)

        elif [num66["text"],num67["text"],num68["text"],num76["text"],num77["text"],num78["text"],num86["text"],num87["text"],num88["text"]].count(num87["text"])>1:
            deshabilitar_botones()
            num87.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia87)

        elif [num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count(num87["text"])>1:
            deshabilitar_botones()
            num87.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia87)
                    
        elif [num07["text"],num17["text"],num27["text"],num37["text"],num47["text"],num57["text"],num67["text"],num77["text"],num87["text"]].count(num87["text"])>1:
            deshabilitar_botones()
            num87.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia87)
        else:
            jugadas_viejas.meter([num87,anterior])


        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()
    def func88():
        global elección,jugadas_viejas
        anterior=num88["text"]
        color_anterior=num88["bg"]
        num88.config(text=elección)
        def cerrar_advertencia88(event):
            habilitar_botones()
            num88.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
        if elección=="":
                deshabilitar_botones()
                num88.config(bg="red")
                lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
                lbl_advertencia_1.config(text="Jugada no es válida porque no ha  ya\n seleccionado ningún elemento")
                lbl_advertencia_1.place(x=370,y=450)
                ventana_principal_juego.bind("<Return>", cerrar_advertencia88)
        elif num88["bg"]!="#02ac66":
            deshabilitar_botones()
            num88.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia88)
        elif [num66["text"],num67["text"],num68["text"],num76["text"],num77["text"],num78["text"],num86["text"],num87["text"],num88["text"]].count(num88["text"])>1:
            deshabilitar_botones()
            num88.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia88)

        elif [num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count(num88["text"])>1:
            deshabilitar_botones()
            num88.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia88)
                    
        elif [num08["text"],num18["text"],num28["text"],num38["text"],num48["text"],num58["text"],num68["text"],num78["text"],num88["text"]].count(num88["text"])>1:
            deshabilitar_botones()
            num88.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia88)
        else:
            jugadas_viejas.meter([num88,anterior])

        if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
            ganó()





    num00.config(command=func00)
    num01.config(command=func01)
    num02.config(command=func02)
    num03.config(command=func03)
    num04.config(command=func04)
    num05.config(command=func05)
    num06.config(command=func06)
    num07.config(command=func07)
    num08.config(command=func08)
    num10.config(command=func10)
    num11.config(command=func11)
    num12.config(command=func12)
    num13.config(command=func13)
    num14.config(command=func14)
    num15.config(command=func15)
    num16.config(command=func16)
    num17.config(command=func17)
    num18.config(command=func18)
    num20.config(command=func20)
    num21.config(command=func21)
    num22.config(command=func22)
    num23.config(command=func23)
    num24.config(command=func24)
    num25.config(command=func25)
    num26.config(command=func26)
    num27.config(command=func27)
    num28.config(command=func28)
    num30.config(command=func30)
    num31.config(command=func31)
    num32.config(command=func32)
    num33.config(command=func33)
    num34.config(command=func34)
    num35.config(command=func35)
    num36.config(command=func36)
    num37.config(command=func37)
    num38.config(command=func38)
    num40.config(command=func40)
    num41.config(command=func41)
    num42.config(command=func42)
    num43.config(command=func43)
    num44.config(command=func44)
    num45.config(command=func45)
    num46.config(command=func46)
    num47.config(command=func47)
    num48.config(command=func48)
    num50.config(command=func50)
    num51.config(command=func51)
    num52.config(command=func52)
    num53.config(command=func53)
    num54.config(command=func54)
    num55.config(command=func55)
    num56.config(command=func56)
    num57.config(command=func57)
    num58.config(command=func58)
    num60.config(command=func60)
    num61.config(command=func61)
    num62.config(command=func62)
    num63.config(command=func63)
    num64.config(command=func64)
    num65.config(command=func65)
    num66.config(command=func66)
    num67.config(command=func67)
    num68.config(command=func68)
    num70.config(command=func70)
    num71.config(command=func71)
    num72.config(command=func72)
    num73.config(command=func73)
    num74.config(command=func74)
    num75.config(command=func75)
    num76.config(command=func76)
    num77.config(command=func77)
    num78.config(command=func78)
    num80.config(command=func80)
    num81.config(command=func81)
    num82.config(command=func82)
    num83.config(command=func83)
    num84.config(command=func84)
    num85.config(command=func85)
    num86.config(command=func86)
    num87.config(command=func87)
    num88.config(command=func88)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def ganó():
        global top_jugadores,reloj,jugando
        jugando=False
        messagebox.showinfo(message="Logró completar el juego", title="Felicidades!")
        if configu["reloj"]==1:
            configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
            configu=pickle.load(configuración_de_archivo) 
            configuración_de_archivo.close()
            configuración_de_archivo=open("archivos\\documentos\\sudoku2021topx.dat","rb")
            top_viejo=pickle.load(configuración_de_archivo) 
            configuración_de_archivo.close()
            if configu["dificultad"]==0:
                fácilTop.meter(entryNombre.get(),reloj)
            if configu["dificultad"]==1:
                intermedioTop.meter(entryNombre.get(),reloj)
            if configu["dificultad"]==2:
                difícilTop.meter(entryNombre.get(),reloj)
            lista_final=[list(fácilTop.concatenar(top_viejo[0])),list(intermedioTop.concatenar(top_viejo[1])),list(difícilTop.concatenar(top_viejo[2]))]
            partidas_iniciales=open("archivos\\documentos\\sudoku2021topx.dat","wb")
            pickle.dump(lista_final,partidas_iniciales)                    
            partidas_iniciales.close()
            
            sudoku2021topx
        else:
            ventana_principal_juego.destroy()
            jugar()
        return
    def convertir(n):
        horas_convertir = n // 3600
        minutos_convertir = n % 3600 // 60
        segundos_convertir = n % 3600 % 60
        if minutos_convertir < 10:
            minutos_convertir = '0' + str(minutos_convertir)
        else:
            minutos_convertir = str(minutos_convertir)

        if segundos_convertir < 10:
            segundos_convertir = '0' + str(segundos_convertir)
        else:
            segundos_convertir = str(segundos_convertir)
        return str(horas_convertir) + ":" + minutos_convertir + ":" + str(segundos_convertir)
    configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
    configu=pickle.load(configuración_de_archivo) 
    configuración_de_archivo.close()
    if configu["reloj"]==3:
        lblhoras = tk.Label(ventana_principal_juego, bg="#8c004b", font=("Century", 16),text="Horas:")
        lblhoras.place(x=470, y=0)
        lblminutos = tk.Label(ventana_principal_juego, bg="#8c004b", font=("Century", 16),text="Minutos:")
        lblminutos.place(x=470, y=30)
        lblsegundos = tk.Label(ventana_principal_juego, bg="#8c004b", font=("Century", 16),text="Segundos:")
        lblsegundos.place(x=470, y=60)
        entryhoras = tk.Entry(ventana_principal_juego, bg="#8c004b", font=("Century", 16))
        entryhoras.place(x=575, y=0)
        entryminutos = tk.Entry(ventana_principal_juego, bg="#8c004b", font=("Century", 16))
        entryminutos.place(x=575, y=30)
        entrysegundos = tk.Entry(ventana_principal_juego, bg="#8c004b", font=("Century", 16))
        entrysegundos.place(x=575,y=60)
        def actualiza_reloj():
            global temporizador,tiempo_expirado
            try:
                configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
                configu=pickle.load(configuración_de_archivo) 
                configuración_de_archivo.close()
                configu["horas"]=int(entryhoras.get())
                configu["minutos"]=int(entryminutos.get())
                configu["segundos"]=int(entrysegundos.get())
                tiempo_expirado=int(entryhoras.get())*3600+int(entryminutos.get())*60+int(entrysegundos.get())
                configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","wb")
                pickle.dump(configu,configuración_de_archivo)
                configuración_de_archivo.close()
                
                temporizador = int(entryhoras.get())*3600+int(entryminutos.get())*60+int(entrysegundos.get())
                
            except ValueError:
                messagebox.showerror("Error", "Los números de entrada deben ser enteros")
                
        btnActualizar = tk.Button(ventana_principal_juego, text="Actualizar reloj",
                                  bg="#6ae997", fg="black",
                                  font=("Century", 12),
                                  activebackground="#a4e647",
                                  activeforeground="black",
                                  command=actualiza_reloj)
        btnActualizar.place(x=475, y=100)
    # Dibuja el reloj en la pantalla
    if cargando:
        configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
        configu=pickle.load(configuración_de_archivo) 
        configuración_de_archivo.close()
        if configu["reloj"] == 1:
            reloj=guardado[3]
        if configu["reloj"] == 3:
            temporizador=guardado[3]
            
    def tic():
        global reloj, temporizador, configuración_reloj
        configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
        configu=pickle.load(configuración_de_archivo) 
        configuración_de_archivo.close()
        if configu["reloj"] == 1:
            lblClock['text'] = convertir(reloj)
        if configu["reloj"] == 3:
            lblTimer['text'] = convertir(temporizador)

    # Llama solo una vez al reloj
    tic()

    # Actualiza el cronometro
    def tac():
        global reloj, configuración_reloj, jugando
        # Sigue dibujando para estar actualizando el reloj
        tic()
        lblTimer.after(1000, tac)
        configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
        configu=pickle.load(configuración_de_archivo) 
        configuración_de_archivo.close()
        # Cada 1000 milisegundos llama a la funcion tac (after)
        if configu["reloj"] == 1 and jugando:
            reloj += 1

    def run_timer():
        global temporizador, configuración_reloj, jugando,tiempo_expirado,reloj
        # Sigue dibujando para estar actualizando el reloj
        tic()
        # Cada 1000 milisegundos llama a la funcion run timer (after)
        lblTimer.after(1000, run_timer)
        configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
        configu=pickle.load(configuración_de_archivo) 
        configuración_de_archivo.close()
        if temporizador==0 and configu["reloj"]==3 and jugando:
            jugando=False
            if messagebox.askyesno(message="¿Desea continuar con el mismo juego (sí o no)?", title="Tiempo expirado."):
                configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
                configu=pickle.load(configuración_de_archivo) 
                configuración_de_archivo.close()
                lblTimer.config(text="")
                reloj=tiempo_expirado
                configu["reloj"]=1
                partidas_iniciales=open("archivos\\documentos\\sudoku2021configuración.dat","wb")
                pickle.dump(configu,partidas_iniciales)                    
                partidas_iniciales.close()
                jugando=True
            else:
                ventana_principal_juego.destroy()
                jugar()
                    
        if configu["reloj"] == 3 and jugando:
            temporizador -= 1

    # Llama a tac una vez para que aparezca en pantalla
    tac()
    run_timer()

    # Dibuja la matriz
    def draw(cuadrícula, matriz):
        for x in range(9):
            for y in range(9):
                # Si la matriz tiene un numero
                if (matriz[y][x]) != "":
                    # Se modifica la matriz  y se coloca ese nuemro con el color respectivo
                    cuadrícula[x][y].config(text=str(matriz[y][x]), bg="#8c004b")
                else:
                    # Si la matriz tiene un cero, no se coloca un numero y se deja el fondo del mismo color
                    cuadrícula[x][y].config(bg="#02ac66")
                # Acomoda los labels segun la cuadricula
                cuadrícula[x][y].grid(column=x, row=y)
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Funciones de los botones 

    def iniciarPartida():
        global grid, tablero, jugando, nombre_jugador, reloj, temporizador,guardado, configuración_reloj,dificultad,partida,cargando,cuadrí_cargando #globales
        global horas, minutos, segundos, jugadas_viejas,guardado,cargando #globales
        configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
        configu=pickle.load(configuración_de_archivo) 
        configuración_de_archivo.close()
        jugando = False #flag
        reloj = 0 # define la variable de reloj
        temporizador = configu["horas"] * 3600 + configu["minutos"]* 60 + configu["segundos"] #contiene la cantidad de los tiempos  
        # Inicia la matriz con numeros del diccionario deseado
        partidas_iniciales=open("archivos\\documentos\\sudoku2021partidas.dat","rb") #abre el archivo 
        lista_diccionarios_partidas=pickle.load(partidas_iniciales) #lee varios archivos
        partidas_iniciales.close() #cierra el archivo que estaba abierto
        #variables con cada nivel
        diccionario_fácil=lista_diccionarios_partidas[0]
        diccionario_intermedio=lista_diccionarios_partidas[1]
        diccionario_difícil=lista_diccionarios_partidas[2]
        if not cargando:
            if dificultad.get()==0:
                partida=random.randint(0,len(diccionario_fácil)-1)
            elif dificultad.get()==1:
                partida=random.randint(0,len(diccionario_fácil)-1)
            elif dificultad.get()==2:
                partida=random.randint(0,len(diccionario_fácil)-1)
                
        escoger_partida(partida)
        
        if cargando:
            for fila in range(len(tablero)):
                for columna in range(len(tablero[fila])):
                    tablero[fila][columna]=guardado[0][fila][columna]
        # Dibuja la matriz
        draw(grid, tablero)
        deshabilitar_botones()

        btnIniciarPartida.config(text="INICIAR \n  PARTIDA  ")
        #  Se habilita nuevamente el espacio para escribir el nombre
        entryNombre.config(state='normal')
        # Limpiar el entry, end=constante que va desde el inicio hasta el final
        if cargando:
            entryNombre.insert(0,guardado[3])
        
    def iniciar_juego():
        #inicia partida si se escribe el nombre
        global jugando, jugadas_viejas,jugadas_nuevas,playreloj
        playreloj=True
        nombre_jugador = entryNombre.get() #recupera el valor del diccionario
        if nombre_jugador == "":
            # Envia mensaje de error si no se introduce el nombre
            messagebox.showerror("Nombre no asignado",
                                 "Debe ingresar el nombre del jugador antes de iniciar la partida")
        elif len(nombre_jugador) > 30:
            # Si el nombre ingresado es mayor a 30  retorna error
            messagebox.showerror("Nombre invalido", "El nombre del jugador debe contener máximo 30 caracteres")
        else:
            # State: cambia el estado del boton
            # Disable : desabilita la ventana
            jugando=True
            entryNombre.config(state='disabled')
            btnIniciarPartida.config(state="disabled")
            configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
            configu=pickle.load(configuración_de_archivo) 
            configuración_de_archivo.close()
            if configu["reloj"]==3:

                entryhoras.config(state="disabled")
                entryminutos.config(state="disabled")
                entrysegundos.config(state="disabled")
                btnActualizar.config(state="disabled")
            habilitar_botones() #habilita los botones
            jugadas_viejas.elementos=[]
            jugadas_nuevas.elementos=[]
            if not guardado==[]:
                jugadas_viejas.elementos=guardado[5]
                jugadas_nuevas.elementos=guardado[6]
        return
    
    def deshacer_jugada():
        global jugando,jugadas_viejas,jugadas_nuevas
        if jugando:
            if len(jugadas_viejas.elementos)==0:
                messagebox.showerror("Botón no válido", "No hay jugadas para deshacer") #envia mensaje de error si no hay ningun movimiento por dehacer
            else:
                cambio=jugadas_viejas.sacar() #elimina las jugadas viejas
                jugadas_nuevas.meter([cambio[0],cambio[0]["text"]]) #introduce las nuevas
                cambio[0].config(text=cambio[1])
        else:
            messagebox.showerror("Botón no válido", "Juego no se ha iniciado.") #envia mensaje de error si no se ha iniciado una partida 

    def rehacer_jugada():
        global jugando,jugadas_viejas,jugadas_nuevas
        if jugando:
            if len(jugadas_nuevas.elementos)==0:
                messagebox.showerror("Botón no válido", "No hay jugadas para rehacer") #envia mensaje de error si no hay ningun movimiento que se pueda rehacer
            else:
                cambio=jugadas_nuevas.sacar()
                jugadas_viejas.meter([cambio[0],cambio[0]["text"]])
                cambio[0].config(text=cambio[1])
        else:
            messagebox.showerror("Botón no válido", "Juego no se ha iniciado.") #envia mensaje de error si no se ha iniciado una partida

    def cargar_juego():
        global jugando, reloj, temporizador, configuración_reloj,tablero,grid,partida,cuadrí_cargando,config,guardado
        if jugando:
            messagebox.showerror("Botón no válido", "Juego ya se ha iniciado.")
        else:
            configuración_de_archivo=open("archivos\\documentos\\sudoku2021juegoactual.dat","rb")
            guardado=pickle.load(configuración_de_archivo)
            configuración_de_archivo.close()
            config=guardado[2]
            partidas_iniciales=open("archivos\\documentos\\sudoku2021configuración.dat","wb")
            pickle.dump(guardado[2],partidas_iniciales)                    
            partidas_iniciales.close()

            ventana_principal_juego.destroy() #elimina el juego si indica que si
            cargando=True
            jugar()
            config=guardado[2]               
            partida=guardado[1]
            cuadrí_cargando=guardado[0]
            colores=guardado[4]
            colores=invertir(colores)
            cargando=False
            jugando=False
            cuadrí_cargando=guardado[0]
            cuadrí_cargando=invertir(cuadrí_cargando)
            playreloj=True
            for x in range(len(grid)):
                for y in range(len(grid)):
                    grid[y][x].config(text=cuadrí_cargando[x][y])
                    grid[y][x].config(bg=colores[x][y])
                    
            
        return
    def guardar_juego():
        global jugando,partida
        if not jugando:
            messagebox.showerror("Botón no válido", "Juego no se ha iniciado.")
        else:
            configuración_de_archivo=open("archivos\\documentos\\sudoku2021juegoactual.dat","wb")
            tablero=[[num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"]],[num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"]],[num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"]],[num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"]],[num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"]],[num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"]],[num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"]],[num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"]],[num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]]]
            colores=[[num00["bg"],num01["bg"],num02["bg"],num03["bg"],num04["bg"],num05["bg"],num06["bg"],num07["bg"],num08["bg"]],[num10["bg"],num11["bg"],num12["bg"],num13["bg"],num14["bg"],num15["bg"],num16["bg"],num17["bg"],num18["bg"]],[num20["bg"],num21["bg"],num22["bg"],num23["bg"],num24["bg"],num25["bg"],num26["bg"],num27["bg"],num28["bg"]],[num30["bg"],num31["bg"],num32["bg"],num33["bg"],num34["bg"],num35["bg"],num36["bg"],num37["bg"],num38["bg"]],[num40["bg"],num41["bg"],num42["bg"],num43["bg"],num44["bg"],num45["bg"],num46["bg"],num47["bg"],num48["bg"]],[num50["bg"],num51["bg"],num52["bg"],num53["bg"],num54["bg"],num55["bg"],num56["bg"],num57["bg"],num58["bg"]],[num60["bg"],num61["bg"],num62["bg"],num63["bg"],num64["bg"],num65["bg"],num66["bg"],num67["bg"],num68["bg"]],[num70["bg"],num71["bg"],num72["bg"],num73["bg"],num74["bg"],num75["bg"],num76["bg"],num77["bg"],num78["bg"]],[num80["bg"],num81["bg"],num82["bg"],num83["bg"],num84["bg"],num85["bg"],num86["bg"],num87["bg"],num88["bg"]]]
            configuración_de_archivo2=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
            configu=pickle.load(configuración_de_archivo2) 
            configuración_de_archivo2.close()
            if configu["reloj"] == 1:
                reloj_guardar=lblClock["text"].split(":")
            if configu["reloj"] == 3:
                reloj_guardar=lblTimer["text"].split(":")
            else:
                reloj_guardar=["0","0","0"]
            configu["horas"]=int(reloj_guardar[0])
            configu["minutos"]=int(reloj_guardar[1])
            configu["segundos"]=int(reloj_guardar[2])
            
            
            nombre=entryNombre.get()
            pickle.dump([tablero,partida,configu,nombre,colores],configuración_de_archivo)
            configuración_de_archivo.close()
            
        return
    
    def borrar_juego():
        global jugadas_viejas,jugadas_nuevas,jugando,reloj, temporizador, configuración_reloj
        if not jugando:
            messagebox.showinfo(message="No se ha iniciado el juego", title="Atención") #envia un mensaje de que no se puede borrar el juego si no hay una partida iniciada 
        if jugando:
            deshabilitar_botones() # deshabilita los botones 
            if messagebox.askyesno(message="¿Desea borrar el juego?", title="Atención"): #envia un mensaje de que si está seguro de borrar el juego ya iniciado
                
                # deshace la jugada si indica que si 
                while jugadas_viejas.elementos!=[]:
                    deshacer_jugada()
                jugadas_viejas.elementos=[]
                jugadas_nuevas.elementos=[]
                habilitar_botones()
                jugando=False
                configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
                configu=pickle.load(configuración_de_archivo) 
                configuración_de_archivo.close()
                if configu["reloj"] == 1:
                    reloj=0
                    lblClock['text'] = convertir(reloj)
                if configu["reloj"] == 3:
                    temporizador=configu["horas"]*3600+configu["minutos"]*60+configu["segundos"]
                    lblTimer['text'] = convertir(temporizador)
                deshabilitar_botones()
                entryNombre.config(state='normal')
                btnIniciarPartida.config(state="normal")
              # si no sigue con la partida
            else:
                habilitar_botones()
                
    def terminar_juego():
        global jugando
        if not jugando:
            messagebox.showinfo(message="No se ha iniciado el juego", title="Atención") # envia un mensaje si no ha iniciado ninguna partida
        if jugando:
            deshabilitar_botones()
            if messagebox.askyesno(message="¿Desea terminar el juego?", title="Atención"): # envia un mensaje de si desea terminar el juego o continua
                ventana_principal_juego.destroy() #elimina el juego si indica que si
                jugar()
            #si indica que no, continua la partida 
            else:
                habilitar_botones()
    def top_x():
        global fácilTop, intermedioTop, difícilTop
        configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
        configu=pickle.load(configuración_de_archivo) 
        configuración_de_archivo.close()
        c = canvas.Canvas("archivos\\documentos\\TopPdf.pdf", pagesize="A4")
        text = c.beginText(50, 750)
        text.setFont("Times-Roman", 12)
        c.drawString(50, 750, "Top "+str(configu["cantidad_Top"])+" mejores tiempos en el Juego de Sudoku")
        lista_fácil=fácilTop.parcial(configu["cantidad_Top"])
        lista_intermedio=intermedioTop.parcial(configu["cantidad_Top"])
        lista_difícil=difícilTop.parcial(configu["cantidad_Top"])
        lista_top=[[lista_fácil],[lista_intermedio],[lista_difícil]]
        
        
        c.showPage()
        c.save()
        os.system("archivos\\documentos\\TopPdf.pdf")
        return
    
    configuración_de_archivo=open("archivos\\documentos\\sudoku2021configuración.dat","rb")
    configu=pickle.load(configuración_de_archivo) 
    configuración_de_archivo.close()
    def selecciona_1():
        global elección
        btn1.config(bg="light blue")
        btn2.config(bg="#e9fb2c")
        btn3.config(bg="#e9fb2c")
        btn4.config(bg="#e9fb2c")
        btn5.config(bg="#e9fb2c")
        btn6.config(bg="#e9fb2c")
        btn7.config(bg="#e9fb2c")
        btn8.config(bg="#e9fb2c")
        btn9.config(bg="#e9fb2c")
        elección=configu["símbolos"][0]
        return
    def selecciona_2():
        global elección
        btn1.config(bg="#e9fb2c")
        btn2.config(bg="light blue")
        btn3.config(bg="#e9fb2c")
        btn4.config(bg="#e9fb2c")
        btn5.config(bg="#e9fb2c")
        btn6.config(bg="#e9fb2c")
        btn7.config(bg="#e9fb2c")
        btn8.config(bg="#e9fb2c")
        btn9.config(bg="#e9fb2c")
        elección=configu["símbolos"][1]
        return
    def selecciona_3():
        global elección
        btn1.config(bg="#e9fb2c")
        btn2.config(bg="#e9fb2c")
        btn3.config(bg="light blue")
        btn4.config(bg="#e9fb2c")
        btn5.config(bg="#e9fb2c")
        btn6.config(bg="#e9fb2c")
        btn7.config(bg="#e9fb2c")
        btn8.config(bg="#e9fb2c")
        btn9.config(bg="#e9fb2c")
        elección=configu["símbolos"][2]
        return
    def selecciona_4():
        global elección
        btn1.config(bg="#e9fb2c")
        btn2.config(bg="#e9fb2c")
        btn3.config(bg="#e9fb2c")
        btn4.config(bg="light blue")
        btn5.config(bg="#e9fb2c")
        btn6.config(bg="#e9fb2c")
        btn7.config(bg="#e9fb2c")
        btn8.config(bg="#e9fb2c")
        btn9.config(bg="#e9fb2c")
        elección=configu["símbolos"][3]
        return
    def selecciona_5():
        global elección
        btn1.config(bg="#e9fb2c")
        btn2.config(bg="#e9fb2c")
        btn3.config(bg="#e9fb2c")
        btn4.config(bg="#e9fb2c")
        btn5.config(bg="light blue")
        btn6.config(bg="#e9fb2c")
        btn7.config(bg="#e9fb2c")
        btn8.config(bg="#e9fb2c")
        btn9.config(bg="#e9fb2c")
        elección=configu["símbolos"][4]
        return
    def selecciona_6():
        global elección
        btn1.config(bg="#e9fb2c")
        btn2.config(bg="#e9fb2c")
        btn3.config(bg="#e9fb2c")
        btn4.config(bg="#e9fb2c")
        btn5.config(bg="#e9fb2c")
        btn6.config(bg="light blue")
        btn7.config(bg="#e9fb2c")
        btn8.config(bg="#e9fb2c")
        btn9.config(bg="#e9fb2c")
        elección=configu["símbolos"][5]
        return
    def selecciona_7():
        global elección
        btn1.config(bg="#e9fb2c")
        btn2.config(bg="#e9fb2c")
        btn3.config(bg="#e9fb2c")
        btn4.config(bg="#e9fb2c")
        btn5.config(bg="#e9fb2c")
        btn6.config(bg="#e9fb2c")
        btn7.config(bg="light blue")
        btn8.config(bg="#e9fb2c")
        btn9.config(bg="#e9fb2c")
        elección=configu["símbolos"][6]
        return
    def selecciona_8():
        global elección
        btn1.config(bg="#e9fb2c")
        btn2.config(bg="#e9fb2c")
        btn3.config(bg="#e9fb2c")
        btn4.config(bg="#e9fb2c")
        btn5.config(bg="#e9fb2c")
        btn6.config(bg="#e9fb2c")
        btn7.config(bg="#e9fb2c")
        btn8.config(bg="light blue")
        btn9.config(bg="#e9fb2c")
        elección=configu["símbolos"][7]
        return
    def selecciona_9():
        global elección,jugadas_viejas
        
        btn1.config(bg="#e9fb2c")
        btn2.config(bg="#e9fb2c")
        btn3.config(bg="#e9fb2c")
        btn4.config(bg="#e9fb2c")
        btn5.config(bg="#e9fb2c")
        btn6.config(bg="#e9fb2c")
        btn7.config(bg="#e9fb2c")
        btn8.config(bg="#e9fb2c")
        btn9.config(bg="light blue")
        elección=configu["símbolos"][8]
        return
    
    # Agrega espacio donde se coloca el nombre del jugador
    entryNombre = tk.Entry(ventana_principal_juego, bd=2, bg="#8c004b", font=("Century", 13))
    entryNombre.place(x=100, y=0)
    if not guardado==[]:
        entryNombre.insert(0,guardado[3])
    #botones de la ventana jugar 
    btnIniciarPartida = tk.Button(ventana_principal_juego, text="INICIAR \n  JUEGO  ",
                                  bg="#de14e5", fg="black",
                                  font=("Century", 12),
                                  activebackground="#a4e647",
                                  activeforeground="black",
                                  command=iniciar_juego)
    btnIniciarPartida.place(x=370, y=160)

    btnDeshacerJugada = tk.Button(ventana_principal_juego, text="   DESHACER   \nJUGADA",
                               bg="#e7880f", fg="black",
                               font=("Century", 12),
                               activebackground="#e8e54a",
                               activeforeground="black",
                               command=deshacer_jugada)
    btnDeshacerJugada.place(x=500, y=160)
    
    btnRehacerJugada = tk.Button(ventana_principal_juego, text="   REHACER   \nJUGADA",
                               bg="#22fceb", fg="black",
                               font=("Century", 12),
                               activebackground="#e8e54a",
                               activeforeground="black",
                               command=rehacer_jugada)
    btnRehacerJugada.place(x=500, y=220)
    
    btnBorrarJuego = tk.Button(ventana_principal_juego, text="  BORRAR  \n JUEGO ",
                                bg="#4f5312", fg="black",
                                font=("Century", 12),
                                activebackground="#e34257",
                                activeforeground="black",
                                command=borrar_juego)
    btnBorrarJuego.place(x=370, y=340)

    btnTerminarJuego = tk.Button(ventana_principal_juego, text="  TERMINAR \nJUEGO ",
                            bg="#c86e76", fg="black",
                            font=("Century", 12),
                            activebackground="#33cca1",
                            activeforeground="black",
                            command=terminar_juego)
    btnTerminarJuego.place(x=500, y=280)

    btnCargarJuego = tk.Button(ventana_principal_juego, text="   CARGAR   \nJUEGO",
                               bg="#285e78", fg="black",
                               font=("Century", 12),
                               activebackground="#e8e54a",
                               activeforeground="black",
                               command=cargar_juego)
    btnCargarJuego.place(x=370, y=280)
    
    btnGuardarJuego = tk.Button(ventana_principal_juego, text="  GUARDAR  \nJUEGO",
                                bg="#61254c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=guardar_juego)
    btnGuardarJuego.place(x=370, y=220)
    btnTopX = tk.Button(ventana_principal_juego, text="  TOP X ",
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=top_x)
    btnTopX.place(x=500, y=340)

    btn1 = tk.Button(ventana_principal_juego, text=str(configu["símbolos"][0]),
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_1)
    btn1.place(x=370, y=50)

    btn2 = tk.Button(ventana_principal_juego, text=str(configu["símbolos"][1]),
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_2)
    btn2.place(x=405, y=50)

    btn3 = tk.Button(ventana_principal_juego, text=str(configu["símbolos"][2]),
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_3)
    btn3.place(x=440, y=50)

    btn4 = tk.Button(ventana_principal_juego, text=str(configu["símbolos"][3]),
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_4)
    btn4.place(x=370, y=85)

    btn5 = tk.Button(ventana_principal_juego, text=str(configu["símbolos"][4]),
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_5)
    btn5.place(x=405, y=85)

    btn6 = tk.Button(ventana_principal_juego, text=str(configu["símbolos"][5]),
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_6)
    btn6.place(x=440, y=85)

    btn7 = tk.Button(ventana_principal_juego, text=str(configu["símbolos"][6]),
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_7)
    btn7.place(x=370, y=120)

    btn8 = tk.Button(ventana_principal_juego, text=str(configu["símbolos"][7]),
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_8)
    btn8.place(x=405, y=120)

    btn9 = tk.Button(ventana_principal_juego, text=str(configu["símbolos"][8]),
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_9)
    btn9.config(bg="light blue")
    btn9.place(x=440, y=120)
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
    def habilitar_botones(): #funcion que habilita los botones
        num00.config(state="normal") #state: cambia el estado del boton 
        num01.config(state="normal")
        num02.config(state="normal")
        num03.config(state="normal")
        num04.config(state="normal")
        num05.config(state="normal")
        num06.config(state="normal")
        num07.config(state="normal")
        num08.config(state="normal")
        num10.config(state="normal")
        num11.config(state="normal")
        num12.config(state="normal")
        num13.config(state="normal")
        num14.config(state="normal")
        num15.config(state="normal")
        num16.config(state="normal")
        num17.config(state="normal")
        num18.config(state="normal")
        num20.config(state="normal")
        num21.config(state="normal")
        num22.config(state="normal")
        num23.config(state="normal")
        num24.config(state="normal")
        num25.config(state="normal")
        num26.config(state="normal")
        num27.config(state="normal")
        num28.config(state="normal")
        num30.config(state="normal")
        num31.config(state="normal")
        num32.config(state="normal")
        num33.config(state="normal")
        num34.config(state="normal")
        num35.config(state="normal")
        num36.config(state="normal")
        num37.config(state="normal")
        num38.config(state="normal")
        num40.config(state="normal")
        num41.config(state="normal")
        num42.config(state="normal")
        num43.config(state="normal")
        num44.config(state="normal")
        num45.config(state="normal")
        num46.config(state="normal")
        num47.config(state="normal")
        num48.config(state="normal")
        num50.config(state="normal")
        num51.config(state="normal")
        num52.config(state="normal")
        num53.config(state="normal")
        num54.config(state="normal")
        num55.config(state="normal")
        num56.config(state="normal")
        num57.config(state="normal")
        num58.config(state="normal")
        num60.config(state="normal")
        num61.config(state="normal")
        num62.config(state="normal")
        num63.config(state="normal")
        num64.config(state="normal")
        num65.config(state="normal")
        num66.config(state="normal")
        num67.config(state="normal")
        num68.config(state="normal")
        num70.config(state="normal")
        num71.config(state="normal")
        num72.config(state="normal")
        num73.config(state="normal")
        num74.config(state="normal")
        num75.config(state="normal")
        num76.config(state="normal")
        num77.config(state="normal")
        num78.config(state="normal")
        num80.config(state="normal")
        num81.config(state="normal")
        num82.config(state="normal")
        num83.config(state="normal")
        num84.config(state="normal")
        num85.config(state="normal")
        num86.config(state="normal")
        num87.config(state="normal")
        num88.config(state="normal")
        btn1.config(state="normal")
        btn2.config(state="normal")
        btn3.config(state="normal")
        btn4.config(state="normal")
        btn5.config(state="normal")
        btn6.config(state="normal")
        btn7.config(state="normal")
        btn8.config(state="normal")
        btn9.config(state="normal")
        
    def deshabilitar_botones(): #funcion que deshabilita los botones
        num00.config(state="disabled") #state: cambia el estado del boton
        num01.config(state="disabled")
        num02.config(state="disabled")
        num03.config(state="disabled")
        num04.config(state="disabled")
        num05.config(state="disabled")
        num06.config(state="disabled")
        num07.config(state="disabled")
        num08.config(state="disabled")
        num10.config(state="disabled")
        num11.config(state="disabled")
        num12.config(state="disabled")
        num13.config(state="disabled")
        num14.config(state="disabled")
        num15.config(state="disabled")
        num16.config(state="disabled")
        num17.config(state="disabled")
        num18.config(state="disabled")
        num20.config(state="disabled")
        num21.config(state="disabled")
        num22.config(state="disabled")
        num23.config(state="disabled")
        num24.config(state="disabled")
        num25.config(state="disabled")
        num26.config(state="disabled")
        num27.config(state="disabled")
        num28.config(state="disabled")
        num30.config(state="disabled")
        num31.config(state="disabled")
        num32.config(state="disabled")
        num33.config(state="disabled")
        num34.config(state="disabled")
        num35.config(state="disabled")
        num36.config(state="disabled")
        num37.config(state="disabled")
        num38.config(state="disabled")
        num40.config(state="disabled")
        num41.config(state="disabled")
        num42.config(state="disabled")
        num43.config(state="disabled")
        num44.config(state="disabled")
        num45.config(state="disabled")
        num46.config(state="disabled")
        num47.config(state="disabled")
        num48.config(state="disabled")
        num50.config(state="disabled")
        num51.config(state="disabled")
        num52.config(state="disabled")
        num53.config(state="disabled")
        num54.config(state="disabled")
        num55.config(state="disabled")
        num56.config(state="disabled")
        num57.config(state="disabled")
        num58.config(state="disabled")
        num60.config(state="disabled")
        num61.config(state="disabled")
        num62.config(state="disabled")
        num63.config(state="disabled")
        num64.config(state="disabled")
        num65.config(state="disabled")
        num66.config(state="disabled")
        num67.config(state="disabled")
        num68.config(state="disabled")
        num70.config(state="disabled")
        num71.config(state="disabled")
        num72.config(state="disabled")
        num73.config(state="disabled")
        num74.config(state="disabled")
        num75.config(state="disabled")
        num76.config(state="disabled")
        num77.config(state="disabled")
        num78.config(state="disabled")
        num80.config(state="disabled")
        num81.config(state="disabled")
        num82.config(state="disabled")
        num83.config(state="disabled")
        num84.config(state="disabled")
        num85.config(state="disabled")
        num86.config(state="disabled")
        num87.config(state="disabled")
        num88.config(state="disabled")
        btn1.config(state="disabled")
        btn2.config(state="disabled")
        btn3.config(state="disabled")
        btn4.config(state="disabled")
        btn5.config(state="disabled")
        btn6.config(state="disabled")
        btn7.config(state="disabled")
        btn8.config(state="disabled")
        btn9.config(state="disabled")
        btn1.config(bg="#e9fb2c")
        btn2.config(bg="#e9fb2c")
        btn3.config(bg="#e9fb2c")
        btn4.config(bg="#e9fb2c")
        btn5.config(bg="#e9fb2c")
        btn6.config(bg="#e9fb2c")
        btn7.config(bg="#e9fb2c")
        btn8.config(bg="#e9fb2c")
        btn9.config(bg="#e9fb2c")
    
    # Crea el tablero inicial
    iniciarPartida()
    return
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------------Funcion de configuracion------------------------#
def configuración():
    global hay_reloj, hay_temporizador, configuración_reloj,configuración_valores, horas, minutos, segundos, configu #globales
    global dificultad,cantidad_top,símbolos
    menú.withdraw()
    # Genera una ventana secundaria
    ventanaConfig = tk.Toplevel()
    ventanaConfig.title("Juego Sudoku")
    ventanaConfig.geometry("{}x{}+{}+{}".format(700, 700, int((menú.winfo_screenwidth() / 2) - (750 / 2)),
                                                int((menú.winfo_screenheight() / 2) - (750 / 2))))
    ventanaConfig.resizable(width=False, height=False)
    ventanaConfig.config(bg="#8c004b")

    lblhora = tk.Label(ventanaConfig, text="Ingrese hora:", bg="#8c004b", fg="black", font=("Century", 16))
    lblhora.place(x=0, y=175)

    lblminutos = tk.Label(ventanaConfig, text="Ingrese minutos:", bg="#8c004b", fg="black",
                          font=("Century", 16))
    lblminutos.place(x=0, y=250)

    lblsegundos = tk.Label(ventanaConfig, text="Ingrese segundos:", bg="#8c004b", fg="black",
                           font=("Century", 16))
    lblsegundos.place(x=0, y=325)
    
    dificultad.set(configu["dificultad"])
    configuración_reloj.set(configu["reloj"])
    configuración_valores.set(configu['símbolos_rbotón'])
    horas=configu["horas"]
    minutos=configu["minutos"]
    segundos=configu["segundos"]
    cantidad_top=configu['cantidad_Top']
    símbolos=configu["símbolos"]

    entryHoras = tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryHoras.insert(0, str(horas))
    entryHoras.place(x=210, y=175)

    entryMinutos = tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryMinutos.insert(0, str(minutos))
    entryMinutos.place(x=210, y=250)

    entrySegundos = tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entrySegundos.insert(0, str(segundos))
    entrySegundos.place(x=210, y=325)

    entryTopX = tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryTopX.insert(0, str(cantidad_top))
    entryTopX.place(x=475, y=360)

    entryEsp1= tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryEsp1.insert(0,str(símbolos[0]))
    entryEsp1.place(x=335, y=430)

    entryEsp2= tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryEsp2.insert(0, str(símbolos[1]))
    entryEsp2.place(x=335, y=455)

    entryEsp3= tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryEsp3.insert(0, str(símbolos[2]))
    entryEsp3.place(x=335, y=475)

    entryEsp4= tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryEsp4.insert(0, str(símbolos[3]))
    entryEsp4.place(x=335, y=495)

    entryEsp5= tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryEsp5.insert(0, str(símbolos[4]))
    entryEsp5.place(x=335, y=515)

    entryEsp6= tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryEsp6.insert(0, str(símbolos[5]))
    entryEsp6.place(x=335, y=535)

    entryEsp7= tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryEsp7.insert(0, str(símbolos[6]))
    entryEsp7.place(x=335, y=555)

    entryEsp8= tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryEsp8.insert(0, str(símbolos[7]))
    entryEsp8.place(x=335, y=575)

    entryEsp9= tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryEsp9.insert(0, str(símbolos[8]))
    entryEsp9.place(x=335, y=595)
    
    #guarda los datos ingresados 
    def guardarConfig():
        global tiempo_expirado
        try:
            horas = int(entryHoras.get())
            minutos = int(entryMinutos.get())
            segundos = int(entrySegundos.get())
            cantidad_top = int(entryTopX.get())
            if horas in range(0,5):
                if minutos in range(0,60):
                    if segundos in range(0,60):
                        if configuración_valores.get()==1:
                            símbolos=["1","2","3","4","5","6","7","8","9"]
                        elif configuración_valores.get()==2:
                            símbolos=["A","B","C","D","E","F","G","H","I"]
                        elif configuración_valores.get()==3:
                            símbolos=[entryEsp1.get(),entryEsp2.get(),entryEsp3.get(),entryEsp4.get(),entryEsp5.get(),entryEsp6.get(),entryEsp7.get(),entryEsp8.get(),entryEsp9.get()]
            
                        for símbolo in símbolos:
                            if símbolos.count(símbolo)!=1:
                                messagebox.showerror('Error', 'Los símbolos deben ser diferentes')
                            else:
                                tiempo_expirado=horas*3600+minutos*60+segundos
                                partidas_iniciales=open("archivos\\documentos\\sudoku2021configuración.dat","wb")
                                pickle.dump({"reloj":configuración_reloj.get(),"dificultad":dificultad.get(),"horas":horas,"minutos":minutos,"segundos":segundos,"cantidad_Top":cantidad_top,"símbolos":símbolos,"símbolos_rbotón":configuración_valores.get()},partidas_iniciales)                    
                                partidas_iniciales.close()
                                menú.deiconify()
                                ventanaConfig.destroy()
                    else:
                        messagebox.showerror("Error", "Los segundos no están dentro del límite")
                else:
                    messagebox.showerror("Error", "Los minutos no están dentro del límite")
            else:
                messagebox.showerror("Error", "Los horas no están dentro del límite")
        except ValueError:
            messagebox.showerror('Error', 'Los campos no deben estar vacios')
            
    #no guarda los cambios en la configuracion 
    def cancelarConfig():
        menú.deiconify()
        ventanaConfig.destroy()
    #botones de la configuracion 
    btnGuardarConfig = tk.Button(ventanaConfig, text="     Guardar     ",
                                 bg="#de2644", fg="black",
                                 font=("Century", 12),
                                 activebackground="#e8e54a",
                                 activeforeground="black",
                                 command=guardarConfig)
    btnGuardarConfig.place(x=20, y=650)

    btnCancelar = tk.Button(ventanaConfig, text="     Cancelar     ",
                            bg="#ed5caa", fg="black",
                            font=("Century", 12),
                            activebackground="#33cc6b",
                            activeforeground="black",
                            command=cancelarConfig)
    btnCancelar.place(x=250, y=650)
    
    def recomendación_reloj():
        if configuración_reloj.get()==3:
            entrySegundos.delete(0,"end")
            entryMinutos.delete(0,"end")
            entryHoras.delete(0,"end")
            entryMinutos.insert(0,"30")
            entryHoras.insert(0,"0")
            entrySegundos.insert(0,"0")
            dificultad.set(0)
        else:
            entrySegundos.delete(0,"end")
            entryMinutos.delete(0,"end")
            entryHoras.delete(0,"end")
            entryMinutos.insert(0,"0")
            entryHoras.insert(0,"0")
            entrySegundos.insert(0,"0")
            

    rbtnSi = tk.Radiobutton(ventanaConfig,
                            text="Si",
                            padx=20,
                            variable=configuración_reloj,
                            bg="#8c004b",
                            font=("Century", 16),
                            value=1,command=recomendación_reloj)
    rbtnSi.place(x=0, y=80)

    rbtnNo = tk.Radiobutton(ventanaConfig,
                            text="No",
                            padx=20,
                            variable=configuración_reloj,
                            bg="#8c004b",
                            font=("Century", 16),
                            value=2,command=recomendación_reloj)
    rbtnNo.place(x=0, y=110)
    rbtnTimer = tk.Radiobutton(ventanaConfig,
                               text="Timer",
                               padx=20,
                               variable=configuración_reloj,
                               bg="#8c004b",
                               font=("Century", 16),
                               value=3,command=recomendación_reloj)
    rbtnTimer.place(x=0, y=50)
    def recomendación_tiempos():
        if dificultad.get()==0 and configuración_reloj.get()==3:
            entrySegundos.delete(0,"end")
            entryMinutos.delete(0,"end")
            entryHoras.delete(0,"end")
            entryMinutos.insert(0,"30")
            entryHoras.insert(0,"0")
            entrySegundos.insert(0,"0")
        if dificultad.get()==1 and configuración_reloj.get()==3:
            entrySegundos.delete(0,"end")
            entryMinutos.delete(0,"end")
            entryHoras.delete(0,"end")
            entryHoras.insert(0,"1")
            entrySegundos.insert(0,"0")
            entryMinutos.insert(0,"0")
        if dificultad.get()==2 and configuración_reloj.get()==3:
            entrySegundos.delete(0,"end")
            entryMinutos.delete(0,"end")
            entryHoras.delete(0,"end")
            entryHoras.insert(0,"2")
            entrySegundos.insert(0,"0")
            entryMinutos.insert(0,"0")
        
    rbtnIntermedio = tk.Radiobutton(ventanaConfig,
                            text="Intermedio",
                            padx=20,
                            variable=dificultad,
                            bg="#8c004b",
                            font=("Century", 16),
                            value=1,command=recomendación_tiempos)
    rbtnIntermedio.place(x=150, y=80)

    rbtnDifícil = tk.Radiobutton(ventanaConfig,
                            text="Difícil",
                            padx=20,
                            variable=dificultad,
                            bg="#8c004b",
                            font=("Century", 16),
                            value=2,command=recomendación_tiempos)
    rbtnDifícil.place(x=150, y=110)
    rbtnFácil = tk.Radiobutton(ventanaConfig,
                               text="Fácil",
                               padx=20,
                               variable=dificultad,
                               bg="#8c004b",
                               font=("Century", 16),
                               value=0,command=recomendación_tiempos)
    rbtnFácil.place(x=150, y=50)

    rbtnNúmeros = tk.Radiobutton(ventanaConfig,
                            text="Números\n1\n2\n3\n4\n5\n6\n7\n8\n9",
                            padx=20,
                            variable=configuración_valores,
                            bg="#8c004b",
                            font=("Century", 16),
                            value=1)
    rbtnNúmeros.place(x=0, y=390)

    rbtnLetras = tk.Radiobutton(ventanaConfig,
                            text="Letras\nA\nB\nC\nD\nE\nF\nG\nH\nI",
                            padx=20,
                            variable=configuración_valores,
                            bg="#8c004b",
                            font=("Century", 16),
                            value=2)
    rbtnLetras.place(x=150, y=390)
    rbtnEspecial = tk.Radiobutton(ventanaConfig,
                               text="Usted lo define",
                               padx=20,
                               variable=configuración_valores,
                               bg="#8c004b",
                               font=("Century", 16),
                               value=3)
    rbtnEspecial.place(x=300, y=390)
    lblhora = tk.Label(ventanaConfig, text="Reloj:", bg="#8c004b", fg="black",
                       font=("Century", 16))
    lblhora.place(x=0, y=15)
    
    lbldificultad = tk.Label(ventanaConfig, text="Dificultad:", bg="#8c004b", fg="black",
                       font=("Century", 16))
    lbldificultad.place(x=150, y=15)
    
    lbltopX = tk.Label(ventanaConfig, text="Cantidad de jugadas desplegadas en el TOP X:", bg="#8c004b", fg="black",
                       font=("Century", 16))
    lbltopX.place(x=0, y=360)
    return 

#------------------------Funcion para dar informacion a base del documento------------------------#
def acerca_de():
    ventanaAcercaDe = tk.Toplevel() # Con top level se crea una ventana secundaria donde se van a ingresar los datos del documento
    ventanaAcercaDe.title("Juego Sudoku")
    ventanaAcercaDe.geometry("{}x{}+{}+{}".format(440, 440, int((menú.winfo_screenwidth() / 2) - (440 / 2)),
                                                  int((menú.winfo_screenheight() / 2) - (440 / 2))))

    ventanaAcercaDe.resizable(width=False, height=False)
    ventanaAcercaDe.config(bg="white")
    #datos del documento con label
    lblnombreJuego = tk.Label(ventanaAcercaDe, text="Sudoku", bg="#0CB7F2", fg="black", font=("Century", 24))
    lblnombreJuego.place(x=440 // 2, y=100, anchor="center")

    lblversion = tk.Label(ventanaAcercaDe, text="version 1.0.0", bg="#0CB7F2", fg="black",
                          font=("Century", 24))
    lblversion.place(x=440 // 2, y=175, anchor="center")

    lblfecha = tk.Label(ventanaAcercaDe, text="01/12/21", bg="#0CB7F2", fg="black", font=("Century", 24))
    lblfecha.place(x=440 // 2, y=250, anchor="center")

    lblautora = tk.Label(ventanaAcercaDe, text="Kendall Guzmán Ramírez", bg="#0CB7F2", fg="black",
                         font=("Century", 24))
    lblautora.place(x=440 // 2, y=325, anchor="center")

    lblautorb = tk.Label(ventanaAcercaDe, text="María Solís Sojo", bg="#0CB7F2", fg="black",
                         font=("Century", 24))
    lblautorb.place(x=440 // 2, y=400, anchor="center")
    return

#------------------------Funcion para desplegar el manual de usuario------------------------#
def ayuda():
    os.system("archivos\\documentos\\manual_de_usuario_sudoku.pdf") #ejecuta el comando (una cadena) en un subshell. (abre el pdf
    return

#------------------------Funcion para cerrar el programa------------------------#
def salir():
    # Destruye la ventana
    menú.destroy()

#------------------------botones del menu principal------------------------#
btnjugar = tk.Button(menú, text="Jugar",
                     bg="#FF99C4", fg="black",
                     font=("Century", 9),
                     activebackground="#32551e",
                     activeforeground="black",
                     command=jugar)
btnjugar.place(x=0, y=362, width=60, height=20)

btnconfiguración = tk.Button(menú, text=" Configuración ",
                             bg="#8AFFD1", fg="black",
                             font=("Century", 9),
                             activebackground="#e34257",
                             activeforeground="black",
                             command=configuración)
btnconfiguración.place(x=62, y=362, width=95, height=20)

btnacercade = tk.Button(menú, text="   Acerca de   ",
                        bg="#90FF8F", fg="black",
                        font=("Century", 9),
                        activebackground="#33cca1",
                        activeforeground="black",
                        command=acerca_de)
btnacercade.place(x=221, y=362, width=85, height=20)

btnayuda = tk.Button(menú, text="    Ayuda    ",
                     bg="#EAC2FF", fg="black",
                     font=("Century", 9),
                     activebackground="#9d42e3",
                     activeforeground="black",
                     command=ayuda)
btnayuda.place(x=159, y=362, width=60, height=20)

btnSalir = tk.Button(menú, text="     Salir     ",
                     bg="#FFBA9E", fg="black",
                     font=("Century", 9),
                     activebackground="#e8e54a",
                     activeforeground="black",
                     command=salir)
btnSalir.place(x=308, y=362, width=60, height=20)


menú.mainloop() #ejecuta el ciclo de eventos de la ventana de tkinter
