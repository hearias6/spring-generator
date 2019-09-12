import createEntityModule
import createColumnModule
import createConstructorModule
import createSetterModule
import createGetterModule
import fileModule
import columModule
import createDaoModule
import createServiceModule
import createServiceImplModule

print("Ingrese el nombre de la tabla")
nombreTabla=raw_input()
print("Ingrese el nombre de la clase")
nombreClase=raw_input()


respuesta = 'S'
listaColumnas = []

while respuesta.upper() != 'N':

    # Declarar todas las variables.
    llavePrimaria = "N"
    llaveForanea = "N"
    referencia = "N"
    atributo = "N"
    columna = "N"
    tipoDato = "N"

    # Preguntar todos los registros.
    print('Llave Primaria (S/N)')
    llavePrimaria=raw_input()
        
    if llavePrimaria.upper() !="S":
        print('Llave Foranea (S/N)')
        llaveForanea=raw_input()

    if llaveForanea.upper() =="S":
        print('Nombre de la entidad de referencia')
        tipoDato=raw_input()
        print('Ingrese el nombre del atributo')
        atributo=raw_input()

    if llaveForanea.upper() =="N": 
        print('Ingrese el nombre de la columna de acuerdo a la tabla')
        columna=raw_input()
        print('Ingrese el nombre del atributo')
        atributo=raw_input()
        print('Ingrese el tipo de dato (String=>s Integer=>i Long=>l Boolean=>b Date=>d)')
        tipoDato=raw_input()
        # settear el tipo de dato.
        if tipoDato.upper() =='S':
            tipoDato = "String"
        elif tipoDato.upper() =='D':
            tipoDato = "Date"
        elif tipoDato.upper() =='I':
            tipoDato = "Integer"
        elif tipoDato.upper() =='B':
            tipoDato = "Boolean"                        
        elif tipoDato.upper() =='L':
            tipoDato = "Long"  

    #contenido += createColumnModule.generateColumnMapping(columna, atributo, tipoDato, llavePrimaria, llaveForanea, referencia)
    col = columModule.Columna(columna, atributo, tipoDato, llavePrimaria, llaveForanea, referencia)
    listaColumnas.append(col)
    print("Ingresar otro registro.. (S/N)")
    respuesta=raw_input()

# generate entity
contenido = createEntityModule.createEntity(nombreTabla, nombreClase)    

encabezado=""
cuerpo=""

# generate las columnas mapeadas.
for item in listaColumnas:
    contenido += createColumnModule.generateColumnMapping(
        item._nombre_columna,
        item._atributo,
        item._type,
        item._pk,
        item._fk,
        item._reference
    )

    encabezado += item._type + " " + item._atributo + ", "
    cuerpo += "\t\tthis." + item._atributo + " = " + item._atributo + "; \n"

# generate los constructores
total = len(encabezado) - 2
encabezadoNuevo = encabezado[0:total]
contenido += createConstructorModule.createConstruct(nombreClase)
contenido += "\n"
contenido += "\tpublic " + nombreClase + "(" + encabezadoNuevo + ") { \n"
contenido += cuerpo
contenido += "\t}"

# generate los getters y los setters
for item in listaColumnas:
    contenido += createSetterModule.createSetter(item._atributo,item._type)
    contenido += createGetterModule.createGetter(item._atributo,item._type)

contenido += "\n\n}"

# generate los archivos.
rutaProyecto = "/home/hans/Documentos/Proyectos/spring-generator/generate/"
path =rutaProyecto + nombreClase + ".java"
file_java_entity = fileModule.establecerArchivo(path,'w')
fileModule.escribirArchivo(file_java_entity,contenido)

createDaoModule.createDao(rutaProyecto,nombreClase, "Long")
createServiceModule.createService(rutaProyecto, nombreClase)
createServiceImplModule.createServiceImpl(rutaProyecto, nombreClase)

print("se ha generado exitosamente")




