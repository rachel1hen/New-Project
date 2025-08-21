# generate_tts.py

from tortoise.api import TextToSpeech
from tortoise.utils.audio import save_wav

# Initialize the TTS model
tts = TextToSpeech()


output = tts.tts('Hello, my name is Suno. [clears throat] And, uh — and I like pizza. But I also have other interests such as playing tic tac toe.', voice_samples=None, conditioning_latents=None)

# Save output to a WAV file
save_wav(output, "output.wav")

print("✅ Audio generated: output.wav")
