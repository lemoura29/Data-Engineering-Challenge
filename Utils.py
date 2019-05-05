import re
from urllib import parse

class Utils:

    def separa_string(self,frase, simbolo, posicao):
        aux1 = frase.split(simbolo)
        return aux1[posicao].strip()

    def extrai_campos(self, dicionario, campo):
        if (campo in dicionario):
            return dicionario[campo]
        else:
            return '0'

    def separa_urls_params(self,valor):
        urls = re.findall('(?:(?:(?:ftp|http)[s]*:\/\/|www\.)[^\.]+\.[^ \n]+)', valor)
        return dict(parse.parse_qsl(parse.urlsplit(urls[0]).query))