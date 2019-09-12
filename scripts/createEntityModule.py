# crear solamente la entidad.

def createEntity(tableName, claseName):
    
    contenido = "package com.resident.app.entities; \n"
    contenido += "import javax.persistence.Column; \n"
    contenido += "import javax.persistence.Entity; \n"
    contenido += "import javax.persistence.Id; \n"
    contenido += "import javax.persistence.ManyToOne; \n"
    contenido += "import javax.persistence.Table; \n\n\n"
    contenido += "@Entity \n"
    contenido += "@Table(name=\"" + tableName + "\") \n"
    contenido += "public class  "+ claseName + " implements Serializable { \n\n"
    contenido += "\tprivate static final long serialVersionUID = 1L;\n\n"
    return contenido


