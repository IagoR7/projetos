//dom
const shadow =document.querySelector('#shadow')

//evento
document.addEventListener('keydown', function(event){
    if(event.key == 'ArrowUp'){
        if(!shadow.classList.contains('pulot')){
            shadow.classList.add('pulot')
        }
    }
        
})








//funções


