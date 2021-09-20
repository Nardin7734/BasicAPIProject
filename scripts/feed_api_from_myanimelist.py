from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup
import re
from datetime import datetime


codificacao = 'iso-8859-1'
cabecalho = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
url = 'https://myanimelist.net/topmanga.php'
busca_padrao = 'https://myanimelist.net/manga/'
total_desejado = 10
lista_mangas = []



def return_soup(url, cabecalho):
    """Retorna um objeto BS4 pronto para ser vasculhado"""
    document = urlopen(Request(url, headers=cabecalho))
    document_readed = document.read()
    return BeautifulSoup(document_readed.decode(codificacao), 'html.parser')


def para_data_valida(texto):
    try:
        return datetime.strptime(texto.replace('  ', ' '), '%b %d, %Y').date()
    except:
        print('Não conseguiu retornar uma data válida!')


def create_dict(sopa):
    """Cria o dicionario para o envio a API"""
    links = sopa.find_all(href=True)
    for link in links:
        midia = {}
        if len(lista_mangas) <= total_desejado:
            if re.search(busca_padrao, link['href']):
                if len(link.text.strip()) > 0:
                    manga_page = return_soup(link['href'], cabecalho)
                    midia['nome'] = manga_page.find(itemprop='name').text
                    midia['descricao'] = manga_page.find(itemprop='description').text
                    midia['nota'] = manga_page.find('div', {'score-label'}).text.split('.')[0]
                    divs = manga_page.findAll('div', {'spaceit_pad'})
                    for t in divs:
                        if re.search('Published:', t.text):
                            lancamento = t.text.split(': ')[1].split(' to')[0]
                            midia['lancamento'] = para_data_valida(lancamento)

                    lista_mangas.append(midia)


create_dict(return_soup(url, cabecalho))

for i in lista_mangas:
    print(i)