# 📊 Netflix Dataset Analysis: Data Cleaning & Visualization  

## 🔍 Overview  
This project explores the **Netflix dataset** using **Python** to clean and visualize trends in Netflix content. It provides insights into **content distribution, genre popularity, and country-wise contributions**, helping understand the platform's offerings better.  

## 📂 Dataset  
- **Source:** [Netflix Dataset on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)  
- **Format:** CSV  
- **Key Columns:**  
  - `title` – Name of the show  
  - `type` – Movie or TV Show  
  - `listed_in` – Genres  
  - `country` – Country of production  
  - `date_added` – When it was added to Netflix  
  - `release_year` – Year of release  
  - `rating` – Content rating  

## 🛠️ Technologies Used  
- **Python**  
- **pandas** – Data manipulation  
- **matplotlib & seaborn** – Data visualization  

## 📊 Exploratory Data Analysis (EDA)  
### ✅ **Data Cleaning:**  
- Handled missing values in `country`, `rating`, and `date_added`.  
- Converted `date_added` into datetime format.  
- Extracted `year_added` for trend analysis.  

### 📈 **Key Visualizations:**  
1. **Movies vs. TV Shows Count** 📊  
2. **Top 10 Countries by Number of Titles** 🌍  
3. **Yearly Trend of Added Titles** 📆  
4. **Most Common Genres on Netflix** 🎭  

