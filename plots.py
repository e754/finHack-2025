import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'creditcard.csv'
data = pd.read_csv(file_path)

# Create a figure with 4 rows and 7 columns (28 subplots)
fig, axs = plt.subplots(4, 7, figsize=(16, 12))  # Adjust the figure size for better spacing
fig.suptitle('Visualizing Credit Card Data Variables with Fraud Cases Highlighted', fontsize=16)

# List of variables to plot (adjust to your dataset's column names)
variables = [f"V{i}" for i in range(2, 29)]  # Columns V1 to V28

# Flatten the axs array for easy iteration
axs = axs.flatten()

# Iterate over each variable and plot it
for i, var in enumerate(variables):
    sns.scatterplot(
        x='V1', 
        y=var, 
        hue='Class',  # Color points by fraud status
        palette={0: 'gray', 1: 'red'},  # Gray for non-fraud, red for fraud
        alpha=0.7,  # Transparency for better visibility
        ax=axs[i],  # Plot on the specific subplot
        data=data
    )
    axs[i].set_title(f'{var} over V1', fontsize=8)    # Smaller font for titles
    axs[i].set_xlabel('V1', fontsize=7)
    axs[i].set_ylabel(var, fontsize=7)
    axs[i].tick_params(axis='both', labelsize=6)        # Smaller font for axis labels
    axs[i].legend(loc='upper right', fontsize=6)        # Smaller legend

# Hide any unused subplots (in case of extra grid spaces)
for j in range(len(variables), len(axs)):
    axs[j].set_visible(False)

# Adjust layout for readability
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Add space for the main title
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'creditcard.csv'
data = pd.read_csv(file_path)

# Create a figure with 4 rows and 7 columns (28 subplots)
fig, axs = plt.subplots(4, 7, figsize=(16, 12))  # Adjust the figure size for better spacing
fig.suptitle('Visualizing Credit Card Data Variables with Fraud Cases Highlighted', fontsize=16)

# List of variables to plot (adjust to your dataset's column names)
variables = [f"V{i}" for i in range(1, 29)]  # Columns V1 to V28

# Flatten the axs array for easy iteration
axs = axs.flatten()

# Iterate over each variable and plot it
for i, var in enumerate(variables):
    sns.scatterplot(
        x='Time', 
        y=var, 
        hue='Class',  # Color points by fraud status
        palette={0: 'gray', 1: 'red'},  # Gray for non-fraud, red for fraud
        alpha=0.7,  # Transparency for better visibility
        ax=axs[i],  # Plot on the specific subplot
        data=data
    )
    axs[i].set_title(f'{var} over Time', fontsize=8)    # Smaller font for titles
    axs[i].set_xlabel('Time', fontsize=7)
    axs[i].set_ylabel(var, fontsize=7)
    axs[i].tick_params(axis='both', labelsize=6)        # Smaller font for axis labels
    axs[i].legend(loc='upper right', fontsize=6)        # Smaller legend

# Hide any unused subplots (in case of extra grid spaces)
for j in range(len(variables), len(axs)):
    axs[j].set_visible(False)

# Adjust layout for readability
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Add space for the main title
plt.show()

