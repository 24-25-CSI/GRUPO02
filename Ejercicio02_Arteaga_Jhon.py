#2 realice el cifrado de un mensaje por permutacion de columnas, teniendo como clave 5 columnas y
#la cantidad de filas que sean necesarias (garantice al menos 3).los espacios del mensaje original se sustituyen
#con el caracter "#" si en la matriz de cifrado sobran espacios ,estos deben llenarse con el caracter"_"
#el mensaje original 
# matriz de cifrado
#el mensaje cifrado
#en el caso que se produzca algun error en la ejecucion, el mismo debe mostrarse para aletar al usuario

mensaje = input("Ingrese el mensaje que quiere cifrar")
nColumnas = 5

mensaje_sin_espacios = mensaje.replace(" ", "#")
 
while len(mensaje_sin_espacios) % nColumnas != 0:
  mensaje_sin_espacios += "_"
 
matriz = [["" for j in range(nColumnas)] for i in range(len(mensaje_sin_espacios)//nColumnas)]
 
k = 0
for i in range(len(mensaje_sin_espacios)//nColumnas):
    for j in range(nColumnas):
        matriz[i][j] = mensaje_sin_espacios[k]
        k += 1
 
mensaje_cifrado = ""
for j in range(nColumnas):
    
    for i in range(len(mensaje_sin_espacios)//nColumnas):
        
        mensaje_cifrado += matriz[i][j]
 

 
print("Mensaje original: " + mensaje)
print("Matriz de cifrado:")
for fila in matriz:
    print(fila)
print("Mensaje de cifrado: " + mensaje_cifrado)