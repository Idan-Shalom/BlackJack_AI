import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load RL and Basic data
with open('survival/RL.txt', 'r') as f:
    rl_data = [int(line.strip()) for line in f.readlines()]

with open('survival/basic.txt', 'r') as f:
    basic_data = [int(line.strip()) for line in f.readlines()]

# Find the round when the value reaches zero for each dataset
rl_zero_round = next((i for i, value in enumerate(rl_data) if value == 0), len(rl_data))
basic_zero_round = next((i for i, value in enumerate(basic_data) if value == 0), len(basic_data))

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Initialize empty plot lines for RL and Basic data
line_rl, = ax.plot([], [], label='RL', color='blue')
line_basic, = ax.plot([], [], label='Basic', color='green')

# Add the titles and labels
ax.set_title('Comparison of RL and Basic-Strategy agents')
ax.set_xlabel('Rounds')
ax.set_ylabel('Money in ' + '\$' + '- 10' + '\$' + ' bet')
ax.legend()

# Set axis limits based on the data
ax.set_xlim(0, max(len(rl_data), len(basic_data)))
ax.set_ylim(min(min(rl_data), min(basic_data)), max(max(rl_data), max(basic_data)))


# Update function for animation
def update(frame):
    step = 4  # Number of points to plot per frame
    current_frame = frame * step

    # Set data for RL line, only update if within data range
    if current_frame <= len(rl_data):
        line_rl.set_data(range(current_frame), rl_data[:current_frame])

    # Set data for Basic line, only update if within data range
    if current_frame <= len(basic_data):
        line_basic.set_data(range(current_frame), basic_data[:current_frame])

    return line_rl, line_basic


# Create the animation using the longest dataset's length
ani = FuncAnimation(fig, update, frames=range(1, max(len(rl_data), len(basic_data)) // 4 + 1 + 3000), interval=10, blit=True)

# Save the animation as a video
ani.save('animations/game_comparison.mp4', writer='ffmpeg')

# Load RL and Basic data
with open('survival/ExpectimaxRL.txt', 'r') as f:
    RL_data = [int(line.strip()) for line in f.readlines()]

with open('survival/ExpectimaxRA.txt', 'r') as f:
    RA_data = [int(line.strip()) for line in f.readlines()]

with open('survival/ExpectimaxRN.txt', 'r') as f:
    RN_data = [int(line.strip()) for line in f.readlines()]

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Initialize empty plot lines for RL and Basic data
line_RL, = ax.plot([], [], label='ERL', color='blue')
line_RN, = ax.plot([], [], label='ERN', color='purple')
line_RA, = ax.plot([], [], label='ERA', color='red')

# Add the titles and labels
ax.set_title('Comparison of Expectimax agents')
ax.set_xlabel('Rounds')
ax.set_ylabel('Money in ' + '\$' + '- 10' + '\$' + ' bet')
ax.legend()

# Set axis limits based on the data
ax.set_xlim(0, max(len(RL_data), len(RA_data), len(RN_data)))
ax.set_ylim(min(min(RL_data), min(RN_data), min(RA_data)), max(max(RL_data), max(RN_data), max(RA_data)))


# Update function for animation
def update(frame):
    step = 4  # Number of points to plot per frame
    current_frame = frame * step

    # Set data for RL line, only update if within data range
    if current_frame <= len(RL_data):
        line_RL.set_data(range(current_frame), RL_data[:current_frame])

    if current_frame <= len(RA_data):
        line_RA.set_data(range(current_frame), RA_data[:current_frame])

    if current_frame <= len(RN_data):
        line_RN.set_data(range(current_frame), RN_data[:current_frame])

    return line_RL, line_RN, line_RA


# Create the animation using the longest dataset's length
ani = FuncAnimation(fig, update, frames=range(1, max(len(RL_data), len(RA_data), len(RN_data)) // 4 + 1 + 3000), interval=10, blit=True)

# Save the animation as a video
ani.save('animations/exp_comparison.mp4', writer='ffmpeg')

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Data
solutions = {
    'RiskNeutral': 46.04,
    'RiskAverse': 45.14,
    'RiskLoving': 46.15,
    'RL': 46.27
}

comparisons = {
    'NeverBust': 45.36,
    'MimicDealer': 45.37,
    'Basic': 46.98,
    'Random': 32.96
}

# Combine both solutions and comparisons
combined_data = {**solutions, **comparisons}

# Sort by values
sorted_data = dict(sorted(combined_data.items(), key=lambda item: item[1]))

# Separate labels and values for plotting
sorted_labels = list(sorted_data.keys())
sorted_values = list(sorted_data.values())

# Color mapping: blue for solutions, green for comparisons
colors = ['blue' if label in solutions else 'green' for label in sorted_labels]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size if necessary

# Initialize bars with height zero
bars = ax.bar(range(len(sorted_labels)), np.zeros(len(sorted_labels)), color=colors)

# Add labels and title
ax.set_xticks(range(len(sorted_labels)))
ax.set_xticklabels(sorted_labels, rotation=45, ha="right")
ax.set_yticks(np.arange(0, 55, 5))  # Set y-ticks at intervals of 5
ax.set_ylabel('win rate %')
ax.set_title('Agents Winrate Comparison - in 10K games')

# Function to update the heights of the bars in each frame
def update(frame):
    # Compute the new heights based on the frame
    if frame < 100:  # Animate rising bars until frame 100
        current_heights = np.minimum(frame / 100 * np.array(sorted_values), sorted_values)
    else:  # Maintain final heights for frames beyond 100
        current_heights = sorted_values

    # Update the heights of all bars
    for bar, height in zip(bars, current_heights):
        bar.set_height(height)

    return bars

# Total frames: 100 for animation, plus additional frames to hold the final state
total_frames = 100 + 30  # 100 frames to animate, plus 30 frames to hold the final state
interval = 200  # milliseconds between frames

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, total_frames+ 3000), interval=interval, blit=True)

# Adjust layout to prevent clipping
plt.tight_layout()

# Save the animation as a video
ani.save('animations/bar_comparison.mp4', writer='ffmpeg')

