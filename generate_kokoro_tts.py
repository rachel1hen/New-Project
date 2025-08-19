import torch
import soundfile as sf
from kokoro import generate
from models import build_model

def main():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device: {device}')

    # Load model
    MODEL = build_model('kokoro-v0_19.pth', device)
    VOICE_NAME = 'af'  # default mixed voice (Bella + Sarah)
    print(f'Loading voice pack: {VOICE_NAME}')
    VOICEPACK = torch.load(f'voices/{VOICE_NAME}.pt', weights_only=True).to(device)

    # Input text
    text = "Hello, this is Kokoro speaking."
    print(f'Generating TTS for: "{text}"')

    audio, phonemes = generate(MODEL, text, VOICEPACK, lang=VOICE_NAME[0])
    sf.write('output.wav', audio, 24000)
    print(f'Audio saved to output.wav')

    print('Phonemes:', phonemes)

if __name__ == '__main__':
    main()
