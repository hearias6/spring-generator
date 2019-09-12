def establecerArchivo(ruta, permiso):
    archivo = open(ruta, permiso)
    return archivo

def leerArchivo(archivo):
    contenido = archivo.readlines()
    return contenido

def escribirArchivo(archivo, texto):
    archivo.write('\n' + texto)