
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


        
string2="num{x}{y}.config(command=func{x}{y})"


string00="""def func{x}{y}():
    global elección,jugadas_viejas
    anterior=num{x}{y}["text"]
    color_anterior=num{x}{y}["bg"]
    num{x}{y}.config(text=elección)
    def cerrar_advertencia{x}{y}(event):
        habilitar_botones()
        num{x}{y}.config(text=anterior,bg=color_anterior)
        lbl_advertencia_1.destroy()
    if num{x}{y}["bg"]!="#02ac66":
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque la casillabanderocool contiene un elemento fijo")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    elif [num{x}{y}["text"],num{x}{sumay1}["text"],num{x}{sumay2}["text"],num{sumax1}{y}["text"],num{sumax1}{sumay1}["text"],num{sumax1}{sumay2}["text"],num{sumax2}{y}["text"],num{sumax2}{sumay1}["text"],num{sumax2}{sumay2}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la cuadrícula")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{x}0["text"],num{x}1["text"],num{x}2["text"],num{x}3["text"],num{x}4["text"],num{x}5["text"],num{x}6["text"],num{x}7["text"],num{x}8["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la columna")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
                
    elif [num0{y}["text"],num1{y}["text"],num2{y}["text"],num3{y}["text"],num4{y}["text"],num5{y}["text"],num6{y}["text"],num7{y}["text"],num8{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la fila")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    else:
        jugadas_viejas.meter([({y},{x}),anterior])

    if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
        ganó()"""

string01="""def func{x}{y}():
    global elección,jugadas_viejas
    anterior=num{x}{y}["text"]
    color_anterior=num{x}{y}["bg"]
    num{x}{y}.config(text=elección)
    def cerrar_advertencia{x}{y}(event):
        habilitar_botones()
        num{x}{y}.config(text=anterior,bg=color_anterior)
        lbl_advertencia_1.destroy()
    if num{x}{y}["bg"]!="#02ac66":
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque la casillabanderocool contiene un elemento fijo")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{x}{restay1}["text"],num{x}{y}["text"],num{x}{sumay1}["text"],num{sumax1}{restay1}["text"],num{sumax1}{y}["text"],num{sumax1}{sumay1}["text"],num{sumax2}{restay1}["text"],num{sumax2}{y}["text"],num{sumax2}{sumay1}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la cuadrícula")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{x}0["text"],num{x}1["text"],num{x}2["text"],num{x}3["text"],num{x}4["text"],num{x}5["text"],num{x}6["text"],num{x}7["text"],num{x}8["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la columna")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
                
    elif [num0{y}["text"],num1{y}["text"],num2{y}["text"],num3{y}["text"],num4{y}["text"],num5{y}["text"],num6{y}["text"],num7{y}["text"],num8{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la fila")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    else:
        jugadas_viejas.meter([({y},{x}),anterior])

    if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
        ganó()"""


string02="""def func{x}{y}():
    global elección,jugadas_viejas
    anterior=num{x}{y}["text"]
    color_anterior=num{x}{y}["bg"]
    num{x}{y}.config(text=elección)
    def cerrar_advertencia{x}{y}(event):
        habilitar_botones()
        num{x}{y}.config(text=anterior,bg=color_anterior)
        lbl_advertencia_1.destroy()
    if num{x}{y}["bg"]!="#02ac66":
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque la casillabanderocool contiene un elemento fijo")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    elif [num{x}{restay2}["text"],num{x}{restay1}["text"],num{x}{y}["text"],num{sumax1}{restay2}["text"],num{sumax1}{restay1}["text"],num{sumax1}{y}["text"],num{sumax2}{restay2}["text"],num{sumax2}{restay1}["text"],num{sumax2}{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la cuadrícula")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})


    elif [num{x}0["text"],num{x}1["text"],num{x}2["text"],num{x}3["text"],num{x}4["text"],num{x}5["text"],num{x}6["text"],num{x}7["text"],num{x}8["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la columna")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
                
    elif [num0{y}["text"],num1{y}["text"],num2{y}["text"],num3{y}["text"],num4{y}["text"],num5{y}["text"],num6{y}["text"],num7{y}["text"],num8{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la fila")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    else:
        jugadas_viejas.meter([({y},{x}),anterior])

    if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
        ganó()"""

string10="""def func{x}{y}():
    global elección,jugadas_viejas
    anterior=num{x}{y}["text"]
    color_anterior=num{x}{y}["bg"]
    num{x}{y}.config(text=elección)
    def cerrar_advertencia{x}{y}(event):
        habilitar_botones()
        num{x}{y}.config(text=anterior,bg=color_anterior)
        lbl_advertencia_1.destroy()
    if num{x}{y}["bg"]!="#02ac66":
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque la casillabanderocool contiene un elemento fijo")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
        
    elif [num{restax1}{y}["text"],num{restax1}{sumay1}["text"],num{restax1}{sumay2}["text"],num{x}{y}["text"],num{x}{sumay1}["text"],num{x}{sumay2}["text"],num{sumax1}{y}["text"],num{sumax1}{sumay1}["text"],num{sumax1}{sumay2}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la cuadrícula")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{x}0["text"],num{x}1["text"],num{x}2["text"],num{x}3["text"],num{x}4["text"],num{x}5["text"],num{x}6["text"],num{x}7["text"],num{x}8["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la columna")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
                
    elif [num0{y}["text"],num1{y}["text"],num2{y}["text"],num3{y}["text"],num4{y}["text"],num5{y}["text"],num6{y}["text"],num7{y}["text"],num8{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la fila")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    else:
        jugadas_viejas.meter([({y},{x}),anterior])


    if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
        ganó()"""
string11="""def func{x}{y}():
    global elección,jugadas_viejas
    anterior=num{x}{y}["text"]
    color_anterior=num{x}{y}["bg"]
    num{x}{y}.config(text=elección)
    def cerrar_advertencia{x}{y}(event):
        habilitar_botones()
        num{x}{y}.config(text=anterior,bg=color_anterior)
        lbl_advertencia_1.destroy()
    if num{x}{y}["bg"]!="#02ac66":
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque la casillabanderocool contiene un elemento fijo")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
        
    elif [num{restax1}{restay1}["text"],num{restax1}{y}["text"],num{restax1}{sumay1}["text"],num{x}{restay1}["text"],num{x}{y}["text"],num{x}{sumay1}["text"],num{sumax1}{restay1}["text"],num{sumax1}{y}["text"],num{sumax1}{sumay1}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la cuadrícula")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{x}0["text"],num{x}1["text"],num{x}2["text"],num{x}3["text"],num{x}4["text"],num{x}5["text"],num{x}6["text"],num{x}7["text"],num{x}8["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la columna")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
                
    elif [num0{y}["text"],num1{y}["text"],num2{y}["text"],num3{y}["text"],num4{y}["text"],num5{y}["text"],num6{y}["text"],num7{y}["text"],num8{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la fila")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    else:
        jugadas_viejas.meter([({y},{x}),anterior])


    if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
        ganó()"""


string12="""def func{x}{y}():
    global elección,jugadas_viejas
    anterior=num{x}{y}["text"]
    color_anterior=num{x}{y}["bg"]
    num{x}{y}.config(text=elección)
    def cerrar_advertencia{x}{y}(event):
        habilitar_botones()
        num{x}{y}.config(text=anterior,bg=color_anterior)
        lbl_advertencia_1.destroy()
    if num{x}{y}["bg"]!="#02ac66":
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque la casillabanderocool contiene un elemento fijo")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{restax1}{restay2}["text"],num{restax1}{restay1}["text"],num{restax1}{y}["text"],num{x}{restay2}["text"],num{x}{restay1}["text"],num{x}{y}["text"],num{sumax1}{restay2}["text"],num{sumax1}{restay1}["text"],num{sumax1}{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la cuadrícula")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{x}0["text"],num{x}1["text"],num{x}2["text"],num{x}3["text"],num{x}4["text"],num{x}5["text"],num{x}6["text"],num{x}7["text"],num{x}8["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la columna")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
                
    elif [num0{y}["text"],num1{y}["text"],num2{y}["text"],num3{y}["text"],num4{y}["text"],num5{y}["text"],num6{y}["text"],num7{y}["text"],num8{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la fila")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    else:
        jugadas_viejas.meter([({y},{x}),anterior])


    if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
        ganó()"""

string20="""def func{x}{y}():
    global elección,jugadas_viejas
    anterior=num{x}{y}["text"]
    color_anterior=num{x}{y}["bg"]
    num{x}{y}.config(text=elección)
    def cerrar_advertencia{x}{y}(event):
        habilitar_botones()
        num{x}{y}.config(text=anterior,bg=color_anterior)
        lbl_advertencia_1.destroy()
    if num{x}{y}["bg"]!="#02ac66":
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque la casillabanderocool contiene un elemento fijo")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{restax2}{y}["text"],num{restax2}{sumay1}["text"],num{restax2}{sumay2}["text"],num{restax1}{y}["text"],num{restax1}{sumay1}["text"],num{restax1}{sumay2}["text"],num{x}{y}["text"],num{x}{sumay1}["text"],num{x}{sumay2}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la cuadrícula")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{x}0["text"],num{x}1["text"],num{x}2["text"],num{x}3["text"],num{x}4["text"],num{x}5["text"],num{x}6["text"],num{x}7["text"],num{x}8["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la columna")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
                
    elif [num0{y}["text"],num1{y}["text"],num2{y}["text"],num3{y}["text"],num4{y}["text"],num5{y}["text"],num6{y}["text"],num7{y}["text"],num8{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la fila")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    else:
        jugadas_viejas.meter([({y},{x}),anterior])



    if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
        ganó()"""

string21="""def func{x}{y}():
    global elección,jugadas_viejas
    anterior=num{x}{y}["text"]
    color_anterior=num{x}{y}["bg"]
    num{x}{y}.config(text=elección)
    def cerrar_advertencia{x}{y}(event):
        habilitar_botones()
        num{x}{y}.config(text=anterior,bg=color_anterior)
        lbl_advertencia_1.destroy()
    if num{x}{y}["bg"]!="#02ac66":
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque la casillabanderocool contiene un elemento fijo")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{restax2}{restay1}["text"],num{restax2}{y}["text"],num{restax2}{sumay1}["text"],num{restax1}{restay1}["text"],num{restax1}{y}["text"],num{restax1}{sumay1}["text"],num{x}{restay1}["text"],num{x}{y}["text"],num{x}{sumay1}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la cuadrícula")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{x}0["text"],num{x}1["text"],num{x}2["text"],num{x}3["text"],num{x}4["text"],num{x}5["text"],num{x}6["text"],num{x}7["text"],num{x}8["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la columna")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
                
    elif [num0{y}["text"],num1{y}["text"],num2{y}["text"],num3{y}["text"],num4{y}["text"],num5{y}["text"],num6{y}["text"],num7{y}["text"],num8{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la fila")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    else:
        jugadas_viejas.meter([({y},{x}),anterior])


    if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
        ganó()"""

string22="""def func{x}{y}():
    global elección,jugadas_viejas
    anterior=num{x}{y}["text"]
    color_anterior=num{x}{y}["bg"]
    num{x}{y}.config(text=elección)
    def cerrar_advertencia{x}{y}(event):
        habilitar_botones()
        num{x}{y}.config(text=anterior,bg=color_anterior)
        lbl_advertencia_1.destroy()
    if num{x}{y}["bg"]!="#02ac66":
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque la casillabanderocool contiene un elemento fijo")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    elif [num{restax2}{restay2}["text"],num{restax2}{restay1}["text"],num{restax2}{y}["text"],num{restax1}{restay2}["text"],num{restax1}{restay1}["text"],num{restax1}{y}["text"],num{x}{restay2}["text"],num{x}{restay1}["text"],num{x}{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la cuadrícula")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})

    elif [num{x}0["text"],num{x}1["text"],num{x}2["text"],num{x}3["text"],num{x}4["text"],num{x}5["text"],num{x}6["text"],num{x}7["text"],num{x}8["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la columna")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
                
    elif [num0{y}["text"],num1{y}["text"],num2{y}["text"],num3{y}["text"],num4{y}["text"],num5{y}["text"],num6{y}["text"],num7{y}["text"],num8{y}["text"]].count(num{x}{y}["text"])>1:
        deshabilitar_botones()
        num{x}{y}.config(bg="red")
        lbl_advertencia_1 = tk.Label(ventana_principal_juego,bd=3, bg="#e9bd15", fg="black",font=("Century", 11))
        lbl_advertencia_1.config(text="Jugada no es válida porque el elemento yabanderocool está en la fila")
        lbl_advertencia_1.place(x=370,y=450)
        ventana_principal_juego.bind("<Return>", cerrar_advertencia{x}{y})
    else:
        jugadas_viejas.meter([({y},{x}),anterior])

    if [num00["text"],num01["text"],num02["text"],num03["text"],num04["text"],num05["text"],num06["text"],num07["text"],num08["text"],num10["text"],num11["text"],num12["text"],num13["text"],num14["text"],num15["text"],num16["text"],num17["text"],num18["text"],num20["text"],num21["text"],num22["text"],num23["text"],num24["text"],num25["text"],num26["text"],num27["text"],num28["text"],num30["text"],num31["text"],num32["text"],num33["text"],num34["text"],num35["text"],num36["text"],num37["text"],num38["text"],num40["text"],num41["text"],num42["text"],num43["text"],num44["text"],num45["text"],num46["text"],num47["text"],num48["text"],num50["text"],num51["text"],num52["text"],num53["text"],num54["text"],num55["text"],num56["text"],num57["text"],num58["text"],num60["text"],num61["text"],num62["text"],num63["text"],num64["text"],num65["text"],num66["text"],num67["text"],num68["text"],num70["text"],num71["text"],num72["text"],num73["text"],num74["text"],num75["text"],num76["text"],num77["text"],num78["text"],num80["text"],num81["text"],num82["text"],num83["text"],num84["text"],num85["text"],num86["text"],num87["text"],num88["text"]].count("")<1:
        ganó()
        """
    

for x in range(9):
    for y in range(9):
        if x==0 or x==3 or x==6:
            if y==0 or y==3 or y==6:
                sumax1=x+1
                sumax2=x+2
                sumay1=y+1
                sumay2=y+2
                print(string00.format(x=x,sumax1=sumax1,sumax2=sumax2, y=y,sumay1=sumay1,sumay2=sumay2))
            if y==1 or y==4 or y==7:
                sumax1=x+1
                sumax2=x+2
                sumay1=y+1
                sumay2=y+2
                restay1=y-1
                print(string01.format(x=x,sumax1=sumax1,sumax2=sumax2, y=y,sumay1=sumay1,sumay2=sumay2,restay1=restay1))
            if y==2 or y==5 or y==8:
                sumax1=x+1
                sumax2=x+2
                sumay1=y+1
                sumay2=y+2
                restay1=y-1
                restay2=y-2
                print(string02.format(x=x,sumax1=sumax1,sumax2=sumax2, y=y,sumay1=sumay1,sumay2=sumay2,restay1=restay1,restay2=restay2))
        if x==1 or x==4 or x==7:
            if y==0 or y==3 or y==6:
                sumax1=x+1
                sumax2=x+2
                restax1=x-1
                sumay1=y+1
                sumay2=y+2
                print(string10.format(x=x,sumax1=sumax1,sumax2=sumax2,restax1=restax1,y=y,sumay1=sumay1,sumay2=sumay2))
            if y==1 or y==4 or y==7:
                sumax1=x+1
                sumax2=x+2
                restax1=x-1
                sumay1=y+1
                sumay2=y+2
                restay1=y-1
                print(string11.format(x=x,sumax1=sumax1,sumax2=sumax2,restax1=restax1,y=y,sumay1=sumay1,sumay2=sumay2,restay1=restay1))
            if y==2 or y==5 or y==8:
                sumax1=x+1
                sumax2=x+2
                restax1=x-1
                sumay1=y+1
                sumay2=y+2
                restay1=y-1
                restay2=y-2
                print(string12.format(x=x,sumax1=sumax1,sumax2=sumax2,restax1=restax1,y=y,sumay1=sumay1,sumay2=sumay2,restay1=restay1,restay2=restay2))
        if x==2 or x==5 or x==8:
            if y==0 or y==3 or y==6:
                sumax1=x+1
                sumax2=x+2
                restax1=x-1
                restax2=x-2
                sumay1=y+1
                sumay2=y+2
                print(string20.format(x=x,sumax1=sumax1,sumax2=sumax2,restax1=restax1,restax2=restax2,y=y,sumay1=sumay1,sumay2=sumay2))
            if y==1 or y==4 or y==7:
                sumax1=x+1
                sumax2=x+2
                restax1=x-1
                restax2=x-2
                sumay1=y+1
                sumay2=y+2
                restay1=y-1
                print(string21.format(x=x,sumax1=sumax1,sumax2=sumax2,restax1=restax1,restax2=restax2,y=y,sumay1=sumay1,sumay2=sumay2,restay1=restay1))
            if y==2 or y==5 or y==8:
                sumax1=x+1
                sumax2=x+2
                restax1=x-1
                restax2=x-2
                sumay1=y+1
                sumay2=y+2
                restay1=y-1
                restay2=y-2
                print(string22.format(x=x,sumax1=sumax1,sumax2=sumax2,restax1=restax1,restax2=restax2,y=y,sumay1=sumay1,sumay2=sumay2,restay1=restay1,restay2=restay2))

