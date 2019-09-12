
def createConstruct(nombreClase):
    contenido = "\n\n"
    contenido += "\tpublic " + nombreClase + "() { \n"
    contenido += "\t\tsuper(); \n"
    contenido += "\t}";
    return contenido
