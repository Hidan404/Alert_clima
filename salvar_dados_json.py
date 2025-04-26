import json
from dados import dados_api
import os

class salvar_json():
    def __init__(self,cidade = None):
        self.local_arquivo_json = os.getenv("caminho_json")
        self.api = dados_api(cidade)



    def salvar_arquivo_json(self):
        dados = self.api.obter_dados()
        
        with open(self.local_arquivo_json, "w") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent= 4)



    def abrir_arquivo_json(self):
        try:
            with open(self.local_arquivo_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                return dados
        except FileNotFoundError:
            print("Arquivo JSON não encontrado.")
            return None
        except Exception as e:
            print(f"Erro ao abrir o arquivo: {e}")
            return None



