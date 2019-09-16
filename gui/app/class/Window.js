'use strict'

const {BrowserWindow} = require('electron')

// propiedades por default.
const propiedades = {
    widht:800,
    height:600,
    show:false
}

class window extends BrowserWindow{

    constructor ({file, ...windowSettings}){

        super({...propiedades, windowSettings})

        // cargar la vista.
        this.loadFile(file)
        
        this.webContents.openDevTools()
        this.once('ready-to-show',()=>{
            this.show()
        })

    }
}

module.exports  = window;