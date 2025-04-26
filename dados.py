import requests
import os

class dados_api:
    def __init__(self, cidade=None):
        self.linguagem = "pt_br"
        self.pais = "BR"
        self.link = "https://api.openweathermap.org/data/2.5/forecast"
        self.chave_api = os.getenv("OPENWEATHER_KEY")
        # Se caso a cidade não for passada é usada uma automática lembretepara mim não esquecer
        self.cidade = cidade or self.obter_cidade_automatica()

    def obter_cidade_automatica(self):
        try:
            resposta = requests.get("https://ipinfo.io/json", timeout=5)
            if resposta.status_code == 200:
                dados = resposta.json()
                return dados.get("city", "São Paulo")
        except:
            return "São Paulo"

    def obter_dados(self):
        parametros = {
            "q": self.cidade,
            "appid": self.chave_api,
            "lang": f"{self.linguagem},{self.pais}",
            "units": "metric"
        }    

        try:
            resposta = requests.get(self.link, params=parametros, timeout=10)
            if resposta.status_code == 200:
                return resposta.json()
            else:
                print(f"Erro ao obter dados: {resposta.status_code} - {resposta.reason}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return None
