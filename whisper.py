
import os
from openai import OpenAI
import whisper
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

client = OpenAI() # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
MODEL = os.getenv('MODEL')

def audioToText(audioPath, outputPath, initialPrompt):
    model = whisper.load_model(os.getenv('CONFIG')) # choose tiny, base, small, medium, large

    # transcribe audio
    result = model.transcribe(audioPath, fp16=False,
                              language="sv",
                              task="transcribe",
                              temperature=0.4,
                              best_of=2, # number of candidates to consider
                              initial_prompt=initialPrompt
                             )

    # write transcribed text to file
    with open(outputPath, "w") as file:
        file.write(result["text"])

def main():
    
    audioFilepath = os.getenv('AUDIO_PATH')
    textFilepath = os.getenv('TEXT_PATH')
    initialPrompt = os.getenv('INITIAL_PROMPT')

    audioToText(audioFilepath, textFilepath, initialPrompt)

if __name__ == '__main__':
    main()