import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('data\credit_data.csv')


# Para tratar os dados errados é necessário saber quais são os dados errados
# as 3 maneiras de tratar os dados são:

# 1 - Apagar a coluna inteira
# 2 - Apagar somente o registro
# 3 - Preencher os valores manualmente


#1 - Apagar a coluna inteira
base_credit.drop('age', 1)

#2 - Apagar somente o registro
invalidAges = base_credit.loc[base_credit['age'] < 0]
print(invalidAges)
base_credit3 = base_credit.drop(invalidAges.index)

#3 - Preencher os valores manualmente
# Preencher os valores manualmente é a forma mais trabalhosa, porém é a mais correta

#Os algoritimos em ML são mais eficientes quando temos mais dados,
#por isso não é recomendado apagar os dados errados

