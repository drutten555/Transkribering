whisperOF.py transcribes one file at a time using whisper.  

model.transcribe() has many more parameters possible to tune, worth exploring.  

Need an .env file where the following are specified:   

CONFIG - "base", "small", "tiny", "medium" or "large", the different whisper versions  
AUDIO_PATH - path of audiofile to transcribe  
TEXT_PATH - path of transcribed .txt-file  
INITIAL_PROMPT - possible to prompt whisper by e.g. providing setting or unusual words/names used in the audio content  
