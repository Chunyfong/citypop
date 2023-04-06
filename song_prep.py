import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np

#load your song
kpop = r'C:\Users\\Desktop\dataset\songs\aespa.wav' 

signal, sr = librosa.load(kpop)
librosa.display.waveshow(signal, sr=sr)

# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.show()


fft = np.fft.fft(signal)
magnitude = np.abs(fft)
frequency = np.linspace(0, sr, len(magnitude))

left_freq = frequency[:int(len(frequency)/2)]
left_mag = magnitude[:int(len(frequency)/2)]

plt.plot(left_freq, left_mag)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.show()
