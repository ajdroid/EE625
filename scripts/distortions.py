import numpy as np
import pywt
from peakdetect import peakdetect

def PRD(x, y):
	prd = (np.linalg.norm(x-y)/np.linalg.norm(x)*100)
	return prd 

def WEDD(x,y, wavetype='bior4.4'):
	'''
	Function to calculate Wavelet energy based diagnostic distortion measure 
	for ECG signals as in:
	Wavelet energy based diagnostic distortion measure for ECG
		MS Manikandan, S Dandapat
		Biomedical Signal Processing and Control 2 (2), 80-96

	Wavelet used: CDF 9/7 'bior4.4' (Nr = Nd = 4)
	'''
	dec5 = pywt.wavedec(x,wavetype, level = 5)
	cA5, cD5, cD4, cD3, cD2, cD1 = dec5
	dec5 = pywt.wavedec(y,wavetype, level = 5)
	ycA5, ycD5, ycD4, ycD3, ycD2, ycD1 = dec5
	# Calulate weights as energies in sub bands
	Ea = (cA5*cA5).sum(); Ed5 = (cD5*cD5).sum()
	Ed4 = (cD4*cD4).sum();Ed3 = (cD3*cD3).sum();
	Ed2 = (cD2*cD2).sum();Ed1 = (cD1*cD1).sum();
	Esum = Ea+Ed1+Ed2+Ed3+Ed4+Ed5
		
	Wa = Ea/Esum; Wd5 = Ed5/Esum;
	Wd4 = Ed4/Esum; Wd3 = Ed3/Esum;
	Wd2 = Ed2/Esum; Wd1 = Ed1/Esum;
	
	
	# Get WEDD
	wedd = Wa*PRD(cA5,ycA5) + Wd5*PRD(cD5,ycD5) + Wd4*PRD(cD4,ycD4) +\
			Wd3*PRD(cD3,ycD3) + Wd2*PRD(cD2,ycD2) + Wd1*PRD(cD1,ycD1)
	
	return wedd


def MSEPRD(x,y, wavetype='bior4.4'):
	dec5 = pywt.wavedec(x,'bior4.4', level = 5)
	cA5, cD5, cD4, cD3, cD2, cD1 = dec5
	dec5 = pywt.wavedec(y,wavetype, level = 5)
	ycA5, ycD5, ycD4, ycD3, ycD2, ycD1 = dec5

	
	# Calulate energy at each scale
	Ea = (cA5*cA5).sum(); Ed5 = (cD5*cD5).sum()
	Ed4 = (cD4*cD4).sum();Ed3 = (cD3*cD3).sum();
	Ed2 = (cD2*cD2).sum();Ed1 = (cD1*cD1).sum();
	Esum = Ea+Ed1+Ed2+Ed3+Ed4+Ed5
	
	# Calculate probabilities
	Pa = Ea/Esum; Pd5 = Ed5/Esum;
	Pd4 = Ed4/Esum; Pd3 = Ed3/Esum;
	Pd2 = Ed2/Esum; Pd1 = Ed1/Esum;
	
	# Get weight as entropy
	Wa = -Pa*np.log2(Pa); Wd5 = -Pd5*np.log2(Pd5)
	Wd4 = -Pd4*np.log2(Pd4); Wd3 = -Pd3*np.log2(Pd3)
	Wd2 = -Pd2*np.log2(Pd2); Wd1 = -Pd1*np.log2(Pd1)
	
	mseprd = Wa*PRD(cA5,ycA5) + Wd5*PRD(cD5,ycD5) + Wd4*PRD(cD4,ycD4) +\
			Wd3*PRD(cD3,ycD3) + Wd2*PRD(cD2,ycD2) + Wd1*PRD(cD1,ycD1)
	

	return mseprd

def CCD(x, y):
	D = np.array([[0.75, 0], [0, 0.25]])
	# y[y<0.8*y.max()] = 0
	# x[x<0.8*x.max()] = 0
	xpeaks,_ = peakdetect(x, lookahead=10)
	ypeaks,_ = peakdetect(y, lookahead=10)
	a = np.array(featExt(xpeaks))
	b = np.array(featExt(ypeaks))
# 	print a, b
	CCD = np.dot( np.dot((a-b).T,D), (a-b))
	return CCD

def featExt(xpeaks):
	rpeaks = {}
	rAmpPeak = max(max(p[1:]) for p in xpeaks)
	for loc, xpeak in xpeaks:
		if xpeak>0.9*rAmpPeak:  # put max(values of peaks) here
			rpeaks.update({loc: xpeak})
	x = np.sort(rpeaks.keys())
	rInterval = (x[1:] - x[:-1]).mean() # mean of first order differences
	rAmp = np.mean(rpeaks.values())
# 	print rInterval, rAmp
	return rAmp, rInterval


def cepstralDistance():
	return