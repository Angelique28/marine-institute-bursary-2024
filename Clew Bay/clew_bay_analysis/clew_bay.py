
import pandas as pd
import matplotlib.pyplot as plt




# castaways data==========================================================================

# Step 1: Load the CSV file into a DataFrame
file_path =  # Replace with your CSV file path
data = pd.read_csv(file_path)


# Step 2: Plot the data
plt.figure(figsize=(8, 10))


# Loop over each unique location and plot its data
for location in data['location'].unique():
    subset = data[data['location'] == location]
    plt.plot(subset['temperature'], subset['depth'], label=f'Location {location}', alpha=0.7, linewidth=2.5)

# Step 3: Invert y-axis to have depth increasing downwards (optional, based on common practice in depth plots)
plt.gca().invert_yaxis()

# Step 4: Labeling the plot
plt.xlabel('Temperature (°C)', fontsize=15)
plt.ylabel('Depth (m)', fontsize=15)
plt.xticks(fontsize=15)  
plt.yticks(fontsize=15)
plt.legend(loc='upper right', bbox_to_anchor=(1.21, 1), borderaxespad=0)
plt.grid(True)

# Step 5: Show the plot
plt.show()




# Salinity
# Loop over each unique location and plot its data
for location in data['location'].unique():
    subset = data[data['location'] == location]
    plt.plot(subset['salinity'], subset['depth'], label=f'Location {location}', alpha=0.7, linewidth=2.5)

# Step 3: Invert y-axis to have depth increasing downwards (optional, based on common practice in depth plots)
plt.gca().invert_yaxis()

# Step 4: Labeling the plot
plt.xlabel('Salinity (psu)', fontsize=15)
plt.ylabel('Depth (m)', fontsize=15)
plt.xticks(fontsize=15)  
plt.yticks(fontsize=15)
plt.legend(loc='upper right', bbox_to_anchor=(1.21, 1), borderaxespad=0)
plt.grid(True)

# Step 5: Show the plot
plt.show()




# castaway by month
# Filter the data to include only rows where the month is March (i.e., month == 3)
season_data = data[data['month'].isin([2,3])]

# Step 3: Plot the data
plt.figure(figsize=(8, 10))

# Loop over each unique location and plot its data for March only
for location in season_data['location'].unique():
    subset = season_data[season_data['location'] == location]
    plt.plot(subset['salinity'], subset['depth'], label=f'{location}', alpha=0.7, linewidth=2.5)

# Step 4: Invert y-axis to have depth increasing downwards (optional, based on common practice in depth plots)
plt.gca().invert_yaxis()

# Step 5: Labeling the plot
plt.xlabel('Salinity (psu)', fontsize=15)
plt.ylabel('Depth (m)', fontsize=15)
plt.xticks(fontsize=15)  
plt.yticks(fontsize=15)
plt.legend(title="Locations", loc='upper right', bbox_to_anchor=(1.15, 1), borderaxespad=0)
plt.grid(True)

# Step 6: Show the plot
plt.show()





# exo sonde- map===============================================

exo_sonde_file = r"file_path" # download exo_sonde.csv file 
es_data = pd.read_csv(exo_sonde_file)

# Set up the plot with cartopy
plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.PlateCarree())

# Add coastlines and borders
ax.coastlines()
ax.add_feature(cfeature.BORDERS)

# Use seaborn to create a scatter plot with a color gradient
sc = ax.scatter(es_data['longitude'], es_data['latitude'], c=es_data['temperature'], cmap='viridis', s=400, vmin=9.1, vmax=9.75)

# Add a color bar
plt.colorbar(sc, label='Temperature')

# Set plot title and labels
plt.title('Temperature Distribution Heatmap Clew Bay')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


# exo sonde- boxplot==========================================================================
locations = ['Location 1', 'Location 2', 'Location 3', 'Location 4', 
              'Location 5', 'Location 6', 'Location 7', 'Location 8']
temperature_data = {
    'Location 1': es_data['temperature'][0:28],
    'Location 2': es_data['temperature'][28:40],
    'Location 3': es_data['temperature'][40:48],
    'Location 4': es_data['temperature'][48:56],
    'Location 5': es_data['temperature'][56:64],
    'Location 6': es_data['temperature'][64:72],
    'Location 7': es_data['temperature'][72:78],
    'Location 8': es_data['temperature'][78:84]
}

salinity_data = {
    'Location 1': es_data['salinity'][0:28],
    'Location 2': es_data['salinity'][28:40],
    'Location 3': es_data['salinity'][40:48],
    'Location 4': es_data['salinity'][48:56],
    'Location 5': es_data['salinity'][56:64],
    'Location 6': es_data['salinity'][64:72],
    'Location 7': es_data['salinity'][72:78],
    'Location 8': es_data['salinity'][78:84]
}

optical_dissolved_oxygen_data = {
    'Location 1': es_data['ODO mg/L'][0:28],
    'Location 2': es_data['ODO mg/L'][28:40],
    'Location 3': es_data['ODO mg/L'][40:48],
    'Location 4': es_data['ODO mg/L'][48:56],
    'Location 5': es_data['ODO mg/L'][56:64],
    'Location 6': es_data['ODO mg/L'][64:72],
    'Location 7': es_data['ODO mg/L'][72:78],
    'Location 8': es_data['ODO mg/L'][78:84]
}



# Convert data to list of lists for boxplot
temp_data = [temperature_data[loc] for loc in locations]
sal_data = [salinity_data[loc] for loc in locations]
odo_data = [optical_dissolved_oxygen_data[loc] for loc in locations]

# Create a boxplot
# First plot: Temperature data
plt.figure(figsize=(10, 6))  

def create_boxplot(data):
    return plt.boxplot(data, patch_artist=True, showmeans=True)

bp_temp = create_boxplot(temp_data)

# Calculate mean and standard deviation
all_temp_data = np.concatenate(temp_data)
average_temp_mean = np.mean(all_temp_data)
stdev_temp_mean = np.std(all_temp_data)
print('the mean temperature across all locations was ' + str(average_temp_mean) + ' °C')
print('the standard deviation was ' + str(stdev_temp_mean))


# Customise box color
for box in bp_temp['boxes']:
    box.set(facecolor='lightgrey', linewidth=1)

# Customize median and mean colors
for median in bp_temp['medians']:
    median.set(color='blue', linewidth=2)

for mean in bp_temp['means']:
    mean.set(marker='o', markerfacecolor='yellow', markeredgecolor='black', markersize=10)

# Create custom legend for median and mean
legend_elements = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow', markeredgecolor='black', markersize=10, label='Mean'),
    Line2D([0], [0], color='blue', linewidth=2, label='Median')
]

# Add legend
plt.legend(handles=legend_elements, loc='best')

# Customise labels and title
plt.xticks(range(1, len(locations) + 1), locations)
plt.title('Temperature Distribution Across Clew Bay - Exo Sonde')
plt.ylabel('Temperature (°C)')
plt.grid(True)

plt.show()  

# Second plot: Salinity data
plt.figure(figsize=(10, 6))  

bp_sal = create_boxplot(sal_data)

# Calculate mean and standard deviation
all_sal_data = np.concatenate(sal_data)
average_sal_mean = np.mean(all_sal_data)
stdev_sal_mean = np.std(all_sal_data)
print('the mean salinity across all locations was ' + str(average_sal_mean) + ' psu')
print('the standard deviation was ' + str(stdev_sal_mean))

# Customise box color
for box in bp_sal['boxes']:
    box.set(facecolor='lightgreen', linewidth=1)

# Customise median and mean colors
for median in bp_sal['medians']:
    median.set(color='blue', linewidth=2)

for mean in bp_sal['means']:
    mean.set(marker='o', markerfacecolor='yellow', markeredgecolor='black', markersize=10)

# Add legend 
plt.legend(handles=legend_elements, loc='best')

# Customise labels and title
plt.xticks(range(1, len(locations) + 1), locations)
plt.title('Salinity Distribution Across Clew Bay - Exo Sonde')
plt.ylabel('Salinity (psu)')
plt.grid(True)

plt.show()  

# Third plot: DO data
plt.figure(figsize=(10, 6))  

bp_odo = create_boxplot(odo_data)

# Calculate mean and standard deviation
all_odo_data = np.concatenate(odo_data)
average_odo_mean = np.mean(all_odo_data)
stdev_odo_mean = np.std(all_odo_data)
print('the mean dissolved oxygen across all locations was ' + str(average_odo_mean) + ' mg/L')
print('the standard deviation was ' + str(stdev_odo_mean))

# Customise box color
for box in bp_odo['boxes']:
    box.set(facecolor='peachpuff', linewidth=1)

# Customise median and mean colors
for median in bp_odo['medians']:
    median.set(color='blue', linewidth=2)

for mean in bp_odo['means']:
    mean.set(marker='o', markerfacecolor='yellow', markeredgecolor='black', markersize=10)

# Add legend 
plt.legend(handles=legend_elements, loc='best')

# Customise labels and title
plt.xticks(range(1, len(locations) + 1), locations)
plt.title('Dissolved Oxygen Distribution Across Clew Bay - Exo Sonde')
plt.ylabel('Dissolved Oxygen (mg/L)')
plt.grid(True)

plt.show() 


# ANOVA==========================================================================
# ANOVA (and Tukey's HSD test)- temperature
temperature_values = [temperature_data[f'Location {i}'] for i in range(1, 9)]
flat_temp_data = np.concatenate(temperature_values)
temp_labels = np.array([loc for loc, data in zip(locations, temperature_values) for _ in data])


f_statistic, p_value = f_oneway(*temperature_values)

print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

# Interpretation
if p_value < 0.05:
    print("There is a significant difference between the mean temperatures of the locations.")
    # Perform Tukey's HSD test
    tukey_result = pairwise_tukeyhsd(flat_temp_data, temp_labels)
    print(tukey_result)
else:
    print("There is no significant difference between the mean temperatures of the locations.")



# ANOVA(and Tukey's HSD test)- salinity
salinity_values = [salinity_data[f'Location {i}'] for i in range(1, 9)]
flat_sal_data = np.concatenate(salinity_values)
sal_labels = np.array([loc for loc, data in zip(locations, salinity_values) for _ in data])

f_statistic, p_value = f_oneway(*salinity_values)

print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

# Interpretation
if p_value < 0.05:
    print("There is a significant difference between the mean salinities of the locations.")
    # Perform Tukey's HSD test
    tukey_result = pairwise_tukeyhsd(flat_sal_data, sal_labels)
    print(tukey_result)
else:
    print("There is no significant difference between the mean salinities of the locations.")



# ANOVA (and Tukey's HSD test)- ODO
odo_values = [optical_dissolved_oxygen_data[f'Location {i}'] for i in range(1, 9)]
flat_odo_data = np.concatenate(odo_values)
odo_labels = np.array([loc for loc, data in zip(locations, odo_values) for _ in data])

f_statistic, p_value = f_oneway(*odo_values)

print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")

# Interpretation
if p_value < 0.05:
    print("There is a significant difference between the mean dissolved oxygens of the locations.")
    # Perform Tukey's HSD test
    tukey_result = pairwise_tukeyhsd(flat_odo_data, odo_labels)
    print(tukey_result)
else:
    print("There is no significant difference between the mean dissolved oxygens of the locations.")

#=============================================================================





