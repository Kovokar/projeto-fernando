# 🌡️ Smart AC Control - Sistema de Controle Inteligente de Ar Condicionado

## 📝 Visão Geral do Projeto

O **Smart AC Control** é uma solução inovadora de automação residencial que permite controlar a temperatura do ar condicionado de forma inteligente e personalizada, utilizando um Raspberry Pi como núcleo do sistema.

## 🎥 Demonstração do Projeto

[![Vídeo Explicativo do Smart AC Control](https://img.youtube.com/vi/SEU_LINK_AQUI/0.jpg)](https://www.youtube.com/watch?v=SEU_LINK_AQUI)


## 🚀 Funcionalidades Principais

### Controle Manual de Temperatura
- **Interface Intuitiva**: Botões simples de "Frio" e "Quente"
- **Ajuste Preciso**: Incremento e decremento de temperatura
- **Feedback Visual**: Exibição em tempo real da temperatura selecionada

### Modo Automático Inteligente
- **Cálculo Automático**: Ajuste da temperatura baseado na umidade ambiente
- **Algoritmo Adaptativo**: Calcula temperatura ideal considerando condições climáticas

## 🛠️ Arquitetura do Sistema

### Componentes
- **Frontend**: Interface web responsiva
- **Backend**: API Flask em Python
- **Hardware**: Raspberry Pi como controlador central

### Fluxo de Funcionamento

1. **Interação do Usuário**
   - Ajuste manual da temperatura
   - Seleção entre modo manual e automático

2. **Processamento**
   - Envio de requisições HTTP para o backend
   - Processamento da temperatura desejada

3. **Execução**
   - Envio de comandos para o ar condicionado
   - Registro de logs e histórico de alterações

## 🔧 Tecnologias Utilizadas

- **Linguagens**:
  - Python (Backend)
  - JavaScript (Frontend)
  - HTML/CSS (Interface)

- **Frameworks e Bibliotecas**:
  - Flask
  - CORS
  - Vanilla JavaScript

- **Hardware**:
  - Raspberry Pi
  - Módulos de comunicação com ar condicionado

## 📦 Instalação e Configuração

### Pré-requisitos
- Raspberry Pi
- Python 3.7+
- Navegador web moderno

### Passos de Instalação

1. Clone o repositório
   ```bash
   git clone https://github.com/seu-usuario/smart-ac-control.git
   cd smart-ac-control
   ```

2. Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```


3. Inicie o servidor
   ```bash
   python src/main.py
   ```

## 🔒 Segurança

- Validação de entrada de dados
- Proteção contra requisições inválidas
- Suporte a CORS


## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar um pull request.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.


**Feito com ❤️ e 🥶/🥵 por Entusiastas de Automação Residencial**