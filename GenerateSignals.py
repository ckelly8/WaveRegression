import numpy as np

# Function to generate noisy sine wave data
def generate_noisy_sine_wave(duration, frequency, amplitude, noise_level):
    num_samples = int(duration * frequency)
    time = np.arange(num_samples)
    #frequency_perturbation = np.random.normal(1, noise_level, num_samples)
    #amplitude_perturbation = np.random.normal(1, noise_level, num_samples)
    intercept_perturbation = np.random.normal(0, noise_level, num_samples)
    noisy_sine_wave = amplitude * np.sin(2 * np.pi * (time / frequency))
    return noisy_sine_wave

# Parameters
duration = 600  # Duration of the signal in seconds
frequency = 1  # Base frequency of the sine wave (Hz)
amplitude = 10  # Base amplitude of the sine wave
noise_level = 0.001  # Noise level for perturbations

# Generate noisy sine wave data
data = generate_noisy_sine_wave(duration, frequency, amplitude, noise_level)

# Write data to text file
with open("noisy_sine_wave_data.txt", "w") as file:
    for i in range(duration):
        time_stamp = i
        value = data[i]
        file.write(f"{time_stamp} {value}\n")

print("Text file generated successfully.")
