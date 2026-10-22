import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Salary_Data.csv")

# Correlation 
print(df.corr())

# Heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm") 
plt.show()

# Regression Plot
sns.regplot(x="YearsExperience", y="Salary", data=df)

plt.title("Regression Analysis") 
plt.show()
