'use strinct'

const {app} = require('electron')

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