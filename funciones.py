from PIL import Image
import numpy

def convertirImagenAArchivo(nombreImagen, nombreDestino):
    imagen = Image.open(nombreImagen)
    imagen = imagen.convert('RGB')
    matrizNumpy = numpy.array(imagen)
    archivo = open(nombreDestino, 'w')
    for fila in matrizNumpy:
        for pixel in fila :
            for componente in pixel :
                archivo.write(' ' + str(componente))
            archivo.write(',')
        archivo.write('\n')
    archivo.close()
    return True

def leerArchivo(nombreEntrada):
    archivo = open(nombreEntrada,'r')
    matriz = []
    for i in archivo:
        lista = []
        fila = []
        lista = i.strip(",\n").split(',')
        for pixel in lista :
            aux = pixel.split()
            for e in range(3) :
                aux[e] = int(aux[e])
            fila.append(aux)
        matriz.append(fila)
    archivo.close()
    return matriz

def convertirMatrizAImagen(matriz, nombreSalida):
    arr = numpy.array(matriz)
    im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
    im.save(nombreSalida)
    return True

convertirImagenAArchivo("imagen.jpg", "archivo.txt")
matriz=leerArchivo("archivo.txt")

def invertirhorizontal():
    lista = [i for i in range(len(matriz))]
    for i in range(len(matriz)):
        a = abs(i - len(matriz) + 1)
        lista[a] = matriz[i]
    return lista

def verde():
    for i in range(len(matriz)):
        for u in range(len(matriz[i])):
            matriz[i][u] = [int(matriz[i][u][0]*0.3), int(matriz[i][u][1]*0.59), int(matriz[i][u][2]*0.11)]
    return matriz

def gris():
    for i in range(len(matriz)):
        for u in range(len(matriz[i])):
            gris =  int((matriz[i][u][0]*0.3) +(matriz[i][u][1]*0.59)+(matriz[i][u][2]*0.11))
            matriz[i][u] = [gris,gris,gris]
    return matriz

convertirMatrizAImagen("Inserta aqui la funcion que retorne la matriz", "Imagen.jpg")
