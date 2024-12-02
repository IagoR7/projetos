//dom
const peso = document.querySelector('#peso')
const altura = document.querySelector('#altura')
const botao = document.querySelector('#botao')
const resultado = document.querySelector('#resultado')

//evento

botao.addEventListener('click', calculo)







//funções

function calculo(){
    p = Number(peso.value)
    a = Number(altura.value)
    imc = p/(a*a)
    

    if(imc<18.5){
        resultado.textContent = `O seu imc é  ${imc.toFixed(1)} - Voçê está magro!`    
    }else if (imc> 18.5 && imc <24.99){
        resultado.textContent = `O seu imc é  ${imc.toFixed(1)} - Voçê está no peso ideal!`    
    }
    else if (imc> 25 && imc <30){
        resultado.textContent = `O seu imc é  ${imc.toFixed(1)} - Voçê está com sobrepeso!`    
    }
    else{
        resultado.textContent = `O seu imc é  ${imc.toFixed(1)} - Voçê está em obesidade morbida!`    
    }
}