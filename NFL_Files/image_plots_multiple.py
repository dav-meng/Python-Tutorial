##Work in progress


import os
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg

# Team data
teams = [
    "Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills",
    "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
    "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers",
    "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
    "Los Angeles Chargers", "Los Angeles Rams", "Las Vegas Raiders", "Miami Dolphins",
    "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
    "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers",
    "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Football Team"
]

win_rates = [
    0.50, 0.63, 0.63, 0.75, 0.13, 0.57, 0.38, 0.25, 0.43, 0.63, 0.86, 0.75, 0.67,
    0.50, 0.25, 1.00, 0.57, 0.43, 0.25, 0.29, 0.71, 0.25, 0.25, 0.25, 0.33, 0.71,
    0.75, 0.50, 0.50, 0.50, 0.14, 0.75
]

# Folder containing the logo images (using your specified absolute path)
image_folder = r"C:\Users\david\OneDrive\Pictures\New folder\NFL TEAM LOGOS"

# Plot setup
fig, ax = plt.subplots(figsize=(10, 12))
ax.set_xlim(0, 1.0)  # Set x-axis to go    a bit above 1.0 for spacing

# Iterate over teams and their win rates
for i, (team, win_rate) in enumerate(zip(teams, win_rates)):
    # Path to each team's logo image
    logo_path = os.path.join(image_folder, f"{team.replace(' ', '_')}.png")  # assuming file names like "Arizona_Cardinals.png"
    
    # Plotting the team name as a text label
    ax.text(win_rate + 0.05, i, team, va='center', fontsize=8)
    
    # Loading and plotting the logo image if it exists
    if os.path.exists(logo_path):
        img = mpimg.imread(logo_path)
        ax.imshow(img, extent=(win_rate - 0.05, win_rate + 0.05, i - 0.3, i + 0.3), aspect='auto')

# Set labels
ax.set_yticks(range(len(teams)))
ax.set_yticklabels(teams, fontsize=8)
ax.set_xlabel("Win Rate")
ax.set_title("NFL Teams Win Rate with Logos")

# Add average win rate line
average_win_rate = sum(win_rates) / len(win_rates)
ax.axvline(x=average_win_rate, color='green', linestyle='--', label=f'Average Win Rate: {average_win_rate:.2f}')
ax.legend()

plt.tight_layout()
plt.show()