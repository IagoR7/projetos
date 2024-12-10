const shadow = document.querySelector('.shadow');
const charizard = document.querySelector('.charizard');

const jump = () =>{
    shadow.classList.add('jump');

    setTimeout(()=>{
        shadow.classList.remove('jump');

    }, 500);

}
const loop = setInterval(()=>{

    console.log('loop')

    const charposition = charizard.offsetLeft;
    const shadowposition = +window.getComputedStyle(shadow).bottom.replace('px','');

    if(charposition <= 60 && charposition >0 && shadowposition < 65) {

        charizard.style.animation = 'none';
        charizard.style.left = `${charposition}px`; 

        shadow.style.animation = 'none';
        shadow.style.bottom = `${shadowposition}px`;


        shadow.src = 'imagens/shadow-hahaha.gif';
        shadow.style.width = '65px'
        shadow.style.bottom = '0'
        shadow.style.marginLeft = '15px'

        clearInterval(loop)
    }

}, 10);
document.addEventListener('keydown', jump);