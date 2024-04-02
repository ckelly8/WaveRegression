import matplotlib.pyplot as plt

# Read data from text file
time = []
value = []
with open("noisy_sine_wave_data.txt", "r") as file:
    for line in file:
        t, v = map(float, line.strip().split())
        time.append(t)
        value.append(v)

# Plot the sine wave
plt.figure(figsize=(10, 5))
plt.plot(time, value, label='Noisy Sine Wave', color='b')
plt.title('Noisy Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.show()
