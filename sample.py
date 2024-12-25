import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def vec_sample(vector, t, n):
    unique_num = np.empty(t)

    for i in range(t):
        sampled_vec = np.random.choice(vector, size=n, replace=True)
        unq = len(np.unique(sampled_vec))

        unique_num[i] = unq
        vector = sampled_vec

        if unq == 1:
            print(f"Terminating early at iteration {i + 1} as all elements are the same.")
            break

    # Fill remaining values with NaN if loop is terminated early
    unique_num[i + 1:] = np.nan

    return unique_num


def run_vec_samples(start_n, end_n, num_iterations):
    results = []

    for n in range(start_n, end_n + 1):
        initial_vec = np.arange(1, n + 1)  # Create vector from 1 to n
        unique_numbers_per_iteration = vec_sample(initial_vec, num_iterations, n)
        results.append({
            'n': n,
            'unique_numbers': unique_numbers_per_iteration
        })

    return results


# Example usage
start_n = 5
end_n = 15
num_iterations = 50

results = run_vec_samples(start_n, end_n, num_iterations)

# Convert results to DataFrame for plotting
plot_data = pd.DataFrame([
    {
        'n': result['n'],
        'Iteration': np.arange(1, len(result['unique_numbers']) + 1),
        'UniqueNumbers': result['unique_numbers']
    }
    for result in results
])

# Plot using seaborn
plt.figure(figsize=(12, 8))
sns.lineplot(data=plot_data, x='Iteration', y='UniqueNumbers', hue='n', marker='o')
plt.title('Number of Unique Elements Over Iterations for Different n')
plt.xlabel('Iteration')
plt.ylabel('Number of Unique Elements')
plt.legend(title='n')
plt.grid(True)
plt.show()
