from dio_image_processing.processor import combine_images


def test_combine_images():
    result = combine_images("image1.png", "image2.png", "result.png")
    assert result == "result.png"
