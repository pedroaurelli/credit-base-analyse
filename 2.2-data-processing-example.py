import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('data\credit_data.csv')


#Exemplo de caso de uso com dados tratos e não tratados
usersWithIncorrectAge = base_credit.loc[base_credit.age < 0]
print(usersWithIncorrectAge)

averageAge = base_credit['age'].mean()
print(averageAge)

tractiveAverageAge = base_credit['age'][base_credit.age > 0].mean()
print(tractiveAverageAge)

base_credit.loc[base_credit.age < 0, 'age'] = tractiveAverageAge
print(base_credit.head(27))
