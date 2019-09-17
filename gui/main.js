'use strinct'

const {app, BrowserWindow, Menu} = require('electron')
const url = require('url');
const path = require('path');
const Window = require('./app/class/Window')

function main(){
  let mainWindow = new Window({
    file:'./renderer/index/index.html'
  })
}

app.on('ready', main)

app.on('window-all-closed',()=>{
  app.quit()
})

if(process.env.NODE_ENV != 'production'){
  require('electron-reload')(__dirname,{
    electron: path.join(__dirname, '/node_modules/','.bin', 'electron')    
  });  
}
