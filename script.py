import pandas as pd
import matplotlib 

arquivo_livro = 'entrada1.xlsx'
arquivo_razao = 'entrada2.xlsx'

df_livro = pd.read_excel(arquivo_livro)
df_razao = pd.read_excel(arquivo_razao)

df_agrupado_livro = df_livro.groupby('NOME').sum()
df_agrupado_razao = df_razao.groupby('NOME').sum()

df_total = df_agrupado_livro.merge(df_agrupado_razao,on='NOME', how='outer', )



print(df_total)
