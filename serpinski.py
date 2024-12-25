import random
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon, Point
import matplotlib.animation as animation


original_triangle = [(1/2, 1/2), (3/2, 1/2), (1, (np.sqrt(3)+1)/2)]

scaling_factor = 5

triangle = [(x * scaling_factor, y * scaling_factor) for x, y in original_triangle]
x_coords, y_coords = zip(*triangle)
polygon = Polygon(triangle)

def generate_random_point_in_polygon(polygon):
    min_x, min_y, max_x, max_y = polygon.bounds
    while True:
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        point = Point(x, y)
        if polygon.contains(point):
            return (x, y)

current_point = generate_random_point_in_polygon(polygon)

new_array = []
n = 100000


for i in range(n):
    base_point = random.choice(triangle)

    mid_x = (current_point[0] + base_point[0]) / 2
    mid_y = (current_point[1] + base_point[1]) / 2

    current_point = (mid_x, mid_y)
    new_array.append(current_point)

new_array = np.array(new_array)
"""
plt.plot(x_coords, y_coords, 'bo', markersize=5)
plt.scatter(new_array[:, 0], new_array[:, 1], c='black', s=0.1)
plt.axis('equal')
plt.grid(True)
plt.show()
"""


fig, ax = plt.subplots()
scatter = ax.scatter([], [])

# Set the limits and labels
ax.set_xlim(0, 2)
ax.set_ylim(0, 3)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Incrementally Adding Points to Scatter Plot')

# Initialize lists to store x and y data
x_data, y_data = [], []


# Update function for the animation
def update(frame_number):
    # Add the next point from the new_array to the lists
    x_data = new_array[0: frame_number +1]
    y_data = new_array[0: frame_number +1]

    #scatter.set_data(x_data, y_data)

    # Update the scatter plot with the new data
    scatter.set_offsets(np.c_[x_data, y_data])

    return scatter,


# Create the animation
num_frames = len(new_array)
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=0.1, blit=True)

# Show the plot and start the animation
plt.show()

