import pandas as pd

# Simulated Financial Data for BinaryFolks
data = {
    "Year": ["2020", "2021", "2022"],
    "Revenue ($)": [180000, 220000, 260000],
    "Net Profit ($)": [32000, 45000, 54300],
    "Clients Acquired": [10, 15, 20],
    "Client Retention Rate (%)": [90, 92, 94]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Save the dataset to the 'data' folder as 'financial_data.csv'
df.to_csv("../data/financial_data.csv", index=False)
print("Financial data collected and saved successfully!")
