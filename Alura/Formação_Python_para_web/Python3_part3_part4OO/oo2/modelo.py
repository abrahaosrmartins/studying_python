class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self.nome}\nAno: {self.ano}\nLikes: {self.likes}\n'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome}\nAno: {self.ano}\nDuração: {self.duracao} min\nLikes: {self.likes}\n'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome}\nAno: {self.ano}\nTemporadas: {self.temporadas}\nLikes: {self.likes}\n'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'{vingadores.nome} - {vingadores.ano} - {vingadores.duracao} - {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    print(programa)
