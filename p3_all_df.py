import os
import subprocess

# Create the 'data' directory if it doesn't exist

# Este programa gera a estrutura das pastas e baixa os arquivos necessários para as análises
# Útil para análises locais, para as buscas serem mais rápidas
# Gera: data/dataset/*grafico_ano*
#       data/tables/*tabelas_codigos*

# if not os.path.exists('data'):
#     os.makedirs('data')

PATH = 'data'

def folder_creation():
    if not os.path.exists(os.path.join(PATH)):
        os.makedirs(PATH)
    for subdir in ['dataset', 'tables']:
        if not os.path.exists(os.path.join(PATH, subdir)):
            os.mkdir(os.path.join(PATH, subdir))

def get_dataset(subdir):
    # Loop through the years from 2019 to 2024
    for year in range(2019, 2025):  
        url = f'https://balanca.economia.gov.br/balanca/bd/comexstat-bd/mun/EXP_{year}_MUN.csv'
        
        # Extract the file name from the URL
        output_file = os.path.basename(url)
        
        # Define the full path where the file will be saved (inside the 'data' folder)
        output_file_path = os.listdir(os.path.join(PATH, subdir))
        
        if output_file in output_file_path:
            continue
        # print(output_file_path, url)
        try:
            # Run the curl command to download the file and save it in the data/dataset folder
            subprocess.run(
                ["curl", "-o", os.path.join(PATH, subdir, output_file), url],
                check=True
            )
            print(f"Arquivo {output_file} baixado com sucesso em {output_file_path}!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao baixar o arquivo {output_file}: {e}")

def get_tables(subdir):
    for table in ["PAIS", "UF_MUN", "PAIS_BLOCO", "NCM_SH"]:
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

# https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv
# https://balanca.economia.gov.br/balanca/bd/tabelas/UF_MUN.csv
# https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS_BLOCO.csv

def main():
    folder_creation()
    get_dataset('dataset')
    get_tables('tables')

main()

file_list = os.path.join(os.path.split(__file__)[0], 'data', 'dataset')

print(os.listdir(file_list))