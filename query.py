import mysql.connector
import pandas as pd
from sqlalchemy.dialects.mysql import insert
from sqlalchemy import create_engine
from sqlalchemy import text
# import csv
# import numpy as np
# import matplotlib.pyplot as plt



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
# print(df.head(3))

# Replace the following placeholders with your actual database credentials
username = 'root'
password = 'aluno'
host = 'localhost'
port = '3306'  # Default MySQL port is 3306
database = 'pyteste'

# Create the engine
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

df.to_sql(name='sh4', con=engine)
# Test the connection
try:
    with engine.connect() as connection:
        print("Connection to the database was successful!")
        connection.execute(text("SELECT * FROM sh4")).fetchall()

except Exception as e:
    print(f"An error occurred: {e}")

connector_object = mysql.connector.connect(user='root', password='aluno', host='localhost', database='pyteste')
cursor=connector_object.cursor()


# with engine.connect() as conn:
#    conn.execute(text("SELECT * FROM users")).fetchall()

# def insert_on_conflict_update(table, conn, keys, data_iter):
#     # update columns "b" and "c" on primary key conflict
#     data = [dict(zip(keys, row)) for row in data_iter]
#     stmt = (
#         insert(table.table)
#         .values(data)
#     )
#     stmt = stmt.on_duplicate_key_update(b=stmt.inserted.b, c=stmt.inserted.c)
#     result = conn.execute(stmt)
#     return result.rowcount
# df_conflict.to_sql(name="conflict_table", con=conn, if_exists="append", method=insert_on_conflict_update)  





# with open ('data\dataset\EXP_2024_MUN.csv', 'r') as f:
#     reader = csv.reader(f)
#     columns = next(reader) 
#     query = 'insert into MyTable({0}) values ({1})'
#     query = query.format(','.join(columns), ','.join('?' * len(columns)))
#     # cursor = connection.cursor()
#     connector_object = mysql.connector.connect(user='root', password='aluno', host='localhost', database='pyteste')
#     cursor=connector_object.cursor()

#     for data in reader:
#         cursor.execute(query, data)
#     cursor.commit()

# with open ('data\dataset\EXP_2024_MUN.csv', 'r') as f:
#     reader = csv.reader(f)
#     data = next(reader) 
#     query = 'insert into MyTable values ({0})'
#     query = query.format(','.join('?' * len(data)))
#     # cursor = connection.cursor()
#     connector_object = mysql.connector.connect(user='root', password='aluno', host='localhost', database='pyteste')
#     cursor=connector_object.cursor()

#     # cursor.execute(query, data)
#     for data in reader:
#         cursor.execute(query, data)
#     cursor.commit()