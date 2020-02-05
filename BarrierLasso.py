import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import cross_val_score
import numpy as np
import matplotlib.pyplot as plt
import os

def display_plot(cv_scores, cv_scores_std, xscale):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(alpha_space, cv_scores)
    std_error = cv_scores_std / np.sqrt(10)
    ax.fill_between(alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2)
    ax.set_ylabel('CV Score +/- Std Error')
    ax.set_xlabel('Alpha')
    ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
    ax.set_xlim([alpha_space[0], alpha_space[-1]])
    ax.set_xscale(xscale)
    print('The best score is ' + str(np.max(cv_scores)))
    plt.show()

#Select the path to the excel sheet you wish to use
os.chdir('C:\\Users\computer\Desktop')
Barrier = pd.ExcelFile('Barriers.xlsx')

#Select the sheet in excel you wish to use
df = Barrier.parse('Sheet1')
target = df['experimental']
Y = df.iloc[:,2:]

#Drop all parameters which have a low coeff
drop = ['First Atom', 'Hybridization', 'npi', 'esp', 'elst', 'natural charge']
data = Y.drop(columns=drop)
data = data.to_numpy()
target = target.to_numpy()
target = target.reshape(-1,1)
seed = 50

lasso = Lasso(alpha=0.001, normalize=True, random_state=seed)
alpha_space = np.logspace(-10, 10, 100)
lasso_scores = []
lasso_scores_std = []
for alpha in alpha_space:
    lasso.alpha = alpha
    lasso_cv_scores = cross_val_score(lasso, data, target, cv=3)
    lasso_scores.append(np.mean(lasso_cv_scores))
    lasso_scores_std.append(np.std(lasso_cv_scores))
display_plot(lasso_scores, lasso_scores_std, 'log')
print('________________________')

lasso = Lasso(alpha=0.001, normalize=True, random_state=seed)
lasso.fit(data, target)
lasso_cv_score = cross_val_score(lasso, data, target, cv=3, scoring='r2')
print(np.mean(lasso_cv_score))
lasso_coef = lasso.fit(data, target).coef_

columns = Y.columns
columns = columns.drop(drop)
print('These are the parameters used in the Lasso regression: ',columns)
print('The coefficient for ', columns[0], ' is: ', round(lasso_coef[0], 3))
print('The coefficient for ', columns[1], ' is: ', round(lasso_coef[1], 3))
print('The coefficient for ', columns[2], ' is: ', round(lasso_coef[2], 3))

plt.plot(range(0,len(columns)), lasso_coef)
plt.xticks(range(0,len(columns)), columns)
plt.margins(0.1)
plt.show()
