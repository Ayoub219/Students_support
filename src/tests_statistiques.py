from itertools import product
import pandas as pd
import scipy.stats as ss
from scipy.stats import f_oneway

"""
Cette classe permet de réaliser des tests statistiques: khi2 et Anova pour mieux comprendre les associations
entre les variables.

NB: Les tests statistique sont réalisés sur les variables encodés
"""


class TestsStatistiques:
    def __init__(self, data):
        self.data = data

    # Cette méthode réalise un test du khi2 d'indépendance entre chaque paire de variables catégorielles
    # du DataFrame pour vérifier s'il existe une association statistiquement significative entre elles.
    def test_khi2(self):
        df_ = self.data.copy()
        df_ = df_.drop(columns=["age", "absences", "FinalGrade"])
        list1 = df_.columns
        list2 = df_.columns
        combinations = list(product(list1, list2, repeat=1))
        result = []
        for couple in combinations:
            if couple[0] != couple[1]:
                result.append(
                    (
                        couple[0],
                        couple[1],
                        list(
                            ss.chi2_contingency(
                                pd.crosstab(df_[couple[0]], df_[couple[1]])
                            )
                        )[1],
                    )
                )
        chi_test_output = pd.DataFrame(result, columns=["var1", "var2", "p_value"])
        return chi_test_output.pivot(index="var1", columns="var2", values="p_value")

    # Cette méthode réalise un test d'Anova d'indépendance entre chaque variable catégorielle et la variable de
    # la note finale pour vérifier s'il existe une association statistiquement significative entre elles.
    def test_anova(self):
        df_ = self.data.copy()
        df_ = df_.drop(columns=["age", "absences", "FinalGrade"])
        categorical_columns = df_.columns
        significant_anova_results = {}
        for var in categorical_columns:
            groups = [
                self.data[self.data[var] == category]["FinalGrade"]
                for category in self.data[var].unique()
            ]
            anova_stat, p_value = f_oneway(*groups)
            if p_value < 0.05:
                significant_anova_results[var] = {
                    "ANOVA F-statistic": anova_stat,
                    "p-value": p_value,
                }
        for var, result in significant_anova_results.items():
            print(f"Significant ANOVA result for {var} with FinalGrade:")
            print(f"  F-statistic: {result['ANOVA F-statistic']:.4f}")
            print(f"  p-value: {result['p-value']:.4f}\n")
