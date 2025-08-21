# generate_tts.py

from tortoise.api import TextToSpeech
import torchaudio

# Initialize the TTS model
tts = TextToSpeech()


output = tts.tts('Hello, my name is Suno. [clears throat] And, uh — and I like pizza. But I also have other interests such as playing tic tac toe.', voice_samples=None, conditioning_latents=None)

# Save output to a WAV file
torchaudio.save("output.wav", output.cpu(), 24000)

print("✅ Audio generated: output.wav")
