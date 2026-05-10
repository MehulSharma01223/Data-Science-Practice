import pandas as pd

# =====================
# MAP PRACTICE
# =====================

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "City": ["Delhi", "Mumbai", "Pune", "Delhi"]
})

city_codes = {
    "Delhi": "DL",
    "Mumbai": "MH",
    "Pune": "PN"
}

df["City_Code"] = df["City"].map(city_codes)

print(df)