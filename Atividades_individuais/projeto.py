from pathlib import Path
import shutil

def MandaDestino(diretorio, lista_de_diretorios):
    diretorio = Path(diretorio)  # Transformando em Path diretamente

    # Criando as pastas de destino corretamente
    pastas_destino = {ext: diretorio / pasta for ext, pasta in zip(
        ["Fotos", "Documentos", "Instaladores"],
        lista_de_diretorios
    )}

    for pasta in pastas_destino.values():
        pasta.mkdir(parents=True, exist_ok=True)  # Criar pastas caso não existam

    # Iterando sobre os arquivos do diretório
    for arquivo in diretorio.iterdir():
        if not arquivo.is_file():  # Ignorar diretórios
            continue

        if arquivo.suffix in [".png", ".jpeg"]:
            destino = pastas_destino["Fotos"] / arquivo.name
        elif arquivo.suffix in [".pdf", ".zip", ".gz"]:
            destino = pastas_destino["Documentos"] / arquivo.name
        elif arquivo.suffix in [".exe", ".msi", ".pksz"]:
            destino = pastas_destino["Instaladores"] / arquivo.name
        else:
            continue  # Arquivo não categorizado

        shutil.move(str(arquivo), str(destino))  # Movendo arquivo

diretorio = "C:\\Users\\Eduardo\\Downloads"
lista_de_diretorios = ["Fotos_jpeg_png", "Documentos_pdf_zip_gz", "Instaladores_exe_msi_pksz"]

MandaDestino(diretorio, lista_de_diretorios)
