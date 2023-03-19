import numpy as np

class SamplingRate:
    def __init__(self, samplingRate):
        self.value = samplingRate * 1000
        self.arrange =  np.arange(0, 1, 1 / (samplingRate * 1000))

