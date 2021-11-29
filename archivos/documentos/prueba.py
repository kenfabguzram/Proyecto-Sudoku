
a= [ 
[ "5", "3", "", "", "7", "", "", "", "" ],
[ "6", "", "", "1", "9", "5","2", "", "" ],
[ "", "9", "8", "", "", "", "", "6", ""],
[ "8", "", "", "", "6", "", "", "", "3" ],
[ "4", "", "", "8", "" , "3", "", "", "1" ],
[ "7", "", "", "", "2", "", "", "", "6" ],
[ "", "6", "", "", "", "", "2", "8", "" ],
[ "", "", "", "4", "1", "9", "", "", "5" ],
[ "", "", "", "", "8", "", "", "7", "9" ]
]
b= [ 
[ "9", "6", "3", "1", "7", "4", "2", "5", "8" ],
[ "1", "7", "8", "3", "2", "5","6", "4", "9" ],
[ "2", "5", "4", "6", "8", "9", "7", "3", "1"],
[ "8", "2", "1", "4", "3", "7", "5", "9", "6" ],
[ "4", "9", "6", "8", "5" , "2", "3", "1", "7" ],
[ "7", "3", "5", "9", "6", "1", "8", "2", "4" ],
[ "5", "8", "9", "7", "1", "3", "4", "6", "2" ],
[ "3", "1", "7", "2", "4", "6", "9", "8", "5" ],
[ "6", "4", "2", "5", "9", "8", "1", "7", "3" ]
]
def dividir(matriz):
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
def invertir(m):
    resultado=[[],[],[],[],[],[],[],[],[]]
    for fila in range(len(m)):
        for elemento in range(len(m[fila])):
            resultado[elemento].append(m[fila][elemento])
    return resultado
def ganó(matriz):
    for fila in dividir(matriz):
        for elemento in fila:
            if fila.count(elemento)!=1:
                return False
    for fila in matriz:
        for elemento in fila:
            if fila.count(elemento)!=1:
                return False
    for fila in invertir(matriz):
        for elemento in fila:
            if fila.count(elemento)!=1:
                return False
    return True

string="""def func{x}{y}():
    global elección,tablero
    anterior=num{x}{y}["text"]
    color_anterior=num{x}{y}["bg"]
    num{x}{y}.config(text=elección)
    tablero[{x}][{y}]=elección
    def cerrar_advertencia{x}{y}(event):
        habilitar_botones()
        num{x}{y}.config(text=anterior,bg=color_anterior)
        lbl_advertencia_1.destroy()
        tablero[{x}][{y}]=anterior
    if num{x}{y}["bg"]!="#02ac66":
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque la casillabanderocool contiene un elemento fijo")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
        
    elif dividir()[{x}].count(tablero[{x}][{y}])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la cuadrícula")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif tablero[{x}].count(tablero[{x}][{y}])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la fila")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
                
    elif invertir()[{x}].count(tablero[{x}][{y}])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la columna")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})"""
        
string2="num{x}{y}.config(command=func{x}{y})"

for x in range(9):
    for y in range(9):
        print(string.format(x=x,y=y))
for x in range(9):
    for y in range(9):
        print(string2.format(x=x,y=y))

