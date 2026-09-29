import seaborn as sns
import matplotlib.pyplot as plt

# Load the Penguins dataset
penguins = sns.load_dataset("penguins")

# Drop missing values
penguins = penguins.dropna()

# Print head and info
print("First 5 rows:")
print(penguins.head())

print("\nDataset information:")
penguins.info()


# Step 1: Scatter plot
plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=penguins,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species"
)

plt.title("Bill Length vs Bill Depth")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")
plt.show()


# Step 2: Correlation heat map
numeric_data = penguins.select_dtypes(include="number")

correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="RdYlGn",
    fmt=".2f",
    vmin = -1,
    vmax = 1
)

plt.title("Correlation heat map")
plt.show()
