const primeiro = document.querySelector('#primeiro')
const segundo = document.querySelector('#segundo')
const botaoA = document.querySelector('#botaoA')
const botaoS = document.querySelector('#botaoS')
const botaoM = document.querySelector('#botaoM')
const botaoD = document.querySelector('#botaoD')
const resultado = document.querySelector('#resultado')

botaoA.addEventListener('click', adicao)
botaoS.addEventListener('click', subtracao)
botaoM.addEventListener('click', multiplicacao)
botaoD.addEventListener('click', divisao)


function adicao(){
    pri = Number(primeiro.value)
    seg = Number(segundo.value)
    adi = pri + seg

    resultado.textContent = `O Resultado é ${adi}!`    

}
function subtracao(){
    pri = Number(primeiro.value)
    seg = Number(segundo.value)
    sub = pri - seg

    resultado.textContent = `O Resultado é ${sub}!` 

}
function multiplicacao(){
    pri = Number(primeiro.value)
    seg = Number(segundo.value)
    mult = pri * seg

    resultado.textContent = `O Resultado é ${mult}!` 

}
function divisao(){
    pri = Number(primeiro.value)
    seg = Number(segundo.value)
    div = pri / seg

    resultado.textContent = `O Resultado é ${div}!` 

}