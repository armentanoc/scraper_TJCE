<h1 align="left"> Crawler ESAJ TJ-CE</h1>

![GitHub repo size](https://img.shields.io/github/repo-size/scottydocs/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md)
![GitHub stars](https://img.shields.io/github/stars/scottydocs/README-template.md?style=social)
![GitHub forks](https://img.shields.io/github/forks/scottydocs/README-template.md?style=social)

<p>Este é um projeto de Web Scraping que utiliza Flask e Beautiful Soup para construir uma API em Python para consultar e extrair informações sobre processos judiciais, em dois graus diferentes, no sistema processual ESAJ do Tribunal de Justiça do Estado do Ceará, retornando essas informações em formato JSON.</p>

<p> A implementação visa equilibrar a classe dinâmica (coletar_dinamicamente.py) com as particularidades de cada informação que precisa ser extraída. </p>

<h2>Setup</h2>
<p>
Antes de começar, assegure-se de atender aos seguintes requisitos
<p>

* É necessário ter o `python` instalado na máquina
* É necessário salvar os arquivos na mesma pasta
* As demais instalações serão feitas com a criação de um ambiente virtual `venv`, no qual serão atendidos os demais requisitos constantes no  `requirements.txt` 

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
