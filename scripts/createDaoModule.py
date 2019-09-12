
import fileModule

def createDao(ruta, nombreClase, tipoDatoPk):
    claseDao = nombreClase + "Dao"
    contenido = "package com.resident.app.dao; \n\n"
    contenido += "import org.springframework.data.jpa.repository.JpaRepository; \n"
    contenido += "import org.springframework.stereotype.Repository; \n\n"
    contenido += "import com.resident.app.entities.Usuario; \n\n"
    contenido += "@Repository \n"
    contenido += "public interface "+ claseDao +" extends JpaRepository<"+nombreClase+", "+tipoDatoPk+"> { \n\n"
    contenido += "} \n"

    # generate los archivos.
    path = ruta + claseDao + ".java"
    file_java_dao = fileModule.establecerArchivo(path,'w')
    fileModule.escribirArchivo(file_java_dao,contenido)


