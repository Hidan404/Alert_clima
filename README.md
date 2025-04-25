# 🌦️ AlertaClima5D - Aplicativo de Previsão do Tempo com Notificações

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Aplicativo Python que fornece alertas meteorológicos inteligentes com integração ao Telegram e notificações desktop para Linux.

![Demonstração do AlertaClima5D](demo.gif) <!-- Adicione um gif de demonstração posteriormente -->

## ✨ Funcionalidades Principais

- ⏰ Previsão horária estratégica (09h, 15h, 21h)
- 🌍 Suporte a qualquer localização global
- 📊 Consolidação de dados meteorológicos em JSON
- 🔔 Sistema dual de notificações:
  - 💻 Notificações desktop nativas (Linux)
  - 📲 Alertas via Telegram
- 🎨 Visualização intuitiva com emojis descritivos
- 🤖 Integração contínua com APIs meteorológicas

## 🛠️ Tecnologias Utilizadas

| Tecnologia               | Descrição                                  |
|--------------------------|-------------------------------------------|
| Python 3.10+             | Linguagem principal                       |
| OpenWeather API          | Dados meteorológicos em tempo real        |
| Telegram Bot API         | Comunicação com mensageiro                |
| JSON                     | Armazenamento local de dados              |
| notify-send              | Notificações desktop no Linux             |
| Requests                 | Comunicação HTTP com APIs                 |

## 📁 Estrutura do Projeto

```bash
AlertaClima5D/
├── app.py
├── dados.py
├── salvar_dados_json.py
├── icones_descricao.py
├── enviar_msg_telegram.py
├── README.md
├── LICENSE
├── requirements.txt



## ▶️ Como executar

1. **Clone o repositório**
  ```bash
  git clone https://github.com/seuusuario/AlertaClima5D.git
  cd AlertaClima5D
  ```

2. **Crie um ambiente virtual e ative**
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux ou Mac
  venv\Scripts\activate     # Windows
  ```

3. **Instale as dependências**
  ```bash
  pip install -r requirements.txt
  ```
  > **Nota:** Caso o arquivo `requirements.txt` ainda não exista, crie-o e adicione:
  > ```
  > requests
  > ```

4. **Configure o Bot do Telegram**
  - No arquivo `enviar_msg_telegram.py`, atualize as seguintes linhas:
    ```python
    self.token = "SEU_TOKEN_AQUI"
    self.chat_id = "SEU_CHAT_ID_AQUI"
    ```
  - Certifique-se de que o seu bot no Telegram esteja ativo (já tenha enviado uma mensagem para ele).

5. **Execute o aplicativo**
  ```bash
  python app.py
  ```

## ⚙️ Requisitos

- **Sistema Operacional:** Linux ou WSL (requer `notify-send` instalado para notificações gráficas)
- **Conta no Telegram:** Com um Bot configurado via [@BotFather](https://core.telegram.org/bots#botfather)
- **API Key da OpenWeather:** Crie sua chave [aqui](https://openweathermap.org/api)
