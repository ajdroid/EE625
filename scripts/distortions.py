import numpy as np
import pywt

def PRD(x, y):
	prd = (np.linalg.norm(x-y)/np.linalg.norm(x)*100)
	return prd 

def WEDD(x,y):
	'''
	Function to calculate Wavelet energy based diagnostic distortion measure 
	for ECG signals as in:
	Wavelet energy based diagnostic distortion measure for ECG
		MS Manikandan, S Dandapat
		Biomedical Signal Processing and Control 2 (2), 80-96

	Wavelet used: Daubechies 9/7 'bior4.4' (because Nr = Nd = 4)
	'''
	dec5 = pywt.wavedec(x,'bior4.4', level = 5)

	return wedd


def MSEPRD(x,y):
	return mseprd

def CCD(x, y):
	D = np.array([[0.75, 0], [0, 0.25]])
	rInterval = 
	rWave = 
	a = np.array([rAmp, rInt])
	b = np.array([rAmp1, rInt1])
	CCD = np.dot( np.dot((a-b).T,D), (a-b))
	return CCD

def cepstralDistance()