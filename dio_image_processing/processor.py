from PIL import Image
import numpy as np


def combine_images(image_path1, image_path2, output_path="result.png"):
    """
    Combina duas imagens lado a lado e salva o resultado.

    Args:
        image_path1 (str): Caminho da primeira imagem.
        image_path2 (str): Caminho da segunda imagem.
        output_path (str): Caminho para salvar a imagem resultante.

    Returns:
        str: Caminho da imagem resultante.
    """
    img1 = Image.open(image_path1)
    img2 = Image.open(image_path2)

    # Ajustar tamanho se forem diferentes
    img1 = img1.resize((500, 500))
    img2 = img2.resize((500, 500))

    # Criar uma nova imagem com largura = soma das duas
    combined = Image.new('RGB', (img1.width + img2.width, img1.height))
    combined.paste(img1, (0, 0))
    combined.paste(img2, (img1.width, 0))

    combined.save(output_path)
    print(f"Imagem combinada salva em {output_path}")
    return output_path
