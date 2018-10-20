from google.cloud import language
from google.cloud.language import types
from google.cloud.language import enums

client = language.LanguageServiceClient()

textPositive='goog morning'
textNegative='i am angry'

document = types.Document(type=enums.Document.Type.PLAIN_TEXT, content=textNegative)

response = client.analyze_sentiment(document=document)

print(textNegative)
print(response.document_sentiment)