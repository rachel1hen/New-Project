speaker =[
     "v2/en_speaker_9",
     "v2/en_speaker_1",
     "v2/en_speaker_3",
     "v2/en_speaker_5",
     "v2/en_speaker_6",
     "v2/en_speaker_7",
     "v2/en_speaker_11",
     "v2/en_speaker_13"
]

from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
#import numpy as np
#SAMPLE_RATE = 48000 #44100  # or 48000
# download and load all models
preload_models()

history_prompt = "v2/en_speaker_9"

# generate audio from text
text_prompt = """
     Hello, my name is Suno. [clears throat] And, uh — and I like pizza.
     But I also have other interests such as playing tic tac toe.
"""
for speak in speaker:
     try:
          
         audio_array = generate_audio(text_prompt, history_prompt=speak)
         filename = f"{speak.replace('/','_')}.wav"
         write_wav(filename, SAMPLE_RATE,audio_array)
     except Exception as e:
          print("ohno")
#audio_int16 = np.int16(audio_array / np.max(np.abs(audio_array)) * 32767)

# save audio to disk
#write_wav("bark_generation.wav", SAMPLE_RATE, audio_int16)
# save audio to disk
#write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

print("✅ Audio generated and saved to bark_generation.wav")

