
import columModule

def generateColumnMapping(
    nameColumnTable, 
    nameAtribute, 
    type, 
    pk, 
    fk, 
    reference):

    contenido = "\n\n"
    
    # Columna Foreign Key
    if fk.upper() == 'S':
        contenido += "\t@ManyToOne\n";
        contenido += "\tprivate "+type+" "+nameAtribute+" \n"
    else:
        # Llave Primaria
        if pk.upper() == 'S':
            contenido += "\t@Id\n"

        # Mapeo de una columna normal
        contenido +="\t@Column(name=\""+nameColumnTable+"\") \n"
        contenido +="\tprivate "+ type +" " + nameAtribute + "; \n"

    return contenido
        


