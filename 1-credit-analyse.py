import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('data\credit_data.csv')

# Análise de dados
print(base_credit.describe())

# Menor dívida
lessLoan = base_credit.loc[base_credit['loan'] <= 1.377630]

# Maior renda
biggestIncome = base_credit.loc[base_credit['income'] >= 69995.685578]

# Quantos clientes pagam e quantos não pagam as dívidas
closeLoan = np.unique(base_credit['default'], return_counts=True)

# Gráfico de barras para clientes que pagam e não pagam as dívidas
plt.figure(0)
sns.countplot(x = base_credit['default'])
plt.xlabel('Pagantes e não pagantes')

# Gráfico histograma para idade
# histograma - usado para representar a distribuição de frequência de alguns pontos de dados de uma única variável.
plt.figure(1)
plt.hist(x = base_credit['age'])
plt.xlabel('Idade')

# Gráfico histograma para renda
plt.figure(2)
plt.hist(x = base_credit['income'])
plt.xlabel('Renda')

# Gráfico histograma para divida
plt.figure(3)
plt.hist(x = base_credit['loan'])
plt.xlabel('Divida')

# Gráfico de dispersão para idade e renda
grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color='default')

#Tratamento dos dados inconsistentes
invalidAges = base_credit.loc[base_credit['age'] < 0]
print(invalidAges)

base_credit3 = base_credit.drop(invalidAges.index)
