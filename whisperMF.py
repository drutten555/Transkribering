import os
from openai import OpenAI
import whisper
from dotenv import load_dotenv
from tqdm import tqdm

# Load environment variables from the .env file
load_dotenv()

client = OpenAI() # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
MODEL = os.getenv('MODEL')

def audioToText(audioPath, outputPath, initialPrompt):
    model = whisper.load_model(os.getenv('CONFIG')) # choose tiny, base, small, medium, large

    # transcribe audio
    result = model.transcribe(audioPath, fp16=False,
                              #language="sv", # unspecified will be detected automatically
                              task="transcribe",
                              temperature=0.4,
                              best_of=2, # number of candidates to consider
                              initial_prompt=initialPrompt
                             )

    # write transcribed text to file 
    original_filename = outputPath
    new_filename = original_filename.replace(".wav", ".txt")
    data_dir = os.getenv('OUTPUT_PATH')
    os.makedirs(data_dir, exist_ok=True)
    new_filepath = os.path.join(data_dir, new_filename)
    with open(new_filepath, "w") as file: # should generate the files in currect dir
        file.write(result["text"])

def main():
    audioFilepathDir = os.getenv('AUDIO_PATH')
    # textFilepath = os.getenv('TEXT_PATH') # do dynamically instead
    initialPrompt = os.getenv('INITIAL_PROMPT')
    filenames = os.listdir(audioFilepathDir)

    for filename in tqdm(filenames, desc="processing audio files"):
        newFileName = filename + ".txt"
        file_path = os.path.join(audioFilepathDir, filename)
        audioToText(file_path, filename, initialPrompt)

if __name__ == '__main__':
    main()



