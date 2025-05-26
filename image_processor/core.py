# image_processor/core.py
from PIL import Image

def combine_images(image_path1, image_path2, output_path):
    img1 = Image.open(image_path1).convert("RGBA")
    img2 = Image.open(image_path2).convert("RGBA")
    
    # Redimensionar a segunda imagem para o tamanho da primeira
    img2 = img2.resize(img1.size)
    
    # Combinar as duas imagens
    combined = Image.blend(img1, img2, alpha=0.5)  # 50% de cada
    
    combined.save(output_path)
    return output_path
