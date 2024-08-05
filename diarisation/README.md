### whisperx.ipynb

Code from https://github.com/m-bain/whisperX?tab=readme-ov-file. 

Transcription using whisper with diarisation added.

Need an .env file where the following are specified:   

CONFIG - "base", "small", "tiny", "medium" or "large-v2", the different whisper versions  
AUDIO_PATH - path of audiofile to transcribe  
HF_TOKEN - Hugging Face-token

### falcon_pyannote.ipynb

Transcribes using whisper

Diarizes using pyannote and picovoice falcon

Syncs diarizations with transcription and saves as jsons

Need an .env file where the following are specified

CONFIG - "base", "small", "tiny", "medium" or "large-v2", the different whisper versions  
AUDIO_PATH - path of audiofile to transcribe/diarize
JSONS_PATH - path of directory where jsons will be saved
HF_TOKEN - Hugging Face-token
PICO_TOKEN - Picovoice-token
