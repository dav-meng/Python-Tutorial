import matplotlib.pyplot as plt
import pandas as pd
import os
from PIL import Image

# Create your DataFrame with win rates
data = {
    "Team": [
        "Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills",
        "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
        "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers",
        "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
        "Los Angeles Chargers", "Los Angeles Rams", "Las Vegas Raiders", "Miami Dolphins",
        "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
        "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers",
        "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Football Team"
    ],
    "Win_Rate": [
        0.50, 0.63, 0.63, 0.75, 0.13, 0.57, 0.38, 0.25, 0.43, 0.63,
        0.86, 0.75, 0.67, 0.50, 0.25, 1.00, 0.57, 0.43, 0.25, 0.29,
        0.71, 0.25, 0.25, 0.25, 0.33, 0.71, 0.75, 0.50, 0.50, 0.50,
        0.14, 0.75
    ]
}

df = pd.DataFrame(data)

# Define the path to your images
image_folder = r"C:\Users\david\OneDrive\Pictures\New folder\NFL TEAM LOGOS"

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title("NFL Team Win Rates", fontsize=16)
ax.set_xlabel("Win Rate", fontsize=12)
ax.set_ylabel("Teams", fontsize=12)

# Create a horizontal bar chart
bars = ax.barh(df['Team'], df['Win_Rate'], color='blue')

# Add images to the bars
for i, bar in enumerate(bars):
    # Get the team's abbreviation based on the index
    team_abbr = df['Team'].iloc[i].split(' ')[0][:3].upper()  # Get abbreviation

    # Construct the image path
    img_path = os.path.join(image_folder, f"{team_abbr}.png")  # Assuming images are in PNG format

    # Load the image
    try:
        img = Image.open(img_path)
        img = img.resize((40, 40))  # Resize image
        # Calculate position for the image
        ax.imshow(img, aspect='auto', extent=(bar.get_width(), bar.get_width() + 0.04, bar.get_y(), bar.get_y() + 0.5), zorder=10)
    except FileNotFoundError:
        print(f"Image for {team_abbr} not found at {img_path}.")

plt.show()