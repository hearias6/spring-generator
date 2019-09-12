
import fileModule

def createService(ruta, nombreClase):
    claseService = nombreClase + "Service"
    contenido = "package com.resident.app.services; \n\n";
    contenido += "import org.springframework.http.ResponseEntity; \n"
    contenido += "import com.resident.app.response.Response; \n\n"
    contenido += "public interface UsuarioService { \n\n "
    contenido += "\tResponseEntity<Response> save(Usuario entity);\n"
    contenido += "\tResponseEntity<Response> findAll();\n"
    contenido += "\tResponseEntity<Response> findAllWithPaginate();\n"
    contenido += "\tResponseEntity<Response> findById(Long id);\n"
    contenido += "\tResponseEntity<Response> update(Usuario entity);\n";
    contenido += "\tResponseEntity<Response> deleteById(Long id);\n";

    # generate los archivos.
    path = ruta + claseService + ".java"
    file_java_service = fileModule.establecerArchivo(path,'w')
    fileModule.escribirArchivo(file_java_service,contenido)


