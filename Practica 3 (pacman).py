from asyncio.windows_events import NULL
import random
opc = 2.1
n = 0
def opcion1():##metodo para la opcion 1
    global nom, c, fil, col, tablero, pos, pts, contd, contq, contres,  hist
    pacman="[:V]"
    p10 =  "[ @]"
    p15 =  "[ $]"
    q10 =  "[ #]"
    
    hist=["[  ]"for i in range(3*n)]
    nom = input("ingrese su nombre: ")
    c = int(input("ingrese su carnet: "))
    fil = int(input("ingrese no filas: "))
    while(fil < 7):
        fil = int(input("ingrese no filas mayor a 7: "))
    col = int(input("ingrese no columnas: "))
    while(col < 7):
        col = int(input("ingrese no columnas mayor a 7: "))
    tablero = ["[  ]"for i in range(fil*col)]
    pos = random.randint(0, len(tablero)-1)
    if tablero[pos]=="[  ]":
        tablero[pos]=pacman
    contd = random.randint(8, (len(tablero)*30)//100)
    contq = random.randint(6, (len(tablero)*20)//100)
    contres = random.randint(8, (len(tablero)*25)//100)
    continuar = True
    pts = 10
    for d in range(0, contd):
        posd = random.randint(0, len(tablero)-1)
        while tablero[posd] == "[  ]":
            tablero[posd]=p10
    for d in range(0, contq):
        posq = random.randint(0, len(tablero)-1)
        while tablero[posq] == "[  ]":
            tablero[posq]=p15
    for d in range(0, contres):
        posr = random.randint(0, len(tablero)-1)
        while tablero[posr] == "[  ]":
            tablero[posr]=q10        
    
    while continuar == True:
        print(f"nombre: {nom} carnet: {c} puntos: {pts}")
        if pts >= 30:            
            print("ganaste")
            pts=30
            continuar = False
        elif pts <= 0:            
            print("perdiste")
            pts=0
            continuar = False
      
        for i in range(fil):
            for j in range(col):
                print(tablero[i*col+j], end = " ")
            print()
        mov = input("Ingrese un movimiento: ")
        if mov == "m":
            continuar = False                
        if mov != "a" and mov != "s" and mov != "w" and mov != "d" and mov != "m":
            print("solo puede ingresar las tecas A, S, D, W o M")
        if mov == "w":
            if pos - fil < 0:                
                tablero[pos]="[  ]"
                pos = (fil * col-1)-((col-1)-pos)                
            else:
                pos = pos - col
                tablero[pos+col]="[  ]"
            if tablero[pos]==p10:
                    pts = pts+10
            elif tablero[pos]==p15:
                    pts = pts+15
            elif tablero[pos]==q10:
                    pts = pts-10        
            tablero[pos]="[  ]"
            tablero[pos]=pacman
        if mov == "a":
            if pos % col != 0:
                pos = pos - 1
                tablero[pos+1]="[  ]"     
            elif pos % col == 0:
                pos = pos + (col-1)
                tablero[pos-(col-1)] = "[  ]"
            if tablero[pos]==p10:
                    pts = pts+10
            elif tablero[pos]==p15:
                    pts = pts+15
            elif tablero[pos]==q10:
                    pts = pts-10      
            tablero[pos]=pacman            
        if mov == "s":
            if pos + fil > (fil * col -1):
                tablero[pos]="[  ]"
                pos = (col-1)-((fil * col-1)-pos)               
            else:
                pos = pos + col
                tablero[pos-col]="[  ]"
            if tablero[pos]==p10:
                    pts = pts+10
            elif tablero[pos]==p15:
                    pts = pts+15
            elif tablero[pos]==q10:
                    pts = pts-10      
            tablero[pos]=pacman
        if mov == "d":
            if (pos+1) % col != 0:
                pos = pos + 1
                tablero[pos-1]="[  ]"     
            elif (pos+1) % col == 0:
                pos = pos - (col-1)
                tablero[pos+(col-1)] = "[  ]"
            if tablero[pos]==p10:
                    pts = pts+10
            elif tablero[pos]==p15:
                    pts = pts+15
            elif tablero[pos]==q10:
                    pts = pts-10      
            tablero[pos]=pacman  

while opc != 3 and opc > 0 and opc<4:
    print("*******Bienvenido******* \n****1. Iniciar Juego**** \n****2. Historial******** \n****3. salir************")
    opc = int(input("ingrese una opcion: "))
    if opc < 0 and opc > 4:
        opc = int(input("ingrese una opcion valida: "))
    if opc == 1:
        n = n + 1
        opcion1()
        for i in range(n):
                for j in range(3):
                    if(hist[i*3+j]=="[  ]"):
                        hist[i*3+0]=nom
                        hist[i*3+1]=c
                        hist[i*3+2]=pts
    if opc == 2:
        print("Historial de juego")
        for i in range(n):
            for j in range(3):
                print(hist[i*3+j], end = " ")
            print()