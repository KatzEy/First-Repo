import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Holling-Tanner equations
def holling_tanner(t, z, a, b,c,d):
    x, y = z  # Prey and predator
    dxdt = x * a - x*y*b
    dydt = x*y*c - y*d
    return [dxdt, dydt]

# Parameters
a = 2
b = 2
c = 1
d = 2

# Initial conditions
x0 = 1  # Initial prey population
y0 = 2  # Initial predator population
z0 = [x0, y0]

# Time span for the simulation
t_span = (0, 50)  # From time 0 to 50
t_eval = np.linspace(*t_span, 1000)  # 1000 points for smooth plotting

# Solve the system of equations
sol = solve_ivp(holling_tanner, t_span, z0, args=(a,b,c,d), t_eval=t_eval)

# Extract the solution
x, y = sol.y

# Plot the phase space
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='teal')
plt.title("Phase Space of Holling-Tanner Model", fontsize=14)
plt.xlabel("Prey Population (x)", fontsize=12)
plt.ylabel("Predator Population (y)", fontsize=12)
plt.grid()
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(sol.t, x, label="Prey Population", color='green')
plt.plot(sol.t, y, label="Predator Population", color='red')
plt.title("Prey and Predator Populations Over Time", fontsize=14)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Population", fontsize=12)
plt.legend()
plt.grid()
plt.show()



