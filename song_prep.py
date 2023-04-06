import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

#load your song
kpop = r'C:\Users\\Desktop\dataset\songs\aespa.wav' 

signal, sr = librosa.load(kpop)
librosa.display.waveshow(signal, sr=sr)


plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
