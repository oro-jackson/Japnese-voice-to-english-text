import whisper
from googletrans import Translator

# Load the Whisper model globally
model = whisper.load_model("base")
translator = Translator()

def transcribe_audio(file_path):
    # Transcribe the audio file
    result = model.transcribe(file_path, language="ja")
    transcription = result["text"]

    # Translate the transcription to English
    translation = translator.translate(transcription, src='ja', dest='en').text
    
    return transcription, translation
