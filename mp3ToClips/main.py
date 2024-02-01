from pydub import AudioSegment

# Specify the paths to ffmpeg and ffprobe executables
AudioSegment.ffmpeg = "/opt/homebrew/bin/ffmpeg"
AudioSegment.ffprobe = "/opt/homebrew/bin/ffprobe"

# Rest of your code...

from pydub.playback import play

# Step 1: Load and Convert MP3
audio = AudioSegment.from_mp3("tedtalk.mp3")

# Step 2: Dummy Sentence Segmentation (Replace with actual segmentation logic)
transcribed_text = "This is sentence 1. This is sentence 2. This is sentence 3."
sentence_timestamps = [(0, 5000), (5000, 10000), (10000, len(audio))]

# Step 3: Create and Export Clips
for i, (start_time, end_time) in enumerate(sentence_timestamps):
    sentence_clip = audio[start_time:end_time]
    sentence_clip.export(f"sentence_{i+1}.mp3", format="mp3")

# Optional: Play the first sentence (requires playback support)
play(sentence_clip)
