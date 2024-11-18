//dom
const horas = document.querySelector('#horas')
const minutos = document.querySelector('#minutos')
const segundos = document.querySelector('#segundos')
//evento
setInterval(relogio,1000)






//funções

function relogio(){
    tempo = new Date()
    h = tempo.getHours()
    m = tempo.getMinutes()
    s = tempo.getSeconds()

    /*
    if (h >=5 && h<12){ 
    bom dia!}
    else if (h>=12 && h<13 )
    else(boa noite)



    */

    horas.textContent = h
    minutos.textContent = m
    segundos.textContent = s
    
}