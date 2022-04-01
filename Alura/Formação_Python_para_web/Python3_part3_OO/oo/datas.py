# class Data:
#
#     def __init__(self, dia, mes, ano):
#         self.dia = dia
#         self.mes = mes
#         self.ano = ano
#
#     def formatada(self):
#         print("{}/{}/{}".format(self.dia, self.mes, self.ano))

class Retangulo:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__area = x * y

    def obter_area(self):
        return self.__area
