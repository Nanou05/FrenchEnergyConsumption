# French Energy Consumption Analysis

## Overview

This project analyzes gas consumption data across different regions of France from 2014 to 2022. It provides insights into consumption trends, regional differences, and growth patterns using Python and data visualization techniques.

## Features

- Data cleaning and preprocessing
- Basic statistical analysis
- Yearly consumption trends
- Regional consumption comparisons
- Visualization of consumption patterns over time
- Growth rate analysis
- Time Series Analysis
- GeoData visualization

## Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn

## Installation

1. Clone this repository:
```
git clone https://github.com/Nanou05/FrenchEnergyConsumption.git
```
```
cd FrenchEnergyConsumption
```
2. Install the required packages:
```
pip install -r requirements.txt
```
## Usage

1. Ensure your data is in a CSV file named `consommation-regionale-cleaned.csv` in the project directory.

2. Run the analysis script:
```
data_analysis.ipynb
```

## Data Structure

The input data should be a CSV file with the following columns:
- annee: Year of consumption
- code_insee_region: INSEE code for the region
- region: Name of the region
- consommation_kwh_pcs: Gaz Consumption in kWh
- consommation_gwh_pcs: Gaz Consumption in GWh
- geom: Geometry data for the region
- centroid: Centroid coordinates of the region

## Output

The script generates:
- Console output with basic statistics, yearly consumption, and top consuming regions
- Line plot of gas consumption by region over time
- Heatmap of consumption by region and year
- Bar plot of average growth rates by region

## Contributing

Contributions to improve the analysis or extend the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/feature`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/feature`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Data provided by [(https://www.data.gouv.fr/fr/datasets/consommation-regionale-de-gaz-naturel-carburant-gnc/)]
- Inspired by the need for energy consumption analysis in France
