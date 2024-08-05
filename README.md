### video_transcription.py

Takes a recorded video meeting from e.g. Teams and returns a transcription by whisper.

### manage_transcription.ipynb

Manages transcriptions for different use cases (summarize, improve grammar, obtain action points or template-based notes) using OpenAI's GPT.

Requires API-key.

### whisperOF.py

Transcribes one file at a time using whisper.  

model.transcribe() has many more parameters possible to tune, worth exploring.  

Need an .env file where the following are specified:   

CONFIG - "base", "small", "tiny", "medium" or "large-v2", the different whisper versions  
AUDIO_PATH - path of audiofile to transcribe  
TEXT_PATH - path of transcribed .txt-file  
INITIAL_PROMPT - possible to prompt whisper by e.g. providing setting or unusual words/names used in the audio content  

### whisperMF.py

Transcribes all files in a folder at once using whisper.  

Requires the following in an .env file:

CONFIG - "base", "small", "tiny", "medium" or "large-v2", the different whisper versions  
AUDIO_PATH - path of folder with audiofiles to transcribe  
OUTPUT_PATH - path of folder for output .txt-files 
