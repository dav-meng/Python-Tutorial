
import pandas as pd
import matplotlib.pyplot as plt

# Create your DataFrame with win rates
data = pd.DataFrame({
    'Team': [
        "Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills", 
        "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
        "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers",
        "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
        "Los Angeles Chargers", "Los Angeles Rams", "Las Vegas Raiders", "Miami Dolphins",
        "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
        "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers",
        "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Football Team"
    ],
    'Win_Rate': [
        0.50, 0.63, 0.63, 0.75, 0.13, 0.57, 0.38, 0.25, 0.43, 0.63, 
        0.86, 0.75, 0.67, 0.50, 0.25, 1.00, 0.57, 0.43, 0.25, 0.29, 
        0.71, 0.25, 0.25, 0.25, 0.33, 0.71, 0.75, 0.50, 0.50, 0.50, 
        0.14, 0.75
    ]
})

# Calculate average win rate
average_win_rate = data['Win_Rate'].mean()

# Plotting
plt.figure(figsize=(10, 8))
plt.barh(data['Team'], data['Win_Rate'], color='blue', alpha=0.7)

# Adding dotted average line
plt.axvline(x=average_win_rate, color='red', linestyle='dotted', linewidth=2)

# Customizing the plot
plt.title('NFL Team Win Ratio', fontsize=16, fontweight='bold')
plt.xlabel('Win Ratio', fontsize=14)
plt.ylabel('Team', fontsize=14)
plt.xlim(0, 1)  # Set x-axis limits from 0 to 1
plt.grid(axis='x', color='gray', linestyle='--', linewidth=0.5)  # Adding grid lines

# Adding average win rate text
plt.text(average_win_rate + 0.02, 5, f'Average Win Ratio: {average_win_rate:.2f}', 
         color='red', fontsize=12, verticalalignment='center')

plt.tight_layout()

# Show the plot
plt.show()