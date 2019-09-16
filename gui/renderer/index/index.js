const python = require('../../app/class/Scrpting')

//const Scripting = require('./app/class/Scrpting')
const pathScript = '../../../scripts/'

function getHolaMundo(){
    let scripsPython = new Scripting()
    scripsPython.ejecutarScript(pathScript,'holamundo.py')
    scripsPython.enviarInfoScript(pathScript,'holamundo.py')
}