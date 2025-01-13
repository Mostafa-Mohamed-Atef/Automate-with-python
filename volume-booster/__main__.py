import pyaudio
import numpy as np

# Parameters
SAMPLE_RATE = 44100  # 44.1 kHz sample rate
FRAMES_PER_BUFFER = 1024
BOOST_FACTOR = 1.0  # 200% volume


def process_audio(input_data, boost_factor):
    # Convert input byte data to numpy array
    audio_data = np.frombuffer(input_data, dtype=np.float32)
    # Apply volume boost
    boosted_audio = audio_data * boost_factor
    # Clip to prevent overflow
    boosted_audio = np.clip(boosted_audio, -1.0, 1.0)
    # Convert back to byte data
    return boosted_audio.tobytes()


def main():
    p = pyaudio.PyAudio()

    # Open input and output streams
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=SAMPLE_RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=FRAMES_PER_BUFFER)

    print("Volume boost active (200%). Press Ctrl+C to stop.")

    try:
        while True:
            # Read audio data from input stream
            input_data = stream.read(FRAMES_PER_BUFFER, exception_on_overflow=False)
            # Process the audio
            output_data = process_audio(input_data, BOOST_FACTOR)
            # Write boosted audio data to output stream
            stream.write(output_data)
    except KeyboardInterrupt:
        print("Stopping...")
    finally:
        # Cleanup
        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == "__main__":
    main()
