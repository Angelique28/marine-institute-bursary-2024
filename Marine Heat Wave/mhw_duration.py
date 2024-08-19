import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.dates import YearLocator, DateFormatter
from scipy import stats


# Load the CSV file into a pandas DataFrame
duration_file = r"C:\Users\acheryl\Desktop\mhw_series\mhw_duration\duration_data.csv"

data = pd.read_csv(duration_file)

# Initialize lists to store x and y variables
x_variables = []
y_variables = []

# Define the number of pairs (adjust if needed based on your specific data structure)
num_pairs = 9  # Assuming there are 9 pairs of x and y variables

# Iterate over each pair of columns
for i in range(num_pairs):
    # Extract x column and convert to DatetimeIndex
    x_col_index = 2 * i  # Index of the x column in each pair
    x_col = data.iloc[:, x_col_index]
    x_col = pd.to_datetime(x_col, format='%d/%m/%Y')
    #    x_col = pd.DatetimeIndex(x_col) # use this to generate time series plot
    #    x_variables.append(x_col) # use this to generate time series plot
    x_years = x_col.dt.year # Extract the year from the datetime column and convert to integer, use this to generate linear regression plots
    x_variables.append(x_years)
    
    # Extract y column and convert to list
    y_col_index = 2 * i + 1  # Index of the y column in each pair
    y_col = data.iloc[:, y_col_index].tolist()
    y_variables.append(y_col)

# Separate variables for each x and y pair
x1, x2, x3, x4, x5, x6, x7, x8, x9 = x_variables
y1, y2, y3, y4, y5, y6, y7, y8, y9 = y_variables



plt.figure(figsize=(8, 6))

# Plot each set of data 
plt.plot(x1, y1, color='darkblue', linestyle='-')
plt.plot(x2, y2, color='darkblue', linestyle='-')
plt.plot(x3, y3, color='darkblue', linestyle='-')
plt.plot(x4, y4, color='darkblue', linestyle='-')
plt.plot(x5, y5, color='darkblue', linestyle='-')
plt.plot(x6, y6, color='darkblue', linestyle='-')
plt.plot(x7, y7, color='darkblue', linestyle='-')
plt.plot(x8, y8, color='darkblue', linestyle='-')
plt.plot(x9, y9, color='darkblue', linestyle='-')




# Setting major ticks to yearly intervals
plt.gca().xaxis.set_major_locator(YearLocator(base=4))
plt.gca().xaxis.set_major_formatter(DateFormatter("%Y"))

# Rotating the x-axis labels
plt.gcf().autofmt_xdate()


plt.xlabel('Year', fontsize=14)
plt.ylabel('Duration (days)', fontsize=14)
plt.title('Marine Heat Wave Event Duration Across All Sites')
plt.legend()
plt.tight_layout()
plt.show()



# Linear Regression for MHW Duration

# List of all sites
sites = ['Malin Shelf', 'Donegal Bay', 'Killary Harbour', 'Galway Bay', 'Clew Bay', 'Castlemaine Harbour', 'Deenish Island', 'Bantry Bay', 'Dumanus Bay']

# Perform linear regression and plot for each y-value
for i, (x, y) in enumerate(zip(x_variables, y_variables)):
    x_series = pd.Series(x) # Convert x and y to pandas Series to use isna() method
    y_series = pd.Series(y)
    
    # Remove NaN values from both x and y
    valid_indices = ~x_series.isna() & ~y_series.isna()
    x_clean = x_series[valid_indices]
    y_clean = y_series[valid_indices]
    
    if len(x_clean) > 1:  # Ensure there is more than one data point
        slope, intercept, r_value, p_value, std_err = stats.linregress(x_clean, y_clean)
        
        def myfunc(x):
            return slope * x + intercept
        
        mymodel = [myfunc(xi) for xi in x_clean]
        
        print(f'p-value for {sites[i]} is {p_value}')
        
        if p_value < 0.05:
            print(f'The regression for {sites[i]} duration is significant')
        else:
            print(f'The regression for {sites[i]} duration is not significant')
    
    # Plot the data and linear regression line
        plt.figure(figsize=(8, 6))
        plt.scatter(x_clean, y_clean, label='Data Points')
        plt.plot(x_clean, mymodel, color='red', label='Linear Regression')
        plt.title(sites[i])
        plt.xlabel('Year')
        plt.ylabel('Duration (days)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
