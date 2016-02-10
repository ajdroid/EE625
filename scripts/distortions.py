import numpy as np

def PRD(x, y):
	prd = (np.linalg.norm(x-y)/np.linalg.norm(x)*100)
	return prd 

def WEDD():
	return wedd


def MSEPRD():
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