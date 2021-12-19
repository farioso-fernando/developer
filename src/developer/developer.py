"""
Depuração. Log personalizado para aplicativos Python3.

Você tem uma opção de registro para seu aplicativo. Que é usar log. Geralmente, isso é feito usando a instrução print():
A opção para o log do aplicativo é usar a developer.log() função. Isso permite que você inclua um pouco mais de\ngranularidade e informações na saída de registro. Aqui está um exemplo:

import developer
developer.log(message= "Olá, Mundo!")

SAÍDA: \033[33;2m[Log]:\033[0m\033[33m Olá, Mundo!\033[0m

Nota: Você verá os logs com a cor amarela no console do seu sistema. Na próxima atualização irá ter como escolher as cores.
"""

log = lambda message: print("\033[33;2m[Log]:\033[0m" + " " + "\033[33m{}\033[0m".format(message))
log.__doc__ = """Retorna a impressao do resultado a cor amarela.

    Parametros:
        log (message):A mensagem que será deve ser convertida em log.

    O Parametro "message" pode receber qualquer tipo seja int ou string, boleano ou float.
"""
if __name__ == "__main__":
    log(message="Hello World!")