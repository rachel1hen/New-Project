# import os
# os.environ["SUNO_USE_SMALL_MODELS"] = "True"
# os.environ["SUNO_OFFLOAD_CPU"] = "True"

from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
SAMPLE_RATE = 44100  # or 48000
# download and load all models
preload_models()

# generate audio from text
text_prompt = """
     Hello, ♪ my name is Suno ♪. [clears throat] And, uh — and I like pizza. [laughs] 
     But I also [music] have other interests such as playing tic tac toe.
"""
audio_array = generate_audio(text_prompt)

# save audio to disk
write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

print("✅ Audio generated and saved to bark_generation.wav")

