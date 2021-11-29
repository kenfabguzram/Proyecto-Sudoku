import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
import random
import pickle
# -----------------------------------------------------------------------------------------------------------------------
# Definición de variables iniciales requeridas para las funciones
menú = tk.Tk()
menú.title("Juego Sudoku")
menú.geometry("{}x{}+{}+{}".format(370, 382, int((menú.winfo_screenwidth() / 2) - (370 / 2)),
                                   int((menú.winfo_screenheight() / 2) - (382 / 2))))
tablero=[]
anterior=0
elección=""
reloj = 0
temporizador = 0
horas = 0
minutos = 0
segundos = 0
configuración_reloj = tk.IntVar()
configuración_reloj.set(1)
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
dificultad=1
def jugar():
    global grid, reloj
    reloj = 0
    # Esconde el menú
    menú.withdraw()
    # Con top level se crea una ventana secundaria donde se van a ingresar los datos del juego
    ventana_principal_juego = tk.Toplevel()
    elección=""
    # matriz inicia en 0
    
    # Verifica si hay espacios vacios en la matriz
    def terminoElJuego(matriz):
        for filas in range(len(matriz)):
            for columnas in range(len(matriz[filas])):
                if matriz[filas][columnas] == 0:
                    return False
        return True

    #  Aparecen numeros según la partida escogida del diccionario en configuración
    def escoger_partida():
        global dificultad,tablero
        partidas_iniciales=open("archivos\\documentos\\sudoku2021partidas.dat","rb")
        lista_diccionarios_partidas=pickle.load(partidas_iniciales)
        partidas_iniciales.close()
        diccionario_fácil=lista_diccionarios_partidas[0]
        diccionario_intermedio=lista_diccionarios_partidas[1]
        diccionario_difícil=lista_diccionarios_partidas[2]
        if dificultad==1:
            tablero=diccionario_fácil[list(diccionario_fácil.keys())[random.randint(0,len(diccionario_fácil)-1)]]
        elif dificultad==2:
            tablero=diccionario_intermedio[list(diccionario_intermedio.keys())[random.randint(0,len(diccionario_intermedio)-1)]]
        elif dificultad==3:
            tablero=diccionario_difícil[list(diccionario_difícil.keys())[random.randint(0,len(diccionario_difícil)-1)]]
    
    ventana_principal_juego.title("Juego Sudoku")
    ventana_principal_juego.geometry("{}x{}+{}+{}".format(700, 500, int((menú.winfo_screenwidth() / 2) - (382 / 2)),
                                                          int((menú.winfo_screenheight() / 2) - (360 / 2))))

    ventana_principal_juego.resizable(width=False, height=False)
    ventana_principal_juego.config(bg="#e9bd15")

    frame = tk.Frame(ventana_principal_juego)
    frame.place(x=0, y=45)
    frame.config(width="1", height="1")
    
    lblJugador = tk.Label(ventana_principal_juego, text="Jugador:", bd=3, bg="#e9bd15", fg="black",
                          font=("Century", 11))
    lblJugador.place(x=0, y=0)

    lblClock = tk.Label(ventana_principal_juego, bg="#e9bd15", font=("Century", 16))
    lblClock.place(x=250, y=465)

    lblTimer = tk.Label(ventana_principal_juego, bg="#e9bd15", font=("Century", 16))
    lblTimer.place(x=250, y=465)
    def dividir():
        global tablero
        matriz=tablero
        parcial=[]
        resultado=[]
        for fila in range(3):
            for columna in range(3):
                parcial.append(matriz[fila][columna])
        resultado.append(parcial)
        parcial=[]
        for fila in range(3):
            for columna in range(3,6):
                parcial.append(matriz[fila][columna])
        resultado.append(parcial)
        parcial=[]
        for fila in range(3):
            for columna in range(6,9):
                parcial.append(matriz[fila][columna])
        resultado.append(parcial)
        parcial=[]
        for fila in range(3,6):
            for columna in range(3):
                parcial.append(matriz[fila][columna])
        resultado.append(parcial)
        parcial=[]
        for fila in range(3,6):
            for columna in range(3,6):
                parcial.append(matriz[fila][columna])
        resultado.append(parcial)
        parcial=[]
        for fila in range(3,6):
            for columna in range(6,9):
                parcial.append(matriz[fila][columna])
        resultado.append(parcial)
        parcial=[]
        for fila in range(6,9):
            for columna in range(3):
                parcial.append(matriz[fila][columna])
        resultado.append(parcial)
        parcial=[]
        for fila in range(6,9):
            for columna in range(3,6):
                parcial.append(matriz[fila][columna])
        resultado.append(parcial)
        parcial=[]
        for fila in range(6,9):
            for columna in range(6,9):
                parcial.append(matriz[fila][columna])
        resultado.append(parcial)
        parcial=[]
        return resultado
    def invertir():
        global tablero
        m=tablero
        resultado=[[],[],[],[],[],[],[],[],[]]
        for fila in range(len(m)):
            for elemento in range(len(m[fila])):
                resultado[elemento].append(m[fila][elemento])
        return resultado
    # Label que dibuja  la matriz
            
    grid = [[tk.Button(frame, width=2, height=1, borderwidth=2, relief="solid", font=("Century", 18)) for i in
             range(9)] for j in range(9)]
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




    def func00():
        global elección,tablero
        anterior=num00["text"]
        color_anterior=num00["bg"]
        num00.config(text=elección)
        tablero[0][0]=elección
        def cerrar_advertencia00(event):
            habilitar_botones()
            num00.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[0][0]=anterior
        if num00["bg"]!="#02ac66":
            deshabilitar_botones()
            num00.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia00)
            
        elif dividir()[0].count(tablero[0][0])>1:
            deshabilitar_botones()
            num00.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia00)

        elif tablero[0].count(tablero[0][0])>1:
            deshabilitar_botones()
            num00.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia00)
                    
        elif invertir()[0].count(tablero[0][0])>1:
            deshabilitar_botones()
            num00.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia00)
    def func01():
        global elección,tablero
        anterior=num01["text"]
        color_anterior=num01["bg"]
        num01.config(text=elección)
        tablero[0][1]=elección
        def cerrar_advertencia01(event):
            habilitar_botones()
            num01.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[0][1]=anterior
        if num01["bg"]!="#02ac66":
            deshabilitar_botones()
            num01.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia01)
            
        elif dividir()[0].count(tablero[0][1])>1:
            deshabilitar_botones()
            num01.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia01)

        elif tablero[0].count(tablero[0][1])>1:
            deshabilitar_botones()
            num01.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia01)
                    
        elif invertir()[0].count(tablero[0][1])>1:
            deshabilitar_botones()
            num01.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia01)
    def func02():
        global elección,tablero
        anterior=num02["text"]
        color_anterior=num02["bg"]
        num02.config(text=elección)
        tablero[0][2]=elección
        def cerrar_advertencia02(event):
            habilitar_botones()
            num02.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[0][2]=anterior
        if num02["bg"]!="#02ac66":
            deshabilitar_botones()
            num02.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia02)
            
        elif dividir()[0].count(tablero[0][2])>1:
            deshabilitar_botones()
            num02.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia02)

        elif tablero[0].count(tablero[0][2])>1:
            deshabilitar_botones()
            num02.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia02)
                    
        elif invertir()[0].count(tablero[0][2])>1:
            deshabilitar_botones()
            num02.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia02)
    def func03():
        global elección,tablero
        anterior=num03["text"]
        color_anterior=num03["bg"]
        num03.config(text=elección)
        tablero[0][3]=elección
        def cerrar_advertencia03(event):
            habilitar_botones()
            num03.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[0][3]=anterior
        if num03["bg"]!="#02ac66":
            deshabilitar_botones()
            num03.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia03)
            
        elif dividir()[0].count(tablero[0][3])>1:
            deshabilitar_botones()
            num03.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia03)

        elif tablero[0].count(tablero[0][3])>1:
            deshabilitar_botones()
            num03.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia03)
                    
        elif invertir()[0].count(tablero[0][3])>1:
            deshabilitar_botones()
            num03.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia03)
    def func04():
        global elección,tablero
        anterior=num04["text"]
        color_anterior=num04["bg"]
        num04.config(text=elección)
        tablero[0][4]=elección
        def cerrar_advertencia04(event):
            habilitar_botones()
            num04.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[0][4]=anterior
        if num04["bg"]!="#02ac66":
            deshabilitar_botones()
            num04.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia04)
            
        elif dividir()[0].count(tablero[0][4])>1:
            deshabilitar_botones()
            num04.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia04)

        elif tablero[0].count(tablero[0][4])>1:
            deshabilitar_botones()
            num04.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia04)
                    
        elif invertir()[0].count(tablero[0][4])>1:
            deshabilitar_botones()
            num04.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia04)
    def func05():
        global elección,tablero
        anterior=num05["text"]
        color_anterior=num05["bg"]
        num05.config(text=elección)
        tablero[0][5]=elección
        def cerrar_advertencia05(event):
            habilitar_botones()
            num05.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[0][5]=anterior
        if num05["bg"]!="#02ac66":
            deshabilitar_botones()
            num05.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia05)
            
        elif dividir()[0].count(tablero[0][5])>1:
            deshabilitar_botones()
            num05.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia05)

        elif tablero[0].count(tablero[0][5])>1:
            deshabilitar_botones()
            num05.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia05)
                    
        elif invertir()[0].count(tablero[0][5])>1:
            deshabilitar_botones()
            num05.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia05)
    def func06():
        global elección,tablero
        anterior=num06["text"]
        color_anterior=num06["bg"]
        num06.config(text=elección)
        tablero[0][6]=elección
        def cerrar_advertencia06(event):
            habilitar_botones()
            num06.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[0][6]=anterior
        if num06["bg"]!="#02ac66":
            deshabilitar_botones()
            num06.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia06)
            
        elif dividir()[0].count(tablero[0][6])>1:
            deshabilitar_botones()
            num06.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia06)

        elif tablero[0].count(tablero[0][6])>1:
            deshabilitar_botones()
            num06.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia06)
                    
        elif invertir()[0].count(tablero[0][6])>1:
            deshabilitar_botones()
            num06.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia06)
    def func07():
        global elección,tablero
        anterior=num07["text"]
        color_anterior=num07["bg"]
        num07.config(text=elección)
        tablero[0][7]=elección
        def cerrar_advertencia07(event):
            habilitar_botones()
            num07.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[0][7]=anterior
        if num07["bg"]!="#02ac66":
            deshabilitar_botones()
            num07.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia07)
            
        elif dividir()[0].count(tablero[0][7])>1:
            deshabilitar_botones()
            num07.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia07)

        elif tablero[0].count(tablero[0][7])>1:
            deshabilitar_botones()
            num07.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia07)
                    
        elif invertir()[0].count(tablero[0][7])>1:
            deshabilitar_botones()
            num07.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia07)
    def func08():
        global elección,tablero
        anterior=num08["text"]
        color_anterior=num08["bg"]
        num08.config(text=elección)
        tablero[0][8]=elección
        def cerrar_advertencia08(event):
            habilitar_botones()
            num08.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[0][8]=anterior
        if num08["bg"]!="#02ac66":
            deshabilitar_botones()
            num08.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia08)
            
        elif dividir()[0].count(tablero[0][8])>1:
            deshabilitar_botones()
            num08.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia08)

        elif tablero[0].count(tablero[0][8])>1:
            deshabilitar_botones()
            num08.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia08)
                    
        elif invertir()[0].count(tablero[0][8])>1:
            deshabilitar_botones()
            num08.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia08)
    def func10():
        global elección,tablero
        anterior=num10["text"]
        color_anterior=num10["bg"]
        num10.config(text=elección)
        tablero[1][0]=elección
        def cerrar_advertencia10(event):
            habilitar_botones()
            num10.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[1][0]=anterior
        if num10["bg"]!="#02ac66":
            deshabilitar_botones()
            num10.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia10)
            
        elif dividir()[1].count(tablero[1][0])>1:
            deshabilitar_botones()
            num10.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia10)

        elif tablero[1].count(tablero[1][0])>1:
            deshabilitar_botones()
            num10.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia10)
                    
        elif invertir()[1].count(tablero[1][0])>1:
            deshabilitar_botones()
            num10.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia10)
    def func11():
        global elección,tablero
        anterior=num11["text"]
        color_anterior=num11["bg"]
        num11.config(text=elección)
        tablero[1][1]=elección
        def cerrar_advertencia11(event):
            habilitar_botones()
            num11.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[1][1]=anterior
        if num11["bg"]!="#02ac66":
            deshabilitar_botones()
            num11.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia11)
            
        elif dividir()[1].count(tablero[1][1])>1:
            deshabilitar_botones()
            num11.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia11)

        elif tablero[1].count(tablero[1][1])>1:
            deshabilitar_botones()
            num11.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia11)
                    
        elif invertir()[1].count(tablero[1][1])>1:
            deshabilitar_botones()
            num11.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia11)
    def func12():
        global elección,tablero
        anterior=num12["text"]
        color_anterior=num12["bg"]
        num12.config(text=elección)
        tablero[1][2]=elección
        def cerrar_advertencia12(event):
            habilitar_botones()
            num12.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[1][2]=anterior
        if num12["bg"]!="#02ac66":
            deshabilitar_botones()
            num12.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia12)
            
        elif dividir()[1].count(tablero[1][2])>1:
            deshabilitar_botones()
            num12.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia12)

        elif tablero[1].count(tablero[1][2])>1:
            deshabilitar_botones()
            num12.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia12)
                    
        elif invertir()[1].count(tablero[1][2])>1:
            deshabilitar_botones()
            num12.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia12)
    def func13():
        global elección,tablero
        anterior=num13["text"]
        color_anterior=num13["bg"]
        num13.config(text=elección)
        tablero[1][3]=elección
        def cerrar_advertencia13(event):
            habilitar_botones()
            num13.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[1][3]=anterior
        if num13["bg"]!="#02ac66":
            deshabilitar_botones()
            num13.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia13)
            
        elif dividir()[1].count(tablero[1][3])>1:
            deshabilitar_botones()
            num13.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia13)

        elif tablero[1].count(tablero[1][3])>1:
            deshabilitar_botones()
            num13.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia13)
                    
        elif invertir()[1].count(tablero[1][3])>1:
            deshabilitar_botones()
            num13.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia13)
    def func14():
        global elección,tablero
        anterior=num14["text"]
        color_anterior=num14["bg"]
        num14.config(text=elección)
        tablero[1][4]=elección
        def cerrar_advertencia14(event):
            habilitar_botones()
            num14.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[1][4]=anterior
        if num14["bg"]!="#02ac66":
            deshabilitar_botones()
            num14.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia14)
            
        elif dividir()[1].count(tablero[1][4])>1:
            deshabilitar_botones()
            num14.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia14)

        elif tablero[1].count(tablero[1][4])>1:
            deshabilitar_botones()
            num14.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia14)
                    
        elif invertir()[1].count(tablero[1][4])>1:
            deshabilitar_botones()
            num14.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia14)
    def func15():
        global elección,tablero
        anterior=num15["text"]
        color_anterior=num15["bg"]
        num15.config(text=elección)
        tablero[1][5]=elección
        def cerrar_advertencia15(event):
            habilitar_botones()
            num15.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[1][5]=anterior
        if num15["bg"]!="#02ac66":
            deshabilitar_botones()
            num15.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia15)
            
        elif dividir()[1].count(tablero[1][5])>1:
            deshabilitar_botones()
            num15.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia15)

        elif tablero[1].count(tablero[1][5])>1:
            deshabilitar_botones()
            num15.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia15)
                    
        elif invertir()[1].count(tablero[1][5])>1:
            deshabilitar_botones()
            num15.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia15)
    def func16():
        global elección,tablero
        anterior=num16["text"]
        color_anterior=num16["bg"]
        num16.config(text=elección)
        tablero[1][6]=elección
        def cerrar_advertencia16(event):
            habilitar_botones()
            num16.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[1][6]=anterior
        if num16["bg"]!="#02ac66":
            deshabilitar_botones()
            num16.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia16)
            
        elif dividir()[1].count(tablero[1][6])>1:
            deshabilitar_botones()
            num16.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia16)

        elif tablero[1].count(tablero[1][6])>1:
            deshabilitar_botones()
            num16.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia16)
                    
        elif invertir()[1].count(tablero[1][6])>1:
            deshabilitar_botones()
            num16.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia16)
    def func17():
        global elección,tablero
        anterior=num17["text"]
        color_anterior=num17["bg"]
        num17.config(text=elección)
        tablero[1][7]=elección
        def cerrar_advertencia17(event):
            habilitar_botones()
            num17.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[1][7]=anterior
        if num17["bg"]!="#02ac66":
            deshabilitar_botones()
            num17.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia17)
            
        elif dividir()[1].count(tablero[1][7])>1:
            deshabilitar_botones()
            num17.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia17)

        elif tablero[1].count(tablero[1][7])>1:
            deshabilitar_botones()
            num17.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia17)
                    
        elif invertir()[1].count(tablero[1][7])>1:
            deshabilitar_botones()
            num17.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia17)
    def func18():
        global elección,tablero
        anterior=num18["text"]
        color_anterior=num18["bg"]
        num18.config(text=elección)
        tablero[1][8]=elección
        def cerrar_advertencia18(event):
            habilitar_botones()
            num18.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[1][8]=anterior
        if num18["bg"]!="#02ac66":
            deshabilitar_botones()
            num18.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia18)
            
        elif dividir()[1].count(tablero[1][8])>1:
            deshabilitar_botones()
            num18.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia18)

        elif tablero[1].count(tablero[1][8])>1:
            deshabilitar_botones()
            num18.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia18)
                    
        elif invertir()[1].count(tablero[1][8])>1:
            deshabilitar_botones()
            num18.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia18)
    def func20():
        global elección,tablero
        anterior=num20["text"]
        color_anterior=num20["bg"]
        num20.config(text=elección)
        tablero[2][0]=elección
        def cerrar_advertencia20(event):
            habilitar_botones()
            num20.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[2][0]=anterior
        if num20["bg"]!="#02ac66":
            deshabilitar_botones()
            num20.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia20)
            
        elif dividir()[2].count(tablero[2][0])>1:
            deshabilitar_botones()
            num20.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia20)

        elif tablero[2].count(tablero[2][0])>1:
            deshabilitar_botones()
            num20.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia20)
                    
        elif invertir()[2].count(tablero[2][0])>1:
            deshabilitar_botones()
            num20.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia20)
    def func21():
        global elección,tablero
        anterior=num21["text"]
        color_anterior=num21["bg"]
        num21.config(text=elección)
        tablero[2][1]=elección
        def cerrar_advertencia21(event):
            habilitar_botones()
            num21.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[2][1]=anterior
        if num21["bg"]!="#02ac66":
            deshabilitar_botones()
            num21.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia21)
            
        elif dividir()[2].count(tablero[2][1])>1:
            deshabilitar_botones()
            num21.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia21)

        elif tablero[2].count(tablero[2][1])>1:
            deshabilitar_botones()
            num21.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia21)
                    
        elif invertir()[2].count(tablero[2][1])>1:
            deshabilitar_botones()
            num21.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia21)
    def func22():
        global elección,tablero
        anterior=num22["text"]
        color_anterior=num22["bg"]
        num22.config(text=elección)
        tablero[2][2]=elección
        def cerrar_advertencia22(event):
            habilitar_botones()
            num22.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[2][2]=anterior
        if num22["bg"]!="#02ac66":
            deshabilitar_botones()
            num22.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia22)
            
        elif dividir()[2].count(tablero[2][2])>1:
            deshabilitar_botones()
            num22.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia22)

        elif tablero[2].count(tablero[2][2])>1:
            deshabilitar_botones()
            num22.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia22)
                    
        elif invertir()[2].count(tablero[2][2])>1:
            deshabilitar_botones()
            num22.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia22)
    def func23():
        global elección,tablero
        anterior=num23["text"]
        color_anterior=num23["bg"]
        num23.config(text=elección)
        tablero[2][3]=elección
        def cerrar_advertencia23(event):
            habilitar_botones()
            num23.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[2][3]=anterior
        if num23["bg"]!="#02ac66":
            deshabilitar_botones()
            num23.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia23)
            
        elif dividir()[2].count(tablero[2][3])>1:
            deshabilitar_botones()
            num23.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia23)

        elif tablero[2].count(tablero[2][3])>1:
            deshabilitar_botones()
            num23.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia23)
                    
        elif invertir()[2].count(tablero[2][3])>1:
            deshabilitar_botones()
            num23.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia23)
    def func24():
        global elección,tablero
        anterior=num24["text"]
        color_anterior=num24["bg"]
        num24.config(text=elección)
        tablero[2][4]=elección
        def cerrar_advertencia24(event):
            habilitar_botones()
            num24.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[2][4]=anterior
        if num24["bg"]!="#02ac66":
            deshabilitar_botones()
            num24.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia24)
            
        elif dividir()[2].count(tablero[2][4])>1:
            deshabilitar_botones()
            num24.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia24)

        elif tablero[2].count(tablero[2][4])>1:
            deshabilitar_botones()
            num24.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia24)
                    
        elif invertir()[2].count(tablero[2][4])>1:
            deshabilitar_botones()
            num24.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia24)
    def func25():
        global elección,tablero
        anterior=num25["text"]
        color_anterior=num25["bg"]
        num25.config(text=elección)
        tablero[2][5]=elección
        def cerrar_advertencia25(event):
            habilitar_botones()
            num25.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[2][5]=anterior
        if num25["bg"]!="#02ac66":
            deshabilitar_botones()
            num25.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia25)
            
        elif dividir()[2].count(tablero[2][5])>1:
            deshabilitar_botones()
            num25.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia25)

        elif tablero[2].count(tablero[2][5])>1:
            deshabilitar_botones()
            num25.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia25)
                    
        elif invertir()[2].count(tablero[2][5])>1:
            deshabilitar_botones()
            num25.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia25)
    def func26():
        global elección,tablero
        anterior=num26["text"]
        color_anterior=num26["bg"]
        num26.config(text=elección)
        tablero[2][6]=elección
        def cerrar_advertencia26(event):
            habilitar_botones()
            num26.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[2][6]=anterior
        if num26["bg"]!="#02ac66":
            deshabilitar_botones()
            num26.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia26)
            
        elif dividir()[2].count(tablero[2][6])>1:
            deshabilitar_botones()
            num26.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia26)

        elif tablero[2].count(tablero[2][6])>1:
            deshabilitar_botones()
            num26.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia26)
                    
        elif invertir()[2].count(tablero[2][6])>1:
            deshabilitar_botones()
            num26.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia26)
    def func27():
        global elección,tablero
        anterior=num27["text"]
        color_anterior=num27["bg"]
        num27.config(text=elección)
        tablero[2][7]=elección
        def cerrar_advertencia27(event):
            habilitar_botones()
            num27.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[2][7]=anterior
        if num27["bg"]!="#02ac66":
            deshabilitar_botones()
            num27.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia27)
            
        elif dividir()[2].count(tablero[2][7])>1:
            deshabilitar_botones()
            num27.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia27)

        elif tablero[2].count(tablero[2][7])>1:
            deshabilitar_botones()
            num27.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia27)
                    
        elif invertir()[2].count(tablero[2][7])>1:
            deshabilitar_botones()
            num27.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia27)
    def func28():
        global elección,tablero
        anterior=num28["text"]
        color_anterior=num28["bg"]
        num28.config(text=elección)
        tablero[2][8]=elección
        def cerrar_advertencia28(event):
            habilitar_botones()
            num28.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[2][8]=anterior
        if num28["bg"]!="#02ac66":
            deshabilitar_botones()
            num28.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia28)
            
        elif dividir()[2].count(tablero[2][8])>1:
            deshabilitar_botones()
            num28.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia28)

        elif tablero[2].count(tablero[2][8])>1:
            deshabilitar_botones()
            num28.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia28)
                    
        elif invertir()[2].count(tablero[2][8])>1:
            deshabilitar_botones()
            num28.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia28)
    def func30():
        global elección,tablero
        anterior=num30["text"]
        color_anterior=num30["bg"]
        num30.config(text=elección)
        tablero[3][0]=elección
        def cerrar_advertencia30(event):
            habilitar_botones()
            num30.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[3][0]=anterior
        if num30["bg"]!="#02ac66":
            deshabilitar_botones()
            num30.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia30)
            
        elif dividir()[3].count(tablero[3][0])>1:
            deshabilitar_botones()
            num30.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia30)

        elif tablero[3].count(tablero[3][0])>1:
            deshabilitar_botones()
            num30.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia30)
                    
        elif invertir()[3].count(tablero[3][0])>1:
            deshabilitar_botones()
            num30.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia30)
    def func31():
        global elección,tablero
        anterior=num31["text"]
        color_anterior=num31["bg"]
        num31.config(text=elección)
        tablero[3][1]=elección
        def cerrar_advertencia31(event):
            habilitar_botones()
            num31.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[3][1]=anterior
        if num31["bg"]!="#02ac66":
            deshabilitar_botones()
            num31.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia31)
            
        elif dividir()[3].count(tablero[3][1])>1:
            deshabilitar_botones()
            num31.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia31)

        elif tablero[3].count(tablero[3][1])>1:
            deshabilitar_botones()
            num31.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia31)
                    
        elif invertir()[3].count(tablero[3][1])>1:
            deshabilitar_botones()
            num31.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia31)
    def func32():
        global elección,tablero
        anterior=num32["text"]
        color_anterior=num32["bg"]
        num32.config(text=elección)
        tablero[3][2]=elección
        def cerrar_advertencia32(event):
            habilitar_botones()
            num32.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[3][2]=anterior
        if num32["bg"]!="#02ac66":
            deshabilitar_botones()
            num32.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia32)
            
        elif dividir()[3].count(tablero[3][2])>1:
            deshabilitar_botones()
            num32.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia32)

        elif tablero[3].count(tablero[3][2])>1:
            deshabilitar_botones()
            num32.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia32)
                    
        elif invertir()[3].count(tablero[3][2])>1:
            deshabilitar_botones()
            num32.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia32)
    def func33():
        global elección,tablero
        anterior=num33["text"]
        color_anterior=num33["bg"]
        num33.config(text=elección)
        tablero[3][3]=elección
        def cerrar_advertencia33(event):
            habilitar_botones()
            num33.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[3][3]=anterior
        if num33["bg"]!="#02ac66":
            deshabilitar_botones()
            num33.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia33)
            
        elif dividir()[3].count(tablero[3][3])>1:
            deshabilitar_botones()
            num33.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia33)

        elif tablero[3].count(tablero[3][3])>1:
            deshabilitar_botones()
            num33.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia33)
                    
        elif invertir()[3].count(tablero[3][3])>1:
            deshabilitar_botones()
            num33.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia33)
    def func34():
        global elección,tablero
        anterior=num34["text"]
        color_anterior=num34["bg"]
        num34.config(text=elección)
        tablero[3][4]=elección
        def cerrar_advertencia34(event):
            habilitar_botones()
            num34.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[3][4]=anterior
        if num34["bg"]!="#02ac66":
            deshabilitar_botones()
            num34.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia34)
            
        elif dividir()[3].count(tablero[3][4])>1:
            deshabilitar_botones()
            num34.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia34)

        elif tablero[3].count(tablero[3][4])>1:
            deshabilitar_botones()
            num34.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia34)
                    
        elif invertir()[3].count(tablero[3][4])>1:
            deshabilitar_botones()
            num34.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia34)
    def func35():
        global elección,tablero
        anterior=num35["text"]
        color_anterior=num35["bg"]
        num35.config(text=elección)
        tablero[3][5]=elección
        def cerrar_advertencia35(event):
            habilitar_botones()
            num35.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[3][5]=anterior
        if num35["bg"]!="#02ac66":
            deshabilitar_botones()
            num35.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia35)
            
        elif dividir()[3].count(tablero[3][5])>1:
            deshabilitar_botones()
            num35.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia35)

        elif tablero[3].count(tablero[3][5])>1:
            deshabilitar_botones()
            num35.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia35)
                    
        elif invertir()[3].count(tablero[3][5])>1:
            deshabilitar_botones()
            num35.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia35)
    def func36():
        global elección,tablero
        anterior=num36["text"]
        color_anterior=num36["bg"]
        num36.config(text=elección)
        tablero[3][6]=elección
        def cerrar_advertencia36(event):
            habilitar_botones()
            num36.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[3][6]=anterior
        if num36["bg"]!="#02ac66":
            deshabilitar_botones()
            num36.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia36)
            
        elif dividir()[3].count(tablero[3][6])>1:
            deshabilitar_botones()
            num36.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia36)

        elif tablero[3].count(tablero[3][6])>1:
            deshabilitar_botones()
            num36.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia36)
                    
        elif invertir()[3].count(tablero[3][6])>1:
            deshabilitar_botones()
            num36.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia36)
    def func37():
        global elección,tablero
        anterior=num37["text"]
        color_anterior=num37["bg"]
        num37.config(text=elección)
        tablero[3][7]=elección
        def cerrar_advertencia37(event):
            habilitar_botones()
            num37.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[3][7]=anterior
        if num37["bg"]!="#02ac66":
            deshabilitar_botones()
            num37.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia37)
            
        elif dividir()[3].count(tablero[3][7])>1:
            deshabilitar_botones()
            num37.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia37)

        elif tablero[3].count(tablero[3][7])>1:
            deshabilitar_botones()
            num37.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia37)
                    
        elif invertir()[3].count(tablero[3][7])>1:
            deshabilitar_botones()
            num37.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia37)
    def func38():
        global elección,tablero
        anterior=num38["text"]
        color_anterior=num38["bg"]
        num38.config(text=elección)
        tablero[3][8]=elección
        def cerrar_advertencia38(event):
            habilitar_botones()
            num38.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[3][8]=anterior
        if num38["bg"]!="#02ac66":
            deshabilitar_botones()
            num38.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia38)
            
        elif dividir()[3].count(tablero[3][8])>1:
            deshabilitar_botones()
            num38.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia38)

        elif tablero[3].count(tablero[3][8])>1:
            deshabilitar_botones()
            num38.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia38)
                    
        elif invertir()[3].count(tablero[3][8])>1:
            deshabilitar_botones()
            num38.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia38)
    def func40():
        global elección,tablero
        anterior=num40["text"]
        color_anterior=num40["bg"]
        num40.config(text=elección)
        tablero[4][0]=elección
        def cerrar_advertencia40(event):
            habilitar_botones()
            num40.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[4][0]=anterior
        if num40["bg"]!="#02ac66":
            deshabilitar_botones()
            num40.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia40)
            
        elif dividir()[4].count(tablero[4][0])>1:
            deshabilitar_botones()
            num40.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia40)

        elif tablero[4].count(tablero[4][0])>1:
            deshabilitar_botones()
            num40.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia40)
                    
        elif invertir()[4].count(tablero[4][0])>1:
            deshabilitar_botones()
            num40.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia40)
    def func41():
        global elección,tablero
        anterior=num41["text"]
        color_anterior=num41["bg"]
        num41.config(text=elección)
        tablero[4][1]=elección
        def cerrar_advertencia41(event):
            habilitar_botones()
            num41.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[4][1]=anterior
        if num41["bg"]!="#02ac66":
            deshabilitar_botones()
            num41.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia41)
            
        elif dividir()[4].count(tablero[4][1])>1:
            deshabilitar_botones()
            num41.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia41)

        elif tablero[4].count(tablero[4][1])>1:
            deshabilitar_botones()
            num41.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia41)
                    
        elif invertir()[4].count(tablero[4][1])>1:
            deshabilitar_botones()
            num41.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia41)
    def func42():
        global elección,tablero
        anterior=num42["text"]
        color_anterior=num42["bg"]
        num42.config(text=elección)
        tablero[4][2]=elección
        def cerrar_advertencia42(event):
            habilitar_botones()
            num42.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[4][2]=anterior
        if num42["bg"]!="#02ac66":
            deshabilitar_botones()
            num42.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia42)
            
        elif dividir()[4].count(tablero[4][2])>1:
            deshabilitar_botones()
            num42.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia42)

        elif tablero[4].count(tablero[4][2])>1:
            deshabilitar_botones()
            num42.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia42)
                    
        elif invertir()[4].count(tablero[4][2])>1:
            deshabilitar_botones()
            num42.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia42)
    def func43():
        global elección,tablero
        anterior=num43["text"]
        color_anterior=num43["bg"]
        num43.config(text=elección)
        tablero[4][3]=elección
        def cerrar_advertencia43(event):
            habilitar_botones()
            num43.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[4][3]=anterior
        if num43["bg"]!="#02ac66":
            deshabilitar_botones()
            num43.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia43)
            
        elif dividir()[4].count(tablero[4][3])>1:
            deshabilitar_botones()
            num43.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia43)

        elif tablero[4].count(tablero[4][3])>1:
            deshabilitar_botones()
            num43.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia43)
                    
        elif invertir()[4].count(tablero[4][3])>1:
            deshabilitar_botones()
            num43.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia43)
    def func44():
        global elección,tablero
        anterior=num44["text"]
        color_anterior=num44["bg"]
        num44.config(text=elección)
        tablero[4][4]=elección
        def cerrar_advertencia44(event):
            habilitar_botones()
            num44.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[4][4]=anterior
        if num44["bg"]!="#02ac66":
            deshabilitar_botones()
            num44.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia44)
            
        elif dividir()[4].count(tablero[4][4])>1:
            deshabilitar_botones()
            num44.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia44)

        elif tablero[4].count(tablero[4][4])>1:
            deshabilitar_botones()
            num44.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia44)
                    
        elif invertir()[4].count(tablero[4][4])>1:
            deshabilitar_botones()
            num44.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia44)
    def func45():
        global elección,tablero
        anterior=num45["text"]
        color_anterior=num45["bg"]
        num45.config(text=elección)
        tablero[4][5]=elección
        def cerrar_advertencia45(event):
            habilitar_botones()
            num45.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[4][5]=anterior
        if num45["bg"]!="#02ac66":
            deshabilitar_botones()
            num45.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia45)
            
        elif dividir()[4].count(tablero[4][5])>1:
            deshabilitar_botones()
            num45.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia45)

        elif tablero[4].count(tablero[4][5])>1:
            deshabilitar_botones()
            num45.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia45)
                    
        elif invertir()[4].count(tablero[4][5])>1:
            deshabilitar_botones()
            num45.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia45)
    def func46():
        global elección,tablero
        anterior=num46["text"]
        color_anterior=num46["bg"]
        num46.config(text=elección)
        tablero[4][6]=elección
        def cerrar_advertencia46(event):
            habilitar_botones()
            num46.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[4][6]=anterior
        if num46["bg"]!="#02ac66":
            deshabilitar_botones()
            num46.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia46)
            
        elif dividir()[4].count(tablero[4][6])>1:
            deshabilitar_botones()
            num46.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia46)

        elif tablero[4].count(tablero[4][6])>1:
            deshabilitar_botones()
            num46.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia46)
                    
        elif invertir()[4].count(tablero[4][6])>1:
            deshabilitar_botones()
            num46.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia46)
    def func47():
        global elección,tablero
        anterior=num47["text"]
        color_anterior=num47["bg"]
        num47.config(text=elección)
        tablero[4][7]=elección
        def cerrar_advertencia47(event):
            habilitar_botones()
            num47.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[4][7]=anterior
        if num47["bg"]!="#02ac66":
            deshabilitar_botones()
            num47.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia47)
            
        elif dividir()[4].count(tablero[4][7])>1:
            deshabilitar_botones()
            num47.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia47)

        elif tablero[4].count(tablero[4][7])>1:
            deshabilitar_botones()
            num47.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia47)
                    
        elif invertir()[4].count(tablero[4][7])>1:
            deshabilitar_botones()
            num47.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia47)
    def func48():
        global elección,tablero
        anterior=num48["text"]
        color_anterior=num48["bg"]
        num48.config(text=elección)
        tablero[4][8]=elección
        def cerrar_advertencia48(event):
            habilitar_botones()
            num48.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[4][8]=anterior
        if num48["bg"]!="#02ac66":
            deshabilitar_botones()
            num48.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia48)
            
        elif dividir()[4].count(tablero[4][8])>1:
            deshabilitar_botones()
            num48.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia48)

        elif tablero[4].count(tablero[4][8])>1:
            deshabilitar_botones()
            num48.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia48)
                    
        elif invertir()[4].count(tablero[4][8])>1:
            deshabilitar_botones()
            num48.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia48)
    def func50():
        global elección,tablero
        anterior=num50["text"]
        color_anterior=num50["bg"]
        num50.config(text=elección)
        tablero[5][0]=elección
        def cerrar_advertencia50(event):
            habilitar_botones()
            num50.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[5][0]=anterior
        if num50["bg"]!="#02ac66":
            deshabilitar_botones()
            num50.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia50)
            
        elif dividir()[5].count(tablero[5][0])>1:
            deshabilitar_botones()
            num50.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia50)

        elif tablero[5].count(tablero[5][0])>1:
            deshabilitar_botones()
            num50.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia50)
                    
        elif invertir()[5].count(tablero[5][0])>1:
            deshabilitar_botones()
            num50.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia50)
    def func51():
        global elección,tablero
        anterior=num51["text"]
        color_anterior=num51["bg"]
        num51.config(text=elección)
        tablero[5][1]=elección
        def cerrar_advertencia51(event):
            habilitar_botones()
            num51.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[5][1]=anterior
        if num51["bg"]!="#02ac66":
            deshabilitar_botones()
            num51.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia51)
            
        elif dividir()[5].count(tablero[5][1])>1:
            deshabilitar_botones()
            num51.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia51)

        elif tablero[5].count(tablero[5][1])>1:
            deshabilitar_botones()
            num51.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia51)
                    
        elif invertir()[5].count(tablero[5][1])>1:
            deshabilitar_botones()
            num51.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia51)
    def func52():
        global elección,tablero
        anterior=num52["text"]
        color_anterior=num52["bg"]
        num52.config(text=elección)
        tablero[5][2]=elección
        def cerrar_advertencia52(event):
            habilitar_botones()
            num52.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[5][2]=anterior
        if num52["bg"]!="#02ac66":
            deshabilitar_botones()
            num52.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia52)
            
        elif dividir()[5].count(tablero[5][2])>1:
            deshabilitar_botones()
            num52.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia52)

        elif tablero[5].count(tablero[5][2])>1:
            deshabilitar_botones()
            num52.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia52)
                    
        elif invertir()[5].count(tablero[5][2])>1:
            deshabilitar_botones()
            num52.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia52)
    def func53():
        global elección,tablero
        anterior=num53["text"]
        color_anterior=num53["bg"]
        num53.config(text=elección)
        tablero[5][3]=elección
        def cerrar_advertencia53(event):
            habilitar_botones()
            num53.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[5][3]=anterior
        if num53["bg"]!="#02ac66":
            deshabilitar_botones()
            num53.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia53)
            
        elif dividir()[5].count(tablero[5][3])>1:
            deshabilitar_botones()
            num53.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia53)

        elif tablero[5].count(tablero[5][3])>1:
            deshabilitar_botones()
            num53.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia53)
                    
        elif invertir()[5].count(tablero[5][3])>1:
            deshabilitar_botones()
            num53.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia53)
    def func54():
        global elección,tablero
        anterior=num54["text"]
        color_anterior=num54["bg"]
        num54.config(text=elección)
        tablero[5][4]=elección
        def cerrar_advertencia54(event):
            habilitar_botones()
            num54.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[5][4]=anterior
        if num54["bg"]!="#02ac66":
            deshabilitar_botones()
            num54.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia54)
            
        elif dividir()[5].count(tablero[5][4])>1:
            deshabilitar_botones()
            num54.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia54)

        elif tablero[5].count(tablero[5][4])>1:
            deshabilitar_botones()
            num54.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia54)
                    
        elif invertir()[5].count(tablero[5][4])>1:
            deshabilitar_botones()
            num54.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia54)
    def func55():
        global elección,tablero
        anterior=num55["text"]
        color_anterior=num55["bg"]
        num55.config(text=elección)
        tablero[5][5]=elección
        def cerrar_advertencia55(event):
            habilitar_botones()
            num55.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[5][5]=anterior
        if num55["bg"]!="#02ac66":
            deshabilitar_botones()
            num55.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia55)
            
        elif dividir()[5].count(tablero[5][5])>1:
            deshabilitar_botones()
            num55.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia55)

        elif tablero[5].count(tablero[5][5])>1:
            deshabilitar_botones()
            num55.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia55)
                    
        elif invertir()[5].count(tablero[5][5])>1:
            deshabilitar_botones()
            num55.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia55)
    def func56():
        global elección,tablero
        anterior=num56["text"]
        color_anterior=num56["bg"]
        num56.config(text=elección)
        tablero[5][6]=elección
        def cerrar_advertencia56(event):
            habilitar_botones()
            num56.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[5][6]=anterior
        if num56["bg"]!="#02ac66":
            deshabilitar_botones()
            num56.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia56)
            
        elif dividir()[5].count(tablero[5][6])>1:
            deshabilitar_botones()
            num56.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia56)

        elif tablero[5].count(tablero[5][6])>1:
            deshabilitar_botones()
            num56.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia56)
                    
        elif invertir()[5].count(tablero[5][6])>1:
            deshabilitar_botones()
            num56.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia56)
    def func57():
        global elección,tablero
        anterior=num57["text"]
        color_anterior=num57["bg"]
        num57.config(text=elección)
        tablero[5][7]=elección
        def cerrar_advertencia57(event):
            habilitar_botones()
            num57.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[5][7]=anterior
        if num57["bg"]!="#02ac66":
            deshabilitar_botones()
            num57.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia57)
            
        elif dividir()[5].count(tablero[5][7])>1:
            deshabilitar_botones()
            num57.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia57)

        elif tablero[5].count(tablero[5][7])>1:
            deshabilitar_botones()
            num57.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia57)
                    
        elif invertir()[5].count(tablero[5][7])>1:
            deshabilitar_botones()
            num57.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia57)
    def func58():
        global elección,tablero
        anterior=num58["text"]
        color_anterior=num58["bg"]
        num58.config(text=elección)
        tablero[5][8]=elección
        def cerrar_advertencia58(event):
            habilitar_botones()
            num58.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[5][8]=anterior
        if num58["bg"]!="#02ac66":
            deshabilitar_botones()
            num58.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia58)
            
        elif dividir()[5].count(tablero[5][8])>1:
            deshabilitar_botones()
            num58.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia58)

        elif tablero[5].count(tablero[5][8])>1:
            deshabilitar_botones()
            num58.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia58)
                    
        elif invertir()[5].count(tablero[5][8])>1:
            deshabilitar_botones()
            num58.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia58)
    def func60():
        global elección,tablero
        anterior=num60["text"]
        color_anterior=num60["bg"]
        num60.config(text=elección)
        tablero[6][0]=elección
        def cerrar_advertencia60(event):
            habilitar_botones()
            num60.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[6][0]=anterior
        if num60["bg"]!="#02ac66":
            deshabilitar_botones()
            num60.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia60)
            
        elif dividir()[6].count(tablero[6][0])>1:
            deshabilitar_botones()
            num60.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia60)

        elif tablero[6].count(tablero[6][0])>1:
            deshabilitar_botones()
            num60.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia60)
                    
        elif invertir()[6].count(tablero[6][0])>1:
            deshabilitar_botones()
            num60.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia60)
    def func61():
        global elección,tablero
        anterior=num61["text"]
        color_anterior=num61["bg"]
        num61.config(text=elección)
        tablero[6][1]=elección
        def cerrar_advertencia61(event):
            habilitar_botones()
            num61.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[6][1]=anterior
        if num61["bg"]!="#02ac66":
            deshabilitar_botones()
            num61.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia61)
            
        elif dividir()[6].count(tablero[6][1])>1:
            deshabilitar_botones()
            num61.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia61)

        elif tablero[6].count(tablero[6][1])>1:
            deshabilitar_botones()
            num61.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia61)
                    
        elif invertir()[6].count(tablero[6][1])>1:
            deshabilitar_botones()
            num61.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia61)
    def func62():
        global elección,tablero
        anterior=num62["text"]
        color_anterior=num62["bg"]
        num62.config(text=elección)
        tablero[6][2]=elección
        def cerrar_advertencia62(event):
            habilitar_botones()
            num62.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[6][2]=anterior
        if num62["bg"]!="#02ac66":
            deshabilitar_botones()
            num62.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia62)
            
        elif dividir()[6].count(tablero[6][2])>1:
            deshabilitar_botones()
            num62.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia62)

        elif tablero[6].count(tablero[6][2])>1:
            deshabilitar_botones()
            num62.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia62)
                    
        elif invertir()[6].count(tablero[6][2])>1:
            deshabilitar_botones()
            num62.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia62)
    def func63():
        global elección,tablero
        anterior=num63["text"]
        color_anterior=num63["bg"]
        num63.config(text=elección)
        tablero[6][3]=elección
        def cerrar_advertencia63(event):
            habilitar_botones()
            num63.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[6][3]=anterior
        if num63["bg"]!="#02ac66":
            deshabilitar_botones()
            num63.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia63)
            
        elif dividir()[6].count(tablero[6][3])>1:
            deshabilitar_botones()
            num63.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia63)

        elif tablero[6].count(tablero[6][3])>1:
            deshabilitar_botones()
            num63.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia63)
                    
        elif invertir()[6].count(tablero[6][3])>1:
            deshabilitar_botones()
            num63.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia63)
    def func64():
        global elección,tablero
        anterior=num64["text"]
        color_anterior=num64["bg"]
        num64.config(text=elección)
        tablero[6][4]=elección
        def cerrar_advertencia64(event):
            habilitar_botones()
            num64.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[6][4]=anterior
        if num64["bg"]!="#02ac66":
            deshabilitar_botones()
            num64.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia64)
            
        elif dividir()[6].count(tablero[6][4])>1:
            deshabilitar_botones()
            num64.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia64)

        elif tablero[6].count(tablero[6][4])>1:
            deshabilitar_botones()
            num64.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia64)
                    
        elif invertir()[6].count(tablero[6][4])>1:
            deshabilitar_botones()
            num64.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia64)
    def func65():
        global elección,tablero
        anterior=num65["text"]
        color_anterior=num65["bg"]
        num65.config(text=elección)
        tablero[6][5]=elección
        def cerrar_advertencia65(event):
            habilitar_botones()
            num65.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[6][5]=anterior
        if num65["bg"]!="#02ac66":
            deshabilitar_botones()
            num65.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia65)
            
        elif dividir()[6].count(tablero[6][5])>1:
            deshabilitar_botones()
            num65.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia65)

        elif tablero[6].count(tablero[6][5])>1:
            deshabilitar_botones()
            num65.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia65)
                    
        elif invertir()[6].count(tablero[6][5])>1:
            deshabilitar_botones()
            num65.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia65)
    def func66():
        global elección,tablero
        anterior=num66["text"]
        color_anterior=num66["bg"]
        num66.config(text=elección)
        tablero[6][6]=elección
        def cerrar_advertencia66(event):
            habilitar_botones()
            num66.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[6][6]=anterior
        if num66["bg"]!="#02ac66":
            deshabilitar_botones()
            num66.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia66)
            
        elif dividir()[6].count(tablero[6][6])>1:
            deshabilitar_botones()
            num66.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia66)

        elif tablero[6].count(tablero[6][6])>1:
            deshabilitar_botones()
            num66.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia66)
                    
        elif invertir()[6].count(tablero[6][6])>1:
            deshabilitar_botones()
            num66.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia66)
    def func67():
        global elección,tablero
        anterior=num67["text"]
        color_anterior=num67["bg"]
        num67.config(text=elección)
        tablero[6][7]=elección
        def cerrar_advertencia67(event):
            habilitar_botones()
            num67.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[6][7]=anterior
        if num67["bg"]!="#02ac66":
            deshabilitar_botones()
            num67.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia67)
            
        elif dividir()[6].count(tablero[6][7])>1:
            deshabilitar_botones()
            num67.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia67)

        elif tablero[6].count(tablero[6][7])>1:
            deshabilitar_botones()
            num67.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia67)
                    
        elif invertir()[6].count(tablero[6][7])>1:
            deshabilitar_botones()
            num67.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia67)
    def func68():
        global elección,tablero
        anterior=num68["text"]
        color_anterior=num68["bg"]
        num68.config(text=elección)
        tablero[6][8]=elección
        def cerrar_advertencia68(event):
            habilitar_botones()
            num68.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[6][8]=anterior
        if num68["bg"]!="#02ac66":
            deshabilitar_botones()
            num68.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia68)
            
        elif dividir()[6].count(tablero[6][8])>1:
            deshabilitar_botones()
            num68.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia68)

        elif tablero[6].count(tablero[6][8])>1:
            deshabilitar_botones()
            num68.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia68)
                    
        elif invertir()[6].count(tablero[6][8])>1:
            deshabilitar_botones()
            num68.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia68)
    def func70():
        global elección,tablero
        anterior=num70["text"]
        color_anterior=num70["bg"]
        num70.config(text=elección)
        tablero[7][0]=elección
        def cerrar_advertencia70(event):
            habilitar_botones()
            num70.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[7][0]=anterior
        if num70["bg"]!="#02ac66":
            deshabilitar_botones()
            num70.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia70)
            
        elif dividir()[7].count(tablero[7][0])>1:
            deshabilitar_botones()
            num70.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia70)

        elif tablero[7].count(tablero[7][0])>1:
            deshabilitar_botones()
            num70.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia70)
                    
        elif invertir()[7].count(tablero[7][0])>1:
            deshabilitar_botones()
            num70.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia70)
    def func71():
        global elección,tablero
        anterior=num71["text"]
        color_anterior=num71["bg"]
        num71.config(text=elección)
        tablero[7][1]=elección
        def cerrar_advertencia71(event):
            habilitar_botones()
            num71.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[7][1]=anterior
        if num71["bg"]!="#02ac66":
            deshabilitar_botones()
            num71.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia71)
            
        elif dividir()[7].count(tablero[7][1])>1:
            deshabilitar_botones()
            num71.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia71)

        elif tablero[7].count(tablero[7][1])>1:
            deshabilitar_botones()
            num71.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia71)
                    
        elif invertir()[7].count(tablero[7][1])>1:
            deshabilitar_botones()
            num71.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia71)
    def func72():
        global elección,tablero
        anterior=num72["text"]
        color_anterior=num72["bg"]
        num72.config(text=elección)
        tablero[7][2]=elección
        def cerrar_advertencia72(event):
            habilitar_botones()
            num72.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[7][2]=anterior
        if num72["bg"]!="#02ac66":
            deshabilitar_botones()
            num72.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia72)
            
        elif dividir()[7].count(tablero[7][2])>1:
            deshabilitar_botones()
            num72.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia72)

        elif tablero[7].count(tablero[7][2])>1:
            deshabilitar_botones()
            num72.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia72)
                    
        elif invertir()[7].count(tablero[7][2])>1:
            deshabilitar_botones()
            num72.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia72)
    def func73():
        global elección,tablero
        anterior=num73["text"]
        color_anterior=num73["bg"]
        num73.config(text=elección)
        tablero[7][3]=elección
        def cerrar_advertencia73(event):
            habilitar_botones()
            num73.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[7][3]=anterior
        if num73["bg"]!="#02ac66":
            deshabilitar_botones()
            num73.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia73)
            
        elif dividir()[7].count(tablero[7][3])>1:
            deshabilitar_botones()
            num73.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia73)

        elif tablero[7].count(tablero[7][3])>1:
            deshabilitar_botones()
            num73.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia73)
                    
        elif invertir()[7].count(tablero[7][3])>1:
            deshabilitar_botones()
            num73.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia73)
    def func74():
        global elección,tablero
        anterior=num74["text"]
        color_anterior=num74["bg"]
        num74.config(text=elección)
        tablero[7][4]=elección
        def cerrar_advertencia74(event):
            habilitar_botones()
            num74.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[7][4]=anterior
        if num74["bg"]!="#02ac66":
            deshabilitar_botones()
            num74.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia74)
            
        elif dividir()[7].count(tablero[7][4])>1:
            deshabilitar_botones()
            num74.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia74)

        elif tablero[7].count(tablero[7][4])>1:
            deshabilitar_botones()
            num74.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia74)
                    
        elif invertir()[7].count(tablero[7][4])>1:
            deshabilitar_botones()
            num74.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia74)
    def func75():
        global elección,tablero
        anterior=num75["text"]
        color_anterior=num75["bg"]
        num75.config(text=elección)
        tablero[7][5]=elección
        def cerrar_advertencia75(event):
            habilitar_botones()
            num75.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[7][5]=anterior
        if num75["bg"]!="#02ac66":
            deshabilitar_botones()
            num75.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia75)
            
        elif dividir()[7].count(tablero[7][5])>1:
            deshabilitar_botones()
            num75.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia75)

        elif tablero[7].count(tablero[7][5])>1:
            deshabilitar_botones()
            num75.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia75)
                    
        elif invertir()[7].count(tablero[7][5])>1:
            deshabilitar_botones()
            num75.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia75)
    def func76():
        global elección,tablero
        anterior=num76["text"]
        color_anterior=num76["bg"]
        num76.config(text=elección)
        tablero[7][6]=elección
        def cerrar_advertencia76(event):
            habilitar_botones()
            num76.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[7][6]=anterior
        if num76["bg"]!="#02ac66":
            deshabilitar_botones()
            num76.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia76)
            
        elif dividir()[7].count(tablero[7][6])>1:
            deshabilitar_botones()
            num76.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia76)

        elif tablero[7].count(tablero[7][6])>1:
            deshabilitar_botones()
            num76.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia76)
                    
        elif invertir()[7].count(tablero[7][6])>1:
            deshabilitar_botones()
            num76.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia76)
    def func77():
        global elección,tablero
        anterior=num77["text"]
        color_anterior=num77["bg"]
        num77.config(text=elección)
        tablero[7][7]=elección
        def cerrar_advertencia77(event):
            habilitar_botones()
            num77.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[7][7]=anterior
        if num77["bg"]!="#02ac66":
            deshabilitar_botones()
            num77.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia77)
            
        elif dividir()[7].count(tablero[7][7])>1:
            deshabilitar_botones()
            num77.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia77)

        elif tablero[7].count(tablero[7][7])>1:
            deshabilitar_botones()
            num77.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia77)
                    
        elif invertir()[7].count(tablero[7][7])>1:
            deshabilitar_botones()
            num77.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia77)
    def func78():
        global elección,tablero
        anterior=num78["text"]
        color_anterior=num78["bg"]
        num78.config(text=elección)
        tablero[7][8]=elección
        def cerrar_advertencia78(event):
            habilitar_botones()
            num78.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[7][8]=anterior
        if num78["bg"]!="#02ac66":
            deshabilitar_botones()
            num78.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia78)
            
        elif dividir()[7].count(tablero[7][8])>1:
            deshabilitar_botones()
            num78.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia78)

        elif tablero[7].count(tablero[7][8])>1:
            deshabilitar_botones()
            num78.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia78)
                    
        elif invertir()[7].count(tablero[7][8])>1:
            deshabilitar_botones()
            num78.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia78)
    def func80():
        global elección,tablero
        anterior=num80["text"]
        color_anterior=num80["bg"]
        num80.config(text=elección)
        tablero[8][0]=elección
        def cerrar_advertencia80(event):
            habilitar_botones()
            num80.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[8][0]=anterior
        if num80["bg"]!="#02ac66":
            deshabilitar_botones()
            num80.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia80)
            
        elif dividir()[8].count(tablero[8][0])>1:
            deshabilitar_botones()
            num80.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia80)

        elif tablero[8].count(tablero[8][0])>1:
            deshabilitar_botones()
            num80.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia80)
                    
        elif invertir()[8].count(tablero[8][0])>1:
            deshabilitar_botones()
            num80.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia80)
    def func81():
        global elección,tablero
        anterior=num81["text"]
        color_anterior=num81["bg"]
        num81.config(text=elección)
        tablero[8][1]=elección
        def cerrar_advertencia81(event):
            habilitar_botones()
            num81.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[8][1]=anterior
        if num81["bg"]!="#02ac66":
            deshabilitar_botones()
            num81.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia81)
            
        elif dividir()[8].count(tablero[8][1])>1:
            deshabilitar_botones()
            num81.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia81)

        elif tablero[8].count(tablero[8][1])>1:
            deshabilitar_botones()
            num81.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia81)
                    
        elif invertir()[8].count(tablero[8][1])>1:
            deshabilitar_botones()
            num81.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia81)
    def func82():
        global elección,tablero
        anterior=num82["text"]
        color_anterior=num82["bg"]
        num82.config(text=elección)
        tablero[8][2]=elección
        def cerrar_advertencia82(event):
            habilitar_botones()
            num82.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[8][2]=anterior
        if num82["bg"]!="#02ac66":
            deshabilitar_botones()
            num82.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia82)
            
        elif dividir()[8].count(tablero[8][2])>1:
            deshabilitar_botones()
            num82.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia82)

        elif tablero[8].count(tablero[8][2])>1:
            deshabilitar_botones()
            num82.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia82)
                    
        elif invertir()[8].count(tablero[8][2])>1:
            deshabilitar_botones()
            num82.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia82)
    def func83():
        global elección,tablero
        anterior=num83["text"]
        color_anterior=num83["bg"]
        num83.config(text=elección)
        tablero[8][3]=elección
        def cerrar_advertencia83(event):
            habilitar_botones()
            num83.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[8][3]=anterior
        if num83["bg"]!="#02ac66":
            deshabilitar_botones()
            num83.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia83)
            
        elif dividir()[8].count(tablero[8][3])>1:
            deshabilitar_botones()
            num83.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia83)

        elif tablero[8].count(tablero[8][3])>1:
            deshabilitar_botones()
            num83.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia83)
                    
        elif invertir()[8].count(tablero[8][3])>1:
            deshabilitar_botones()
            num83.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia83)
    def func84():
        global elección,tablero
        anterior=num84["text"]
        color_anterior=num84["bg"]
        num84.config(text=elección)
        tablero[8][4]=elección
        def cerrar_advertencia84(event):
            habilitar_botones()
            num84.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[8][4]=anterior
        if num84["bg"]!="#02ac66":
            deshabilitar_botones()
            num84.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia84)
            
        elif dividir()[8].count(tablero[8][4])>1:
            deshabilitar_botones()
            num84.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia84)

        elif tablero[8].count(tablero[8][4])>1:
            deshabilitar_botones()
            num84.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia84)
                    
        elif invertir()[8].count(tablero[8][4])>1:
            deshabilitar_botones()
            num84.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia84)
    def func85():
        global elección,tablero
        anterior=num85["text"]
        color_anterior=num85["bg"]
        num85.config(text=elección)
        tablero[8][5]=elección
        def cerrar_advertencia85(event):
            habilitar_botones()
            num85.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[8][5]=anterior
        if num85["bg"]!="#02ac66":
            deshabilitar_botones()
            num85.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia85)
            
        elif dividir()[8].count(tablero[8][5])>1:
            deshabilitar_botones()
            num85.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia85)

        elif tablero[8].count(tablero[8][5])>1:
            deshabilitar_botones()
            num85.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia85)
                    
        elif invertir()[8].count(tablero[8][5])>1:
            deshabilitar_botones()
            num85.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia85)
    def func86():
        global elección,tablero
        anterior=num86["text"]
        color_anterior=num86["bg"]
        num86.config(text=elección)
        tablero[8][6]=elección
        def cerrar_advertencia86(event):
            habilitar_botones()
            num86.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[8][6]=anterior
        if num86["bg"]!="#02ac66":
            deshabilitar_botones()
            num86.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia86)
            
        elif dividir()[8].count(tablero[8][6])>1:
            deshabilitar_botones()
            num86.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia86)

        elif tablero[8].count(tablero[8][6])>1:
            deshabilitar_botones()
            num86.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia86)
                    
        elif invertir()[8].count(tablero[8][6])>1:
            deshabilitar_botones()
            num86.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia86)
    def func87():
        global elección,tablero
        anterior=num87["text"]
        color_anterior=num87["bg"]
        num87.config(text=elección)
        tablero[8][7]=elección
        def cerrar_advertencia87(event):
            habilitar_botones()
            num87.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[8][7]=anterior
        if num87["bg"]!="#02ac66":
            deshabilitar_botones()
            num87.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia87)
            
        elif dividir()[8].count(tablero[8][7])>1:
            deshabilitar_botones()
            num87.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia87)

        elif tablero[8].count(tablero[8][7])>1:
            deshabilitar_botones()
            num87.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia87)
                    
        elif invertir()[8].count(tablero[8][7])>1:
            deshabilitar_botones()
            num87.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia87)
    def func88():
        global elección,tablero
        anterior=num88["text"]
        color_anterior=num88["bg"]
        num88.config(text=elección)
        tablero[8][8]=elección
        def cerrar_advertencia88(event):
            habilitar_botones()
            num88.config(text=anterior,bg=color_anterior)
            lbl_advertencia_1.destroy()
            tablero[8][8]=anterior
        if num88["bg"]!="#02ac66":
            deshabilitar_botones()
            num88.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque la casilla\n contiene un elemento fijo")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia88)
            
        elif dividir()[8].count(tablero[8][8])>1:
            deshabilitar_botones()
            num88.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la cuadrícula")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia88)

        elif tablero[8].count(tablero[8][8])>1:
            deshabilitar_botones()
            num88.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la fila")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia88)
                    
        elif invertir()[8].count(tablero[8][8])>1:
            deshabilitar_botones()
            num88.config(bg="red")
            lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
            lbl_advertencia_1.config(text="Jugada no es válida porque el elemento ya\n está en la columna")
            lbl_advertencia_1.place(x=370,y=450)
            ventana_principal_juego.bind("<Return>", cerrar_advertencia88)
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


    """def convertir(n):
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

    # Dibuja el reloj en la pantalla
    def tic():
        global reloj, temporizador, configuración_reloj
        if configuración_reloj.get() == 1:
            lblClock['text'] = convertir(reloj)
        if configuración_reloj.get() == 3:
            lblTimer['text'] = convertir(temporizador)

    # Llama solo una vez al reloj
    tic()

    # Actualiza el cronometro
    def tac():
        global reloj, configuración_reloj, jugando
        # Sigue dibujando para estar actualizando el reloj
        tic()
        lblTimer.after(1000, tac)
        # Cada 1000 milisegundos llama a la funcion tac (after)
        if configuración_reloj.get() == 1 and jugando:
            reloj += 1

    def run_timer():
        global temporizador, configuración_reloj, jugando
        # Sigue dibujando para estar actualizando el reloj
        tic()
        # Cada 1000 milisegundos llama a la funcion tac (after)
        lblTimer.after(1000, run_timer)
        if configuración_reloj.get() == 3 and jugando:
            temporizador -= 1

    # Llama a tac una vez para que aparezca en pantalla
    tac()
    run_timer()
"""
    # Dibuja la matriz
    def draw(cuadrícula, matriz):
        for x in range(9):
            for y in range(9):
                # Si la matriz tiene un numero
                if (matriz[y][x]) != "":
                    # Se modifica la matriz  y se coloca ese nuemro con el color respectivo
                    cuadrícula[x][y].config(text=str(matriz[y][x]), bg="#e9bd15")
                else:
                    # Si la matriz tiene un cero, no se coloca un numero y se deja el fondo del mismo color
                    cuadrícula[x][y].config(bg="#02ac66")
                # Acomoda los labels segun la cuadricula
                cuadrícula[x][y].grid(column=x, row=y)
                
    def iniciarPartida():
        global grid, tablero, jugando, nombre_jugador, reloj, temporizador, configuración_reloj
        global horas, minutos, segundos
        jugando = False
        reloj = 0
        temporizador = horas * 3600 + minutos * 60 + segundos
        # Inicia la matriz con numeros del diccionario deseado
        escoger_partida()
        # Dibuja la matriz
        draw(grid, tablero)
        
        
        btnIniciarPartida.config(text="INICIAR \n  PARTIDA  ")
        #  Se habilita nuevamente el espacio para escribir el nombre
        entryNombre.config(state='normal')
        # Limpiar el entry, end=constante que va desde el inicio hasta el final
        entryNombre.delete(0, tk.END)
    """def iniciarPausarPartida():
        global jugando, nombre_jugador
        # Obtiene el nombre del jugador
        nombre_jugador = entryNombre.get()
        if nombre_jugador == "":
            # Envia mensaje de error si no se introduce el nombre
            messagebox.showerror("Nombre no asignado",
                                 "Debe ingresar el nombre del jugador antes de iniciar la partida")
        elif len(nombre_jugador) > 30:
            # Si el nombre ingresado es mayor a 30  retorna error
            messagebox.showerror("Nombre invalido", "El nombre del jugador debe contener maximo 30 caracteres")
        else:
            #  Disable : desabilita la ventana
            entryNombre.config(state='disabled')
            # Me niega el valor que tenga jugando
            jugando = not jugando
            # Si esta jugando muestre  el boton pausar
            if jugando:
                btnIniciarPartida.config(text="PAUSAR \n  PARTIDA  ")
            else:
                # Si no esta jugando muestre el boton de iniciar partida
                btnIniciarPartida.config(text="INICIAR \n  PARTIDA  ")

    def guardarJuego():
        global archivo_datos, nombre_jugador, tablero, jugando
        # si se esta jugando
        if jugando:
            # Abre el archivo
            archivo_para_escribir = open(archivo_datos, 'w')
            # Escribe  el nombre del jugador
            archivo_para_escribir.write(nombre_jugador + '\n')
            # Escribe la matriz como string
            archivo_para_escribir.write(str(tablero))
            # Se cierra el archivo
            archivo_para_escribir.close()
            messagebox.showinfo("Guardado", "Partida guardada")
        else:
            messagebox.showerror("Error", "No hay partida en curso")

    def cargarJuego():
        global archivo_datos, nombre_jugador, tablero, jugando, grid
        # Lee los datos guardados
        archivo_para_cargar = open(archivo_datos, 'r')
        datos = archivo_para_cargar.read()
        # Si no hay datos muestra el error
        if datos == "":
            messagebox.showerror("Error", "No hay partida guardad")
        else:
            # Me devuelve los datos separados
            lineas = datos.split('\n')
            # El nombre del jugador va a ser el primer elemento del string
            nombre_jugador = lineas[0]
            # Devuelve la matriz en su estado  original
            tablero = eval(lineas[1])
            # Se habilita el juego de nuevo
            jugando = True
            # Se dibuja la matriz de nuevo
            draw(grid, tablero)
            # Se habilita espacio para esribir nombre
            entryNombre.config(state='normal')
            #  Limpia el entry
            entryNombre.delete(0, tk.END)
            # Se guarda el nombre desde la primera posicion del entry (por eso el cero)
            entryNombre.insert(0, nombre_jugador)
            # Se vuelve a desabilitar entry
            entryNombre.config(state='disabled')"""
    def iniciar_juego():
        return
    def deshacer_jugada():
        return
    def rehacer_jugada():
        return
    def cargar_juego():
        return
    def guardar_juego():
        return
    def borrar_juego():
        return
    def terminar_juego():
        return
    def top_x():
        return
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
        elección="1"
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
        elección="2"
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
        elección="3"
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
        elección="4"
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
        elección="5"
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
        elección="6"
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
        elección="7"
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
        elección="8"
        return
    def selecciona_9():
        global elección
        btn1.config(bg="#e9fb2c")
        btn2.config(bg="#e9fb2c")
        btn3.config(bg="#e9fb2c")
        btn4.config(bg="#e9fb2c")
        btn5.config(bg="#e9fb2c")
        btn6.config(bg="#e9fb2c")
        btn7.config(bg="#e9fb2c")
        btn8.config(bg="#e9fb2c")
        btn9.config(bg="light blue")
        elección="9"
        return
    # Agrega espacio donde se coloca el nombre del jugador
    entryNombre = tk.Entry(ventana_principal_juego, bd=2, bg="#e9bd15", font=("Century", 13))
    entryNombre.place(x=100, y=0)

    btnIniciarPartida = tk.Button(ventana_principal_juego, text="INICIAR \n  JUEGO  ",
                                  bg="#de14e5", fg="black",
                                  font=("Century", 12),
                                  activebackground="#a4e647",
                                  activeforeground="black",
                                  command=iniciar_juego)
    btnIniciarPartida.place(x=370, y=160)

    btnDeshacerJugada = tk.Button(ventana_principal_juego, text="   DESHACER   \nJUGADA",
                               bg="#285e78", fg="black",
                               font=("Century", 12),
                               activebackground="#e8e54a",
                               activeforeground="black",
                               command=deshacer_jugada)
    btnDeshacerJugada.place(x=500, y=160)
    
    btnRehacerJugada = tk.Button(ventana_principal_juego, text="   REHACER   \nJUGADA",
                               bg="#285e78", fg="black",
                               font=("Century", 12),
                               activebackground="#e8e54a",
                               activeforeground="black",
                               command=rehacer_jugada)
    btnRehacerJugada.place(x=230, y=220)
    
    btnBorrarJuego = tk.Button(ventana_principal_juego, text="  BORRAR  \n JUEGO ",
                                bg="#4f5312", fg="black",
                                font=("Century", 12),
                                activebackground="#e34257",
                                activeforeground="black",
                                command=borrar_juego)
    btnBorrarJuego.place(x=370, y=340)

    btnTerminarJuego = tk.Button(ventana_principal_juego, text="  TERMINAR JUEGO ",
                            bg="#c86e76", fg="black",
                            font=("Century", 12),
                            activebackground="#33cca1",
                            activeforeground="black",
                            command=terminar_juego)
    btnTerminarJuego.place(x=75, y=465)

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
    btnTopX.place(x=0, y=465)

    btn1 = tk.Button(ventana_principal_juego, text=" 1 ",
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_1)
    btn1.place(x=370, y=50)

    btn2 = tk.Button(ventana_principal_juego, text=" 2 ",
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_2)
    btn2.place(x=405, y=50)

    btn3 = tk.Button(ventana_principal_juego, text=" 3 ",
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_3)
    btn3.place(x=440, y=50)

    btn4 = tk.Button(ventana_principal_juego, text=" 4 ",
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_4)
    btn4.place(x=370, y=85)

    btn5 = tk.Button(ventana_principal_juego, text=" 5 ",
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_5)
    btn5.place(x=405, y=85)

    btn6 = tk.Button(ventana_principal_juego, text=" 6 ",
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_6)
    btn6.place(x=440, y=85)

    btn7 = tk.Button(ventana_principal_juego, text=" 7 ",
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_7)
    btn7.place(x=370, y=120)

    btn8 = tk.Button(ventana_principal_juego, text=" 8 ",
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_8)
    btn8.place(x=405, y=120)

    btn9 = tk.Button(ventana_principal_juego, text=" 9 ",
                                bg="#e9fb2c", fg="black",
                                font=("Century", 12),
                                activebackground="#e08a89",
                                activeforeground="black",
                                command=selecciona_9)
    btn9.config(bg="light blue")
    btn9.place(x=440, y=120)
    def habilitar_botones():
        num00.config(state="normal")
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
    def deshabilitar_botones():
        num00.config(state="disabled")
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
    # Crea el tablero inicial
    iniciarPartida()
    return
def configuración():
    global hay_reloj, hay_temporizador, configuración_reloj, horas, minutos, segundos
    menú.withdraw()
    # Genera una ventana secundaria
    ventanaConfig = tk.Toplevel()
    ventanaConfig.title("Juego Sudoku")
    ventanaConfig.geometry("{}x{}+{}+{}".format(400, 400, int((menú.winfo_screenwidth() / 2) - (400 / 2)),
                                                int((menú.winfo_screenheight() / 2) - (400 / 2))))
    ventanaConfig.resizable(width=False, height=False)
    ventanaConfig.config(bg="#e9bd15")

    lblhora = tk.Label(ventanaConfig, text="Ingrese hora:", bg="#e9bd15", fg="black", font=("Century", 16))
    lblhora.place(x=0, y=175)

    lblminutos = tk.Label(ventanaConfig, text="Ingrese minutos:", bg="#e9bd15", fg="black",
                          font=("Century", 16))
    lblminutos.place(x=0, y=250)

    lblsegundos = tk.Label(ventanaConfig, text="Ingrese segundos:", bg="#e9bd15", fg="black",
                           font=("Century", 16))
    lblsegundos.place(x=0, y=325)

    entryHoras = tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryHoras.insert(0, str(horas))
    entryHoras.place(x=210, y=175)

    entryMinutos = tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entryMinutos.insert(0, str(minutos))
    entryMinutos.place(x=210, y=250)

    entrySegundos = tk.Entry(ventanaConfig, bd=2, bg="white", font=("Century", 12))
    entrySegundos.insert(0, str(segundos))
    entrySegundos.place(x=210, y=325)

    def guardarConfig():
        global horas, minutos, segundos
        try:
            horas = int(entryHoras.get())
            minutos = int(entryMinutos.get())
            segundos = int(entrySegundos.get())
            menú.deiconify()
            ventanaConfig.destroy()
            print(horas, minutos, segundos, rbtnSi,rbtnNo,rbtnTimer)
        except ValueError:
            messagebox.showerror('Error', 'Los campos no deben estar vacios')

    def cancelarConfig():
        menú.deiconify()
        ventanaConfig.destroy()

    btnGuardarConfig = tk.Button(ventanaConfig, text="     Guardar     ",
                                 bg="#de2644", fg="black",
                                 font=("Century", 12),
                                 activebackground="#e8e54a",
                                 activeforeground="black",
                                 command=guardarConfig)
    btnGuardarConfig.place(x=20, y=360)

    btnCancelar = tk.Button(ventanaConfig, text="     Cancelar     ",
                            bg="#ed5caa", fg="black",
                            font=("Century", 12),
                            activebackground="#33cc6b",
                            activeforeground="black",
                            command=cancelarConfig)
    btnCancelar.place(x=250, y=360)

    rbtnSi = tk.Radiobutton(ventanaConfig,
                            text="Si",
                            padx=20,
                            variable=configuración_reloj,
                            bg="#e9bd15",
                            font=("Century", 16),
                            value=1)
    rbtnSi.place(x=0, y=80)

    rbtnNo = tk.Radiobutton(ventanaConfig,
                            text="No",
                            padx=20,
                            variable=configuración_reloj,
                            bg="#e9bd15",
                            font=("Century", 16),
                            value=2)
    rbtnNo.place(x=0, y=110)
    rbtnTimer = tk.Radiobutton(ventanaConfig,
                               text="Timer",
                               padx=20,
                               variable=configuración_reloj,
                               bg="#e9bd15",
                               font=("Century", 16),
                               value=3)
    rbtnTimer.place(x=0, y=50)

    lblhora = tk.Label(ventanaConfig, text="¿Desea jugar con reloj?", bg="#e9bd15", fg="black",
                       font=("Century", 16))
    lblhora.place(x=0, y=15)
    return 

def acerca_de():
    ventanaAcercaDe = tk.Toplevel()
    ventanaAcercaDe.title("Juego Sudoku")
    ventanaAcercaDe.geometry("{}x{}+{}+{}".format(440, 440, int((menú.winfo_screenwidth() / 2) - (440 / 2)),
                                                  int((menú.winfo_screenheight() / 2) - (440 / 2))))

    ventanaAcercaDe.resizable(width=False, height=False)
    ventanaAcercaDe.config(bg="white")

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

def ayuda():
    os.system("archivos\\documentos\\manual_de_usuario_sudoku.pdf")
    return
def salir():
    # Destruye la ventana
    menú.destroy()
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


menú.mainloop()
