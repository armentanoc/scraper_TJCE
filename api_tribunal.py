from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import json
import requests
import re
from coletar_dinamicamente import coletar_informacao

app = Flask(__name__)

@app.route('/api', methods=['POST'])

def consultar_processo():

    cnj = request.json['numero_processo']

    url_1grau = f'https://esaj.tjce.jus.br/cpopg/show.do?processo.codigo=01Z081I9T0000&processo.foro=1&processo.numero={cnj}'
    url_2grau = f'https://esaj.tjce.jus.br/cposg5/search.do?conversationId=&paginaConsulta=0&cbPesquisa=NUMPROC&numeroDigitoAnoUnificado=0624478-78.2023&foroNumeroUnificado=0000&dePesquisaNuUnificado={cnj}&dePesquisaNuUnificado=UNIFICADO&dePesquisa=&tipoNuProcesso=UNIFICADO'

    #Realizando o request com a url do primeiro grau e parseando o HTML
    response_1grau = requests.get(url_1grau)
    soup_1grau = BeautifulSoup(response_1grau.text, 'html.parser')

    #Inicializando a variável de lista e coletando dinamicamente os campos
    dados = []
    
    #Dicionário com dados a serem coletados no 1º grau
    dados_1grau = {
    "numeroProcesso":"Número do Processo", #id_elemento : chave_json
    "classeProcesso":"Classe",
    "areaProcesso":"Área",
    "assuntoProcesso":"Assunto",
    "dataHoraDistribuicaoProcesso":"Data da Distribuição",
    "numeroProcesso":"Número do Processo",
    "valorAcaoProcesso":"Valor da Ação",
    "tableTodasPartes":"Partes",
    "juizProcesso":"Juiz(a)", #exclusivo 1º grau
    "foroProcesso":"Foro", #exclusivo 1º grau
    "varaProcesso":"Vara" #exclusivo 1º grau
    }
    
    for key, value in dados_1grau.items():
        id_elemento = key
        chave_json = value
        dados = coletar_informacao(id_elemento, chave_json, dados, soup_1grau)

    # Crawleando as movimentações

    movimentacoes_1grau = soup_1grau.find_all(class_=["dataMovimentacao", "descricaoMovimentacao"])
    movimentacoes = []

    for i in range(0, len(movimentacoes_1grau), 2):
        data = movimentacoes_1grau[i].text.strip()
        data_tratada = re.sub(r"(\n+)|(\t+)|(\r+)", "", data)
        descricao = movimentacoes_1grau[i].find_next_sibling(class_="descricaoMovimentacao").text.strip()
        descricao_tratada = re.sub(r"(\n+)|(\t+)|(\r+)", "", descricao)

        movimentacoes.append({
            'Data': data_tratada,
            'Descrição': descricao_tratada
        })

    if movimentacoes:
        info = {"Últimas Movimentações": movimentacoes }
    else:
        info = {"Últimas Movimentações": "Não localizado(a)."}
    dados.append(info)

    #Começa a pesquisa para o 2º Grau

    response_2grau = requests.get(url_2grau)
    soup_2grau = BeautifulSoup(response_2grau.text, 'html.parser')

    #Pegando como base os 8 primeiros itens do dicionário de 1º grau, transformando em lista e fazendo o slice
        #Juiz, Foro e Vara, porque não existem no 2º grau
    dados_2grau = list(dados_1grau.items())[:7]

    #Transformando novamente em dict
    dados_2grau = dict(dados_2grau)

    #Adicionando campos exclusivos do 2º grau
    dados_2grau["secaoProcesso"] = "Seção"
    dados_2grau["orgaoJulgadorProcesso"] = "Órgão julgador"
    dados_2grau["relatorProcesso"] = "Relator(a)"
    dados_2grau["volumeApensoProcesso"] = "Volume"

    for key, value in dados_2grau.items():
        id_elemento = key
        chave_json = value
        dados = coletar_informacao(id_elemento, chave_json, dados, soup_2grau)

    movimentacoes_2grau = soup_2grau.find_all(class_=["dataMovimentacao", "descricaoMovimentacao"])
    movimentacoes = []

    for i in range(0, len(movimentacoes_1grau), 2):
        data = movimentacoes_1grau[i].text.strip()
        data_tratada = re.sub(r"(\n+)|(\t+)|(\r+)", "", data)
        descricao = movimentacoes_1grau[i].find_next_sibling(class_="descricaoMovimentacao").text.strip()
        descricao_tratada = re.sub(r"(\n+)|(\t+)|(\r+)", "", descricao)

        movimentacoes.append({
            'Data': data_tratada,
            'Descrição': descricao_tratada
        })

    if movimentacoes:
        info = {"Últimas Movimentações": movimentacoes }
    else:
        info = { "Últimas Movimentações": "Não localizado(a)."}
    dados.append(info)

    return jsonify(dados)

if __name__ == '__main__':
    app.run()