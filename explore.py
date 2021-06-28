import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from sklearn.feature_selection import SelectKBest, f_regression, chi2
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE

def plot_variable_pairs(train, cols, hue=None):
    '''
    This function takes in a df, a list of cols to plot, and default hue=None 
    and displays a pairplot with a red regression line.
    '''
    return sns.pairplot(train[cols], hue=hue, kind="reg",plot_kws={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.1}})
           

def plot_categorical_and_continuous_vars(data_set, cat_var, con_var):
    '''plot_categorical_and_continuous_vars(data_set, cat_var, con_var)
    returns a barplot, violinplot, and boxplot of the continuous and categorical variables'''
    return (sns.barplot(data = data_set, y = con_var, x = cat_var),
            plt.show(),
            sns.violinplot(data = data_set, y = con_var, x = cat_var),
            plt.show(),
            sns.boxplot(data = data_set, y = con_var, x = cat_var))

def heat_corr(data_set):
    '''takes in a data_set, returns a heatmap of correlation values'''
    return sns.heatmap(data_set.corr(), cmap='Blues', annot=True, linewidth=0.5, mask= np.triu(data_set.corr()))

def select_kbest(X, y, stats = f_regression, k = 3):
    '''select_kbest(X, y, stats = f_regression, k = 3)
    can change stats test to chi2 if working with categorical variables.
    k is default to 3, but can be edited to give more features.
    returns a list of k best features '''
    X_best= SelectKBest(stats, k).fit(X, y)
    mask = X_best.get_support() #list of booleans for selected features
    new_feat = [] 
    for bool, feature in zip(mask, X.columns):
        if bool:
            new_feat.append(feature)
    return print('The best features are:{}'.format(new_feat))

def rfe(X,y, k = 2, rankings = False):
    ''' takes in X_train and target
    returns k best features using recursive feature elimination'''
    lm = LinearRegression()
    rfe = RFE(lm, k)
    X_rfe = rfe.fit_transform(X, y)
    mask = rfe.get_support()
    new_feat = []
    for bool, feature in zip(mask, X.columns):
        if bool:
            new_feat.append(feature)
    if rankings:
        rankings = pd.Series(dict(zip(X.columns, rfe.ranking_)))
        return rankings
    else:
        return print(f'Best features are {new_feat}')
    
def t_test(t_var, df, target, alpha):
    '''
        This method will produce a 2 tailed t test  equate the p value to the alpha to determine whether the null hypothesis can be rejected.
    '''
    for i in t_var:
        t, p = stats.ttest_ind(df[i],df[target], equal_var=False)
        print('Null Hypothesis: {} is not correlated to value '.format(i))
        print('Alternative hypothesis:  {} is correlated to value '.format(i))
        if p < alpha:
            print('p value {} is less than alpha {} , we reject our null hypothesis'.format(p,alpha))
        else:
            print('p value {} is not less than alpha {} , we  fail to reject our null hypothesis'.format(p,alpha))
        print('-------------------------------------')
    