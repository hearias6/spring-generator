

def createGetter(columna, tipoDato):
    contenido = "\n\n"
    contenido += "\tprivate " + tipoDato + " get" + columna.capitalize() + "() { \n";
    contenido += "\t\treturn this." + columna + "; \n";
    contenido += "\t}";
    return contenido;
