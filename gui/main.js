const {app, BrowserWindow, Menu} = require('electron')
const url = require('url');
const path = require('path');

let mainWindow
let proyectoWindow
let generacionCodigoWindow

function createWindow () {
  mainWindow = new BrowserWindow({
    width: 950,
    height: 600
    /*,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
    */
  })

  mainWindow.loadFile('index.html')

  mainWindow.on('closed', function () {
    mainWindow = null;
    app.quit();
  })

  createMenu()
}

app.on('ready', createWindow)

app.on('window-all-closed', function () {
  if (process.platform !== 'darwin') app.quit()
})

app.on('activate', function () {
  if (mainWindow === null) createWindow()
})

// metodos.
let template = [
  {
    label:'Inicio'
  },{
    label:'Proyectos',
    accelerator :'Ctrl+N',
    click(){ventanaProyecto()}
  },
  {
    label:'Generador Codigo',
    click(){ventanaGeneracionCodigo()}
  },
  {
    label:'Salir',
    accelerator:'Ctrl+Q',
    click(){
      app.quit();
    }
  },
  {
    label:'Desarrollo',
    submenu:[
      {
        label:'Mostrar / Ocultar Consola',
        click(item, focusedWindow){
          focusedWindow.toggleDevTools();
        }
      },{
        role:'reload'
      }
    ]
  }
]

if(process.env.NODE_ENV != 'production'){
  require('electron-reload')(__dirname,{
    electron: path.join(__dirname, '/node_modules/','.bin', 'electron')    
  });  
}

function createMenu(){
  const menu = Menu.buildFromTemplate(template)
  Menu.setApplicationMenu(menu)
}

function ventanaProyecto(){
  proyectoWindow = new BrowserWindow({
    width: 950,
    height: 600,
    title:'Proyectos'
  })

  //proyectoWindow.loadFile('pages/proyectos.html')
  //proyectoWindow.setMenu(null)
  proyectoWindow.setMenu(null);

  proyectoWindow.loadURL(url.format({
    pathname: path.join(__dirname, '/pages/proyectos.html'),
    protocol: 'file',
    slashes: true
  }));

  proyectoWindow.on('closed', function () {
    proyectoWindow = null
  })
}


function ventanaGeneracionCodigo(){
  generacionCodigoWindow = new BrowserWindow({
    width: 950,
    height: 600,
    title:'Generación Código'
  })

  // generacionCodigoWindow.loadFile('pages/generador-codigo.html')

  generacionCodigoWindow.setMenu(null);

  generacionCodigoWindow.loadURL(url.format({
    pathname: path.join(__dirname, '/pages/generador-codigo.html'),
    protocol: 'file',
    slashes: true
  }));


  generacionCodigoWindow.on('closed', function () {
    generacionCodigoWindow = null
  })
}