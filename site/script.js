// Obtém o elemento do slider e o valor do texto
const slider = document.getElementById('temperature');
const temperatureValue = document.getElementById('temperature-value');

// Atualiza o valor exibido conforme o slider é movido
slider.addEventListener('input', function() {
    temperatureValue.textContent = `${slider.value}°C`;
});
