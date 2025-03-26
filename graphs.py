import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# arquivos e diretórios organizados pelo arquivo p3_all_df, basta rodar o arquivo
exp_2024 = 'data/dataset/EXP_2024_MUN.csv'
mun = 'data/tables/UF_MUN.csv'
sh4 = 'data/tables/NCM_SH.csv'

# em caso de não possuir os arquivos locais
# exp_2024 = 'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_2024_MUN.csv'
# mun = 'https://balanca.economia.gov.br/balanca/bd/tabelas/UF_MUN.csv'
# sh4 = 'https://balanca.economia.gov.br/balanca/bd/tabelas/NCM_SH.csv'


df = pd.read_csv(exp_2024, sep=";", encoding="latin1")
df_mun = pd.read_csv(mun, sep=";", encoding="latin1")
df_sh4 = pd.read_csv(sh4, sep=";", encoding="latin1")

## TOP 10 MUNICIPIOS POR QUANTIDADE DE EXPORTAÇÃO

# municipios_top10 = kg_total_per_mun.sort_values(by="TOTAL_KG_LIQUIDO", ascending=False).head(10)


# RENOMEAR PARA SER COMPATIVEL COM BASE MUN
df_mun = df_mun.rename(columns={"CO_MUN_GEO": "CO_MUN"})

# APENAS ESTADO DE SP // MESCLAR COM A TABELA DE MUN PARA PEGAR OS NOMES
df_mun_sp = df[df["SG_UF_MUN"] == "SP"]
df_mun_sp = pd.merge(df_mun_sp, df_mun[['CO_MUN', 'NO_MUN']], on='CO_MUN', how='left')

mun_counts= df_mun_sp["NO_MUN"].value_counts()
print(mun_counts)
mun_counts = mun_counts.head(10) # top 10 (pega os 10 primeiros valores)

# grafico
plt.figure(figsize=(10, 6))
mun_counts.plot(kind='bar')

# Customize the plot
plt.title('Quantidade de exportações por município de SP', fontsize=14)
plt.xlabel('Município', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotate the x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.show()
