import matplotlib.pyplot as plt


ages = [25, 30, 22, 40, 32, 28, 35, 29, 38, 27, 31, 24, 26, 33, 36, 37, 23, 39, 34, 31]


plt.hist(ages, bins=10, edgecolor='black', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Ages in a Population')
plt.grid(True)
plt.show()
