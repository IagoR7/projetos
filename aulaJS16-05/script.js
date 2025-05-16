/*let numeros = [1,2,3,4,5];

// multiplicando
let dobrados = numeros.map(function(numero){
    return numero * 2;
})

console.log(dobrados)

//somando

let soma =  numeros.reduce(function(total, numero){
    return total + numero;
})
console.log(soma);

//removendo

function removerElemento(array, elemento) {
  // Usando o método filter para criar um novo array sem o elemento específico
  return array.filter(function(item) {
    return item !== elemento;
  });
}

let frutas = ["maçã", "banana", "laranja", "manga"];
let resultado = removerElemento(frutas, "laranja");
console.log(resultado);

//maior numero

function maiornumero(array){
    return array.reduce(function(max,atual){
            return array.reduce(function(max,atual){
                return atual > max ? atual : max;
            })
    })
}

let numero = [10,25,35,5,40,20];

let maior = maiornumero(numero);
console.log(maior);

//concatena

let array1 = [1,2,3];
let array2 = [4,5,6];

//usando o metodo concat

let concatenando = array1.concat(array2);

console.log(concatenando)
// verificar se todos os elementos são pares

function todossaopares(array) {
    return array.every(function(numero) {
      return numero % 2 === 0;
    });
  }
  
  let pares = [2, 4, 6, 8];
  console.log(todossaopares(pares)); // true
  
  let numero = [2, 4, 5, 8];
  console.log(todossaopares(numero));

  //somando elemento pares

  function somapares(array){
    return array
    .filter(function(numero){
        return numero %2 == 0;
    })
    .reduce(function(soma,numero){
        return soma + numero;
    } , 0)
  }

  let numeros = [1,2,3,4,5,6];
  let resultado = somapares(numeros)
  console.log(resultado)


  //encontrar a média de um array de número

  function calcularMedia(array) {
    let soma = array.reduce(function(total, numero) {
      return total + numero;
    }, 0);
    return soma / array.length;
  }
  
  let numeros = [5, 10, 2, 25];
  let media = calcularMedia(numeros);
  console.log(media);

//verificar se um array contem um elemento

function contemElemento(array, elemento){
    return array.includes(elemento);
}
  
let frutas = ["maça","banana","laranja"];
console.log(contemElemento(frutas,"banana"));
console.log(contemElemento(frutas,"uva"));


//ordernar em metodo crescente

function ordernarCrescente(array){
    return array.sort(function(a,b){
        return a - b;
    });
}
  
let numeros = [5,3,8,1,2];
let ordernar = ordernarCrescente(numeros);
console.log(ordernar);

//multiplicar

function multiplicar(array, multiplicador){
    return array.map(function(numero){
        return numero * multiplicador ;
    });
}
  
let numeros = [5,3,8,1,2];
let resultado = multiplicar(numero , 5);
console.log(resultado);

//mesclar dois arrays e remover duplicatas


function mesclarEremoverDup(array1, array2){
    let mesclado = array1.concat(array2);
    return[...new Set(mesclado)];
}

let array1 = [1,2,3];

let array2 = [3,4,5];

let resultado = mesclarEremoverDup(array1,array2)
console.log(resultado)

//inverter a ordem dos elemetnso de um array

function inverterArray(array){
    return array.reverse();
}

let numeros = [1,2,3,4,5];

let invertido = inverterArray(numeros);

console.log(invertido);


//remover falsos valores de um array

function removerFalsosValores(array){
    return array.filter(Boolean);
}

let valores = [0, "maça","",false,"banana", null , "laranja"];

let resultado = removerFalsosValores(valores)

console.log(resultado)*/


//agrupar elemento em pares

