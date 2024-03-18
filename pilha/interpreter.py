# Linguagem PILHA
# Interpretador da linguagem
# Pedro B <pedrobuitragons@gmail.com>

from __future__ import annotations

from .lexer import Lexer
from .token import Token, TkTypes

class Interpreter:
    def __init__(self: Interpreter, lexer: Lexer) -> None:
        self.lexer: Lexer = lexer
        self.cur_token: Token = None

        self.stack: list[int] = []
    
    @staticmethod
    def __throw(err_msg: str = 'Erro interpretando prompt') -> None:
        raise Exception(err_msg)

    def eat(self: Interpreter, expected_type: TkTypes) -> None:
        if self.cur_token.type == expected_type:
            self.cur_token = self.lexer.get_next_token()
        else:
            self.__throw(f'Esperava {expected_type}, encontrou {self.cur_token.tk}')
    
    def term(self: Interpreter) -> int:
        token: Token = self.cur_token
        self.eat(TkTypes.INTEGER)

        return token.value

    def expr(self: Interpreter) -> int:
        self.cur_token = self.lexer.get_next_token()
        result: int = 0

        while self.cur_token.type != TkTypes.EOF:
            token: Token = self.cur_token
            
            if token.type == TkTypes.INTEGER:
                self.stack.append(self.term())

            elif token.type == TkTypes.ADD:
                self.eat(TkTypes.ADD)

                b: int = self.stack.pop()
                a: int = self.stack.pop()
                self.stack.append(a + b)

            elif token.type == TkTypes.SUB:
                self.eat(TkTypes.SUB)

                b: int = self.stack.pop()
                a: int = self.stack.pop()
                self.stack.append(a - b)

            elif token.type == TkTypes.MUL:
                self.eat(TkTypes.MUL)

                b: int = self.stack.pop()
                a: int = self.stack.pop()
                self.stack.append(a * b)

            elif token.type == TkTypes.DIV:
                self.eat(TkTypes.DIV)

                b: int = self.stack.pop()
                a: int = self.stack.pop()
                self.stack.append(a / b)

        return self.stack.pop()

