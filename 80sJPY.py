from pydub import AudioSegment
from pydub.effects import speedup, reverb
from pydub.utils import make_chunks

# Load the audio file
audio = AudioSegment.from_file("pop1.mp3")

# Detect the beats in the audio file
beats = audio.detect_beats()

# Split the audio file into chunks at the beat points
chunks = make_chunks(audio, [beat[0] for beat in beats])

# Apply effects to each chunk
for i, chunk in enumerate(chunks):
    # Slow down the chunk by 30%
    chunk = speedup(chunk, playback_speed=0.7)

    # Add some reverb to the chunk
    chunk = reverb(chunk, reverberance=50, damping=10)

    # Export the modified chunk as an MP3
    chunk.export(f"path/to/vaporwave_audio_file_{i}.mp3", format="mp3")
