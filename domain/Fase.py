import numpy as np

class Fase():
    def __init__(self, fase, type, level, frequency, phaseAngle, HF):
        self.fase = fase
        self.type = type
        self.level = level
        self.frequency = frequency
        self.phaseAngle = phaseAngle
        self.HF = HF * 1000
    
    def getWave(self, samplingRateArrange):
        if self.type == 'AM':
            return self.level*np.cos(2*np.pi*self.HF*samplingRateArrange)*(1+np.cos(2*np.pi*self.frequency*samplingRateArrange))
        elif self.type == 'FM':
            return self.level*np.cos((2*np.pi*self.HF*samplingRateArrange)-(1*np.pi*self.frequency))*(np.cos(2*np.pi*self.frequency*samplingRateArrange))
        else:
            return  self.level*np.cos(2*np.pi*self.HF*samplingRateArrange)
        