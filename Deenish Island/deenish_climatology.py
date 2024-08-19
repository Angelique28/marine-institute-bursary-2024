
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the data
# Replace 'path_to_your_file.csv' with the actual file path
data = pd.read_csv(r"C:\Users\acheryl\Desktop\mhw_series\mhw_series\csv-sst-51.575N-9.675W.csv")
# file for Deenish Island: "C:\Users\acheryl\Desktop\Deenish Island\csv-sst-51.725N-10.225W.csv"
# file for Dumanus Bay: "C:\Users\acheryl\Desktop\mhw_series\mhw_series\csv-sst-51.575N-9.675W.csv"
data['Date'] = pd.to_datetime(data['Date'], format='ISO8601', dayfirst=True)


# Extract year and month for easier grouping
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month

# Define seasons
seasons = {
    'Spring': [4, 5, 6],
    'Summer': [7, 8, 9],
    'Autumn': [10, 11, 12],
    'Winter': [1, 2, 3]
}

climatologies = {
    'Spring': 11.51,
    'Summer': 14.89,
    'Autumn': 11.76,
    'Winter': 9.28
}


# Calculate average SST for each season per year
seasonal_avg = {}
for season, months in seasons.items():
    seasonal_avg[season] = data[data['Month'].isin(months)].groupby('Year')['SST (ºC)'].mean()

# Plot the seasonal trends
plt.figure(figsize=(14, 8))
for season, avg_sst in seasonal_avg.items():
    plt.plot(avg_sst.index, avg_sst.values, label=season, linewidth=2)

plt.xlabel('Year', fontsize=15)
plt.ylabel('Average SST (°C)', fontsize=15)
plt.title('Seasonal Average Sea Surface Temperature (1982-2024)', fontsize=15)
plt.xticks(fontsize=15)  
plt.yticks(fontsize=15)
plt.legend()
plt.grid(True)
plt.show()



# =============================================================================
# # Calculate average SST for each season per year and subtract climatology
# seasonal_anomalies = {}
# for season, months in seasons.items():
#     # Calculate the average SST for the season each year
#     seasonal_avg = data[data['Month'].isin(months)].groupby('Year')['SST (ºC)'].mean()
#     
#     # Subtract the climatology to get the anomaly
#     seasonal_anomalies[season] = seasonal_avg - climatologies[season]
# 
# # Step 5: Plot the SST anomalies for each season
# plt.figure(figsize=(14, 8))
# for season, anomalies in seasonal_anomalies.items():
#     plt.plot(anomalies.index, anomalies.values, label=season, linewidth=2)
# 
# # Step 6: Customize the plot
# plt.xlabel('Year', fontsize=15)
# plt.ylabel('SST Anomaly (°C)', fontsize=15)
# plt.title('Seasonal SST Anomalies (1982-2024)', fontsize=15)
# plt.xticks(fontsize=15)
# plt.yticks(fontsize=15)
# plt.legend()
# plt.grid(True)
# plt.show()




# =============================================================================
# # SST anomaly in 4 separate graphs
# seasonal_anomalies = {}
# for season, months in seasons.items():
#     # Calculate the average SST for the season each year
#     seasonal_avg = data[data['Month'].isin(months)].groupby('Year')['SST (ºC)'].mean()
#     
#     # Subtract the climatology to get the anomaly
#     seasonal_anomalies[season] = seasonal_avg - climatologies[season]
# 
# # Step 5: Create a 2x2 grid of subplots
# fig, axs = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)
# fig.suptitle('Seasonal SST Anomalies (1982-2024)', fontsize=15)
# 
# # Plot each season in its respective subplot
# for i, (season, anomalies) in enumerate(seasonal_anomalies.items()):
#     ax = axs[i // 2, i % 2]  # Determine the subplot location
#     
#     # Plot SST anomalies
#     ax.plot(anomalies.index, anomalies.values, color='black', linewidth=2, label='SST Anomaly')
#     
#     # Fit a linear regression line
#     x = anomalies.index.values
#     y = anomalies.values
#     if len(x) > 1:  # Ensure there are at least two data points
#         coefficients = np.polyfit(x, y, 1)
#         polynomial = np.poly1d(coefficients)
#         regression_line = polynomial(x)
#         print(season + " regression values : " + str(regression_line))
#         print(str(abs(regression_line[0]) + abs(regression_line[-1])))
#         ax.plot(x, regression_line, 'r--', label='Regression Line')
#     
#         # Calculate R^2 value
#         residuals = y - regression_line
#         ss_res = np.sum(residuals**2)
#         ss_tot = np.sum((y - np.mean(y))**2)
#         r_squared = 1 - (ss_res / ss_tot)
#         
#         # Annotate the plot with R^2 value
#         ax.text(0.05, 0.95, f'$R^2 = {r_squared:.2f}$', transform=ax.transAxes, fontsize=13, verticalalignment='top')
#         
#     # Customize the subplot
#     ax.set_title(season, fontsize=15)
#     ax.set_xlabel('Year', fontsize=15)
#     ax.set_ylabel('SST Anomaly (°C)', fontsize=15)
#     
#     # Apply font size to ticks within each subplot
#     ax.tick_params(axis='x', labelsize=15)
#     ax.tick_params(axis='y', labelsize=15)
#     
#     ax.grid(True)
# 
# # Adjust layout and display the plot
# plt.tight_layout(rect=[0, 0, 1, 0.96])
# plt.show()
# =============================================================================
