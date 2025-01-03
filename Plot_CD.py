import pandas as pd
import matplotlib.pyplot as plt
from Clean_CD import *
from CD_Price_Conversion import *

# Question: Which car brand has the highest average price for a new and used vehicle?

# Assuming 'avg_price_gb_condition' is the DataFrame created with grouped data
avg_price_gb_condition = converted_DataFrame().groupby(['Brand', 'Condition']).agg({'USD': 'mean'}).reset_index()

# Split the data and sort by price in descending order for each condition
new_cars = avg_price_gb_condition[avg_price_gb_condition['Condition'] == 'New'].sort_values(by='USD', ascending=False)
used_cars = avg_price_gb_condition[avg_price_gb_condition['Condition'] == 'Used'].sort_values(by='USD', ascending=False)

# Calculate the y-axis limits based on min and max values with padding for visibility
new_min, new_max = new_cars['USD'].min() * 0.9, new_cars['USD'].max() * 1.1
used_min, used_max = used_cars['USD'].min() * 0.9, used_cars['USD'].max() * 1.1

# Plot for New Cars
plt.figure(figsize=(10, 5))
bars = plt.bar(new_cars['Brand'], new_cars['USD'], color='skyblue')
plt.title('Average Price by Brand for New Cars')
plt.xlabel('Brand')
plt.ylabel('Average Price (USD)')
plt.ylim(new_min, new_max)  # Set y-axis limits for New Cars plot
plt.xticks(rotation=45)

# Adding value labels on each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}', ha='center', va='bottom', rotation = 45)

plt.show()

# Plot for Used Cars
plt.figure(figsize=(10, 5))
bars = plt.bar(used_cars['Brand'], used_cars['USD'], color='salmon')
plt.title('Average Price by Brand for Used Cars')
plt.xlabel('Brand')
plt.ylabel('Average Price (USD)')
plt.ylim(used_min, used_max)  # Set y-axis limits for Used Cars plot
plt.xticks(rotation=45)

# Adding value labels on each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}', ha='center', va='bottom', rotation = 45)


plt.show()