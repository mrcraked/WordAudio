# WordAudio

WordAudio is a collection of MP3 audio files for every English word, allowing easy access and use. Users can manually generate audio files using a Python script and access them in structured folders.

## 📁 Project Structure

- `/audio/` - Contains individual MP3 files for each English word.
- `/release/` - Contains a ZIP archive of all audio files for easy download.
- `/script/` - Contains Python scripts to generate the MP3 files.

## 🚀 How to Generate Audio Files

To manually generate MP3 audio files, follow these steps:

1. Navigate to the `/script/` directory.
2. Add words to `words.txt` (one word per line).
3. Run the following commands:

   ```sh
   python arrayword.py
   python audio.py
   ```
4. The generated MP3 files will be saved in the /audio/ folder.

## 🔊 Accessing Audio Files

- Browse /audio/ for individual word MP3 files.
- Download /release/WordAudio.zip for a full collection.

# 📜 License
This project is licensed under the MIT License – feel free to use, modify, and distribute. aslong you credit @mrcracked me
