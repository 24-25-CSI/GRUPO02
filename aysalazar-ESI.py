print("cifrado por permutación de filas Ejericio 1")     
def cifrarPermutacionFila(mensajeOriginal):
    try:
       
        mensajeOriginal = mensajeOriginal.replace(" ", "-")

        filas = 5
        longitud_mensaje = len(mensajeOriginal)
        columnas = max(3, (longitud_mensaje + filas - 1) // filas)
        
        matriz = [['*' for _ in range(columnas)] for _ in range(filas)]
        
        index = 0
        for i in range(filas):
            for j in range(columnas):
                if index < longitud_mensaje:
                    matriz[i][j] = mensajeOriginal[index]
                    index += 1
        
        print("Mensaje Original:", mensajeOriginal)
        
        print("Matriz de Cifrado por permutación:")
        for fila in matriz:
            print(" ".join(fila))
        
        mensajeCifrado = ""
        for j in range(columnas):
            for i in range(filas):
                mensajeCifrado += matriz[i][j]
        
        print("Mensaje cifrado:", mensajeCifrado)
    
    except Exception as e:
        print("Alerta! Error en la ejecución:", str(e))

mensajeOriginal = input("Introduce el mensaje a cifrar: ")
cifrarPermutacionFila(mensajeOriginal)
       