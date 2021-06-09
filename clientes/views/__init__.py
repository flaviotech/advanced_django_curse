'''
Favor colocar as importações em ordem alfabética para uma melhor organização
'''

from .person_form import person_form
from .person_list import person_list
from .person_update import person_update

__all__ = [
    person_form,
    person_list,
    person_update,
]