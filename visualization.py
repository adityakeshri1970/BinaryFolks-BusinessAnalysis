import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed financial analysis data
df = pd.read_csv("../data/financial_analysis.csv")

# Set the style for the plot using Seaborn
sns.set(style="whitegrid")

# Create a figure for the line chart
plt.figure(figsize=(10, 6))

# Plot Revenue and Net Profit Trends with markers
sns.lineplot(x="Year", y="Revenue ($)", data=df, marker="o", label="Revenue")
sns.lineplot(x="Year", y="Net Profit ($)", data=df, marker="s", label="Net Profit")

# Set plot title and axis labels
plt.title("BinaryFolks Revenue & Profit Growth")
plt.xlabel("Year")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()

# Save the visualization image to the 'reports' folder
plt.savefig("../reports/Revenue_Profit_Growth.png")
plt.show()
