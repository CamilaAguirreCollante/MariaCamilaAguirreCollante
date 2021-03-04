def sumaTriangular(A):
    matriz = list(list(A)) #Convertir la Matriz en lista para facilitar su operación
    n = len(matriz) #Obtener la longitud de la matriz convertida en lista
    suma = 0 #Variable para sumar
    nOperaciones = 0 #Contador de operaciones
    for x in range(0,n): #Recorrer la matriz y sumarla 
        for y in range(x,n):
            suma+=matriz[x][y]
            nOperaciones += 1
            import matplotlib.pyplot as plt#Gráfica n vs nOperaciones
            plt.title('n vs nOperaciones')
            plt.xlabel('nOperaciones')
            plt.ylabel('n')
            plt.plot(nOperaciones,n,'m.')
            plt.show()
    print("La suma de la matriz triangular superior es:"+str(suma))
    print("La cantidad de operaciones es: " + str(nOperaciones) + "\n")
    return suma
    
def main():
    
    #Matrices Ejemplo
    matrizA = [[1,2,3,4],[5,6,7,8],[9,0,1,2],[1,2,3,4]] #4x4
    matrizB = [[18,68,8,88],[0,90,23,49],[0,0,29,10],[0,0,0,85]] #4x4
    matrizC = [[16,12,13],[17,16,18],[5,14,18]] #4x3
    matrizD = [[16,12,13],[0,16,18],[0,0,18]] #3x3
    matrizE = [[1,16,3,16,15],[17,1,6,6,15],[14,10,1,15,8],[11,6,10,14,12],[11,6,10,14,12]] #5x5
    

    print("Primera Prueba: 4x4\n")
    sumaTriangular(matrizA)
    print("Segunda Prueba: 4x4\n")
    sumaTriangular(matrizB)
    print("Tercera Prueba: 3x3\n")
    sumaTriangular(matrizC)
    print("Cuarta Prueba: 3x3\n")
    sumaTriangular(matrizD)
    print("Quinta Prueba: 5x5\n")
    sumaTriangular(matrizE)
        
if __name__ == "__main__":
    main()

