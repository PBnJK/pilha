# Linguagem PILHA
# Sessão de prompt
# Pedro B. <pedrobuitragons@gmail.com>

from .lexer import Lexer
from .interpreter import Interpreter

def run_prompt() -> None:
    while True:
        try:
            text: str = input('pilha $ ')
        except EOFError:
            break

        if not text:
            continue
        
        if text == 'exit':
            return
        
        lexer: Lexer = Lexer(text)
        interpreter: Interpreter = Interpreter(lexer)

        print(interpreter.expr())

