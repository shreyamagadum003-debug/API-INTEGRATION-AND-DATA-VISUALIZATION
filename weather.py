
# -------------------------------
# Weather API Integration & Visualization
# -------------------------------

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Step 1: Set API Key & City
# -------------------------------
API_KEY = "7b79f2759454235bbac7572780c2bfdc"   # Replace with your OpenWeatherMap API key
CITY = "Kolhapur"

# -------------------------------
# Step 2: Fetch Weather Data
# -------------------------------
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

# -------------------------------
# Step 3: Extract Required Info
# -------------------------------
weather_data = {
    "Parameter": ["Temperature (°C)", "Feels Like (°C)", "Humidity (%)"],
    "Value": [data["main"]["temp"], data["main"]["feels_like"], data["main"]["humidity"]]
}

df = pd.DataFrame(weather_data)

# -------------------------------
# Step 4: Visualization (Column Graph)
# -------------------------------
plt.figure(figsize=(8,6))
sns.barplot(x="Parameter", y="Value", data=df, palette="viridis")

# Add labels and title
plt.xlabel("Weather Parameters")
plt.ylabel("Value")
plt.title(f"Weather Overview for {CITY}")
plt.ylim(0, max(df["Value"])+10)  # Add space above bars
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Horizontal gridlines

# Display graph
plt.show()
