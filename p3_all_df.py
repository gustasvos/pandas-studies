import os
import subprocess
import pandas as pd
import numpy as np

# Create the 'data' directory if it doesn't exist

# if not os.path.exists('data'):
#     os.makedirs('data')

PATH = 'data'

def folder_creation():
    path = 'data'
    if not os.path.exists(os.path.join(PATH)):
        os.makedirs(path)
    for subdir in ['dataset', 'tables']:
        if not os.path.exists(os.path.join(path, subdir)):
            os.mkdir(os.path.join(path, subdir))

def get_dataset(subdir):
    # Loop through the years from 2019 to 2024
    for year in range(2019, 2025):  
        # The range is inclusive of 2019 and exclusive of 2025, so it covers 2019 to 2024
        # Construct the URL by replacing the year value
        url = f'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_{year}_MUN.csv'
        
        # Extract the file name from the URL
        output_file = os.path.basename(url)
        
        # Define the full path where the file will be saved (inside the 'data' folder)
        output_file_path = os.listdir(os.path.join(PATH, subdir))
        
        if output_file in output_file_path:
            continue
        print(output_file_path, url)
        try:
            # Run the curl command to download the file and save it in the dataset folder
            subprocess.run(
                ["curl", "-o", os.path.join(PATH, subdir, output_file), url],
                check=True
            )
            print(f"Arquivo {output_file} baixado com sucesso em {output_file_path}!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao baixar o arquivo {output_file}: {e}")

def get_tables(subdir):
    for table in ["PAIS", "UF_MUN", "PAIS_BLOCO"]:
        url = f"https://balanca.economia.gov.br/balanca/bd/tabelas/{table}.csv"
        output_file = os.path.basename(url)
        output_file_path = os.listdir(os.path.join(PATH, subdir))

        if output_file in output_file_path:
            continue
        
        try:
            subprocess.run(
                ["curl", "-o", os.path.join(PATH, subdir, output_file), url],
                check=True,
            )
            print(f"Arquivo {output_file} baixado com sucesso em {output_file_path}!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao baixar o arquivo {output_file}: {e}")


def main():
    folder_creation()
    get_dataset('dataset')
    get_tables('tables')

main()


# https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv
# https://balanca.economia.gov.br/balanca/bd/tabelas/UF_MUN.csv
# https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS_BLOCO.csv