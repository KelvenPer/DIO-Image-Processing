from dio_image_processing.processor import combine_images


def test_combine_images():
    result = combine_images(["imagem1.png"], ["imagem2.jpg"], "result.png")
    assert result == "result.png"
