
import numpy as np
import matplotlib.pyplot as plt

weather_states = ["Sunny", "Rainy", "Cloudy"]
transition_matrix = np.array([
    [0.6, 0.3, 0.1],
    [0.2, 0.5, 0.3],
    [0.3, 0.3, 0.4]
])

start_state = input("Enter starting state (Sunny/Rainy/Cloudy): ")
num_days = int(input("Enter number of days to predict: "))

state_index = weather_states.index(start_state)
sequence = [start_state]

for _ in range(num_days):
    state_index = np.random.choice(range(3), p=transition_matrix[state_index])
    sequence.append(weather_states[state_index])

print("\nPredicted Weather Sequence:")
print(" - ".join(sequence))

occurrences = {state: sequence.count(state) for state in weather_states}

print("\nState Occurrences:")
for state, count in occurrences.items():
    print(f"{state}: {count} times")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.bar(occurrences.keys(), occurrences.values(), color=['red', 'green', 'blue'])
plt.xlabel("Weather State")
plt.ylabel("Occurrences") 
plt.title("Weather State Frequency -Samir")

plt.subplot(1, 2, 2)
plt.plot(sequence, marker='o', linestyle='-', color='black')
plt.yticks(range(3), weather_states)
plt.xlabel("Time Steps (Days)")
plt.ylabel("Weather State")
plt.title("Weather Transitions Over Time - Samir")

plt.tight_layout()
plt.show()
