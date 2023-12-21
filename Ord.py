import os

# Diretório onde estão as imagens
diretorio = 'dataset_2'

# Função para reordenar as imagens
def reordenar_imagens(diretorio):
    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio)
    
    # Filtra apenas os arquivos de imagem (você pode mudar a extensão conforme necessário)
    imagens = [imagem for imagem in arquivos if imagem.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # Ordena as imagens por nome
    imagens.sort()
    
    # Renomeia as imagens de acordo com a sequência desejada
    for indice, imagem in enumerate(imagens, start=1):
        nome_original, extensao = os.path.splitext(imagem)
        novo_nome = f'{indice:04d}{extensao}'  # Adiciona zeros à esquerda para manter o formato desejado (por exemplo, 0001, 0002)
        caminho_antigo = os.path.join(diretorio, imagem)
        caminho_novo = os.path.join(diretorio, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        print(f'Imagem {imagem} renomeada para {novo_nome}')

# Chama a função para reordenar as imagens no diretório especificado
reordenar_imagens(diretorio)
