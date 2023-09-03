import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic_data = pd.read_csv('train.csv')

# Create a figure with multiple subplots
fig, axes = plt.subplots(3, 2, figsize=(12, 10))
plt.subplots_adjust(hspace=0.5)

# Plot 1: Passenger Gender Distribution
sns.countplot(x='Sex', data=titanic_data, ax=axes[0, 0])
axes[0, 0].set_title('Passenger Gender Distribution')

# Plot 2: Survival Rate by Gender
sns.barplot(x='Sex', y='Survived', data=titanic_data, ax=axes[0, 1])
axes[0, 1].set_title('Survival Rate by Gender')

# Plot 3: Passenger Class Distribution
sns.countplot(x='Pclass', data=titanic_data, ax=axes[1, 0])
axes[1, 0].set_title('Passenger Class Distribution')

# Plot 4: Survival Rate by Class
sns.barplot(x='Pclass', y='Survived', data=titanic_data, ax=axes[1, 1])
axes[1, 1].set_title('Survival Rate by Class')

# Plot 5: Age Distribution
sns.histplot(data=titanic_data, x='Age', bins=20, kde=True, ax=axes[2, 0])
axes[2, 0].set_title('Age Distribution')

# Plot 6: Survival Rate by Age
sns.histplot(data=titanic_data, x='Age', hue='Survived', bins=20, multiple='stack', ax=axes[2, 1])
axes[2, 1].set_title('Survival Rate by Age')

# Display the plots
plt.show()
