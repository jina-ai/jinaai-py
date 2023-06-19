import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(root_dir)
from jinaai import JinaAI

jinaai = JinaAI()

imageFile = '../examples/images/factory-1.png'
imageUrl = 'https://picsum.photos/200'
imageB64 = jinaai.utils.image_to_base64(imageFile)

def test_is_url():
    assert jinaai.utils.is_url(imageFile) == False
    assert jinaai.utils.is_url(imageUrl) == True
    assert jinaai.utils.is_url(imageB64) == False

def test_is_base64():
    assert jinaai.utils.is_base64(imageFile) == False
    assert jinaai.utils.is_base64(imageUrl) == False
    assert jinaai.utils.is_base64(imageB64) == True

def test_image_to_base64():
    assert jinaai.utils.is_base64(imageB64) == True
