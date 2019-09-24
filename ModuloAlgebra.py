#Este módulo tiene diversas funciones algebraicas.
def transpuestaMatriz(matriz):    #Esta funcion crea una matriz transpuesta.
    trans=[]
    for i in range(len(matriz[0])):
        fila=[]
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        trans.append(fila)
    return trans


def productoVectorial(v1,v2):    #Esta funcion realiza el producto vectorial entre dos vectores.
    vx=v1[1]*v2[2]-v2[1]*v1[2]
    vy=v2[0]*v1[2]-v1[0]*v2[2]
    vz=v1[0]*v2[1]-v2[0]*v1[1]
    return (vx,vy,vz)


def multiplicacionMatriz(matriz1,matriz2,n,m):    #Esta funcion realiza la multiplicación entre dos matrices.
    if n!=m:
        print("no se puede realizar la multiplicación, deben ser iguales los valores de m y n")
    else:    
        matriz_produc=[]
        for i in range(n):
            fila=[]
            for j in range(n):
                fila.append(0)
            matriz_produc.append(fila)
        for i in range(n):
            for j in range(n):
                acu=0
                for k in range(m):
                    acu=acu+a[i][k]*b[k][j]
                matriz_produc[i][j]=acu
    return matriz_produc

    
def det(matriz):    #Esta funcion calcula el determinante de una matriz.
    
    def copy(matriz):
        matriz_copy=[]
        for i in range(0,len(matriz)):
            copy=[]
            for j in range(0,len(matriz[i])):
                copy.append(matriz[i][j])
            matriz_copy.append(copy)
        return matriz_copy
    
    def encoger(matriz,k):
        matriz_copy=copy(matriz)
        matriz_copy.remove(matriz_copy[0])
        for i in range(0,len(matriz_copy)):
            (matriz_copy[i]).remove((matriz_copy[i])[k])
        return matriz_copy
    
        
    if len(matriz)==1:
        return matriz[0]
    elif len(matriz)==2:
        return (matriz[0][0])*(matriz[1][1])-(matriz[0][1])*(matriz[1][0])
    else:
        total=0
        for i in range(0,len(matriz)):
            total=total+((-1)**i)*matriz[0][i]*det(encoger(matriz,i))
    return total


def gaussJordan(matriz):    #Funcion para hallar la inversa de una matriz.
    import copy
    inversa=[]		
    for h in range(0,len(matriz)):
        lis_inversa=[]
        for k in range(0,len(matriz)):
            if h==k:
                lis_inversa.append(1)
            else:
                lis_inversa.append(0)
        inversa.append(lis_inversa)
	
    def pivote(fil,fila,columna):
        pivote=copy.deepcopy(fila[columna])
        for i in range(0,len(fila)):
            fil[i]=fil[i]/pivote
        return fil

    def intercambioFila(matriz,fila1,fila2):
        fila3=matriz[fila1]
        matriz[fila1]=matriz[fila2]
        matriz[fila2]=fila3
        return matriz
        
    def sumafilas(fila1,fila2,escalar):
        for i in range(0,len(fila1)):
            fila2[i]=(escalar * fila1[i])+fila2[i]
        return fila2

    for columna in range(0,len(matriz)):
        if matriz[columna][columna]!=0:			
            inversa[columna]=pivote(inversa[columna],matriz[columna],columna)
        matriz[columna]=pivote(matriz[columna],matriz[columna],columna)

        for fila in range(0,len(matriz)):
            if matriz[fila][columna]!=0 and columna!=fila:
                escalar=-1 * copy.deepcopy(matriz[fila][columna])				
            inversa[fila]=sumafilas(inversa[columna],inversa[fila],escalar)
            matriz[fila]=sumafilas(matriz[columna],matriz[fila],escalar)
    return inversa
    
    
