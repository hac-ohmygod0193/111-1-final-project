import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('loan_data.csv')
print(data.describe())
print(data.columns)
X=data.drop(['not.fully.paid','purpose'],axis=1)
Y=data['not.fully.paid']


