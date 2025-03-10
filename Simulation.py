import numpy as np

# Constants
K1 = 0.025  # Reaction rate constant for the decrease of Ch1 and Ch2
K2 = 0.0    # Reaction rate constant for the increase of Ch3
DT = 0.01   # Time step
TIME = 100.0  # Total simulation time in seconds

# Initial concentrations
C1 = [60.0]
C2 = [35.0]
C3 = [0.0]

# Time initialization
time = [0.0]

# Simulation loop
while time[-1] < TIME:
    t = time[-1]
    c1 = C1[-1]
    c2 = C2[-1]
    c3 = C3[-1]

    # Calculate next values
    c1_next = c1 + ((K2 * c3 - K1 * c1 * c2) * DT)
    c2_next = c2 + ((K2 * c3 - K1 * c1 * c2) * DT)
    c3_next = c3 + (2.0 * (K1 * c1 * c2 - K2 * c3) * DT)

    # Append new values
    C1.append(c1_next)
    C2.append(c2_next)
    C3.append(c3_next)
    time.append(t + DT)

# Write results to a file
with open("lab01.txt", "w") as file:
    for t, c1, c2, c3 in zip(time, C1, C2, C3):
        file.write(f"{t:.4f} {c1:.4f} {c2:.4f} {c3:.4f}\n")

print("Reaction simulated!")
