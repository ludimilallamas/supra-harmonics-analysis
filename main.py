import numpy as np
import matplotlib.pyplot as plt
from domain.SamplingRate import SamplingRate
from domain.Fase import Fase
from domain.SupraHarmonic import SupraHarmonic

def inputFase(componentFase) -> Fase:
    type = input("AM, FM ou None: ")
    level = float(input("Digite a amplitude p.u. do " + componentFase + "ª componente: "))
    frequency = float(input("Digite a frequência Hz do " + componentFase + "ª componente:  "))
    phaseAngle = float(input("Digite o ângulo de fase do " + componentFase + "ª componente: "))
    HF =  float(input("Digite o componente supra harmônico kHz do " + componentFase + "ª componente: "))
    return Fase(componentFase, type, level, frequency, phaseAngle, HF);

def inputSupraHarmonic(identifier) -> SupraHarmonic:
    return SupraHarmonic(float(input('Digite o valor KHz do ' + identifier + 'º supra harmônico: ')))
  
def plotInputSignal(samplingRate, faseWavesSum):
    plt.plot(samplingRate.arrange, faseWavesSum)
    plt.title('Input Signal')
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude (p.u.)")
    plt.show()

def plotSpecgram(faseWavesSum, nfft, samplingRate, hop):
    Mc, fv, t, im = plt.specgram(faseWavesSum, int(nfft), samplingRate, None, None, None, hop)
    plt.title('Estimated Spectrum')
    plt.xlabel('Time(s)')
    plt.ylabel('Frequency (Hz)')
    plt.show()


def main():
    samplingRate = SamplingRate(float(input("Sampling rate kHz: " )))

    firstFase = inputFase('1')
    secondFase = inputFase('2')
    thirdFase = inputFase('3')

    faseWavesSum = firstFase.getWave(samplingRate.arrange) + secondFase.getWave(samplingRate.arrange) + thirdFase.getWave(samplingRate.arrange)

    plotInputSignal(samplingRate, faseWavesSum)

    nfft = samplingRate.value * 20e-3
    wlen = 5e-3 * samplingRate.value 
    hop = int(0.75 * wlen)

    plotSpecgram(faseWavesSum, nfft, samplingRate.value, hop)

    
    firstSupraHarmonic = inputSupraHarmonic('1')
    secondSupraHarmonic = inputSupraHarmonic('2')
    thirdSupraHarmonic = inputSupraHarmonic('3')

    


if __name__ == '__main__':
    main()