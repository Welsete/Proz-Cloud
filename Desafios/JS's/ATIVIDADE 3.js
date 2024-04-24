// Capturando os elementos
const titulo = document.getElementById('titulo');
const listaNaoOrdenada = document.querySelector('ul');
const link = document.querySelector('a');
const listaOrdenada = document.getElementById('lista-ordenada');

// Adicionando conteúdo aos elementos
titulo.innerText = "Título da Página";
link.innerText = "Link para Proz Educação";
listaNaoOrdenada.innerHTML = "<li>Item 1</li><li>Item 2</li><li>Item 3</li>";

// Adicionando itens com links na lista ordenada
listaOrdenada.innerHTML = "<li><a href='https://site1.com'>Link 1</a></li><li><a href='https://site2.com'>Link 2</a></li><li><a href='https://site3.com'>Link 3</a></li>";
