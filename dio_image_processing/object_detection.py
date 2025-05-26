from ultralytics import YOLO
import cv2
import os


def detect_and_crop_objects(image_path, output_folder="images/objects", model_name="yolov8n.pt"):
    """
    Detecta objetos em uma imagem e salva cada objeto como uma nova imagem recortada.

    :param image_path: Caminho da imagem de entrada.
    :param output_folder: Pasta onde as imagens dos objetos serão salvas.
    :param model_name: Modelo YOLO usado (padrão yolov8n.pt).
    :return: Lista com os caminhos dos objetos recortados.
    """
    os.makedirs(output_folder, exist_ok=True)

    model = YOLO(model_name)

    # Carregar imagem
    img = cv2.imread(image_path)

    if img is None:
        raise FileNotFoundError(f"Imagem {image_path} não encontrada.")

    results = model(img)

    object_paths = []

    for i, result in enumerate(results):
        boxes = result.boxes.xyxy.cpu().numpy().astype(int)  # Coordenadas das caixas

        for j, box in enumerate(boxes):
            x1, y1, x2, y2 = box
            cropped = img[y1:y2, x1:x2]
            obj_path = os.path.join(output_folder, f"{os.path.basename(image_path).split('.')[0]}_obj{j}.png")
            cv2.imwrite(obj_path, cropped)
            object_paths.append(obj_path)
            print(f"Objeto salvo em {obj_path}")

    return object_paths
