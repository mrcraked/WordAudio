import os
import json
from gtts import gTTS
from gtts.tts import gTTSError

# Function to convert words to speech and save as MP3
def words_to_speech():
    # Read words from ArrayWords.txt
    with open('ArrayWords.txt', 'r') as file:
        words = json.load(file)  # Parse JSON array

    # Create a directory for audio files if it doesn't exist
    if not os.path.exists('audio'):
        os.makedirs('audio')

    # Convert each word to speech and save as MP3
    for word in words:
        mp3_file = f'audio/{word}.mp3'
        if os.path.exists(mp3_file):
            print(f"File '{mp3_file}' already exists. Skipping...")
            continue
        
        try:
            tts = gTTS(text=word, lang='en')
            tts.save(mp3_file)
        except gTTSError as e:
            print(f"Error converting '{word}': {e}")

# Call the function
if __name__ == "__main__":
    words_to_speech()
