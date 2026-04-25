import pandas as pd
import matplotlib.pyplot as plt

# Data load
df = pd.DataFrame({
    "Name": ["A","B","C","D","E","F","G","H"],
    "City": ["Delhi","Mumbai","Delhi","Pune","Chennai","Delhi","Mumbai","Pune"],
    "Marks": [80, 55, 90, 40, 70, 85, 60, 30]
})

# City-wise average marks
avg = df.groupby("City")["Marks"].mean()

# Bar chart
avg.plot(kind='bar')

plt.title("City-wise Average Marks")
plt.xlabel("City")
plt.ylabel("Average Marks")

plt.show()
