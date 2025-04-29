from app.audio_handler import AudioHandler
import time

audio_handler = AudioHandler()

# Start the audio stream
audio_handler.start_audio_stream()

# Read audio levels for 10 seconds
try:
    for _ in range(100):  # 10 seconds at 10 readings per second
        audio_level = audio_handler.get_audio_level()
        print(f"Audio Level: {audio_level}")
        time.sleep(0.1)
finally:
    # Stop the audio stream
    audio_handler.stop_audio_stream()