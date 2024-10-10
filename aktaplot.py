import os
import pandas as pd
import matplotlib.pyplot as plt

# Set font to Arial
plt.rcParams['font.family'] = 'Arial'

# User setting to show fractions on individual plots
show_fractions = 1  # Set to 1 to show fraction markers, 0 to hide

# To store data for combined plot
combined_elution_volume = []
combined_uv280 = []
labels = []

# Loop through all files in the current directory
for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        # Load the CSV file, including both the header and second row
        full_data = pd.read_csv(filename, encoding='utf-16', sep='\t')

        # Load the data without the first two rows (which are headers)
        data = pd.read_csv(filename, skiprows=2, encoding='utf-16', sep='\t')

        # **Use the first column for the chromatogram elution volume**
        elution_volume = data['ml']  # Assuming the first column is labeled 'ml'
        uv280 = data['mAU']  # Assuming 'mAU' column is correct for UV280 data

        # **Identify the correct column by index for fractions**
        # Find the column index that contains 'Fraction' in the second row
        fraction_column_name = full_data.columns[full_data.iloc[1] == 'Fraction']

        if not fraction_column_name.empty:
            # Get the integer index of the 'Fraction' column
            fraction_column_idx = full_data.columns.get_loc(fraction_column_name[0])

            # The correct "mL" column should be the one just before 'Fraction' for fractions
            fraction_ml_column_index = fraction_column_idx - 1

            # Get the fraction mL values and fraction labels
            fraction_volumes = data.iloc[:, fraction_ml_column_index]
            fractions = data['Fraction']
        else:
            print("having trouble finding fraction data...")
            fraction_volumes = pd.Series([])  # Empty series for no fractions
            fractions = pd.Series([])

        # **Clean the chromatogram data by dropping rows with non-numeric or missing values**
        elution_volume = pd.to_numeric(elution_volume, errors='coerce')
        uv280 = pd.to_numeric(uv280, errors='coerce')
        clean_data = pd.DataFrame({'elution_volume': elution_volume, 'uv280': uv280}).dropna()

        elution_volume = clean_data['elution_volume']
        uv280 = clean_data['uv280']

        # Extract the sample name from the filename (e.g., "B5" from "B5.csv")
        sample_name = filename.split('.')[0]

        # Plot the individual chromatogram data
        plt.figure(figsize=(10, 6))
        plt.plot(elution_volume, uv280, label=f'{sample_name} UV280 (AU) vs Elution Volume (mL)', color="black")
        plt.title(f'{sample_name}')
        plt.xlabel('Elution Volume (mL)', fontsize=12)
        plt.ylabel('UV280 (mAU)', fontsize=12)

        # If show_fractions is on, plot vertical lines for fraction markers
        if show_fractions:
            # **Plot vertical lines using the fraction mL values**
            ymax_value = uv280.max()  # Get the maximum y-value to position the label correctly
            for i, frac_vol in enumerate(fraction_volumes):
                if pd.notna(frac_vol):  # Only plot valid (non-NaN) fraction volumes
                    plt.axvline(x=frac_vol, color='red', linestyle='-', ymax=0.03)  # Solid vertical lines at fraction volumes
                    plt.text(frac_vol, ymax_value * 0.03, f'{fractions[i]}', color='red', rotation=90, fontsize=8, ha='center')  # Labels just above ymax

        # Save the individual plot as a PNG file
        output_file = f'{sample_name}_UV280_vs_ElutionVolume.png'
        plt.savefig(output_file)
        plt.close()  # Close the individual plot

        # Append data for the combined and stacked plots
        combined_elution_volume.append(elution_volume)
        combined_uv280.append(uv280)
        labels.append(sample_name)

# Sort the data alphabetically based on sample names (labels)
sorted_indices = sorted(range(len(labels)), key=lambda i: labels[i])
sorted_labels = [labels[i] for i in sorted_indices]
sorted_elution_volume = [combined_elution_volume[i] for i in sorted_indices]
sorted_uv280 = [combined_uv280[i] for i in sorted_indices]

# Plot the combined data
plt.figure(figsize=(10, 6))

# Iterate over each dataset and plot it (now sorted)
for i in range(len(sorted_labels)):
    plt.plot(sorted_elution_volume[i], sorted_uv280[i], label=f'{sorted_labels[i]}')

# Customize the combined plot
plt.title('Comparison of SEC Chromatograms')
plt.xlabel('Elution Volume (mL)', fontsize=12)
plt.ylabel('UV280 (mAU)', fontsize=12)
plt.legend()

# Save the combined plot as a PNG file
combined_output_file = 'Combined_UV280_vs_ElutionVolume.png'
plt.savefig(combined_output_file)
plt.close()

# Stacked subplot (now sorted)
num_samples = len(sorted_labels)
fig, axs = plt.subplots(num_samples, 1, figsize=(10, 2*num_samples), sharex=True)

for i in range(num_samples):
    axs[i].plot(sorted_elution_volume[i], sorted_uv280[i], label=f'{sorted_labels[i]}', color='black')
    axs[i].set_ylabel('UV280 (mAU)', fontsize=16)
    axs[i].legend(loc="upper right", fontsize=20, handlelength=0, handletextpad=0)  # Hide the black line in the legend
    axs[i].set_ylim(0, 2100)
    axs[i].set_xlim(0, 120)
    axs[i].tick_params(axis='x', labelsize=16)  # Increase x-tick font size
    axs[i].tick_params(axis='y', labelsize=16)  # Increase y-tick font size

# Label the common x-axis
plt.xlabel('Elution Volume (mL)', fontsize=24)

# Adjust layout so titles/labels don't overlap
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the stacked plot as a PNG file
stacked_output_file = 'Stacked_UV280_vs_ElutionVolume.png'
plt.savefig(stacked_output_file)
plt.close()

print("Individual, combined, and stacked plots (in alphabetical order) have been created and saved.")