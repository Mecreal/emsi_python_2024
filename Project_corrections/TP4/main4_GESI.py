from signaux import signal_sinusoïdal, signal_carre, signal_triangulaire, caracteristiques
import matplotlib.pyplot as plt

# Paramètres du signal
frequence = 10  # Hz
amplitude = 5  # Volts
duree = 1  # seconde
echantillons = 1000

# Génération d'un signal sinusoïdal
t, signal = signal_sinusoïdal(frequence, amplitude, duree, echantillons)

# Visualisation
plt.plot(t, signal)
plt.title("Signal Sinusoïdal")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude (V)")
plt.grid(True)
plt.savefig("signal_sinusoïdal.png")

# Analyse
amplitude, frequence_principale = caracteristiques(signal)
print(f"Amplitude : {amplitude}")
print(f"Fréquence principale : {frequence_principale} Hz")
