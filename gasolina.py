import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# código de geração do gráfico

df = pd.read_csv('gasolina.csv')

sns.lineplot(x = 'dia', y = 'venda', data = df)
plt.savefig('gasolina.png')
