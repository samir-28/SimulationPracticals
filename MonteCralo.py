
import matplotlib.pyplot as plt
import random

def main():
    iterations = int(input("Enter the number of iterations: "))

    x_inside, y_inside, x_outside, y_outside = [], [], [], []
    for _ in range(iterations):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal')
    plt.gca().add_artist(plt.Circle((0, 0), 1, color='black', fill=False))
    plt.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], color='black')
    plt.scatter(x_inside, y_inside, color='green', s=1, label='Inside Circle')
    plt.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')

    pi_estimate = 4 * len(x_inside) / iterations
    print(f"Estimated value of pi: {pi_estimate}")
    plt.title(f"Samir:Monte Carlo Simulation (Pi Estimate: {pi_estimate:.4f})")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
