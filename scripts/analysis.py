import os
import pandas as pd
import matplotlib.pyplot as plt

path = './results'
if not os.path.exists(path):
    os.makedirs(path,exist_ok=True)
else:
    print(f'{path} already exist')

columns = ['class','Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
df = pd.read_csv('./data/wine.data', names=columns, sep=',', engine='python')
new_df = df[['Malic acid','Flavanoids']]

summary_statistics = new_df.describe()
summary_statistics.to_csv('./results/summary_statistics-Malic_acid&Flavanoids.txt', header=True)
print("Successfully print summary statistics file(.txt) in the results folder")

plt.figure(figsize=(15, 10))
new_df.boxplot()
plt.title('Malic_acid vs. Flavanoids')
plt.xlabel('Name')
plt.ylabel('Value')
plt.savefig('./results/boxplots-Malic_acid&Flavanoids.png')
print("Successfully print summary statistics plot(.png) in the results folder")