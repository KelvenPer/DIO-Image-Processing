from dio_image_processing.object_detection import detect_and_crop_objects
from dio_image_processing.image_combiner import combine_images


# 1. Detectar objetos
objects_1 = detect_and_crop_objects("imagens/pessoa1.jpeg", output_folder="outputs/obj1")
objects_2 = detect_and_crop_objects("imagens/pessoa2.jpeg", output_folder="outputs/obj2")

# Verificar se há objetos detectados para combinar
if not objects_1 and not objects_2:
    print("⚠️ Nenhum objeto detectado nas duas imagens. Abortando combinação.")
else:
    combine_images(objects_1, objects_2, output_path="outputs/final_combined.png")
