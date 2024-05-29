# Whisper Transcription API

This project provides a Flask API to transcribe Japanese audio files to text using OpenAI's Whisper and then translates the transcription into English.

## Project Structure

```
whisper_transcription_api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── routes.py
├── models/
│   └── whisper_model.py
├── requirements.txt
├── run.py
└── README.md
```

## Requirements

- Python 3.7+
- Flask
- torch
- whisper
- googletrans

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/whisper_transcription_api.git
cd whisper_transcription_api
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the Flask application:

```bash
python run.py
```

## Usage

Send a POST request to `/transcribe` with an audio file:

```bash
curl -X POST http://localhost:5000/transcribe -F "audio=@path_to_your_audio_file.wav"
```

The response will contain the transcription and translation:

```json
{
    "transcription": "Japanese text",
    "translation": "Translated English text"
}
```

## Notes

- The `uploads` folder is used to temporarily store audio files during processing.
- The Whisper model and Google Translate are used for transcription and translation, respectively.
