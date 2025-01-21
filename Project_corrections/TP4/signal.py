import numpy as np

# Génération des signaux
def signal_sinusoïdal(frequence, amplitude, duree, echantillons):
    t = np.linspace(0, duree, echantillons)
    signal = amplitude * np.sin(2 * np.pi * frequence * t)
    return t, signal

def signal_carre(frequence, amplitude, duree, echantillons):
    t = np.linspace(0, duree, echantillons)
    signal = amplitude * np.sign(np.sin(2 * np.pi * frequence * t))
    return t, signal

def signal_triangulaire(frequence, amplitude, duree, echantillons):
    t = np.linspace(0, duree, echantillons)
    signal = amplitude * (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * frequence * t))
    return t, signal

# Analyse des caractéristiques
def caracteristiques(signal):
    amplitude = np.max(signal) - np.min(signal)
    frequence = np.fft.fftfreq(len(signal))
    frequence_principale = abs(frequence[np.argmax(np.abs(np.fft.fft(signal)))])
    return amplitude, frequence_principale

# Filtre passe-bas récursif
def filtre_passe_bas(signal, alpha):
    if len(signal) <= 1:
        return signal
    else:
        signal_filtré = filtre_passe_bas(signal[:-1], alpha)
        signal_filtré.append(alpha * signal[-1] + (1 - alpha) * signal_filtré[-1])
        return signal_filtré
