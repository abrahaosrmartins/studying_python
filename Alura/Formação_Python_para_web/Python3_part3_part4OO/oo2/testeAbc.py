from abc import ABC
from collections.abc import MutableSequence


class MinhaListinhaMutavel(MutableSequence, ABC):


objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)