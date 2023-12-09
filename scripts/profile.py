import pandas as pd
import os
from ydata_profiling import ProfileReport

path = './profiling'
if not os.path.exists(path):
    os.makedirs(path,exist_ok=True)
else:
    print(f'{path} already exist')

columns = ['class','Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']
df = pd.read_csv('./data/wine.data', names=columns, sep=',', engine='python')

file = './profiling/report.html'
if os.path.exists(file):
    print(f"The report.html file already exists. Check if you need to delete it. \npath:{file}")
else:
    profile = ProfileReport(df, title="Profiling Report")
    profile.to_file(file)