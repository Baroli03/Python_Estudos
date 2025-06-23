from contextlib import contextmanager


class MyContextManager:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print('Abrindo arquivo')
        self._arquivo =  open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('Fechando arquivo')
        self._arquivo.close()


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro', e)

    finally:
        print('Fechando arquivo')
        arquivo.close()






with my_open('aula149.txt', 'w') as arquivo:  # Retorno do __enter__ Vai para alguma_coisa
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n', 123)
    arquivo.write('Linha3\n')
    print('WITH', arquivo)