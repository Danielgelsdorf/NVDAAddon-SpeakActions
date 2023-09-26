import requests
import re
class RequestAcoes:
    def buscarAcaoCodigo(self, codigo):

        url=f"http://gelsdorf.com.br/acao?cod={codigo}"
        url2=f"http://localhost/acao?cod={codigo}"
        res= requests.get(url)
        return res.text.split(",")
    def buscarSelic(self):
        url="http://gelsdorf.com.br/selic"
        url2="http://localhost/selic"
        res=requests.get(url)
        return res.text.split(',')
    def separarPalavras(self, frase):
        dividido=frase.split(":\"")
        return re.sub('["]','', dividido[1])
    def tratarPreco(self, preco):
        preco=preco.split(":")
        return preco[1]
