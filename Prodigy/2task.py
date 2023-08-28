import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic_data = pd.read_csv('train.csv')

print(titanic_data.info())


print(titanic_data.head())


print(titanic_data.describe())


print(titanic_data.isnull().sum())

sns.countplot(x='Sex', data=titanic_data)
plt.title('Passenger Gender Distribution')
plt.show()

sns.barplot(x='Sex', y='Survived', data=titanic_data)
plt.title('Survival Rate by Gender')
plt.show()


sns.countplot(x='Pclass', data=titanic_data)
plt.title('Passenger Class Distribution')
plt.show()


sns.barplot(x='Pclass', y='Survived', data=titanic_data)
plt.title('Survival Rate by Class')
plt.show()

sns.histplot(data=titanic_data, x='Age', bins=20, kde=True)
plt.title('Age Distribution')
plt.show()


sns.histplot(data=titanic_data, x='Age', hue='Survived', bins=20, multiple='stack')
plt.title('Survival Rate by Age')
plt.show()


sns.histplot(data=titanic_data, x='Fare', bins=20, kde=True)
plt.title('Fare Distribution')
plt.show()

sns.histplot(data=titanic_data, x='Fare', hue='Survived', bins=20, multiple='stack')
plt.title('Survival Rate by Fare')
plt.show()
