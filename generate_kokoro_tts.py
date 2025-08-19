from kokoro import KPipeline
import soundfile as sf
import numpy as np
import os

def generate_audio(text, voice, lang='a'):
    pipeline = KPipeline(lang_code=lang)
    generator = pipeline(text, voice=voice)
    return np.concatenate([audio for _, _, audio in generator])

def main():
    # os.makedirs("audio", exist_ok=True)

    text = "This is a voice test using Kokoro. The next sentence will be spoken by a different voice."

    voices = {
        "female": "af_sarah",
        "male": "am_michael"
    }

    audio_data = {}
    for label, voice in voices.items():
        print(f"🔈 Generating {label} voice with '{voice}'...")
        audio = generate_audio(text, voice)
        audio_data[label] = audio
        sf.write(f"{label}.wav", audio, 24000)

    # Combine both voices sequentially
    combined = np.concatenate([audio_data["female"], audio_data["male"]])
    sf.write("combined.wav", combined, 24000)

    print("✅ Saved female.wav, male.wav, combined.wav")

if __name__ == "__main__":
    main()
