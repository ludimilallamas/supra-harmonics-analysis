import numpy as np

class SamplingRate:
    def __init__(self, samplingRate):
        self.samplingRate = samplingRate * 1000

    def getSamplingRateArrange(self):
        return np.arange(0, 1, 1 / self.samplingRate)
