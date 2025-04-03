import mysql.connector
import pandas as pd
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import create_engine
from sqlalchemy import text


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

# Replace the following placeholders with your actual database credentials
username = 'root'
password = 'aluno'
host = 'localhost'
port = '3306'  # Default MySQL port is 3306
database = 'pyteste'

# Create the engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection to the database was successful!")
        # connection.execute(text("SELECT * FROM sh4")).fetchall()

except Exception as e:
    print(f"An error occurred: {e}")

for y in range(2019, 2025):

    # df of a url
    # url = f'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_{year}_MUN.csv'
    # df = pd.read_csv(url, sep=";", encoding="latin1")

    # df of a file
    fil = f'data/dataset/EXP_{y}_MUN.csv'
    df = pd.read_csv(fil, sep=';', encoding='latin1')

    df.to_sql(name=f'mun_{y}', con=engine)

connector_object = mysql.connector.connect(user='root', password='aluno', host='localhost', database='pyteste')
cursor=connector_object.cursor()

