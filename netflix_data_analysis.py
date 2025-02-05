# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Netflix dataset from the local file
file_path = "D:\\netflix_titles.csv"  
netflix_data = pd.read_csv(file_path)

# Displays the first 5 rows of the dataset, providing a quick overview of its structure and contents.
print("Dataset Head:")
print(netflix_data.head()) 

# Basic information about the dataset including the number of entries, column names, data types, and non-null counts.
print("\nDataset Info:")
print(netflix_data.info())

# Check for missing values in each column and returns their count.
print("\nMissing Values:")
print(netflix_data.isnull().sum())

# Data Cleaning
# Replacing missing values in 'country' and 'rating' with 'Unknown'
netflix_data['country'].fillna('Unknown', inplace=True)
netflix_data['rating'].fillna('Unknown', inplace=True)

# Drop rows with missing values in 'date_added'
netflix_data.dropna(subset=['date_added'], inplace=True)

# Convert 'date_added' to datetime format, allowing easy extraction and manipulation of date components.
netflix_data['date_added'] = pd.to_datetime(netflix_data['date_added'])

# Extract the year content was added
netflix_data['year_added'] = netflix_data['date_added'].dt.year

# Visualizations
# 1. Count of Movies vs TV Shows
plt.figure(figsize=(8, 5))
sns.countplot(data=netflix_data, x='type', palette='Set2')
plt.title('Count of Movies vs TV Shows')
plt.xlabel('Type')
plt.ylabel('Count')
plt.show()

# 2. Top 10 Countries by Number of Titles
top_countries = netflix_data['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Top 10 Countries by Number of Titles')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()

# 3. Number of Titles Added Each Year
titles_per_year = netflix_data['year_added'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x=titles_per_year.index, y=titles_per_year.values, marker='o', color='blue')
plt.title('Number of Titles Added Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.show()

# 4. Most Common Genres
plt.figure(figsize=(10, 6))
genres = netflix_data['listed_in'].str.split(', ').explode().value_counts().head(10)
sns.barplot(x=genres.values, y=genres.index, palette='coolwarm')
plt.title('Most Common Genres on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.show()
