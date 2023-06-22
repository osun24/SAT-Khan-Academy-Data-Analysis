import matplotlib.pyplot as plt
import numpy as np

# Data points
points = np.genfromtxt('practice-tests.csv', delimiter=',', skip_header=1)

# Extracting columns
practice_test = points[:, 0]
overall = points[:, 1]
math = points[:, 2]
reading = points[:, 3]

# Plotting
fig, ax1 = plt.subplots()

# Plotting on primary axis
ax1.plot(practice_test, overall, label='Overall', color='blue', linewidth=3)
ax1.set_xlabel('Practice Test')
ax1.set_ylabel('Overall Score', color='black')
ax1.tick_params(axis='y', labelcolor='black')
ax1.set_ylim(min(overall), 1600)

# Creating secondary axis
ax2 = ax1.twinx()

# Plotting on secondary axis
ax2.plot(practice_test, math, label='Math', color='green')
ax2.plot(practice_test, reading, label='Reading', color='red')
ax2.set_ylabel('Math and Reading Score', color='black')
ax2.tick_params(axis='y', labelcolor='black')

# Manually set the limits for secondary y-axis based on data range
ax2.set_ylim(min(math.min(), reading.min()), 800)
ax1.invert_xaxis()

# Labeling and styling
plt.title('Scores vs Practice Test')
plt.legend()

# Displaying the plot
plt.show()