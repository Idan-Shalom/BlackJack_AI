import matplotlib.pyplot as plt

# Data
solutions = {
    'RiskNeutral':  46.04,
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
fig, ax = plt.subplots()

# Plot bars
ax.bar(range(len(sorted_labels)), sorted_values, color=colors)

# Add labels and title
ax.set_xticks(range(len(sorted_labels)))
ax.set_xticklabels(sorted_labels, rotation=45, ha="right")
ax.set_yticks(range(0, 55, 5))  # Set y-ticks at intervals of 5
ax.set_ylabel('win rate %')
ax.set_title('Agents Winrate Comparison - in 10K games')
plt.tight_layout()

plt.savefig('figures/WRcomp.png')

import matplotlib.pyplot as plt
import numpy as np

# Define the table data
# Rows: Player's hand total (12-21)
# Columns: Dealer's visible card (2-11, where 11 is Ace)
basic_hit_stand_table_hard = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 11-
    ['Hit', 'Hit', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 12
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=basic_hit_stand_table_hard,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['U11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("Basic Strategy Table - Hard")
plt.savefig('figures/BasicTableHard.png')

basic_hit_stand_table_soft = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 12
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=basic_hit_stand_table_soft,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("Basic Strategy Table - Soft")
plt.savefig('figures/BasicTableSoft.png')

NB_hit_stand_table_hard = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 11-
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # Player total 12
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 13
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 14
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 15
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=NB_hit_stand_table_hard,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['U11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("Never-Bust Strategy Table - Hard")
plt.savefig('figures/NBTableHard.png')

NB_hit_stand_table_soft = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 12
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=NB_hit_stand_table_soft,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("Never-Bust Strategy Table - Soft")
plt.savefig('figures/NBTableSoft.png')

#

MTD_hit_stand_table_hard = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 11-
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 12
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=MTD_hit_stand_table_hard,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['U11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("Mimic-The-Dealer Strategy Table - Hard")
plt.savefig('figures/MTDTableHard.png')

MTD_hit_stand_table_soft = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 12
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=MTD_hit_stand_table_soft,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['12','13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("Mimic-The-Dealer Strategy Table - Soft")
plt.savefig('figures/MTDTableSoft.png')

#

ERN_hit_stand_table_hard = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 11-
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 12
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Hit', 'Hit', 'Hit', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=ERN_hit_stand_table_hard,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['U11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("ExpectiMax Risk-Neutral Strategy Table - Hard")
plt.savefig('figures/ERNTableHard.png')

ERN_hit_stand_table_soft = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 12
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Hit', 'Hit', 'Hit', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=ERN_hit_stand_table_soft,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['12','13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("ExpectiMax Risk-Neutral Strategy Table - Soft")
plt.savefig('figures/ERNTableSoft.png')

#

ERL_hit_stand_table_hard = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 11-
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 12
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=ERL_hit_stand_table_hard,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['U11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("ExpectiMax Risk-Loving Strategy Table - Hard")
plt.savefig('figures/ERLTableHard.png')

ERL_hit_stand_table_soft = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 12
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=ERL_hit_stand_table_soft,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['12','13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("ExpectiMax Risk-Loving Strategy Table - Soft")
plt.savefig('figures/ERLTableSoft.png')

#

ERA_hit_stand_table_hard = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 11-
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 12
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 15
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=ERA_hit_stand_table_hard,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['U11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("ExpectiMax Risk-Averse Strategy Table - Hard")
plt.savefig('figures/ERATableHard.png')

ERA_hit_stand_table_soft = np.array([
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 12
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=ERA_hit_stand_table_soft,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("ExpectiMax Risk-Averse Strategy Table - Soft")
plt.savefig('figures/ERATableSoft.png')

#

RL_hit_stand_table_hard = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 11-
    ['Hit', 'Hit', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # Player total 12
    ['Stand', 'Hit', 'Hit', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Hit', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 17
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 18
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=RL_hit_stand_table_hard,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['U11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("Q-Learner Strategy Table - Hard")
plt.savefig('figures/RLTableHard.png')

RL_hit_stand_table_soft = np.array([
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 12
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 13
    ['Hit', 'Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 14
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 15
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 16
    ['Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit', 'Hit'],  # 17
    ['Stand', 'Hit', 'Hit', 'Hit', 'Hit', 'Stand', 'Stand', 'Hit', 'Hit', 'Hit'],  # 18
    ['Stand', 'Hit', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Hit', 'Hit', 'Stand'],  # 19
    ['Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand', 'Stand'],  # 20
])

# Create figure and axis
fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)

# Create the table
table = ax.table(cellText=RL_hit_stand_table_soft,
                 colLabels=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'A'],
                 rowLabels=['12', '13', '14', '15', '16', '17', '18', '19', '20'],
                 loc='center', cellLoc='center')

# Adjust layout
table.scale(1, 2)  # Adjust cell size
plt.title("Q-Learner Strategy Table - Soft")
plt.savefig('figures/RLTableSoft.png')

########

with open('survival/RL.txt', 'r') as f:
    rl_data = [int(line.strip()) for line in f.readlines()]

with open('survival/basic.txt', 'r') as f:
    basic_data = [int(line.strip()) for line in f.readlines()]

with open('survival/RandomPlayer.txt', 'r') as f:
    rand_data = [int(line.strip()) for line in f.readlines()]

# Find the round when the value reaches zero for each dataset
rl_zero_round = next((i for i, value in enumerate(rl_data) if value == 0), len(rl_data))
basic_zero_round = next((i for i, value in enumerate(basic_data) if value == 0), len(basic_data))
random_zero_round = next((i for i, value in enumerate(rand_data) if value == 0), len(rand_data))

# Plot the data
plt.figure(figsize=(10, 6))

# Plot RL data
plt.plot(rl_data, label='RL', color='blue')
plt.axvline(rl_zero_round, color='blue', linestyle='--', label=f'RL reaches zero at round {rl_zero_round}')

# Plot Basic data
plt.plot(basic_data, label='Basic', color='green')
plt.axvline(basic_zero_round, color='green', linestyle='--', label=f'Basic reaches zero at round {basic_zero_round}')

plt.plot(rand_data, label='Random', color='black')
plt.axvline(random_zero_round, color='black', linestyle='--', label=f'Random reaches zero at round {random_zero_round}')

# Add titles and labels
plt.title('Comparison of RL and Basic-Strategy agents')
plt.xlabel('Rounds')
plt.ylabel('Money in '+'\$' + '- 10' + '\$' + ' bet')
plt.legend()

# Save the figure
plt.savefig('figures/RLvsBasic.png')

with open('survival/ExpectimaxRA.txt', 'r') as f:
    RA_data = [int(line.strip()) for line in f.readlines()]

with open('survival/ExpectimaxRL.txt', 'r') as f:
    RL_data = [int(line.strip()) for line in f.readlines()]

with open('survival/ExpectimaxRN.txt', 'r') as f:
    RN_data = [int(line.strip()) for line in f.readlines()]

# Find the round when the value reaches zero for each dataset
RA_zero_round = next((i for i, value in enumerate(RA_data) if value == 0), len(RA_data))
RL_zero_round = next((i for i, value in enumerate(RL_data) if value == 0), len(RL_data))
RN_zero_round = next((i for i, value in enumerate(RN_data) if value == 0), len(RN_data))

# Plot the data
plt.figure(figsize=(10, 6))

# Plot Expectimax data
plt.plot(RA_data, label='Risk-Averse', color='blue')
plt.axvline(RA_zero_round, color='blue', linestyle='--', label=f'Risk-Averse reaches zero at round {RA_zero_round}')

plt.plot(RL_data, label='Risk-Loving', color='red')
plt.axvline(RL_zero_round, color='red', linestyle='--', label=f'Risk-Loving reaches zero at round {RL_zero_round}')

plt.plot(RN_data, label='Risk-Neutral', color='purple')
plt.axvline(RN_zero_round, color='purple', linestyle='--', label=f'Risk-Neutral reaches zero at round {RN_zero_round}')

# Add titles and labels
plt.title('Comparison of ExpectiMax agents')
plt.xlabel('Rounds')
plt.ylabel('Money in '+'\$' + '- 10' + '\$' + ' bet')
plt.legend()

# Save the figure
plt.savefig('figures/ExpectimaxVs.png')

# Read the file and extract data
file_path = 'training1000.txt'

games_played = []
win_rates = []

with open(file_path, 'r') as file:
    for line in file:
        if 'Games played' in line:
            parts = line.split(',')
            games = int(parts[0].split(':')[1].strip())
            win_rate = float(parts[2].split(':')[1].strip().replace('%', ''))
            games_played.append(games)
            win_rates.append(win_rate)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(games_played, win_rates, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Games Played')
plt.ylabel('Win Rate (%)')
plt.title('Win Rate % every 1000 episodes')
plt.grid(True)
plt.savefig('figures/training.png')

