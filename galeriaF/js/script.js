//dom
const alvo = document.querySelector('#alvo')
const bttwilight = document.querySelector('#bttwilight')
const bttheend = document.querySelector('#bttheend')
const btoverworld = document.querySelector('#btoverworld')
const btnether = document.querySelector('#btnether')
const btghast = document.querySelector('#btghast')
const btwither = document.querySelector('#btwither')
const btdragon = document.querySelector('#btdragon')
const btwarder = document.querySelector('#btwarder')



//event

bttwilight.addEventListener('click', twilight)
bttheend.addEventListener('click', theend)
btoverworld.addEventListener('click', overworld)
btnether.addEventListener('click', nether)
btwither.addEventListener('click', wither)
btdragon.addEventListener('click', dragon)
btwarder.addEventListener('click', warder)
btghast.addEventListener('click', ghast)
alvo.addEventListener('dblclick', herobrine)
alvo.addEventListener('click', home)


//funç


function twilight(){
    alvo.src = 'imagens/waterside-tower.png'
}
function theend(){
    alvo.src = 'imagens/TheEnd.png'
}
function overworld(){
    alvo.src = 'imagens/minecraft-verde-750x445.jpg'
}
function nether(){
    alvo.src = 'imagens/waj_in_the_nether__minecraft_wallpaper__by_blenden92_d70g7pw-fullview.jpg'
}
function wither(){
    alvo.src = 'imagens/minecraft-wither-boss-1280-x-700-wallpaper-agr42bts69ae73wv.jpg'
}
function dragon(){
    alvo.src = 'imagens/Minecraft-Ender-Dragon-Diamond-Armor-The-End.png'
}
function warder(){
    alvo.src = 'imagens/is-the-warden-technically-a-boss-v0-c5ylz28vzwza1.png'
}
function ghast(){
    alvo.src = 'imagens/Ur-Ghast.png'
}

function herobrine(){
    alvo.src= 'imagens/hq720.jpg'
}
function home(){
    alvo.src = 'imagens/Minecraft-1.jpg'
}