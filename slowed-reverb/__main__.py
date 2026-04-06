import soundfile as sf
from pedalboard import Pedalboard, Reverb
from math import trunc
from pydub import AudioSegment
import numpy as np
from scipy.io import wavfile

def slowedreverb(audio, output):
    # -------- SETTINGS --------
    input_file = audio
    output_file = output

    slow_factor = 0.8   # 0.8 = slower (try 0.7–0.9)
    reverb_delay = 0.2  # seconds
    reverb_decay = 0.5  # echo strength
    # --------------------------

    # Load audio
    audio = AudioSegment.from_file(input_file)

    # Convert to WAV for processing
    audio.export("temp.wav", format="wav")

    # Read wav data
    rate, data = wavfile.read("temp.wav")

    # -------- SLOW DOWN --------
    def slow_audio(data, factor):
        indices = np.round(np.arange(0, len(data), factor))
        indices = indices[indices < len(data)].astype(int)
        return data[indices]

    slowed_data = slow_audio(data, slow_factor)

    # -------- ADD REVERB --------
    def add_reverb(data, rate, delay, decay):
        delay_samples = int(delay * rate)
        output = np.copy(data).astype(np.float32)

        for i in range(delay_samples, len(data)):
            output[i] += decay * output[i - delay_samples]

        # Normalize to avoid clipping
        output = output / np.max(np.abs(output))
        return output

    reverb_data = add_reverb(slowed_data, rate, reverb_delay, reverb_decay)

    # Convert back to int16
    reverb_data = np.int16(reverb_data * 32767)

    # Save output
    wavfile.write(output_file, rate, reverb_data)

    print("Done! Saved as:", output_file)

if __name__ == '__main__':
    file = input('Enter path to audio file: ')
    slowedreverb(file, file)