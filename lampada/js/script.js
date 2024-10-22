//dom
const breno = document.querySelector('#breno')
const btligar = document.querySelector('#btligar')
const btdesligar = document.querySelector('#btdesligar')


//event

btligar.addEventListener('click',ligar )
    
btdesligar.addEventListener('click',desligar)

btligar.addEventListener('dblclick', quebrar)

//função

function ligar(){
    breno.src = 'imagens/acesa (1).gif'
}
function desligar(){
    breno.src = 'imagens/apagada.gif'
}
function quebrar(){
    breno.src = 'imagens/quebrada.jpg'
}