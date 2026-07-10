import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load titanic dataset
data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

#Inspect data
print(data.describe())
print(data.head())

#Remove Duplicates
data = data.drop_duplicates()

#Handling missing values
data["Age"] = data["Age"].fillna(data["Age"].median())
data["Embarked"] = data["Embarked"].fillna(data["Embarked"].mode()[0])
data["Cabin"] = data["Cabin"].fillna(data["Cabin"].bfill())
print(data)

#Filter data: Passengers in first class
first_class = data[data["Pclass"] == 1]
print("First Class Passangers: \n", first_class.head())

#Bar chart: Survival rate by class
survival_by_class = data.groupby("Pclass")["Survived"].mean() 
survival_by_class.plot(kind = "bar", color = "skyblue")
plt.title("Survival rate by class")
plt.ylabel("Survival Rate")
plt.show()
plt.close()

#Histogram: Age distribution
sns.histplot(data["Age"], bins = 20, kde = True, color = "purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
plt.close()

#Scatter Plot: Age vs Fare
plt.scatter(data["Age"], data["Fare"], color = "Red", alpha = 0.5)
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()
plt.close()

#Box Plot: Age distribution and outlier detection
sns.boxplot(x=data["Age"])
plt.show()
plt.close()
