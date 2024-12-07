import pandas as pd

# Load dataset
data = pd.read_csv('data/Air_Quality_data.csv')

# Data cleaning
data['Date of the record'] = pd.to_datetime(data['Date of the record'], errors='coerce')
data = data.dropna(subset=['Air Quality Index (AQI) value'])

# Save cleaned data
data.to_csv('data/Processed_Data.csv', index=False)
print("Data cleaning completed. Processed data saved to 'data/Processed_Data.csv'.")
