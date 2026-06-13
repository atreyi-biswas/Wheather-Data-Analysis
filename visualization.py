import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/weather_report.csv")

plt.figure()
plt.bar(df["city_name"], df["temperature_c"])
plt.title("Temperature by City", color='Purple', weight='bold')
plt.xlabel("City", color='red')
plt.ylabel("Temperature (°C)", color='red')
plt.savefig("output assets/temperature.png")
plt.show()

