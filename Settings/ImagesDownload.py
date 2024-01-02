from bing_image_downloader import downloader

busca = input("Digite as palavras-chave: ")
limite = input("Digite o limite de imagens: ")

downloader.download(busca, limit=int(limite), output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60)
