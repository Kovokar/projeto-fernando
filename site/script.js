// Variáveis para os elementos HTML que representam os botões de "Frio" e "Quente", e o botão de temperatura
var cold = document.getElementById("cold");
var hot = document.getElementById("hot");
var btnCold = document.getElementById("btn-cold");
var btnHot = document.getElementById("btn-hot");
var result = document.getElementById("result");
var score = 23; // Valor inicial da temperatura
var timeout; // Variável que irá armazenar o temporizador de inatividade

// Função para enviar a temperatura para o backend
function sendTemperature() {
  console.log("Enviando temperatura: " + score); // Exibe a temperatura no console antes de enviar

  // Exemplo de chamada para o endpoint usando Fetch
  fetch('http://127.0.0.1:5000/temperatura-manual', {
    method: 'POST', // Método HTTP para enviar dados
    headers: {
      'Content-Type': 'application/json' // Define o tipo de conteúdo como JSON
    },
    body: JSON.stringify({
      temperatura: score, // Envia a temperatura como um valor JSON
      ie_manual: true // Envia a flag 'ie_manual' como true para indicar que a temperatura foi ajustada manualmente
    })
  })
    .then(response => response.json()) // Converte a resposta para JSON
    .then(data => console.log("Resposta do endpoint:", data)) // Exibe a resposta do servidor no console
    .catch(error => console.error("Erro na chamada ao endpoint:", error)); // Exibe erros, se houver
}

// Função para aumentar a temperatura
function up() {
  if (score < 30) { // Impede que a temperatura ultrapasse 30°C
    score++; // Aumenta a temperatura em 1
  }
  result.innerHTML = score; // Atualiza o valor da temperatura exibido na tela
  resetInactivityTimer(); // Reseta o timer de inatividade para 3 segundos
}

// Função para diminuir a temperatura
function down() {
  if (score > 18) { // Impede que a temperatura caia abaixo de 18°C
    score--; // Diminui a temperatura em 1
  }
  result.innerHTML = score; // Atualiza o valor da temperatura exibido na tela
  resetInactivityTimer(); // Reseta o timer de inatividade para 3 segundos
}

// Adiciona o efeito de hover no botão "Frio" para mostrar uma classe de estilo
cold.addEventListener('mouseover', function () {
  btnCold.classList.add('cold-active'); // Adiciona a classe 'cold-active' quando o mouse está sobre o botão
  resetInactivityTimer(); // Reseta o timer de inatividade
});

// Remove o efeito de hover no botão "Frio" quando o mouse sai do botão
cold.addEventListener('mouseout', function () {
  btnCold.classList.remove('cold-active'); // Remove a classe 'cold-active'
});

// Adiciona o efeito de hover no botão "Quente" para mostrar uma classe de estilo
hot.addEventListener('mouseover', function () {
  btnHot.classList.add('hot-active'); // Adiciona a classe 'hot-active' quando o mouse está sobre o botão
  resetInactivityTimer(); // Reseta o timer de inatividade
});

// Remove o efeito de hover no botão "Quente" quando o mouse sai do botão
hot.addEventListener('mouseout', function () {
  btnHot.classList.remove('hot-active'); // Remove a classe 'hot-active'
});

// Função para resetar o timer de inatividade
function resetInactivityTimer() {
  clearTimeout(timeout); // Limpa o temporizador atual
  timeout = setTimeout(sendTemperature, 3000); // Cria um novo temporizador de 3 segundos que chama a função sendTemperature
}

// Inicializa o timer de inatividade quando a página carregar
resetInactivityTimer(); // Chama a função para garantir que o timer comece imediatamente
