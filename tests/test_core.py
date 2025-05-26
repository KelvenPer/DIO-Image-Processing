# tests/test_core.py
from image_processor.core import combine_images
import os

def test_combine_images():
    output = "tests/output.png"
    combine_images("tests/img1.png", "tests/img2.png", output)
    assert os.path.exists(output)
