from ultralytics import YOLO
import cv2
import os
from typing import List
import uuid  # Para gerar nomes únicos


def detect_and_crop_objects(
    image_path: str,
    output_folder: str = "imagens/objects",
    model_name: str = "yolov8n.pt",
    conf_threshold: float = 0.25
) -> List[str]:
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Imagem '{image_path}' não encontrada.")

    os.makedirs(output_folder, exist_ok=True)

    model = YOLO(model_name)
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Não foi possível carregar a imagem '{image_path}'.")

    results = model(image, conf=conf_threshold)

    object_paths = []
    height, width = image.shape[:2]
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy().astype(int)

        for (x1, y1, x2, y2) in boxes:
            # Limita caixas dentro da imagem
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(width, x2), min(height, y2)

            cropped = image[y1:y2, x1:x2]
            if cropped.size == 0:
                continue

            unique_id = uuid.uuid4().hex[:8]  # ID curto para nome único
            output_path = os.path.join(output_folder, f"{base_name}_obj_{unique_id}.png")
            cv2.imwrite(output_path, cropped)
            object_paths.append(output_path)
            print(f"✅ Objeto salvo em: {output_path}")

    if not object_paths:
        print("⚠️ Nenhum objeto detectado na imagem.")

    return object_paths
