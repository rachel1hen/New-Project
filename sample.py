import torch
import torchaudio
from zonos.model import Zonos
from zonos.conditioning import make_cond_dict

def run_zonos_tts():
    device = torch.device('cpu')
    model = Zonos.from_pretrained('Zyphra/Zonos-v0.1-transformer', device=device)
    model.eval()

    text = "Hello from Zonos running on GitHub Actions CPU environment!"
    cond_dict = make_cond_dict(text=text, speaker=None, language='en-us')
    conditioning = model.prepare_conditioning(cond_dict)

    codes = model.generate(conditioning)

    wavs = model.autoencoder.decode(codes).cpu()
    torchaudio.save('sample.wav', wavs[0], model.autoencoder.sampling_rate)
    print('Audio saved as sample.wav')

if __name__ == "__main__":
    run_zonos_tts()
  
