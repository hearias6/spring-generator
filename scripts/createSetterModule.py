

def createSetter(columna, tipoDato):
    contenido = "\n\n"
    contenido += "\tprivate void set" + columna.capitalize() + "("+ tipoDato +" "+columna+") {\n"
    contenido += "\t\tthis." + columna + " = " + columna + ";\n"
    contenido += "\t}"
    return contenido;