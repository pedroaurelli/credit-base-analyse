import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

base_credit = pd.read_csv('data\credit_data.csv')

# Análise de dados
print(base_credit.describe())

# Menor dívida
lessLoan = base_credit.loc[base_credit['loan'] <= 1.377630]
print(lessLoan)

# Maior renda
biggestIncome = base_credit.loc[base_credit['income'] >= 69995.685578]
print(biggestIncome)

