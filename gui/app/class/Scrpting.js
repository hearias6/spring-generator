
const {PythonShell} = require('python-shell')

class Scripting{

    constructor (){}
    
    // enviamos datos al script .
    enviarInfoScript(ruta, script){
        let pyshell = new PythonShell(ruta+script);
 
        // sends a message to the Python script via stdin
        pyshell.send('Nuevo Mensaje');
         
        pyshell.on('message', function (message) {
          // received a message sent from the Python script (a simple "print" statement)
          console.log(message);
        });
    }

    // ejecutar un script  ok testado.
    ejecutarScript(ruta, script){
        PythonShell.run(ruta + script, null, function (err, results) {
            if (err) throw err;
            console.log(results);
        });
    }
    
}

module.exports = Scripting

