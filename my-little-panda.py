import pandas as pd
from math import nan

def make_peso(serie, peso):
    print("Series que vemos e o peso (ex: 0.3)")

def sum_pesos(series):
    print("Pega as 5 notas, e soma com o peso")

def stats():
    print("Traz os principais dados da table como top 5 melhores e piores notas")
    
def get_filtered_data():
    table = pd.read_csv('segundos-anos.csv', header=2)  # Ler arquivo

    # Seleciona apenas as colunas desejadas
    table = table.iloc[:, [1, 7, 8, 9, 10, 11]]

    print(table.dtypes) # Mostra os tipos de cada coluna

    print(table)

    # Index, de todos os "Nome do aluno" da primeira coluna
    rows_to_drop = table[table.iloc[:, 0] == "Nome do aluno"].index
    print(rows_to_drop) # array de indexes (numeros inteiros no caso)
    
    # Faz o drop naqueles indexes
    table.drop(rows_to_drop, inplace=True)

    # Checa por "X" ou NaN ou "#ERROR!" e substitui por 0
    table.replace({"X":0, nan:0, "#ERROR!": 0, "-":0}, inplace=True) 

    
    return table

filtered_data = get_filtered_data()

print(filtered_data)
