// Método Simples
const produtoSimples = document.getElementById('produto-simples');
produtoSimples.innerHTML = `
    <h2>Produto Simples</h2>
    <p>Nome: Caneta</p>
    <p>Descrição: Caneta azul de qualidade premium.</p>
    <p>Preço: R$ 2,50</p>
`;

// Método Complexo
const produtoComplexo = document.getElementById('produto-complexo');
const h2 = document.createElement('h2');
h2.textContent = 'Produto Complexo';

const nome = document.createElement('p');
nome.textContent = 'Nome: Caderno';

const descricao = document.createElement('p');
descricao.textContent = 'Descrição: Caderno grande com capa dura e 100 folhas pautadas.';

const preco = document.createElement('p');
preco.textContent = 'Preço: R$ 15,00';

produtoComplexo.appendChild(h2);
produtoComplexo.appendChild(nome);
produtoComplexo.appendChild(descricao);
produtoComplexo.appendChild(preco);
