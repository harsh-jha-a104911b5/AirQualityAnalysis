# Air Quality Analysis and Recommendations

This repository contains the analysis of air quality data from various Indian cities. The goal is to identify key pollutants, analyze trends, and propose actionable solutions. It also includes simulations of improvements based on the proposed recommendations.

## Features
- Identification of key pollutants affecting AQI.
- Analysis of city-wise and seasonal AQI trends.
- Simulation of AQI improvements after implementing recommendations.
- Visualizations comparing before-and-after scenarios.

## Repository Structure
- **data/**: Contains the original and processed datasets.
- **notebooks/**: Jupyter notebooks for analysis and simulations.
- **src/**: Python scripts for data cleaning, visualizations, and simulations.
- **results/**: Key visualizations and outputs.
- **docs/**: Supporting documents like the problem statement and presentation.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/username/AirQualityAnalysis.git
   ```
2. Navigate to the repository:
   ```bash
   cd AirQualityAnalysis
   ```
3. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Data Cleaning
Run the `data_cleaning.py` script to clean and prepare the dataset:
```bash
python src/data_cleaning.py
```

### Analysis and Visualizations
Use the `Data_Analysis.ipynb` notebook to perform detailed analysis and generate visualizations.

### Simulating AQI Improvements
Run the `simulate_scenarios.py` script to simulate improvements and generate before-and-after graphs:
```bash
python src/simulate_scenarios.py
```

## Results
Key findings and visualizations can be found in the `results/` directory.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Thanks to the organizers for providing the dataset and guidance.
