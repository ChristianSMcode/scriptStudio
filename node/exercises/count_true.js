//Funcion que retorne la cantidad de valores verdaderos en una lista
//Mi solucion
function countValues(lista){
    let counter=0;
    for (booleanValue of lista){
        if (booleanValue){
            counter+=1;
        };
    };
    return counter;
}

let result=countValues([]);
console.log(result);
//Solucion otras personas
const countTruev1 = r => r.filter(Boolean).length;
function countTruev2(arr){
    return arr.filter(x=> x == true).length;
}
//Aprendido ejercicio ====================================================================================
// Funciones flecha de una linea:
// Nombre funcion (countTrue) parametro (r) => ejecucion y retorno (r.filter(Boolean).lenght)
// Debe contener una sola expresion, debe retornar un valor (implicito, sin la palabra return) y debe ser de contexto
// interno, no modifica variables externas.
// Funcion filter:
// Retorna un NUEVO array sin modificar el que se le pasa, cuando se cumple una condicion.
// Ejecuta una funcion x.filter(funcion definida externa o internamente)