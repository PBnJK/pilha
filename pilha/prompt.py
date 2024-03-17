# Linguagem PILHA
# Sessão de prompt
# Pedro B. <pedrobuitragons@gmail.com>

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
        
        interpreter: Interpreter = Interpreter(text)
        print(interpreter.expr())

