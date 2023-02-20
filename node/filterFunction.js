// Funcion filter:
// Retorna un NUEVO array sin modificar el que se le pasa, cuando se cumple una condicion.
// Ejecuta una funcion x.filter(funcion definida externa o internamente)
// Dependiendo de la funcion de validacion se puede tardar mas o menos con grandes cantidades de datos
// La funcion de validacion debe retornar true o false para decidir si un elemento se incluye o no
// en el nuevo array.
function checkOdd(num){
    return num % 2 != 0;
}

let nums = [1,2,3,4,5,6]

//Se define la funcion internamente tipo "callback"
const isEven = listaNums => listaNums.filter(x => x % 2 == 0);
let resultEven = isEven(nums);
console.log(resultEven)

//Se pasa la referencia a a funcion no se ejecuta
const isOdd = listaNums => listaNums.filter(checkOdd);
let resultOdd = isOdd(nums);
console.log(resultOdd)