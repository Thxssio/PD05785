import os
from PIL import Image

# Diretório onde estão as imagens
diretorio = './dataset/Isoladores2'

# Função para rotacionar as imagens
def rotacionar_imagens(diretorio, angulo):
    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio)
    
    # Filtra apenas os arquivos de imagem
    imagens = [imagem for imagem in arquivos if imagem.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # Rotaciona e salva as imagens no mesmo diretório
    for imagem in imagens:
        caminho_imagem = os.path.join(diretorio, imagem)
        img = Image.open(caminho_imagem)
        img_rotacionada = img.rotate(angulo, expand=True)
        img_rotacionada.save(caminho_imagem)
        print(f'Imagem {imagem} rotacionada em {angulo} graus')

# Chama a função para rotacionar as imagens no diretório especificado em 90 graus (por exemplo)
rotacionar_imagens(diretorio, 90)
