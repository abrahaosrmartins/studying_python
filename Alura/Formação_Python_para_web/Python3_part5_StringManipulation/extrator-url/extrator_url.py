import re


class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    @staticmethod
    def sanitiza_url(url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")

    def get_indice_interrogacao(self):
        return self.url.find('?')  # find() retorna o indice do elemento

    def get_url_base(self):
        indice_interrogacao = self.get_indice_interrogacao()  # find() retorna o indice do elemento
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.get_indice_interrogacao()  # find() retorna o indice do elemento
        url_parametros = self.url[(indice_interrogacao + 1):]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\nUrl base: " + self.get_url_base() + "\nParâmetros: " + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url


url = 'https://www.bytebank.com.br/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
extrator_url = ExtratorUrl(url)

valor_dolar = 5.50
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = float(extrator_url.get_valor_parametro('quantidade'))
valor_convertido = quantidade / valor_dolar

print("R$ {:.2f} equivalem a U$ {:.2f}".format(quantidade, valor_convertido))


# extrator_url2 = ExtratorUrl(url)
# print(extrator_url == extrator_url2)

# print("O tamanho da URL: ", len(extrator_url))
# print(extrator_url)
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)

# ______________________________________________________________________________________________
# CHALLENGE, VERSÃO DO PROFESSOR:

# if moeda_origem == "real" and moeda_destino == "dolar":
#     valor_conversao = int(quantidade) / VALOR_DOLAR
#     print("O valor de R$" + quantidade + " reais é igual a $" + str(valor_conversao) + " dólares.")
# elif moeda_origem == "dolar" and moeda_destino == "real":
#     valor_conversao = int(quantidade) * VALOR_DOLAR
#     print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
# else:
#     print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")

# ______________________________________________________________________________________________

