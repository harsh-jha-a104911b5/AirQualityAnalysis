import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
data = pd.read_csv('data/Processed_Data.csv')

# Simulate improvements
reductions = {'PM2.5 levels': 0.3, 'PM10 levels.': 0.25, 'CO (Carbon Monoxide) levels': 0.2, 'NOx levels': 0.15}
data_after = data.copy()
for pollutant, reduction in reductions.items():
    data_after[pollutant] = data_after[pollutant] * (1 - reduction)

# Recalculate AQI (simplified)
data_after['Air Quality Index (AQI) value'] = (
    data_after[['PM2.5 levels', 'PM10 levels.', 'CO (Carbon Monoxide) levels', 'NOx levels']].mean(axis=1)
)

# Generate graphs
# Before vs After: City-wise
city_aqi_before = data.groupby('Name of the city')['Air Quality Index (AQI) value'].mean()
city_aqi_after = data_after.groupby('Name of the city')['Air Quality Index (AQI) value'].mean()

plt.figure(figsize=(12, 6))
plt.bar(city_aqi_before.index, city_aqi_before.values, label='Before', alpha=0.7, color='red')
plt.bar(city_aqi_after.index, city_aqi_after.values, label='After', alpha=0.7, color='green')
plt.title('City-wise AQI: Before vs After Implementation')
plt.xlabel('City')
plt.ylabel('Average AQI')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('results/city_comparison.png')
plt.show()

print("Graphs saved to the 'results/' directory.")
