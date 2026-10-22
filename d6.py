import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("Dataset.csv")

X = df[["YearsExperience"]] 
y = df["Salary"]

model = LinearRegression() 
model.fit(X, y)
prediction = model.predict(X) 
# Plot
plt.scatter(X, y, color="blue")
plt.plot(X, prediction, color="red") 
plt.xlabel("Years of Experience") 
plt.ylabel("Salary") 
plt.title("Simple Linear Regression") 
plt.show()

print("Slope:", model.coef_[0]) 
print("Intercept:", model.intercept_)
