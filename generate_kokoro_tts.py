from kokoro import KPipeline
import soundfile as sf

def main():
    pipeline = KPipeline(lang_code='a')
    text = '''
    Kokoro is an open-weight TTS model with 82 million parameters. Despite its lightweight architecture, it delivers comparable quality to larger models while being significantly faster and more cost-efficient.
    '''
    generator = pipeline(text, voice='af_heart')
    for i, (gs, ps, audio) in enumerate(generator):
        print(f"Segment {i}: {gs}")
        print(f"Phonemes: {ps}")
        sf.write(f'{i}.wav', audio, 24000)
    print("Audio segments saved.")

if __name__ == '__main__':
    main()
