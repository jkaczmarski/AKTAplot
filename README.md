# AKTAplot

> AKTAplot is a (very) simple Python-based script for visualizing chromatographic data, particularly from AKTA systems. The script generates publication-quality plots of UV280 absorbance vs. elution volume, along with optional markers indicating fraction collection points. It’s designed for scientists and researchers working with chromatographic data who want a simple, automated way to visualize their results.

## Features

- **Plot UV280 Absorbance vs. Elution Volume:** Generates line plots of chromatographic data, visualizing UV absorbance (mAU) against elution volume (mL).
- **Fraction Marker Support:** Adds vertical lines to indicate the elution volumes at which fractions were collected, with labels for each fraction.
- **Combined and Stacked Plots:** Supports the generation of combined chromatogram plots from multiple data files, as well as stacked plots for easy comparison.

## Requirements

	•	Python 3.x
	•	Required Python libraries:
	•	pandas
	•	matplotlib

You can install the necessary libraries using pip:

```pip install pandas matplotlib```

## How to Use AKTAplot

### 1. Clone the Repository

Clone this repository to your local machine:

```git clone https://github.com/yourusername/AKTAplot.git```

### 2. Prepare Your Data

To the same folder, add the csv files you have exported from Unicorn (AKTA software). Rename these files based on the sample name (e.g. ProteinA.csv, ProteinB.csv) etc, since names will be extracted from the file names. 

### 3. Run the Script

Once you’ve cloned the repository and installed the required libraries, you can run the script on your data files:

Either as a python notebook, or by using the .py script:

```python AKTAplot.py```

By default, the script will look for CSV files in the same directory, generate individual chromatogram plots, combined plots, and stacked plots for multiple files.

### 4. Customization

The script can be customized by adjusting variables within the script:

- **show_fractions:** Set to 1 to display fraction markers, or 0 to hide them.
- You can modify plot styles, colors, and line formats within the script as needed.
- You can also choose to normalize data or not. 

## Output

- Individual chromatogram plots are saved as PNG files named <sample_name>_UV280_vs_ElutionVolume.png.
- Combined plots of all chromatograms are saved as Combined_UV280_vs_ElutionVolume.png.
- Stacked plots of multiple chromatograms are saved as Stacked_UV280_vs_ElutionVolume.png.

## Example

Here’s an example of how the outputs will look: 

**Basic chromatogram (with fractions)**  
![basic chromatogram](/assets/chromexample.png)

**Overlay of all runs**  
![overlaychromatogram](/assets/overlay.png)

**Stacked chromatograms**  
![stackedchromatogram](/assets/stacked.png)

## Contributing

If you’d like to contribute to AKTAplot, feel free to submit a pull request or open an issue. Contributions such as bug fixes, new features, and improvements are welcome!

> Enjoy using AKTAplot for your chromatographic data visualization needs!
