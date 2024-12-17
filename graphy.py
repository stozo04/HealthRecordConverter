import pandas as pd
import matplotlib.pyplot as plt

# Data
data = [
    {"Value": 58.0, "Date": 1417478400000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 37.0, "Date": 1434585600000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 36.0, "Date": 1446681600000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 47.0, "Date": 1469750400000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 31.0, "Date": 1500940800000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 74.0, "Date": 1520899200000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 55.0, "Date": 1530144000000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 47.0, "Date": 1542412800000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 48.0, "Date": 1552694400000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 49.0, "Date": 1583452800000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 36.0, "Date": 1592524800000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 50.0, "Date": 1611014400000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 49.0, "Date": 1618963200000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 34.0, "Date": 1636416000000, "Lower Normal": 9.0, "Upper Normal": 46.0},
    {"Value": 38.0, "Date": 1663200000000, "Lower Normal": 9.0, "Upper Normal": 46.0},
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to readable datetime format
df['Date'] = pd.to_datetime(df['Date'], unit='ms')

# Plotting the line graph
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Value'], marker='o', linestyle='-', color='blue', label='ALT Levels')
plt.fill_between(df['Date'], df['Lower Normal'], df['Upper Normal'], color='lightgray', label='Normal Range')
plt.axhline(y=46, color='r', linestyle='--', label='Upper Normal Limit (46 U/L)')
plt.axhline(y=9, color='b', linestyle='--', label='Lower Normal Limit (9 U/L)')

# Add labels and title
plt.title('Alanine Aminotransferase (ALT) Levels Over Time')
plt.xlabel('Date')
plt.ylabel('ALT (U/L)')
plt.legend()
plt.grid()
plt.show()
