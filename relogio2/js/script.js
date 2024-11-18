//dom
const horas = document.querySelector('#horas')
const minutos = document.querySelector('#minutos')
const segundos = document.querySelector('#segundos')
const saudacao = document.querySelector('#saudacao')
const dia = document.querySelector('#dia')
const mes = document.querySelector('#mes')
const ano = document.querySelector('#ano')
//evento
setInterval(relogio,1000)
setInterval(apresentacao,1000)







//funções

function relogio(){
    tempo = new Date()
    h = tempo.getHours()
    m = tempo.getMinutes()
    s = tempo.getSeconds()

    horas.textContent = h
    minutos.textContent = m
    segundos.textContent = s


}

function apresentacao(){
    dataa = new Date()
    d = dataa.getDate()
    mm = dataa.getMonth() + 1
    y = dataa.getFullYear()
    sau = saudacao

    if (h >=5 && h<12) {
        sau = "Bom Dia!!";
      } else if (h >=12 && h<18) {
        sau = "Boa Tarde!!";
      } else {
        sau = "Boa Noite!!";
      }



    saudacao.textContent = sau
    dia.textContent = d
    mes.textContent= mm
    ano.textContent = y

    
}