import numpy as np # linear algebra
import matplotlib.pyplot as plt
import pywt


class akd_wav:

    def __init__(self,sampling_freq,min_freq,max_freq,frequency_samples=50,wavelet_type='cmor1.5-1.0'):
        self.sampling_freq = sampling_freq
        self.nquist_f = 4*max_freq
        self.freqs = np.linspace(min_freq,max_freq,frequency_samples)/self.nquist_f
        scales = pywt.frequency2scale('cmor1.5-1.0', self.freqs)
        self.scales = np.flip(scales)
        self.wavtype=wavelet_type
        
    
    def show_wavtransform(self,time_series,figure_no):
        coefficients, frequencies = pywt.cwt(time_series, scales=self.scales, wavelet=self.wavtype)
        time_period = len(time_series)/self.sampling_freq
        plt.figure(num=figure_no,figsize=(10, 6))
        plt.imshow(np.abs(coefficients), aspect='auto', cmap='jet',extent=[0,time_period,1,max(self.freqs*self.nquist_f)])
        plt.colorbar(label="Magnitude")
        plt.ylabel("Frequency")
        plt.xlabel("Time")
        plt.title("CWT of a Chirp Signal")
        plt.show()