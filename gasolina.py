import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carrega o arquivo gasolina.csv
gasolina_df = pd.read_csv('gasolina.csv')

# Cria o gráfico de linha
plt.figure(figsize=(12, 6))
sns.lineplot(x='dia', y='venda', data=gasolina_df)
plt.title('Preço Médio da Gasolina em São Paulo (Julho 2021)')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.savefig('gasolina.png')
plt.show()
