import pandas as pd

# Load the collected financial data from 'financial_data.csv'
df = pd.read_csv("../data/financial_data.csv")

# Calculate growth rates
df["Revenue Growth (%)"] = df["Revenue ($)"].pct_change() * 100
df["Profit Growth (%)"] = df["Net Profit ($)"].pct_change() * 100
df["Client Growth (%)"] = df["Clients Acquired"].pct_change() * 100

# Save the analysis results to 'financial_analysis.csv'
df.to_csv("../data/financial_analysis.csv", index=False)
print("Financial analysis completed and saved!")
print(df)

