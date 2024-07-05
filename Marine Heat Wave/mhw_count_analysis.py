import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.multicomp import pairwise_tukeyhsd



# Load the CSV file into a pandas DataFrame
# =============================================================================
# data = pd.read_csv('C:\\Users\\acheryl\\Desktop\\mhw-series\\mhw-counts-NW-W-SW.csv')
# =============================================================================

# =============================================================================
# PLOT LINEAR REGRESSION + INSPECT THE SLOPES
#==============================================================================
# x = data.iloc[:, 0].tolist()
# y_values = [
#     data.iloc[:, 1].tolist(), 
#     data.iloc[:, 2].tolist(),
#     data.iloc[:, 3].tolist(),
#     data.iloc[:, 4].tolist(),
#     data.iloc[:, 5].tolist(),
#     data.iloc[:, 6].tolist(),
#     data.iloc[:, 7].tolist(),
#     data.iloc[:, 8].tolist(),
#     data.iloc[:, 9].tolist()
# ]
# # Create linear regressions for 9 different sites
# for i, y in enumerate(y_values, start=1):
#     slope, intercept, r, p, std_err = stats.linregress(x, y)
#     
#     def myfunc(x):
#         return slope * x + intercept
#     
#     mymodel = list(map(myfunc, x))
#     
#     plt.figure(figsize=(10, 6))
#     plt.scatter(x, y, label='Data Points')
#     plt.plot(x, mymodel, color='red', label='Fitted Line')
#     plt.title(f'Plot {i}')
#     plt.ylabel(f'Y{i}')
#     plt.show()




# =============================================================================
# PLOT LINE GRAPH
#==============================================================================
# x = data.iloc[:, 0].tolist()
# y1 = data.iloc[:, 1].tolist() 
# y2 = data.iloc[:, 2].tolist()  
# y3 = data.iloc[:, 3].tolist()  
# y4 = data.iloc[:, 4].tolist()
# y5 = data.iloc[:, 5].tolist()
# y6 = data.iloc[:, 6].tolist()
# y7 = data.iloc[:, 7].tolist()
# y8 = data.iloc[:, 8].tolist()
# y9 = data.iloc[:, 9].tolist()
# 
# # Calculate mean of all y-values
# mean_y = data.iloc[:, 1:].mean(axis=1).tolist()
# 
# plt.figure(figsize=(8, 6))
# 
# # Plot each set of data 
# plt.plot(x, y1, color='darkgrey', linestyle='-')
# plt.plot(x, y2, color='darkgrey', linestyle='-')
# plt.plot(x, y3, color='darkgrey', linestyle='-')
# plt.plot(x, y4, color='darkgrey', linestyle='-')
# plt.plot(x, y5, color='darkgrey', linestyle='-')
# plt.plot(x, y6, color='darkgrey', linestyle='-')
# plt.plot(x, y7, color='darkgrey', linestyle='-')
# plt.plot(x, y8, color='darkgrey', linestyle='-')
# plt.plot(x, y9, color='darkgrey', linestyle='-')
# 
# # Plot mean line
# plt.plot(x, mean_y, color='red', linestyle='--', linewidth=2, label='Mean')
# 
# plt.xlabel('Year', fontsize=14)
# plt.ylabel('Marine Heat Wave Count', fontsize=14)
# plt.title('Marine Heat Wave Count Across Sites')
# plt.legend()
# plt.tight_layout()
# plt.show()
# =============================================================================



# =============================================================================
# T-TEST TO CHECK IF EACH SLOPE SIGNIFICANTLY DIFFERS FROM ZERO 
#==============================================================================
# t-test for slope
# Add a constant to the independent variable
# x = sm.add_constant(x)
# 
# for i, y in enumerate(y_values, start=1):
#     # Convert y to a DataFrame
#     y = pd.Series(y)
# 
#     # Fit the linear regression model
#     model = sm.OLS(y, x).fit()
# 
#     # Perform the t-test and get the summary
#     print(f"Summary for Plot {i}")
#     print(model.summary())
#     
#     # Check if the slope is significantly different from zero
#     slope_p_value = model.pvalues[1]  # p-value for the slope (x1)
#     if slope_p_value < 0.05:
#         print(f"The slope for Plot {i} is significantly different from zero (p-value = {slope_p_value}).")
#     else:
#         print(f"The slope for Plot {i} is not significantly different from zero (p-value = {slope_p_value}).")
#     print("\n")




# =============================================================================
# ANOVA
#==============================================================================
# malin_shelf = data['Malin Shelf']
# donegal_bay = data['Donegal Bay']
# killary_harbour = data['Killary Harbour']
# galway_bay = data['Galway Bay']
# clew_bay = data['Clew Bay']
# castlemaine_harbour = data['Castlemaine Harbour']
# deenish_island = data['Deenish Island']
# bantry_bay = data['Bantry Bay']
# dumanus_bay = data['Dumanus Bay']
# 
# # Perform the ANOVA
# f_stat, p_value = stats.f_oneway(malin_shelf, donegal_bay, killary_harbour, galway_bay, clew_bay, castlemaine_harbour, deenish_island, bantry_bay, dumanus_bay)
# print('F-statistic:', f_stat)
# print('p-value:', p_value)
# 
# if p_value < 0.05:
#     print("There is a significant difference between the mean of marine heat wave event counts across sites.")
# else:
#     print("There is no significant difference between the mean of marine heat wave event counts across sites.")



# ============================================================================
# VISUALISING SLOPES BETWEEN SITES 
#=============================================================================
# # Create csv file with slopes from models of each site
# x = data.iloc[:, 0].tolist()  # Year column
# y_malin_shelf = data.iloc[:, 1].tolist()
# y_donegal_bay = data.iloc[:, 2].tolist()
# y_killary_harbour = data.iloc[:, 3].tolist()
# y_galway_bay = data.iloc[:, 4].tolist()
# y_clew_bay = data.iloc[:, 5].tolist()
# y_castlemaine_harbour = data.iloc[:, 6].tolist()
# y_deenish_island = data.iloc[:, 7].tolist()
# y_bantry_bay = data.iloc[:, 8].tolist()
# y_dumanus_bay = data.iloc[:, 9].tolist()
# 
# 
# # Function to calculate model and return predictions
# def calculate_model(x, y):
#     slope, intercept, r, p, std_err = stats.linregress(x, y)
#     
#     def model_func(x):
#         return slope * x + intercept
#     
#     return model_func, slope
# 
# # Calculate models for each site
# malinshelf_model, slope_malin_shelf = calculate_model(x, y_malin_shelf)
# donegalbay_model, slope_donegal_bay = calculate_model(x, y_donegal_bay)
# killaryharbour_model, slope_killary_harbour = calculate_model(x, y_killary_harbour)
# galwaybay_model, slope_galway_bay = calculate_model(x, y_galway_bay)
# clewbay_model, slope_clew_bay = calculate_model(x, y_clew_bay)
# castlemaineharbour_model, slope_castlemaine_harbour = calculate_model(x, y_castlemaine_harbour)
# deenishisland_model, slope_deenish_island = calculate_model(x, y_deenish_island)
# bantrybay_model, slope_bantry_bay = calculate_model(x, y_bantry_bay)
# dumanusbay_model, slope_dumanus_bay = calculate_model(x, y_dumanus_bay)
# 
# # Generate predictions using models
# malinshelf_predictions = list(map(malinshelf_model, x))
# donegalbay_predictions = list(map(donegalbay_model, x))
# killaryharbour_predictions = list(map(killaryharbour_model, x))
# galwaybay_predictions = list(map(galwaybay_model, x))
# clewbay_predictions = list(map(clewbay_model, x))
# castlemaineharbour_predictions = list(map(castlemaineharbour_model, x))
# deenishisland_predictions = list(map(deenishisland_model, x))
# bantrybay_predictions = list(map(bantrybay_model, x))
# dumanusbay_predictions = list(map(dumanusbay_model, x))
# 
# # Create DataFrame with slopes
# slopes_data = pd.DataFrame({
#     'Malin Shelf': [slope_malin_shelf],
#     'Donegal Bay': [slope_donegal_bay],
#     'Killary Harbour': [slope_killary_harbour],
#     'Galway Bay': [slope_galway_bay],
#     'Clew Bay': [slope_clew_bay],
#     'Castlemaine Harbour': [slope_castlemaine_harbour],
#     'Deenish Island': [slope_deenish_island],
#     'Bantry Bay': [slope_bantry_bay],
#     'Dumanus Bay': [slope_dumanus_bay],
# })
# 
# # Save to CSV
# slopes_data.to_csv('site_slopes.csv', index=False)
# =============================================================================
#
# # Create a bar plot
df_s = pd.read_csv('C:\\Users\\acheryl\\Desktop\\mhw-series\\site_slopes.csv')


df_s = df_s.T
df_s.columns = ['Slope']
df_s.reset_index(inplace=True)
df_s.rename(columns={'index': 'Location'}, inplace=True)
colors = ['darkblue', 'darkblue', 'darkgreen', 'darkgreen', 'darkgreen', 'darkgreen', 'darkgrey', 'darkgrey', 'darkgrey']

# Create custom legend handles
legend_handles = [
    Patch(facecolor='darkblue', edgecolor='darkblue', label='Northwest'),
    Patch(facecolor='darkgreen', edgecolor='darkgreen', label='West'),
    Patch(facecolor='darkgrey', edgecolor='darkgrey', label='Southwest')
]

# Visualization
plt.figure(figsize=(10, 6))
plt.bar(df_s['Location'], df_s['Slope'], color=colors)
plt.ylabel('Slope of Linear Regression', fontsize=14)
plt.title('Linear Regression Slopes of Marine Heat Waves from 1982-2024', fontsize=16)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(handles=legend_handles, fontsize=12)
plt.tight_layout()
plt.show()

# test the significance of slopes regionally
df_s['Region'] = ['Northwest', 'Northwest', 'West', 'West', 'West', 'West', 'Southwest', 'Southwest', 'Southwest']
f_stat, p_value = stats.f_oneway(
    df_s[df_s['Region'] == 'Northwest']['Slope'],
    df_s[df_s['Region'] == 'West']['Slope'],
    df_s[df_s['Region'] == 'Southwest']['Slope']
)

print('F-statistic:', f_stat)
print('p-value:', p_value)

if p_value < 0.05:
    print("There is a significant difference between the slopes regionally.")
    
    # Perform Tukey's HSD test
    tukey_result = pairwise_tukeyhsd(endog=df_s['Slope'], groups=df_s['Region'], alpha=0.05)
    print(tukey_result)
    
else:
    print("There is no significant difference between the slopes regionally.")


# =============================================================================











