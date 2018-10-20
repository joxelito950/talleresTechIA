import io
from google.cloud import vision_v1p3beta1 as vision
from google.cloud.vision_v1p3beta1 import types

client = vision.ImageAnnotatorClient()
with io.open('conFondo.jpg','rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

image_context= types.ImageContext(language_hints=['mul-Latn-t-i0-handwrit'])

response = client.document_text_detection(image=image, image_context=image_context)

print('Full text: {}'.format(response.full_text_annotation.text))