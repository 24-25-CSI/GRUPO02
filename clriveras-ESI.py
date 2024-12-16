mensaje = input("Ingresa el mensaje que desea cifrar: ")
n = 5

#Reemplazamos el espacio por el caracter '-'
sin_espacios = mensaje.replace(" ", "-")

num_columnas = max(3, (len(sin_espacios) + n - 1) // n)

if len(sin_espacios) > n * num_columnas:
    print(f"Error: el número de caracteres del mensaje es mayor a {n * num_columnas} caracteres.")
else:
    #Completar el mensaje con '*' hasta llenar la matriz
    while len(sin_espacios) < n * num_columnas:
        sin_espacios += "*"

    # Crear la matriz de cifrado con 3 filas y tantas columnas como sea necesario
    matriz_cifrado = [[] for _ in range(n)]

    # Llenar la matriz por columnas
    k = 0
    for j in range(num_columnas):
        for i in range(n):
            if k < len(sin_espacios):
                matriz_cifrado[i].append(sin_espacios[k])
                k += 1

    # Crear el mensaje cifrado leyendo la matriz por filas
    mensaje_c = ""
    for j in range(n):
        for i in range(num_columnas):
            mensaje_c += matriz_cifrado[j][i]

    # Mostrar resultados
    print("Matriz de cifrado:")
    for fila in matriz_cifrado:
        print(fila)

    print("Mensaje original: " + mensaje)
    print("Mensaje cifrado: " + mensaje_c)
