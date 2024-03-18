# Linguagem PILHA
# Tokenizador
# Pedro B. <pedrobuitragons@gmail.com>

from __future__ import annotations

from .token import Token, TkTypes

class Lexer:
    def __init__(self: Lexer, text: str) -> None:
        self.text: str = text
        self.pos : int = 0

        self.cur_char: str = text[0]
    
    @staticmethod
    def __throw(err_msg: str = 'Caractere inválido') -> None:
        raise Exception(err_msg)
    
    def advance(self: Lexer) -> None:
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.cur_char = None
        else:
            self.cur_char = self.text[self.pos]
    
    def skip_spaces(self: Interpreter) -> None:
        while self.cur_char and self.cur_char.isspace():
            self.advance()
            
    def consume_int(self: Interpreter) -> int:
        result: int = 0

        while self.cur_char and self.cur_char.isdigit():
            result *= 10
            result += int(self.cur_char)
            self.advance()

        return result

    def get_next_token(self: Interpreter) -> Token:
        while self.cur_char:
            if self.cur_char.isspace():
                self.skip_spaces()
                continue
            
            if self.cur_char.isdigit():
                return Token(TkTypes.INTEGER, self.consume_int())

            if self.cur_char == '+':
                self.advance()
                return Token(TkTypes.ADD, None)

            if self.cur_char == '-':
                self.advance()
                return Token(TkTypes.SUB, None)
            
            if self.cur_char == '*':
                self.advance()
                return Token(TkTypes.MUL, None)
            
            if self.cur_char == '/':
                self.advance()
                return Token(TkTypes.DIV, None)
            
            self.__throw('Erro sintático')

        return Token(TkTypes.EOF, None)

