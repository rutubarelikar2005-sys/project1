import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Data Information 
print(df.info())

# Statistical Summary 
print(df.describe())

# Missing Values 
print(df.isnull().sum())

# Remove duplicates 
df.drop_duplicates(inplace=True)

# Fill missing values 
df.fillna("Unknown", inplace=True)

# Count Plot 
sns.countplot(x="type", data=df) 
plt.show()

# Histogram 
df["release_year"].hist()
 
plt.title("Release Year Distribution") 
plt.show()
