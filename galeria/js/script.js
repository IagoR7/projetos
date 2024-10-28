//dom
const alvo = document.querySelector('#alvo')
const btalegria = document.querySelector('#btalegria')
const bttristeza = document.querySelector('#bttristeza')
const btraiva = document.querySelector('#btraiva')
const btnojinho = document.querySelector('#btnojinho')


//event

btalegria.addEventListener('click', alegria)
bttristeza.addEventListener('click', tristeza)
btraiva.addEventListener('click', raiva)
btnojinho.addEventListener('click', nojinho)
btalegria.addEventListener('dblclick', sorrindo)
bttristeza.addEventListener('dblclick', triste)
btraiva.addEventListener('dblclick', puto)
btnojinho.addEventListener('dblclick', nojo)


//funç


function alegria(){
    alvo.src = 'imagens/02.png'
}
function tristeza(){
    alvo.src = 'imagens/04.png'
}
function raiva(){
    alvo.src = 'imagens/01.png'
}
function nojinho(){
    alvo.src = 'imagens/03.png'
}
function sorrindo(){
    alvo.src = 'imagens/sorrindo.jpg'
}
function triste(){
    alvo.src = 'imagens/triste.webp'
}
function puto(){
    alvo.src = 'imagens/puto.webp'
}
function nojo(){
    alvo.src = 'imagens/images.jfif'
}
