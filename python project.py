import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")

# Load the dataset
file_path = r"C:\Users\tanmay\Downloads\Electric_Vehicle_Data.xlsx"
df = pd.read_excel(file_path)

# Display the first few rows of the dataset
print("Dataset Preview:")
print(df.head())


# Objective 1: Most Popular EV Makes
print("\nTop 10 EV Makes:")
top_makes = df['Make'].value_counts().head(10)
print(top_makes)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_makes.values, y=top_makes.index, hue=top_makes.index, palette='viridis', legend=False)
plt.title('Top 10 Most Common EV Makes')
plt.xlabel('Number of Vehicles')
plt.ylabel('Vehicle Make')
plt.tight_layout()
plt.show()


# Objective 2: Distribution of Model Years
print("\nModel Year Distribution:")
plt.figure(figsize=(10, 6))
sns.histplot(df['Model Year'].dropna(), bins=20, kde=True, color='skyblue')
plt.title('Distribution of Electric Vehicle Model Years')
plt.xlabel('Model Year')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


# Objective 3: Top Cities for EV Adoption
print("\nTop 10 Cities with Most EVs:")
top_cities = df['City'].value_counts().head(10)
print(top_cities)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, hue=top_cities.index, palette='coolwarm', legend=False)
plt.title('Top 10 Cities by EV Registrations')
plt.xlabel('Number of EVs')
plt.ylabel('City')
plt.tight_layout()
plt.show()


# Objective 4: Electric Range Analysis
print("\nElectric Range Stats:")
print(df['Electric Range'].describe())
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Electric Range'].dropna(), color='orange')
plt.title('Electric Vehicle Range Distribution')
plt.xlabel('Electric Range (Miles)')
plt.tight_layout()
plt.show()


# Objective 5: EV Types by Fuel Type
print("\nElectric Vehicle Type Counts:")
fuel_counts = df['Electric Vehicle Type'].value_counts()
print(fuel_counts)
plt.figure(figsize=(8, 6))
sns.barplot(x=fuel_counts.index, y=fuel_counts.values, hue=fuel_counts.index, palette='pastel', legend=False)
plt.title('Distribution of EV Types')
plt.ylabel('Number of Vehicles')
plt.xlabel('Electric Vehicle Type')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
