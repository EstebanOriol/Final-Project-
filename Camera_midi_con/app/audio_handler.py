import pyaudio
import numpy as np

class AudioHandler:
    def __init__(self):
        self.chunk = 1024  # Number of audio samples per frame
        self.rate = 44100  # Sampling rate
        self.stream = None
        self.pyaudio_instance = None

    def start_audio_stream(self):
        """Start the audio input stream."""
        try:
            self.pyaudio_instance = pyaudio.PyAudio()
            self.stream = self.pyaudio_instance.open(format=pyaudio.paInt16,
                                                     channels=1,
                                                     rate=self.rate,
                                                     input=True,
                                                     frames_per_buffer=self.chunk)
            print("Audio stream started successfully.")
        except Exception as e:
            print(f"Error starting audio stream: {e}")
            self.stream = None

    def get_audio_level(self):
        """Get the current audio input level."""
        if self.stream is None:
            print("Audio stream is not available.")
            return 0  # Return 0 if the stream is not available

        try:
            # Read audio data from the stream
            data = self.stream.read(self.chunk, exception_on_overflow=False)
            data = np.frombuffer(data, dtype=np.int16)

            # Validate audio data
            if len(data) == 0:
                print("Audio data is empty.")
                return 0

            # Calculate RMS (Root Mean Square) of the audio signal
            rms = np.sqrt(np.mean(data**2))

            # Check for invalid RMS values
            if np.isnan(rms) or np.isinf(rms):
                print("Invalid RMS value detected.")
                return 0

            # Normalize RMS to a range of 0 to 1
            normalized_level = min(rms / 32768.0, 1.0)
            return normalized_level
        except Exception as e:
            print(f"Error reading audio stream: {e}")
            return 0  # Return 0 if an error occurs

    def stop_audio_stream(self):
        """Stop the audio input stream."""
        if self.stream is not None:
            try:
                self.stream.stop_stream()
                self.stream.close()
                self.stream = None
                print("Audio stream stopped successfully.")
            except Exception as e:
                print(f"Error stopping audio stream: {e}")

        if self.pyaudio_instance is not None:
            try:
                self.pyaudio_instance.terminate()
                self.pyaudio_instance = None
                print("PyAudio instance terminated successfully.")
            except Exception as e:
                print(f"Error terminating PyAudio instance: {e}")

