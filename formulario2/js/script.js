//dom
const unid1 = document.querySelector('#uni1')
const unid2 = document.querySelector('#uni2')
const unid3 = document.querySelector('#uni3')
const botao = document.querySelector('#botao')
const resultado = document.querySelector('#resultado')

//evento

botao.addEventListener('click', calcular2)







//funções

function calcular2(){
    u1 = Number(unid1.value)
    u2 = Number(unid2.value)
    u3 = Number(unid3.value)
    nota = (u1 + u2 + u3) / 3
    
    

    if(nota>=7){
        resultado.textContent = `A sua nota é ${nota.toFixed(1)} voce esta aprovado!`    
    }else if (nota> 3 && nota <6.9){
        resultado.textContent = `A sua nota é ${nota.toFixed(1)} voce esta na recuperação`    
    }
    
    else{
        resultado.textContent = `A sua nota é ${nota.toFixed(1)} Voce esta Reprovado `    
    }
}