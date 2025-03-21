import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

exp_2024 = 'data/dataset/EXP_2024_MUN.csv'
mun = 'data/tables/UF_MUN.csv'
sh4 = 'data/tables/NCM_SH.csv'

# exp_2024 = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2024_MUN.csv'
# mun = 'https://balanca.economia.gov.br/balanca/bd/tabelas/UF_MUN.csv'
# sh4 = 'https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_SH.csv'


df = pd.read_csv(exp_2024, sep=";", encoding="latin1")
df_mun = pd.read_csv(mun, sep=";", encoding="latin1")
df_sh4 = pd.read_csv(sh4, sep=";", encoding="latin1")


teste = df.head()
# print(teste)
# teste.groupby()

# apenas sp
# df_mun_sp = df[df["SG_UF_MUN"] == "SP"]
# df_mun_sp = df_mun_sp.tail()
# print(df_mun_sp)

# # Renomear coluna para compatibilidade com a base de municípios
# df_mun = df_mun.rename(columns={"CO_MUN_GEO": "CO_MUN"})

# # Mesclar com os nomes dos municípios
# municipios_agregado = municipios_agregado.merge(df_mun, on=["CO_MUN"], how="left")

# # Renomear coluna para compatibilidade com a base de produtos
# df_sh4 = df_sh4.rename(columns={"CO_SH4": "SH4", "NO_SH4_POR": "PRODUTO"})

# # Mesclar com os nomes dos produtos
# municipios_agregado = municipios_agregado.merge(df_sh4, on=["SH4"], how="left")

# #apenas o estado de SP
# municipios_agregado = municipios_agregado[municipios_agregado["SG_UF_MUN"] == "SP"]

# RENOMEAR PARA SER COMPATIVEL COM BASE MUN
df_mun = df_mun.rename(columns={"CO_MUN_GEO": "CO_MUN"})

df_mun_sp = df[df["SG_UF_MUN"] == "SP"]
df_mun_sp = pd.merge(df_mun_sp, df_mun[['CO_MUN', 'NO_MUN']], on='CO_MUN', how='left')

mun_counts = df_mun_sp["NO_MUN"].value_counts()
print(mun_counts)
mun_counts = mun_counts.head(10) # top 10 (pega os 10 primeiros valores)

plt.figure(figsize=(10, 6))
mun_counts.plot(kind='bar', color='skyblue')

# Customize the plot
plt.title('Quantidade de exportações por município de SP', fontsize=14)
plt.xlabel('Município', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotate the x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.show()



# df['abs'] = df["VL_FOB"] / df['KG_LIQUIDO']
# municipios = df.groupby(["CO_MUN", "SG_UF_MUN", "SH4"])
# print(municipios)


# # Calcular valor agregado (VL_FOB / KG_LIQUIDO)
# df["VALOR_AGREGADO"] = df["VL_FOB"] / df["KG_LIQUIDO"]

# # Tratar casos onde KG_LIQUIDO é zero para evitar divisão por zero
# df = df[df["KG_LIQUIDO"] > 0]

# # Agrupar por município e SH4 e calcular a média do valor agregado
# municipios_agregado = df.groupby(["CO_MUN", "SG_UF_MUN", "SH4"])['VALOR_AGREGADO'].mean().reset_index()

# # Renomear coluna para compatibilidade com a base de municípios
# df_mun = df_mun.rename(columns={"CO_MUN_GEO": "CO_MUN"})

# # Mesclar com os nomes dos municípios
# municipios_agregado = municipios_agregado.merge(df_mun, on=["CO_MUN"], how="left")

# # Renomear coluna para compatibilidade com a base de produtos
# df_sh4 = df_sh4.rename(columns={"CO_SH4": "SH4", "NO_SH4_POR": "PRODUTO"})

# # Mesclar com os nomes dos produtos
# municipios_agregado = municipios_agregado.merge(df_sh4, on=["SH4"], how="left")

# #apenas o estado de SP
# municipios_agregado = municipios_agregado[municipios_agregado["SG_UF_MUN"] == "SP"]

# # Selecionar colunas relevantes e ordenar
# municipios_top10 = municipios_agregado.sort_values(by="VALOR_AGREGADO", ascending=False).head(10)

# # Exibir resultado
# print(municipios_top10[["NO_MUN_MIN", "SG_UF", "PRODUTO", "VALOR_AGREGADO"]]),

# print (df_mun.tail())
# print (df_sh4.tail())

# ab = pd.read_csv('data/dataset/EXP_2024_MUN.csv', sep=';')
# print(ab.tail())