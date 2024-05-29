from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from models.whisper_model import transcribe_audio

main = Blueprint('main', __name__)

UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@main.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    
    audio_file = request.files['audio']
    filename = secure_filename(audio_file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    audio_file.save(file_path)

    transcription, translation = transcribe_audio(file_path)
    
    os.remove(file_path)  # Clean up the file after processing

    return jsonify({'transcription': transcription, 'translation': translation})
