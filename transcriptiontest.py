import os
import subprocess
import whisper

def videoToAudio(videoPath, audioPath):
    command = f"ffmpeg -i {videoPath} -q:a 0 -map a {audioPath}"
    subprocess.run(command, shell=True)

def audioToText(audioPath, textOutputPath):
    model = whisper.load_model("base")    # load the whisper model

    # transcribe
    result = model.transcribe(audioPath, fp16=False) #fp16=False not necessarily needed

    # create transcription file
    with open(textOutputPath, "w") as file:
        file.write(result["text"])

videoPath = "data/ITeamRecording.mp4"
audioPath = "data/ExtractedAudio.wav"
textPath = "data/transcription.txt"

videoToAudio(videoPath, audioPath)
audioToText(audioPath, textPath)