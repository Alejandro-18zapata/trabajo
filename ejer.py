const notas = [
  { materia: "Matemáticas", nota: 4.5 },
  { materia: "Lenguaje", nota: 3.8 },
  { materia: "Ciencias", nota: 4.2 }
];

const promedio = notas.reduce((acc, nota) => acc + nota.nota, 0) / notas.length;
const aprobado = promedio >= 3.5;

console.log("Notas:");
notas.forEach(nota => console.log(`${nota.materia}: ${nota.nota}`));
console.log(`Promedio: ${promedio.toFixed(2)}`);
console.log(`Aprobado: ${aprobado ? "Sí" : "No"}`);
