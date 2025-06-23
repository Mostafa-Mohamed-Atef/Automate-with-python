from gtts import gTTS
import os
from zipfile import ZipFile

# Voiceover text for each slide
voiceover_texts = [
"Hello World"
]

# Create output folder
output_folder = "voiceovers"
os.makedirs(output_folder, exist_ok=True)

# Generate and save voiceovers each separated line will be a separated mp3 file
audio_files = []
for idx, text in enumerate(voiceover_texts, 1):
    tts = gTTS(text)
    filename = os.path.join(output_folder, f"line_{idx}.mp3")
    tts.save(filename)
    audio_files.append(filename)
    print(f"Generated: line_{idx}.mp3")

# Zip all MP3s
zip_filename = "Voiceovers.zip"
with ZipFile(zip_filename, 'w') as zipf:
    for file in audio_files:
        zipf.write(file, os.path.basename(file))

print(f"\nAll files zipped as {zip_filename}")
