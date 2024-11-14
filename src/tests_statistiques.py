from itertools import product
import pandas as pd
import scipy.stats as ss
from scipy.stats import f_oneway

#Les tests stats sont réalisés sur les variables encodés
class TestsStatistiques:
    def __init__(self, data):
        self.data = data
        
    def test_khi2(self, categorical_columns):
        list1 = categorical_columns
        list2 = categorical_columns
        combinations = list(product(list1,list2, repeat = 1))
        result = []
        for couple in combinations:
            if couple[0] != couple[1]:
                result.append((couple[0],couple[1],list(ss.chi2_contingency(pd.crosstab(self.data[couple[0]], self.data[couple[1]])))[1]))
        chi_test_output = pd.DataFrame(result, columns = ['var1', 'var2', 'p_value'])
        return chi_test_output.pivot(index='var1', columns='var2', values='p_value')
    
    def test_anova(self, categorical_columns):
        significant_anova_results = {}
        for var in categorical_columns:
            groups = [self.data[self.data[var] == category]['FinalGrade'] for category in self.data[var].unique()]
            anova_stat, p_value = f_oneway(*groups)
            if p_value < 0.05:
                significant_anova_results[var] = {'ANOVA F-statistic': anova_stat, 'p-value': p_value}
        for var, result in significant_anova_results.items():
            print(f"Significant ANOVA result for {var} with FinalGrade:")
            print(f"  F-statistic: {result['ANOVA F-statistic']:.4f}")
            print(f"  p-value: {result['p-value']:.4f}\n")
                
    