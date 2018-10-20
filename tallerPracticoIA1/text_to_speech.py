from google.cloud import texttospeech

client = texttospeech.TextToSpeechClient()

text="good morning"

synthesis_input = texttospeech.types.SynthesisInput(text=text)

voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)

audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

response = client.synthesize_speech(synthesis_input, voice, audio_config)

with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')