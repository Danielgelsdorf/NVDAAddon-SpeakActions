import globalPluginHandler
import re

import json
from scriptHandler import script
import ui
import api
import datetime
import wx
import gui
from . import RequestAcoes

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = "speakActions"

    @script(
        description="pega a tacha selic.",
        gestures=["kb:nvda+y"]
    )
    def script_get_selic(self, gesture):
        resposta= RequestAcoes.RequestAcoes().buscarSelic()
        valor=resposta[0].split(":\"")
        preco=re.sub('["]','', valor[1])    
        if not resposta:
            ui.message("não foi possível pegar a selic.")
        ui.message(f"o valor atual da selic é: {preco}% .")
    @script(
        description="pega preços de ações de acordo com o código digitado pelo usuário.",
        gestures=["kb:nvda+shift+y"]
    )
    def script_get_precos(self, gesture):
        
        acaoRequest=RequestAcoes.RequestAcoes()
        codigoAcao= api.getClipData()
        if(len(codigoAcao)<1):
            ui.message("área de transferência não contêm nem um código de ação.")
            return
        resposta= acaoRequest.buscarAcaoCodigo(codigoAcao)
        nome=acaoRequest.separarPalavras(resposta[0])
        precoatual=acaoRequest.tratarPreco(resposta[1])
        precoMaisAlto=acaoRequest.tratarPreco(resposta[2])
        precoMaisBaixo=acaoRequest.tratarPreco(resposta[3])
        precoMaisBaixo=re.sub('[}]', '', precoMaisBaixo)
        falar=f"nome da ação: {nome} \n preço atual da ação: R${precoatual} \n preço mais alto do dia: R${precoMaisAlto} \n preço mais baixo do dia: R${precoMaisBaixo} ."
        ui.message(falar)
    