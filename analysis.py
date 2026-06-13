import pandas as pd

df = pd.read_csv("data/weather_report.csv")


# Average Temperature per city
print(df.groupby("city_name")["temperature_c"].mean())

# Average Humidity per city
print(df.groupby("city_name")["humidity_pct"].mean())

# Average Wind Speed per city
print(df.groupby("city_name")["wind_speed_kmh"].mean())

# Maximum Temperature per city
print(df.loc[df["temperature_c"].idxmax()])

# Minimum Temperature per city
print(df.loc[df["temperature_c"].idxmin()])

#summary table
summary = df.groupby("city_name").agg({
    "temperature_c": "mean",
    "humidity_pct": "mean",
    "wind_speed_kmh": "mean"
}).reset_index()

summary.to_csv("data/city_summary.csv", index=False)

#print insights
print("\nCITY ANALYSIS SUMMARY")
print(summary)
