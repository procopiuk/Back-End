let notas = [10, 6.5, 8, 7.5, 10];

notas.pop(10);
notas.pop(7.5);

notas.push(9);

let media = (notas[0] + notas[1] + notas[2] + notas[3]) /notas.length;

console.log(notas)