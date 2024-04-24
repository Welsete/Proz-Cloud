const numerosDaSorte = [37, 14, 26, 5, 94, 87];

for (let i = 0; i < numerosDaSorte.length; i++) {
    const numero = numerosDaSorte[i];
    if (numero < 50) {
        console.log(`${numero} é menor que 50`);
    } else {
        console.log(`${numero} é maior que 50`);
    }
}
