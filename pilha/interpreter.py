# Linguagem PILHA
# Interpretador da linguagem
# Pedro B <pedrobuitragons@gmail.com>

from __future__ import annotations

from .token import Token, TkTypes

class Interpreter:
    def __init__(self: Interpreter, text: str) -> None:
        self.text: str = text
        self.pos : int = 0

        self.cur_token: Token = None
        self.cur_char : str = text[0]

        self.stack: list[int] = []
    
    @staticmethod
    def __throw(err_msg: str = 'Erro interpretando prompt') -> None:
        raise Exception(err_msg)
    
    def advance(self: Interpreter) -> None:
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

    def eat(self: Interpreter, expected_type: TkTypes) -> None:
        if self.cur_token.type == expected_type:
            self.cur_token = self.get_next_token()
        else:
            self.__throw(f'Esperava {expected_type}, encontrou {self.cur_token.tk}')
    
    def term(self: Interpreter) -> int:
        token: Token = self.cur_token
        self.eat(TkTypes.INTEGER)

        return token.value

    def expr(self: Interpreter) -> int:
        self.cur_token = self.get_next_token()
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

