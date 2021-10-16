'''
Shift + Alt + O para organizar as importações (vs code)
'''

from .cliente import Person
from .documento import Documento
from .produto import Produto
from .venda import Venda

__all__ = [
    Person,
    Documento,
    Produto,
    Venda,
]