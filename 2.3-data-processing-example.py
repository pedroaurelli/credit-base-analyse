import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('data\credit_data.csv')


#Processando dados que possivelmente são null

#verificando os campos que possuem dados null
nullableFields = base_credit.isnull().sum()
print(nullableFields)

#localizando os registros com dados null
onlyNulableRegisters = base_credit.loc[pd.isnull(base_credit.age)]
print(onlyNulableRegisters)

# preenche os dados null
base_credit.age.fillna(base_credit.age.mean(), inplace=True)

fixedNullableFields = base_credit.isnull().sum()
print(fixedNullableFields)
