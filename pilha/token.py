# Linguagem PILHA
# Tokens
# Pedro B. <pedrobuitragons@gmail.com>

from __future__ import annotations

from enum import Enum, auto

class TkTypes(Enum):
    # Tipos
    INTEGER = auto()

    # Operações
    ADD     = auto()
    SUB     = auto()
    MUL     = auto()
    DIV     = auto()

    # Fim da linha
    EOF     = auto()

class Token:
    def __init__(self: Token, tk: TkTypes, value: any) -> None:
        self.type  = tk
        self.value = value

    def __str__(self: Token) -> str:
        return f'Token({self.type:12}, {self.value:12})'

    def __repr__(self: Token) -> str:
        return self.__str__()

