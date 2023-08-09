import re

def coletar_informacao(id_elemento, chave_json, dados, soup):

    valor_json = None
    info = soup.find_all(id=id_elemento)

    if info:
        valor_json = info[0].text.strip()
        valor_json_tratado = re.sub(r"(\n+)|(\t+)|(\r+)", "", valor_json)
        info = {f"{chave_json}" : valor_json_tratado}    
    else:
        info = {f"{chave_json}" : "Não localizado(a)."}
    
    dados.append(info)
    return dados