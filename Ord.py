import os

diretorio = './dataset/Isoladores'

arquivos = os.listdir(diretorio)
arquivos.sort()

i = 1

for arquivo in arquivos:
    nome, extensao = os.path.splitext(arquivo)
    novo_nome = f"{i}{extensao}"
    os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio, novo_nome))
    i += 1
