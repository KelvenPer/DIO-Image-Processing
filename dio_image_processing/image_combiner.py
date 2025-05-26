from PIL import Image
import os
from typing import List

# Definir o modo de reamostragem compatível com Pillow 10+ e versões antigas
try:
    resample_mode = Image.Resampling.LANCZOS
except AttributeError:
    resample_mode = Image.ANTIALIAS  # para versões antigas do Pillow

def combine_images(
    image_paths_1: List[str],
    image_paths_2: List[str],
    output_path: str = "outputs/combined_image.png",
    background_color=(255, 255, 255)
) -> str:
    """
    Combina objetos de duas listas de imagens em uma única imagem, lado a lado, mantendo a proporção.

    Args:
        image_paths_1 (List[str]): Lista de caminhos das imagens da primeira fonte.
        image_paths_2 (List[str]): Lista de caminhos das imagens da segunda fonte.
        output_path (str): Caminho para salvar a imagem combinada.
        background_color (tuple): Cor de fundo (R, G, B).

    Returns:
        str: Caminho da imagem combinada gerada.
    """
    images_1 = [Image.open(img).convert("RGBA") for img in image_paths_1]
    images_2 = [Image.open(img).convert("RGBA") for img in image_paths_2]

    all_images = images_1 + images_2

    if not all_images:
        raise ValueError("Nenhuma imagem para combinar.")

    # Definir altura padrão para todas as imagens (usar a maior altura)
    max_height = max(img.height for img in all_images)

    # Redimensionar proporcionalmente cada imagem para a altura máxima
    resized_images = []
    total_width = 0
    for img in all_images:
        ratio = max_height / img.height
        new_width = int(img.width * ratio)
        img_resized = img.resize((new_width, max_height), resample_mode)
        resized_images.append(img_resized)
        total_width += new_width

    # Criar background com largura total e altura máxima
    combined_image = Image.new("RGBA", (total_width, max_height), background_color + (255,))

    # Posicionar as imagens lado a lado
    x_offset = 0
    for img in resized_images:
        combined_image.paste(img, (x_offset, 0), img)
        x_offset += img.width

    # Garantir a pasta de saída
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Salvar como RGB (sem canal alfa)
    combined_image.convert("RGB").save(output_path)
    print(f"✅ Imagem combinada salva em: {output_path}")

    return output_path
