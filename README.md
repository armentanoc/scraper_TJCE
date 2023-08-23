<h1 align="left"> Scraper ESAJ TJ-CE</h1>

<a href='https://docs.python.org/3/' target="_blank"><img alt='python' src='https://img.shields.io/badge/python-100000?style=plastic&logo=python&logoColor=white&labelColor=555555&color=0088CC'/></a>
<a href='https://flask.palletsprojects.com/en/2.3.x/' target="_blank"><img alt='flask' src='https://img.shields.io/badge/flask-100000?style=plastic&logo=flask&logoColor=white&labelColor=555555&color=3cabc3'/></a>
<a href='https://www.json.org/json-en.html' target="_blank"><img alt='json' src='https://img.shields.io/badge/JSON-100000?style=plastic&logo=json&logoColor=white&labelColor=555555&color=191919'/></a>
<a href='https://code.visualstudio.com/docs' target="_blank"><img alt='visual studio code' src='https://img.shields.io/badge/VSCode-100000?style=plastic&logo=visual studio code&logoColor=white&labelColor=555555&color=007ACC'/></a>
<a href='https://www.crummy.com/software/BeautifulSoup/bs4/doc/' target="_blank"><img alt='' src='https://img.shields.io/badge/beautifulsoup-100000?style=plastic&logo=&logoColor=white&labelColor=555555&color=181819'/></a>
<a href='https://docs.python.org/3/library/re.html' target="_blank"><img alt='regex' src='https://img.shields.io/badge/regex-100000?style=plastic&logo=regex&logoColor=white&labelColor=555555&color=8728B3'/></a>

<p>Este é um projeto de Web Scraping que utiliza Flask e Beautiful Soup para construir uma API em Python para consultar e extrair informações sobre processos judiciais, em dois graus diferentes, no sistema processual ESAJ do Tribunal de Justiça do Estado do Ceará, retornando essas informações em formato JSON.</p>

<p> A implementação visa equilibrar a classe dinâmica (coletar_dinamicamente.py) com as particularidades de cada informação que precisa ser extraída. </p>

<h2>Setup</h2>
<p>
Antes de começar, assegure-se de atender aos seguintes requisitos
<p>

* É necessário ter o `python` instalado na máquina
* O Flask suporta Python 3.8 e versões mais novas
* É necessário salvar os arquivos na mesma pasta
* As demais instalações serão feitas com a criação de um ambiente virtual `venv`, no qual serão atendidos os demais requisitos constantes no  `requirements.txt`
* As instruções abaixo consideram que o PATH para o Python é `python` no macOS/linux e `py` no Windows; note que é possível que o padrão demande a versão específica, sendo necessário adaptar para `python3` e `py3`, por exemplo, se não houver um alias configurado.

<h2>Instalando o projeto</h2>

1) Crie um ambiente virtual `python`

```shell
python -m venv venv
```

2) Ative o ambiente virtual

```shell
source venv/bin/activate
```

3) Instale o conteúdo da pasta `requirements.txt`

```shell
pip install -r requirements.txt
```

4) Rode o arquivo `api_tribunal.py`

```shell
python api_tribunal.py
```

Deve aparecer a mensagem `Running on http://127.0.0.1:5000`, que indica que o servidor Flask está em execução.

5) Abra outro terminal. Se necessário, ative novamente o ambiente virtual (2). Rode o arquivo `consultar_processo.py``

```shell
source venv/bin/activate
```

```shell
python consultar_processo.py
```

6) Se tudo tiver corrido bem, o arquivo `output_processo.json` deve ter sido gerado com as informações crawleadas. 
