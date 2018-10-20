from google.cloud import vision_v1p3beta1 as vision
from google.cloud.vision_v1p3beta1 import types as typeVision
from google.cloud import language
from google.cloud.language import types as typeLanguage
from google.cloud.language import enums
import io

clienteVision = vision.ImageAnnotatorClient()
clienteLanguage = language.LanguageServiceClient()

with io.open('aprenderDivertido.jpg','rb') as readFile:
    content=readFile.read()

image = typeVision.Image(content=content)

image_context = typeVision.ImageContext(language_hints=['mul-Latn-t-i0-handwrit'])

response = clienteVision.document_text_detection(image=image,image_context=image_context)

textImage= response.full_text_annotation.text

document = typeLanguage.Document(type=enums.Document.Type.PLAIN_TEXT,content=textImage)

response = clienteLanguage.analyze_sentiment(document=document)

print(textImage)
print(response.document_sentiment)