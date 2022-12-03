import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('loan_data.csv')
print(data.head())
# Feature Correlation: Use Method ==> Spearman Correlation
## Theory: To find any monotonic component
## spearman can be used for finding the strength and direction of this monotonic relationship
## We can use this Method (value would be -1 to 1)to found that how each component relate to others
### 0 means totally not related
### near -1 means they are negative related
### near 1 means they are positive related
################################################
# Set the plt figure size
plt.figure(figsize=(12,10))
# pd.corr(method ='{'pearson'，'kendall'，'spearman'}' , min_periods = 1 )
# Use for findind the relationship between Columns
cor = data.corr(method='spearman')
# use the seaborn to show the heatmap
# seaborn.heatmap(value,annot(True for showing each value in each block),cmap(choose color))
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
plt.title('feature_correlation')
#plt.savefig('feature_correlation.png')
plt.show()
